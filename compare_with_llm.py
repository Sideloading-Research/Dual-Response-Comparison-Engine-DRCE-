# compare_with_llm.py

import argparse
import json
from parse_markdown import parse_markdown_answers
from openai import OpenAI  # or your LLM client (Anthropic, Gemini, etc.)

def compare_qa_with_llm(original, generated, model="gpt-4"):
    client = OpenAI()  # Configure your API key properly
    comparison_results = {}

    for question in original:
        orig_ans = original.get(question, "")
        gen_ans = generated.get(question, "")

        prompt = f"""
Compare the following two answers to the same question. 
Rate from 0 to 10 for:
- Semantic similarity
- Stylistic similarity
- Authenticity to human voice

Question: {question}
Original answer: {orig_ans}
Generated answer: {gen_ans}
Respond with JSON like:
{{"semantic": ..., "style": ..., "authenticity": ..., "summary": "..."}}
"""

        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        score = response.choices[0].message.content
        try:
            comparison_results[question] = json.loads(score)
        except:
            comparison_results[question] = {"error": "LLM response parsing failed", "raw": score}

    return comparison_results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", required=True, help="Original file (markdown)")
    parser.add_argument("--b", required=True, help="Generated file (markdown)")
    parser.add_argument("--model", default="gpt-4", help="LLM model")
    parser.add_argument("--output", default="comparison_scores.json")

    args = parser.parse_args()

    original = parse_markdown_answers(args.a)
    generated = parse_markdown_answers(args.b)

    result = compare_qa_with_llm(original, generated, model=args.model)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"[✔] Comparison completed. Output written to {args.output}")
