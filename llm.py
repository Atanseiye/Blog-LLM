import streamlit as st
import openai
import requests

openai.api_key = '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'


st.title('LLM Test Interface - Mistral v1')

user_input = st.text_area('WHat os the topic for your blog')
user_token_input = st.text_input('Input a number. The higher the number the higher more the text. The number can not exceed 1500')

api_url = {'blog':"https://ll1eo3pfv1us6dw9.us-east-1.aws.endpoints.huggingface.cloud", 'trading llm': "https://u660eedzhbqh8t96.us-east-1.aws.endpoints.huggingface.cloud"}

API_URL = api_url['blog']
headers = {
	"Authorization": "Bearer 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",
	"Content-Type": "application/json"
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def prompt_adendum(topic):
    initial_text = "[INST] As a large language model agent, your task is to generate an extensive, concise, comprehensive and ## unlisted ## blog content for this [\INST]"
    added = initial_text + " " + topic
    return added





# The streamlit code starts here. Use the button to generate response
if st.button('Generate'):
    if len(user_input) == 0:
        response = [{'generated_text':"You haven't given any topic to write on"}]
    else:
        response = query(
            {
                "inputs": prompt_adendum(user_input),
                "parameters": {"max_new_tokens": int(user_token_input)}
            }
        )

    # save the response from the model in a variable called result



    result = response[0]['generated_text']
    result = result.split('[RESPONSE]')[1]

    st.write(result)

