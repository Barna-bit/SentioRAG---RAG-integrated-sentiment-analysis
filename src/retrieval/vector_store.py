import pandas as pd
import numpy as np
import faiss
import pickle


def create_vector_store():

    # Load processed reviews
    df = pd.read_csv("data/processed/reviews_processed.csv")

    # Load embeddings
    embeddings = np.load("data/processed/embeddings.npy")

    # Create FAISS index
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to FAISS
    index.add(embeddings.astype("float32"))

    # Save FAISS index
    faiss.write_index(
        index,
        "data/processed/reviews.index"
    )

    # Save reviews for retrieval
    with open("data/processed/reviews.pkl", "wb") as f:
        pickle.dump(df, f)

    print("Vector store created successfully!")
    print("Number of vectors:", index.ntotal)
    print("Vector dimension:", dimension)


if __name__ == "__main__":
    create_vector_store()