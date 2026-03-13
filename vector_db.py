import os
import pandas as pd
from tqdm import tqdm
from langchain_ollama.embeddings import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

DB_LOCATION = "./burger_reviews_db"
TOP_K = 10

add_docs = not os.path.exists(DB_LOCATION)

embedding_model = OllamaEmbeddings(model="qwen3-embedding")


if add_docs:
    print("Collection does not exist, creating it and adding documents...")
    df = pd.read_csv("./fake_burger_reviews_small.csv")
    docs = []
    ids = []
    for i, row in tqdm(df.iterrows(), total=len(df)):
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={"rating": row["Rating"], "Date": row["Date"]},
        )
        docs.append(document)
        ids.append(str(i))
    print("Finished creating collection, now adding to the database...")


db = Chroma(
    collection_name="burger_reviews",
    embedding_function=embedding_model,
    persist_directory=DB_LOCATION,
)

if add_docs:
    db.add_documents(documents=docs, ids=ids)
    print("Finished adding documents to the database.")
retriever = db.as_retriever(search_kwargs={"k": TOP_K})
