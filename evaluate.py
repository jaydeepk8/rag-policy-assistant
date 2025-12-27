evaluation_questions = {
    "What is the refund period?": "✅ Answerable",
    "How long does standard delivery take?": "✅ Answerable",
    "Can I cancel an order after it is shipped?": "✅ Answerable",
    "Do you ship internationally?": "❌ Unanswerable",
    "Is shipping insured?": "❌ Unanswerable",
    "Are refunds processed instantly?": "⚠️ Partially Answerable"
}

print("Evaluation Results:\n")

for question, expected in evaluation_questions.items():
    print(f"Q: {question}")
    print(f"Expected: {expected}")
    print("-" * 50)
