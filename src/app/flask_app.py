from flask import Flask, request, jsonify, render_template
import sys
import os

# Add src folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

# Add retrieval folder to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "retrieval")
    )
)
from generation.generate_response import generate_response
from langchain_rag import run_rag


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()

        if not data or "query" not in data:
            return jsonify({
                "error": "Please provide a query"
            }), 400

        query = data["query"]

        print("QUERY:", query)

        results = run_rag(query)

        print("RAG RESULTS:", results)

        answer = generate_response(query, results)

        print("GEMINI ANSWER:", answer)

        return jsonify({
            "query": query,
            "results": results,
            "answer": answer
        })

    except Exception as e:
        print("========== ERROR ==========")
        print(type(e).__name__)
        print(str(e))
        print("============================")

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)