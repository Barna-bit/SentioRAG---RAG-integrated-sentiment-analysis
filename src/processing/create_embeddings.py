import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer


def create_embeddings():

    # Load processed reviews
    file_path = "data/processed/reviews_processed.csv"
    df = pd.read_csv(file_path)

    print("Processed reviews loaded successfully!")
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)

    # Load the embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Create embeddings from cleaned review text
    embeddings = model.encode(
        df["clean_text"].tolist(),
        show_progress_bar=True
    )

    # Save embeddings to a NumPy file
    np.save(
        "data/processed/embeddings.npy",
        embeddings
    )

    print("\nEmbeddings created successfully!")
    print("Number of reviews:", len(embeddings))
    print("Embedding size:", embeddings.shape)
    print("Embeddings saved to: data/processed/embeddings.npy")


if __name__ == "__main__":
    create_embeddings()