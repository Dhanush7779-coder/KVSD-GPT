#imports
 
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
#code 

#prompt
prompt1 = ChatPromptTemplate.from_messages([
    ("system","listen to whatever user says"),
    ("user","give a precise answer to the question{question}")
])

#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
#llama-3.3-70b-versatile

#llm

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    groq_api_key="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",
    temperature = 0
)

#output

op = StrOutputParser()

#chain 
chain = prompt1 | llm | op

#streamlit

st.title("KVSD GPT")
input_text = st.text_input("Enter the question")
output = chain.invoke({"question":input_text})
st.write(output)