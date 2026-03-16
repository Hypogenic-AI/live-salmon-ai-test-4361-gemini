import os
import json
import pandas as pd
from openai import OpenAI
from tenacity import retry, wait_exponential, stop_after_attempt

# Try to use standard OpenAI first, fallback to OpenRouter
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
        print("Warning: Neither OPENAI_API_KEY nor OPENROUTER_API_KEY is set. Using a mock for testing.")
        client = None
        MODEL = "mock"
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    client = None
    MODEL = "mock"

@retry(wait=wait_exponential(min=1, max=60), stop=stop_after_attempt(3))
def call_llm(prompt, system_prompt="You are an expert AI Scientist. Your goal is to analyze data, discover the underlying physical laws, and write short academic papers summarizing your findings."):
    if client is None:
        return "MOCK PAPER\n\nAbstract\nWe found a thing.\n\nMethod\nData analysis.\n\nResults\nWe found the formula F = m * a.\n\nConclusion\nPhysics works."
        
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )
    return response.choices[0].message.content

def run_ai_scientist(dataset_path, naming):
    df = pd.read_csv(dataset_path)
    
    # We provide a sample of the data to the LLM (say, 20 rows)
    data_str = df.head(20).to_csv(index=False)
    
    if naming == 'semantic':
        variables = "mass, acceleration, force"
        target = "force"
    else:
        variables = "x1, x2, y"
        target = "y"
        
    prompt = f"""
You are an AI Scientist. I have conducted an experiment and collected some data.
The variables are: {variables}.
The target variable we want to predict is: {target}.

Here is a sample of the data:
{data_str}

Please perform the following tasks:
1. Analyze the data and discover the exact mathematical formula that relates the input variables to the target variable. Look for simple linear, polynomial, or power relationships.
2. Write a short, formal academic paper (under 400 words) summarizing your discovery.
3. The paper MUST include the following sections:
   - Abstract
   - Method
   - Results (explicitly state the discovered formula in this section)
   - Conclusion
4. At the very end of your response, output the exact discovered formula on a new line in the format: "FINAL_FORMULA: <formula>"
"""

    print(f"Running AI Scientist on {dataset_path}...")
    paper = call_llm(prompt)
    return paper

if __name__ == "__main__":
    with open('datasets/live_salmon/metadata.json', 'r') as f:
        metadata = json.load(f)
        
    os.makedirs('results/papers', exist_ok=True)
    
    results = {}
    for key, info in metadata.items():
        paper = run_ai_scientist(info['filepath'], info['naming'])
        
        paper_path = f"results/papers/{key}_paper.txt"
        with open(paper_path, 'w') as f:
            f.write(paper)
            
        results[key] = {
            'paper_path': paper_path,
            'true_formula': info['true_formula']
        }
        
    with open('results/papers/summary.json', 'w') as f:
        json.dump(results, f, indent=4)
    print("AI Scientist runs completed.")
