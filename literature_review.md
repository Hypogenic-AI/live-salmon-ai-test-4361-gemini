# Literature Review: Live Salmon Test for AI Scientists

## Research Area Overview
The "Live Salmon Test" for AI Scientists is a methodological evaluation framework inspired by the "Dead Salmon" fMRI study. While the original study demonstrated how uncorrected statistical methods could "discover" brain activity in a dead salmon, the "Live Salmon" version evaluates whether autonomous AI research agents can genuinely discover scientific laws from a data-generating process (simulation) or if they merely "remix" training data or produce statistically significant but meaningless results. This area is at the intersection of **Autonomous Scientific Discovery (ASD)**, **AI-driven Science (AI4Science)**, and **Benchmark Rigor**.

## Key Papers

### 1. The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery
- **Authors**: Cong Lu, Robert Tjarko Lange, et al. (Sakana AI)
- **Year**: 2024
- **Key Contribution**: Introduced the first comprehensive framework for fully automated scientific discovery, handling the entire research lifecycle from idea generation to paper writing.
- **Methodology**: Uses LLMs to iterate on code, run experiments, and write manuscripts in LaTeX.
- **Relevance**: Foundation of the current "AI Scientist" trend. It uses templates for known ML tasks, which the "Live Salmon" test aims to move beyond by using novel data-generating processes.

### 2. The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search
- **Authors**: Yutaro Yamada, Robert Tjarko Lange, et al. (Sakana AI)
- **Year**: 2025
- **Key Contribution**: Eliminated the reliance on human-authored code templates and introduced agentic tree search for deeper exploration.
- **Methodology**: Employs a Vision-Language Model (VLM) feedback loop and a progressive search algorithm.
- **Relevance**: Represents the state-of-the-art in autonomous research agents.

### 3. PhysGym: Benchmarking LLMs in Interactive Physics Discovery with Controlled Priors
- **Authors**: Yimeng Chen, Piotr Piekos, et al.
- **Year**: 2025
- **Key Contribution**: A benchmark suite for evaluating scientific reasoning in interactive physics environments with "Controlled Prior Knowledge."
- **Methodology**: Agents must probe environments and gather data to formulate hypotheses. It specifically controls variable naming (from descriptive to anonymized) to test for memorization.
- **Relevance**: Directly implements the "Live Salmon" concept by providing a controlled simulator ("live" process).

### 4. NewtonBench: Benchmarking Generalizable Scientific Law Discovery in LLM Agents
- **Authors**: Tianshi Zheng, Kelvin Tam, et al.
- **Year**: 2025
- **Key Contribution**: Addresses the "evaluation trilemma" using **Counterfactual Law Shifts**.
- **Methodology**: Systematic alterations of canonical laws (e.g., changing the exponent of gravity) to ensure agents cannot rely on memorized textbook formulas.
- **Relevance**: A core "Live Salmon" testbed that prevents memorization by shifting the underlying data-generating process.

### 5. Gravity-Bench-v1: A Benchmark on Gravitational Physics Discovery for Agents
- **Authors**: Nolan Koblischke, et al.
- **Year**: 2025
- **Key Contribution**: Focuses on **Strategic Observation Planning** with limited budgets.
- **Methodology**: Challenges agents to act as astronomers observing binary systems and discovering hidden physics in out-of-distribution (OOD) scenarios.
- **Relevance**: Evaluates the agent's ability to "see" the salmon by planning observations efficiently.

### 6. The More You Automate, the Less You See: Hidden Pitfalls of AI Scientist Systems
- **Authors**: Ziming Luo, Atoosa Kasirzadeh, Nihar B. Shah
- **Year**: 2025
- **Key Contribution**: Critical analysis of failure modes: benchmark selection, data leakage, metric misuse, and post-hoc selection bias.
- **Relevance**: The "Reviewer 3" perspective on the Live Salmon Test, warning that AI-generated papers can hide significant methodological flaws.

## Common Methodologies
- **Interactive Probing**: Moving from static datasets to simulators where agents can actively experiment.
- **Anonymization**: Renaming physical variables to `x`, `y`, `z` to prevent the agent from using semantic priors.
- **Counterfactual Shifts**: Changing fundamental constants or laws to test for genuine mechanistic inference.
- **Automated Peer Review**: Using LLM-based reviewers to evaluate the output papers.

## Gaps and Opportunities
- **Cross-Domain Generalization**: Most benchmarks are limited to physics; biology and chemistry remain challenging.
- **Methodological Transparency**: As highlighted by Luo et al., there is a need for trace-log auditing.
- **High-Fidelity Simulation**: Integrating more complex engineering software (e.g., COMSOL in FEABench).

## Recommendations for Our Experiment
- **Simulator**: Use **NewtonBench** or **PhysGym** as they provide the most robust "Live Salmon" (controlled data-generating process).
- **Control**: Implement variable anonymization (as in PhysGym) to distinguish between memorization and discovery.
- **Audit**: Collect and analyze the "thought traces" of the AI Scientist to detect the pitfalls identified by Luo et al.
