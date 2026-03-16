# Resources Catalog: Live Salmon Test for AI Scientists

## Papers
Total papers downloaded: 6

| Title | Authors | Year | ArXiv ID | File |
|-------|---------|------|----------|------|
| The AI Scientist (v1) | Cong Lu et al. | 2024 | 2408.06292 | papers/2408.06292_The_AI_Scientist_v1.pdf |
| The AI Scientist-v2 | Yutaro Yamada et al. | 2025 | 2504.08066 | papers/2504.08066_The_AI_Scientist_v2.pdf |
| NewtonBench | Tianshi Zheng et al. | 2025 | 2501.03154 | papers/2501.03154_NewtonBench.pdf |
| Gravity-Bench-v1 | Nolan Koblischke et al. | 2025 | 2501.06789 | papers/2501.06789_GravityBench.pdf |
| PhysGym | Yimeng Chen et al. | 2025 | 2507.15550 | papers/2507.15550_PhysGym.pdf |
| Hidden Pitfalls | Ziming Luo et al. | 2025 | 2509.08713 | papers/2509.08713_Hidden_Pitfalls.pdf |

## Code Repositories
Total repositories cloned: 6

| Name | Source URL | Purpose | Location |
|------|------------|---------|----------|
| AI-Scientist | SakanaAI/AI-Scientist | ASD Framework | code/AI-Scientist/ |
| AI-Scientist-v2 | SakanaAI/AI-Scientist-v2 | Workshop discovery | code/AI-Scientist-v2/ |
| NewtonBench | HKUST-KnowComp/NewtonBench | Physics Discovery | code/NewtonBench/ |
| GravityBench | NolanKoblischke/GravityBench | Gravitational Discovery | code/GravityBench/ |
| PhysGym | principia-ai/PhysGym | Interactive Discovery | code/PhysGym/ |
| AIScientistPitfalls | niharshah/AIScientistPitfalls | Critical Review tools | code/AIScientistPitfalls/ |

## Datasets
The datasets for this research are primarily **interactive simulators** contained within the code repositories.

| Name | Type | Size | Notes |
|------|------|------|-------|
| NewtonBench Tasks | Physics Tasks | 324 | Counterfactual law shifts |
| PhysGym Problems | Physics Problems | 97 | Controlled priors |
| GravityBench Orbits | Simulations | - | Binary star systems |
| Pitfall Logs | Trace Logs | ~1 GB | Audit data from AI Scientist |

## Recommendations for Experiment Design
1. **Primary Tool**: Use **AI-Scientist-v2** as the research agent.
2. **Benchmark Environment**: Use **NewtonBench** or **PhysGym** as they provide the best implementation of the "Live Salmon" (known data-generating process with controlled variables).
3. **Control Group**: Run agents on "Dead Salmon" (standard physics laws with clear variable names) vs "Live Salmon" (shifted laws with anonymized names).
4. **Validation**: Use the metrics and auditing techniques from **Hidden Pitfalls** to verify the integrity of the agent's discoveries.
