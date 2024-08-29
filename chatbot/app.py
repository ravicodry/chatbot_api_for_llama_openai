from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit  as st
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_kEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
##langsmith trackingrun 
os.environ['LANGCHAIN_TRACKING_V2'] = "true"

####prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are usefull assistant, answer user questions"),
        ("user","question:{question}")
    ]
        )


#### streamlit

st.title("Langchain OpenAI Chat")
input_text = st.text_input("search any topic")

### openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))