# Research Plan: Live Salmon Test for AI Scientists

## Motivation & Novelty Assessment

### Why This Research Matters
As fully automated AI scientists (like Sakana's AI Scientist) become more prevalent, it is critical to evaluate whether they are genuinely discovering new knowledge or simply regurgitating and pattern-matching their training data. A "Live Salmon Test" provides a controlled methodology where we know the ground truth of a data-generating process, allowing us to definitively score the AI's scientific discoveries and highlight methodological flaws or hallucinated findings in their generated papers.

### Gap in Existing Work
Existing AI Scientist benchmarks often evaluate models on standard machine learning tasks (where the model might just be applying known templates) or standard physics data. While benchmarks like PhysGym and NewtonBench introduce controlled priors, there is a lack of end-to-end evaluation that explicitly treats the AI Scientist as a test subject generating full academic papers from an intentionally anomalous "Live Salmon" data source, and evaluating the scientific validity of the resulting papers.

### Our Novel Contribution
We introduce a lightweight, end-to-end "Live Salmon" pipeline where an AI Scientist is provided with data from a synthetic, counterfactual physical law (e.g., $F = m \cdot a^2$ or a complex non-linear relationship). We then prompt the LLM to act as an AI Scientist: analyze the data, discover the underlying law, and write a short academic paper. We evaluate the resulting papers for correct insight versus hallucinated adherence to standard physics.

### Experiment Justification
- **Experiment 1: Standard Law vs Counterfactual Law**: We need to test if the AI Scientist can discover a counterfactual law (the "live salmon") just as well as a standard law ($F=ma$). This isolates genuine discovery capabilities from training data memorization.
- **Experiment 2: Variable Anonymization**: By hiding variable semantics (e.g., calling mass "x1" and acceleration "x2"), we test if the AI Scientist relies on semantic priors rather than empirical data to formulate its conclusions.
- **Experiment 3: Peer Review Evaluation**: Evaluating the AI-generated papers using another LLM as a "Reviewer 3" to see if automated peer review catches the errors or hallucinations when the AI Scientist fails the Live Salmon test.

## Research Question
Can AI Scientists genuinely discover and articulate novel, counterfactual physical laws from raw data, or do their generated papers default to hallucinating standard, memorized scientific laws regardless of empirical evidence?

## Hypothesis Decomposition
1. When given data from a counterfactual law with semantic variable names (e.g., Mass, Acceleration), the AI Scientist will experience negative transfer and attempt to fit the standard law ($F=ma$), failing the "Live Salmon" test.
2. When variable names are anonymized, the AI Scientist will perform better at genuine empirical discovery because semantic priors are removed.
3. The papers produced by the AI Scientist will sound highly plausible and statistically rigorous even when the underlying scientific conclusion is completely wrong, demonstrating the hidden pitfalls of automated science.

## Proposed Methodology

### Approach
We will simulate a simplified "AI Scientist" pipeline. Instead of running the massive, multi-day Sakana AI codebase, we will write a streamlined Python script that:
1. Generates synthetic datasets based on known generating processes.
2. Prompts a state-of-the-art LLM (via OpenRouter API, e.g., GPT-4o or Claude 3.5 Sonnet) to analyze the data, formulate a hypothesis, and write a concise "research paper" (Abstract, Method, Results, Conclusion).
3. Parses the paper to evaluate whether the discovered law matches the true generating process.

### Experimental Steps
1. **Data Generation**: Create datasets for 4 conditions:
   - Standard Physics ($F = ma$), Semantic names
   - Standard Physics ($F = ma$), Anonymous names (x, y, z)
   - Counterfactual Physics ($F = m \cdot a^2$), Semantic names
   - Counterfactual Physics ($F = m \cdot a^2$), Anonymous names
2. **AI Scientist Execution**: For each dataset, prompt the LLM to act as a data scientist, discover the formula relating the variables, and write a short paper summarizing the findings.
3. **Evaluation**: Extract the discovered formula from the papers and compare it to the ground truth. Score the papers on factual accuracy, plausibility, and presence of hallucinations.

### Baselines
We will compare the performance across the 4 conditions to understand the impact of semantic priors vs. counterfactual data.

### Evaluation Metrics
- **Discovery Accuracy**: Binary score of whether the final paper correctly identifies the exact data-generating formula.
- **Hallucination Rate**: Frequency of the AI Scientist claiming a standard law ($F=ma$) when the data actually follows a counterfactual law.
- **Plausibility Score**: How convincing the paper is (graded by an LLM Reviewer).

### Statistical Analysis Plan
Descriptive statistics of success rates across conditions. Qualitative analysis of the generated papers to identify specific failure modes and hallucinations.

## Timeline and Milestones
- Phase 2: Environment Setup & Data Generation (15 min)
- Phase 3: AI Scientist Pipeline Implementation (40 min)
- Phase 4: Experiment Execution (30 min)
- Phase 5: Result Analysis (20 min)
- Phase 6: Documentation and Report Writing (15 min)
