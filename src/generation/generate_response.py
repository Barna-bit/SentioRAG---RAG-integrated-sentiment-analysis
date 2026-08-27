from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_response(query, results):
    """
    Generate a natural-language summary using Gemini
    based only on the retrieved reviews.
    """

    reviews_text = "\n".join(
        [
            f"Review: {r.get('review', '')}\n"
            f"Sentiment: {r.get('sentiment', '')}\n"
            f"Score: {r.get('score', '')}"
            for r in results
        ]
    )

    prompt = f"""
You are a customer review analysis assistant.

User question:
{query}

Retrieved customer reviews:
{reviews_text}

Based ONLY on these retrieved reviews:

1. Give a short overall summary of customer opinion.
2. Mention the main positive points.
3. Mention the main negative points.
4. Mention if customers have mixed or neutral opinions.

Do not invent information that is not present in the reviews.

Keep the answer clear and concise.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text