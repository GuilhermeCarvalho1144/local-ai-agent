from langchain_core.runnables import chain
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector_db import retriever


def main():
    model = OllamaLLM(model="qwen3.5")

    template = """
    You are a helpful assistant, An expert on bugers. You will answer the user's question about burgers.

    Here are some relevant reviews about bugers restaurants: {reviews}

    Here is the user's question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    while True:
        print(20 * "=")
        question = input(
            "Ask a question about burger places in town or q to quit: "
        )
        if question.lower() == "q":
            break
        else:
            reviews = retriever.invoke(question)
            results = chain.invoke(
                {
                    "reviews": reviews,
                    "question": "Which burger restaurant has the best burgers?",
                }
            )

            print(results)


if __name__ == "__main__":
    main()
