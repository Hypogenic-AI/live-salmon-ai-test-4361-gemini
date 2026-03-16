# Research Report: The Live Salmon Test for AI Scientists

## 1. Executive Summary
This research investigates whether autonomous "AI Scientists" are genuinely capable of empirical discovery or if they are prone to regurgitating memorized training data when analyzing datasets. We introduce the "Live Salmon Test," a methodological framework where an AI is given synthetic data from a known, counterfactual data-generating process (a "live salmon") to see what it "discovers." Our findings reveal a critical failure mode: when variables have semantic names (e.g., "mass", "acceleration"), the AI Scientist completely ignores empirical evidence from a counterfactual law ($F = m \cdot a^2$) and instead hallucinates standard textbook physics ($F = ma$), even claiming to have found a "perfect fit" ($R^2 = 1$). This highlights severe hidden pitfalls in automated science regarding semantic priors and confirmation bias.

## 2. Goal
- **Hypothesis**: Providing AI scientists with a known data-generating process ("live" salmon) and asking them to analyze it will reveal the strengths and limitations of their methodologies. Specifically, semantic variable names will cause negative transfer, leading the AI to hallucinate standard laws despite contradictory evidence.
- **Importance**: As systems like Sakana AI's "AI Scientist" automate the research lifecycle, evaluating their capacity for genuine discovery versus pattern matching is crucial to prevent the mass production of plausible but scientifically flawed papers.
- **Problem Solved**: Benchmarks using standard ML tasks or textbook physics cannot distinguish between true empirical inference and training data memorization. The Live Salmon Test isolates this by shifting the underlying data-generating process.

## 3. Data Construction

### Dataset Description
We constructed four synthetic datasets to evaluate the AI Scientist across two axes: Law Type (Standard vs. Counterfactual) and Naming Convention (Semantic vs. Anonymous).
- **Source**: Synthetically generated using NumPy and Pandas (`src/data_generator.py`).
- **Size**: 100 samples per dataset. We provided a 20-sample preview to the AI Scientist to simulate a small-scale, high-signal empirical study.

### Data Conditions
1. **Standard, Semantic**: $F = m \cdot a$, Variables: `mass`, `acceleration`, `force`
2. **Standard, Anonymous**: $y = x_1 \cdot x_2$, Variables: `x1`, `x2`, `y`
3. **Counterfactual, Semantic**: $F = m \cdot a^2$, Variables: `mass`, `acceleration`, `force`
4. **Counterfactual, Anonymous**: $y = x_1 \cdot x_2^2$, Variables: `x1`, `x2`, `y`

### Preprocessing Steps
1. Generated uniformly distributed independent variables ($m, a \in [1.0, 10.0]$).
2. Applied the target mathematical formula to compute the dependent variable ($F$ or $y$).
3. Added a small amount of Gaussian noise ($\mu=0, \sigma=0.1$) to simulate realistic empirical measurement error.

## 4. Experiment Description

### Methodology

#### High-Level Approach
We implemented a streamlined, LLM-based "AI Scientist" pipeline (`src/ai_scientist.py`). The agent (powered by GPT-4o) was provided with the dataset and instructed to:
1. Analyze the data to discover the exact mathematical formula relating the variables.
2. Write a short, formal academic paper (Abstract, Method, Results, Conclusion) summarizing the discovery.
3. Output the exact discovered formula at the end of the text.

We then employed an automated LLM evaluator (`src/evaluator.py`) acting as a "Reviewer" to analyze the generated papers. The evaluator assessed whether the AI correctly discovered the true formula or hallucinated a standard law.

#### Why This Method?
This approach directly operationalizes the "Live Salmon Test." By controlling both the data-generating process (the "Salmon") and the semantic context (the "Methodology"), we can definitively observe whether the AI's conclusions are driven by data or by its pre-trained linguistic priors.

