import pandas as pd


def load_reviews():
    """
    Load the raw review dataset from data/raw/reviews.csv
    """

    file_path = "data/raw/reviews.csv"

    df = pd.read_csv(file_path)

    print("Dataset loaded successfully!")
    print("Columns:", df.columns.tolist())
    print("Shape:", df.shape)

    return df


if __name__ == "__main__":
    load_reviews()