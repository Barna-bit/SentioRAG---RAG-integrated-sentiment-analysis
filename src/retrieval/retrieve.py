import faiss
import pickle
from sentence_transformers import SentenceTransformer


def load_vector_store():
    """
    Load the FAISS vector index and review data.
    """

    # Load FAISS index
    index = faiss.read_index("data/processed/reviews.index")

    # Load review data
    with open("data/processed/reviews.pkl", "rb") as f:
        reviews = pickle.load(f)

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Vector store loaded successfully!")
    print("Number of vectors:", index.ntotal)

    return index, reviews, model


def retrieve_reviews(query, top_k=3):
    """
    Retrieve the most relevant reviews for a query.
    """

    # Load vector store
    index, reviews, model = load_vector_store()

    # Convert query into an embedding
    query_embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    # Search FAISS index
    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    # Process search results
    for distance, index_position in zip(distances[0], indices[0]):

        # Skip invalid index
        if index_position == -1:
            continue

        # Get the corresponding row from DataFrame
        row = reviews.iloc[int(index_position)]

        # Get review text
        review_text = row["text"]

        # Get sentiment if available
        sentiment = row["sentiment"]

        results.append({
            "review": review_text,
            "sentiment": sentiment,
            "score": float(distance)
        })

    return results


if __name__ == "__main__":

    # Ask user for query
    query = input("Enter your query: ")

    # Retrieve relevant reviews
    results = retrieve_reviews(query)

    print("\nRelevant Reviews:\n")

    # Display results
    for i, result in enumerate(results, start=1):

        print(f"{i}. {result['review']}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Similarity Score: {result['score']:.4f}")
        print("-" * 60)