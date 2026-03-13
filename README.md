# local-ai-agent

A simple local AI agent that answers questions about burger restaurants using a small reviews dataset, embeddings, vector search, and a local LLM.

## Overview

This project is a small Retrieval-Augmented Generation (RAG) demo built with:

- **LangChain**
- **Ollama**
- **ChromaDB**
- **Pandas**

It loads burger reviews from a CSV file, creates embeddings, stores them in a local Chroma vector database, retrieves the most relevant reviews for a query, and uses a local Ollama model to generate an answer.

## How it works

1. Load reviews from `fake_burger_reviews_small.csv`
2. Create embeddings with `qwen3-embedding`
3. Store the documents in a local Chroma database
4. Retrieve the top matching reviews for a query
5. Send the retrieved context to `qwen3.5` through Ollama
6. Print the answer in the terminal

## Project structure

```text
local-ai-agent/
├── main.py
├── vector_db.py
├── fake_burger_reviews.csv
├── fake_burger_reviews_small.csv
├── burger_reviews_db/
├── pyproject.toml
└── README.md
```

## Requirements

- Python
- [Ollama](https://ollama.com/)
- The following Ollama models pulled locally:
  - `qwen3.5`
  - `qwen3-embedding`

## Installation

Clone the repository:

```bash
git clone https://github.com/GuilhermeCarvalho1144/local-ai-agent.git
cd local-ai-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Or, if you are using `uv`:

```bash
uv sync
```

Pull the required Ollama models:

```bash
ollama pull qwen3.5
ollama pull qwen3-embedding
```

## Run the project

```bash
python main.py
```

On the first run, the project creates the local vector database in `burger_reviews_db/`.

## Notes

- The current vector database setup reads from `fake_burger_reviews_small.csv`
- The full dataset is also included as `fake_burger_reviews.csv`
- This project is intended as a simple local RAG demo for learning and experimentation

## Future improvements

- Add support for the full reviews dataset by default
- Expose the agent through a web UI or API
- Improve prompt design and answer formatting
- Add filters for rating and date
- Add evaluation for retrieval quality

## License

This project is for educational and experimentation purposes.
