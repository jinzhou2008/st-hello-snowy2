import streamlit as st

st.title("☃️ Snowy") 
st.write('Hello this is a test of Snowy!')

# import openai
# from openai import OpenAI
# import re
# import streamlit as st
# #from promptsmine import get_system_prompt



# # # Set Azure OpenAI API configuration
# openai.api_type = "azure"
# #openai.api_base = "https://edhopenaitest.openai.azure.com/"
# openai.azure_endpoint=  "https://edhopenaitest.openai.azure.com/"
# openai.api_version = "2023-07-01-preview"
# openai.api_key = "e83a3572341642228cd2fbd04b0b2da7"
# #openai.api_key = st.secrets["OPENAI_API_KEY"]

# ## Validate OpenAI connection ##
# #client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# #client = OpenAI(api_key="e83a3572341642228cd2fbd04b0b2da7")
# #client=OpenAI()
# completion = openai.chat.completions.create(
#   model="gpt-4-edh",
#   messages=[
#     {"role": "user", "content": "What is theory of relativity?"}
#   ]
# )
# st.write(completion.choices[0].message.content)

# stream = openai.chat.completions.create(
#     model="gpt-4-edh",
#     messages=[{"role": "user", "content": "Say this is a test"}],
#     stream=True,
# )

# for chunk in stream:
#     if chunk.choices :
#         st.write(chunk.choices[0].delta.content or "")
#     #print(chunk)
#     print(chunk.choices)


