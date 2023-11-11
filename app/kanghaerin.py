from openai import OpenAI
client = OpenAI(api_key='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')

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You are a personal math tutor. Write and run code to answer math questions.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

thread = client.beta.threads.create()
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
)

print(completion.choices[0].message)