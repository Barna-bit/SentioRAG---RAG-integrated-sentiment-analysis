from langchain_core.runnables import RunnableLambda

from retrieve import retrieve_reviews


def retrieve_with_langchain(query):
    """
    Retrieve relevant reviews using the existing
    FAISS retrieval system through LangChain.
    """

    results = retrieve_reviews(query, top_k=5)

    return results


# LangChain Runnable
rag_chain = RunnableLambda(retrieve_with_langchain)


def run_rag(query):
    """
    Run the LangChain RAG pipeline.
    """

    results = rag_chain.invoke(query)

    return results