import g4f

g4f.check_version = False


def generate_response(messages, model=g4f.models.gpt_35_turbo):
    response = g4f.ChatCompletion.create(
        model=model,
        prompt='As a helpful IFS therapist chatbot, your role is to guide users through a simulated IFS session '
               'in a safe and supportive manner with a few changes to the exact steps of the IFS model:',
        messages=messages,
    )
    return response
