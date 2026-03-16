# Live Salmon Test for AI Scientists

## Project Overview
This repository implements the **Live Salmon Test** for AI Scientists—an empirical methodology designed to determine if autonomous AI agents genuinely discover scientific laws from data or if they merely regurgitate memorized, standard textbooks laws due to semantic priors. By using controlled, counterfactual data-generating processes (the "live salmon"), we evaluate the AI's ability to resist negative transfer and confirmation bias.

## Key Findings
- **Semantic Hallucinations**: When variables were named semantically (e.g., "mass", "acceleration"), but the data was generated using a counterfactual law ($F = m \cdot a^2$), the AI Scientist completely ignored the data and confidently hallucinated the standard textbook law ($F = ma$). It even hallucinated a "perfect fit ($R^2 = 1$)" to support its false claim.
- **Anonymization Mitigates Hallucination**: When the same counterfactual data was presented with anonymous variables (`x1`, `x2`, `y`), the AI did not hallucinate the standard linear law, although it struggled to find the exact non-linear relationship without computational tools.
- **Hidden Pitfalls**: Automated science agents are highly vulnerable to semantic confirmation bias. They prioritize generating plausible, consensus-aligned text over rigorous empirical inference.

## How to Reproduce
The experiment is fully automated and runs via a single python script. 

1. **Environment Setup**:
   Ensure you have `uv` or `pip` installed.
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install numpy pandas openai tenacity
   ```
2. **API Keys**:
   Set your OpenAI API key or OpenRouter API key as an environment variable.
   ```bash
   export OPENAI_API_KEY="your_key"
   ```
3. **Run Pipeline**:
   ```bash
   python src/run_experiments.py
   ```
   This will generate the synthetic datasets in `datasets/live_salmon/`, run the AI Scientist to generate papers in `results/papers/`, and evaluate the hallucination rates in `results/evaluation_results.json`.

## File Structure Overview
- `src/data_generator.py`: Generates standard and counterfactual physics datasets.
- `src/ai_scientist.py`: Prompts the LLM to act as a data scientist, discover the law, and write a paper.
- `src/evaluator.py`: Acts as "Reviewer 3" to evaluate if the AI hallucinated standard laws.
- `src/run_experiments.py`: Orchestrates the end-to-end pipeline.
- `REPORT.md`: Comprehensive research report detailing the methodology and the empirical findings.
- `datasets/live_salmon/`: Directory containing the synthetic data generated for the experiments.
- `results/`: Directory containing the generated AI papers and the final evaluation JSON.

## Documentation
For full details on the experimental setup, hypotheses, and in-depth discussion, please refer to [REPORT.md](./REPORT.md).
