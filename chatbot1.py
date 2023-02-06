# importing necessary libraries
import nltk, openai
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

# Load the punkt tokenizer
sent_tokenize = nltk.tokenize.sent_tokenize

# Set the API key for accessing OpenAI's GPT-3 API
openai.api_key = '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'

# the chatbot function
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

    # Split the response into sentences
    sentences = sent_tokenize(response)
    
    # Return the first sentence
    return sentences[0]

# a sample paragraph and question 
paragraph = input("Enter the paragraph: \n")
question = input("Enter the question related to the paragraph: \n")
print(chatbot_response(paragraph, question))