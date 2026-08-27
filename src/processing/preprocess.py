import pandas as pd
import re


def preprocess_text(text):
    """
    Clean and normalize review text.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r"[^a-z\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def preprocess_reviews():
    """
    Load reviews and preprocess the text.
    """

    # Load raw dataset
    file_path = "data/raw/reviews.csv"
    df = pd.read_csv(file_path)

    # Apply preprocessing
    df["clean_text"] = df["text"].apply(preprocess_text)

    # Save processed dataset
    output_path = "data/processed/reviews_processed.csv"
    df.to_csv(output_path, index=False)

    print("Preprocessing completed successfully!")
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)

    return df


if __name__ == "__main__":
    preprocess_reviews()