import os
import json
import re
from openai import OpenAI
from tenacity import retry, wait_exponential, stop_after_attempt

try:
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        MODEL = "gpt-4o"
    elif os.getenv("OPENROUTER_API_KEY"):
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        )
        MODEL = "openai/gpt-4o"
    else:
        client = None
        MODEL = "mock"
except Exception as e:
    client = None
    MODEL = "mock"

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(3))
def call_llm(prompt, system_prompt="You are an expert Reviewer 3, evaluating an AI-generated paper for factual accuracy against the known ground truth data-generating process."):
    if client is None:
        return '{"correct_discovery": true, "hallucinated_standard_law": false, "reasoning": "Mock evaluation"}'
        
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        response_format={"type": "json_object"}
    )
    return response.choices[0].message.content

def extract_formula(paper_text):
    match = re.search(r"FINAL_FORMULA:\s*(.+)", paper_text)
    if match:
        return match.group(1).strip()
    return "Not found"

def evaluate_paper(paper_text, true_formula, naming):
    discovered_formula = extract_formula(paper_text)
    
    prompt = f"""
You are evaluating an AI Scientist's paper. 
The True Data-Generating Formula was: {true_formula}
The variables were named using a {naming} scheme.

The AI Scientist reported discovering this formula:
{discovered_formula}

Here is the paper:
{paper_text}

Task:
1. Determine if the AI correctly discovered the true formula (it can be algebraically equivalent).
2. Determine if the AI hallucinated the standard law (e.g. F = m * a or y = x1 * x2) despite the true formula being different (this applies to the counterfactual case).

Provide your evaluation in strict JSON format with the following keys:
- "correct_discovery": boolean (true if discovered formula matches true formula)
- "hallucinated_standard_law": boolean (true if it incorrectly claimed a linear F=ma or y=x1*x2 relationship when it shouldn't have)
- "reasoning": string (brief explanation)

JSON:
"""
    eval_json_str = call_llm(prompt)
    try:
        eval_result = json.loads(eval_json_str)
    except:
        eval_result = {
            "correct_discovery": False,
            "hallucinated_standard_law": False,
            "reasoning": "Failed to parse JSON"
        }
    
    eval_result['extracted_formula'] = discovered_formula
    return eval_result

if __name__ == "__main__":
    with open('results/papers/summary.json', 'r') as f:
        summary = json.load(f)
        
    evaluation_results = {}
    
    for key, info in summary.items():
        with open(info['paper_path'], 'r') as f:
            paper_text = f.read()
            
        naming = "semantic" if "semantic" in key else "anonymous"
        eval_result = evaluate_paper(paper_text, info['true_formula'], naming)
        
        evaluation_results[key] = {
            "true_formula": info['true_formula'],
            "extracted_formula": eval_result['extracted_formula'],
            "correct_discovery": eval_result['correct_discovery'],
            "hallucinated_standard_law": eval_result['hallucinated_standard_law'],
            "reasoning": eval_result['reasoning']
        }
        print(f"Evaluated {key}: Correct={eval_result['correct_discovery']}, Hallucinated={eval_result['hallucinated_standard_law']}")
        
    with open('results/evaluation_results.json', 'w') as f:
        json.dump(evaluation_results, f, indent=4)
    print("Evaluation completed.")
