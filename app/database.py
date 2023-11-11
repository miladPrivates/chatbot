import uuid
from pymongo import MongoClient
from datetime import datetime
from config import db_name, connection_string
from models import Interaction, Message


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient(connection_string)
            cls._instance.db = cls._instance.client[db_name]
            cls.interactions_collection = cls._instance.db["interactions"]
        return cls._instance

    def create_interaction(self, interaction_data):
        interaction = Interaction(
            id=str(uuid.uuid4()),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            settings=interaction_data.settings,
            messages=[]
        )
        self.interactions_collection.insert_one(interaction.dict())
        return interaction

    def get_interactions(self):
        interactions = self.interactions_collection.find()
        return list(interactions)

    def get_interaction(self, interaction_id: str) -> Interaction:
        interaction = self.interactions_collection.find_one({"id": interaction_id})
        return interaction

    def create_message(self, interaction_id, message_data):
        message = Message(
            id=str(uuid.uuid4()),
            created_at=datetime.now(),
            role=message_data.role,
            content=message_data.content
        )
        update_interaction = {
            "$push": {"messages": message.dict()},
            "$set": {"updated_at": datetime.now()}
        }
        update_result = self.interactions_collection.update_one(
            {"id": interaction_id},
            update_interaction
        )
        if update_result.modified_count == 1:
            return message
        else:
            return None

    def get_messages(self, interaction_id):
        interaction = self.interactions_collection.find_one({"id": interaction_id})
        if not interaction:
            return None
        return interaction["messages"]
