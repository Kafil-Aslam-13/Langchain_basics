import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
from  langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

load_dotenv()
## below is used for langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv('LANGCHAIN_PROJECT')


## Prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant . Please respont to the question asked"),
        ("user","Question:{question}")

    ]
)

## streamlit framework 
st.title('langchain Demo with LLAMA2')
input_text=st.text_input("what question u have in mind?")

## call myb ollama llama2 model

llm=Ollama(model="gemma2:2b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))



