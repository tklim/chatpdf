#!/root/py311env/bin/python

#pip install -q langchain==0.0.150 pypdf pandas matplotlib tiktoken textract transformers openai faiss-cpu

import os
import pandas as pd
import matplotlib.pyplot as plt
import terminalplot as tp
import termplotlib as tpl
from transformers import GPT2TokenizerFast
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain

# Set your OpenAI APIKEY inside .env file
# OPENAI_API_KEY=sk-12rxxxx...
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import textract

# Set your directory path here
directory_path = "/data/docs/gartner"

# Initialize tokenizer
tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

# Define the function to count tokens
def count_tokens(text: str) -> int:
    return len(tokenizer.encode(text))

# Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=512,
    chunk_overlap=24,
    length_function=count_tokens,
)

# Iterate over all files in the directory
all_chunks=[]
print(type(all_chunks))
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    print("file_path=",file_path)

    # Extract text from the PDF file
    doc = textract.process(file_path)

    # Write the extracted text to a temporary file
    with open('temppdf.txt', 'w') as f:
        f.write(doc.decode('utf-8'))

    # Read the text from the temporary file
    with open('temppdf.txt', 'r') as f:
        text = f.read()

    # Create chunks from the text
    chunks = text_splitter.create_documents([text])
    print(type(chunks))
    all_chunks += chunks

print("done chucks")
token_counts = [count_tokens(chunk.page_content) for chunk in all_chunks]
print("token_counts=",token_counts)

import numpy as np
hist,bins = np.histogram(token_counts,bins=40)
print(hist)
fig = tpl.figure()
fig.plot(bins[:-1], hist)
fig.show()

# Get embedding model
embeddings = OpenAIEmbeddings()
print("embeddings")

# Create vector database
db = FAISS.from_documents(chunks, embeddings)

#chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")
chain = load_qa_chain(OpenAI(temperature=0), chain_type="map_reduce")

# Put your Query here
query = "Summarize the article into key points for ease of reading."
docs = db.similarity_search(query)
out=chain.run(input_documents=docs, question=query)
print("out=",out)

