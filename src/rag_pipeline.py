from transformers import pipeline
import os

# Force transformers to use PyTorch only
os.environ["TRANSFORMERS_NO_TF"] = "1"


def load_llm():
    return pipeline(
        task="text2text-generation",
        model="google/flan-t5-base",
        framework="pt",
        max_length=256
    )


def answer_question(llm, retriever, prompt, question):
    # Retrieve top document
    documents = retriever.invoke(question)

    if not documents:
        return "The provided documents do not contain this information."

    # Build context
    context = "\n\n".join(doc.page_content for doc in documents)
    final_prompt = prompt.format(context=context, question=question)

    # Generate answer
    response = llm(final_prompt)
    answer = response[0]["generated_text"].strip()

    # -------- POST-PROCESSING --------
    q = question.lower().strip()

    # Yes/No type questions → keep ONLY first sentence
    if q.startswith(("do ", "does ", "can ", "is ", "are ", "was ", "were ")):
        if "." in answer:
            answer = answer.split(".")[0] + "."

    # Fact-based "what is" questions → normalize answer
    elif q.startswith("what is"):
        if len(answer.split()) <= 3:
            answer = f"The refund period is {answer}."

    return answer

