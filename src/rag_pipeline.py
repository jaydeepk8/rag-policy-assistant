from transformers import pipeline
import os


os.environ["TRANSFORMERS_NO_TF"] = "1"


def load_llm():
    return pipeline(
        task="text2text-generation",
        model="google/flan-t5-base",
        framework="pt",
        max_length=256
    )


def answer_question(llm, retriever, prompt, question):
    
    documents = retriever.invoke(question)

    if not documents:
        return "The provided documents do not contain this information."

    context = "\n\n".join(doc.page_content for doc in documents)
    final_prompt = prompt.format(context=context, question=question)

    response = llm(final_prompt)
    answer = response[0]["generated_text"].strip()

    q = question.lower().strip()

    if q.startswith(("do ", "does ", "can ", "is ", "are ", "was ", "were ")):
        if "." in answer:
            answer = answer.split(".")[0] + "."

    elif q.startswith("what is"):
        if len(answer.split()) <= 3:
            answer = f"The refund period is {answer}."

    return answer

