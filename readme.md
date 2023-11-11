## AI-Chat Application

This is a simple AI-chat application with a RESTful API on top of FastAPI in Python. This application enables users to have AI-powered interactions. Each interaction encapsulates multiple messages that can be from a human or an AI.


### How to Run
you can simply run the following command in the project directory  to run the application:

```shell
docker-compose up
```

This will build the Docker images and run the containers for the application and the MongoDB database. The application will be available at http://localhost:8073.
after running the application, you can access API documentation by visiting http://localhost:8000/docs

### Long-term Considerations for Improvements
Some of the long-term considerations for improving the application are:

**Scalability**: 
- scaling(increasing the number of workers for the app and using MongoDB replication)
- caching(using Redis)
- requests asynchronous processing(using RabbitMQ)

**Security**: 
- enable authentication to ensure that only authorized users can access the database
- defining roles and assign privileges to users based on their roles.
- regularly backup the data to a secure location and recover it in case of accidental deletion or corruption.
- regularly backup data (by doing so, i can recover data in case of accidental deletion)
- using application-level encryption to encrypt the data before storing it in MongoDB

**Monitoring**:
keep track of the performance and health of the application and the database. (use tools such as grafana and loki)