from openai import OpenAI
from transformers import pipeline


def get_openai_response(prompt):
    # Set your OpenAI API key
    client = OpenAI(
        # defaults to os.environ.get("OPENAI_API_KEY")
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content


def get_output(s):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    candidate_labels = ['electrodynamics', 'News', 'Emails', 'Legal', 'Medical', 'Fiction', 'Business',
                        'Advertisements', 'Government', 'Others']
    classifier1 = pipeline("sentiment-analysis", model="michellejieli/inappropriate_text_classifier")

    print(classifier1(s)[0]['label'])
    if classifier1(s)[0]['label'] == "NSFW":
        return "Please do not send inappropriate messages"
    if classifier(s, candidate_labels)['labels'][0] != "electrodynamics":
        return "Please only send questions related to electrodynamics"
    return get_openai_response(s)


if __name__ == '__main__':
    print(get_output("Why do electrons have a curved path when there is a B field?"))
