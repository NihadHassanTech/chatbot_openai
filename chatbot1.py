# the openai library is imported in order to utilize the GPT-3 API.
# The nltk library is imported to break the given text string into words or sentences, called tokens
import openai
import nltk

# The punkt tokenizer is used to split text into separate sentences.Hence, it is downloaded from the Natural Language Toolkit (nltk) library.
# The sent_tokenize function from the nltk.tokenize module is imported to allow the punkt tokenizer to be used in the rest of the code
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Load the punkt tokenizer
sent_tokenize = nltk.tokenize.sent_tokenize

# Set the API key for accessing OpenAI's GPT-3 API
openai.api_key = 'ENTER_API_KEY'

# This function takes two inputs, paragraph and question, and returns the first sentence of a response generated by OpenAI's API, Completion.create()
# The result of the API call, Completion.create(), is a collection of completion choices, and the first item of this collection is accessed with .choices[0].text
# The function then tokenizes the response into sentences using the sent_tokenize function from the nltk.tokenize library and returns the first sentence
def chatbot_response(paragraph, question):
    response = openai.Completion.create(
        engine="curie:ft-techversant-2023-02-01-08-31-14",
        prompt='Given the following paragraph: "' + paragraph + '", what is the answer to the following question: "' + question + '"',
        max_tokens=30,
        n=1,
        stop=[" END"],
        temperature=0.5,
        best_of=1,
    ).choices[0].text

    # Split the response into sentences and return the first sentence.
    sentences = sent_tokenize(response)
    return sentences[0]

# The returned response is assigned to the chatbot_response_text variable, which is a part of the conditional block that executes only when chatbot1.py runs as script
if __name__=="__main__":
    paragraph = "The eligibility to refer candidates under the Employee Referral Programme is to pass Graduation exam. The referral bonus amount is determined based on the specific open position at Techversant."
    question = "What is the purpose of the Employee Referral Programme at Techversant in the above paragraph?"
    chatbot_response_text=chatbot_response(paragraph, question)
    print(chatbot_response_text)