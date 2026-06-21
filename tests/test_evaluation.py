import pandas as pd

from src.pipeline import get_vector_store
from src.rag import answer_question

df = pd.read_csv("data/questions.csv")

vector_store = get_vector_store()

score = 0
total = len(df)
results = []
for _, row in df.iterrows():

    question = row["question"]

    expected_keywords = row["expected_keywords"]

    keywords = expected_keywords.split("|")

    actual = answer_question(
        question,
        vector_store
    )

    passed = all(
        keyword.lower() in actual.lower()
        for keyword in keywords
    )

    if passed:
        score += 1

    print("=" * 50)
    print("Question :", question)
    print("Expected :", expected_keywords)
    print("Actual   :", actual)
    print("Result   :", "PASS" if passed else "FAIL")

    results.append(
        {
            "question": question,
            "expected": expected_keywords,
            "actual": actual,
            "result": "PASS" if passed else "FAIL"
        }
    )

pd.DataFrame(results).to_csv(
    "evaluation_results.csv",
    index=False
)
print("\n" + "=" * 50)
print(f"Score: {score}/{total}")
print(f"Accuracy: {(score/total)*100:.2f}%")