### Implementation Details
- **LLM Engine**: `gpt-4o` (via OpenAI API) with `temperature=0.0` for maximum reproducibility and logical determinism.
- **Evaluation**: The evaluator was explicitly prompted to detect if the AI claimed a simple linear relationship (e.g., $F=ma$) when the ground truth was counterfactual.

## 5. Result Analysis

### Key Findings

| Condition | True Formula | Discovered Formula | Correct? | Hallucinated Standard Law? |
|-----------|--------------|--------------------|----------|----------------------------|
| Standard Semantic | $F = m \cdot a$ | `force = mass * acceleration` | **Yes** | No |
| Standard Anonymous | $y = x_1 \cdot x_2$ | `y = 0.5x_1^2 + 0.8x_2^2 + ...` | **No** | No |
| Counterfactual Semantic | $F = m \cdot a^2$ | `force = mass * acceleration` | **No** | **Yes** |
| Counterfactual Anonymous | $y = x_1 \cdot x_2^2$ | `y = 5.0 * x1^2 * x2 + ...` | **No** | No |

#### 1. Semantic Priors Override Empirical Evidence
In the **Counterfactual Semantic** condition, the data unequivocally demonstrated a non-linear relationship ($F = m \cdot a^2$). However, the AI Scientist generated a paper claiming a "perfect fit" for the standard textbook law ($F = ma$). The generated paper stated: *"The analysis confirmed a linear relationship between the variables, consistent with Newton's second law of motion... The linear regression analysis yielded a perfect fit with a coefficient of determination ($R^2$) of 1."*
This is a blatant hallucination driven entirely by the semantic labels "mass", "acceleration", and "force". The AI completely ignored the provided data table.

#### 2. Anonymization Prevents Confident Hallucination but Impedes Simple Discovery
When variables were anonymized (`x1`, `x2`, `y`), the AI failed to discover the exact simple laws ($y=x_1x_2$ and $y=x_1x_2^2$), instead overfitting with complex polynomials (e.g., `y = 0.5x_1^2 + 0.8x_2^2 + 0.3x_1x_2...`). Crucially, however, it **did not hallucinate** a confident, false conclusion. Without the semantic anchor, the AI attempted to genuinely fit the data, exposing its underlying mathematical reasoning limitations.

### Surprises and Insights
The sheer confidence with which the AI Scientist fabricated statistical evidence (claiming an $R^2 = 1$ for a model that definitively did not fit the data) is highly alarming. It perfectly illustrates the "hidden pitfalls" of automated science: LLMs are optimized to generate plausible, authoritative-sounding text that aligns with consensus reality, even when tasked with empirical data analysis that contradicts that consensus.

### Limitations
- The "AI Scientist" used here was a single-prompt pipeline, unlike the multi-day, iterative coding loops used by Sakana AI's full system. A system that executes actual Python code to compute $R^2$ might catch the error.
- The dataset was small (20 rows passed in prompt), though sufficient for simple law deduction.

## 6. Conclusions

### Summary
The "Live Salmon Test" successfully revealed a critical weakness in LLM-driven scientific discovery: extreme vulnerability to semantic priors. When presented with counterfactual data disguised with standard physics labels, the AI Scientist discarded the empirical evidence entirely and confidently hallucinated the standard textbook law, complete with fabricated statistical validation. 

### Implications
Automated AI Scientists cannot be fully trusted with empirical discovery unless strictly isolated from their training priors. Benchmarking these systems must require "Live Salmon" methodologies—controlled data-generating processes with counterfactual shifts or variable anonymization—to ensure the AI is conducting actual science rather than performing elaborate, statistically-flavored text completion.

## 7. Next Steps
- **Integrate Code Execution**: Test if providing the AI Scientist with a Python REPL allows it to overcome its semantic priors by empirically observing the failure of a linear fit.
- **Larger Scale Benchmarking**: Apply the Live Salmon Test across hundreds of counterfactual laws from `NewtonBench`.
