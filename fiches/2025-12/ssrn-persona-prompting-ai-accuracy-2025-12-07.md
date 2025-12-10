# Veille Technologique

## Titre Article
Playing Pretend: Expert Personas Don't Improve Factual Accuracy

## Date
2025-12-07

## URL
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722

## Keywords
AI Prompting, Persona Prompts, LLM Accuracy, AI Benchmarking, GPQA Diamond, MMLU-Pro, AI Performance, Prompt Engineering, Expert Personas, AI Evaluation

## Authors
Savir Basil, Ina Shapiro, Dan Shapiro, Ethan Mollick, Lilach Mollick, Lennart Meincke (Generative AI Labs, The Wharton School, University of Pennsylvania)

## Résumé
This study from the Generative AI Labs at Wharton examines whether assigning expert personas to AI models improves their performance on difficult objective multiple-choice questions. The research tested six models (GPT-4o, GPT-4o-mini, o3-mini, o4-mini, Gemini 2.0 Flash, Gemini 2.5 Flash) on two challenging benchmarks: GPQA Diamond (graduate-level questions) and MMLU-Pro (professional-level questions). The findings show that persona prompts generally do not improve factual accuracy and can sometimes degrade performance, particularly with low-knowledge personas.

## Points Clés

### Study Design
- **Benchmarks Used**: GPQA Diamond (198 PhD-level questions) and MMLU-Pro (300 professional questions)
- **Models Tested**: GPT-4o, GPT-4o-mini, o3-mini, o4-mini, Gemini 2.0 Flash, Gemini 2.5 Flash
- **Prompt Variations**: Baseline (no persona), expert personas, low-knowledge personas
- **Methodology**: 25 independent responses per question per model-prompt pair

### Key Findings

#### Overall Performance Impact
- **No Significant Improvement**: Most persona conditions produced performance statistically indistinguishable from baseline
- **Negative Effects**: Low-knowledge personas (Toddler, Young Child, Layperson) often reduced accuracy
- **Model-Specific Results**: Gemini 2.0 Flash showed small improvements with expert personas
- **Domain Matching**: Aligning expert personas with question domains did not consistently improve performance

#### Specific Results by Benchmark

**GPQA Diamond Results:**
- No expert or low-knowledge persona reliably improved performance over baseline
- Only exception: "Young Child" prompt on Gemini 2.5 Flash showed small gain (RD = 0.098)
- Low-knowledge personas reduced accuracy on o4-mini and GPT-4o
- Domain-tailored personas showed no positive significant differences

**MMLU-Pro Results:**
- No expert persona showed positive statistically significant improvement for 5/6 models
- Nine statistically significant negative differences observed
- Gemini 2.0 Flash exception: modest positive differences for all five expert personas
- "Toddler" prompt reduced performance in 4/6 models
- Domain analysis: Gemini 2.0 Flash improved in Engineering and Chemistry domains

#### Persona Types Tested

**Expert Personas:**
- Physics Expert, Math Expert, Economics Expert, Biology Expert, Chemistry Expert
- Engineering Expert, Law Expert, History Expert
- Elaborate prompts designed to engage models with domain-specific frameworks

**Low-Knowledge Personas:**
- Layperson: "You are a layperson with no special training in this subject"
- Young Child: "You are a young child who thinks they understand the world but sometimes mixes things up"
- Toddler: "You are a 4-year-old toddler who thinks the moon is made of cheese"

### Statistical Analysis
- **Sample Size**: 4,950 runs per model-prompt pair (GPQA), 7,500 runs (MMLU-Pro)
- **Primary Metric**: Average Rating (fraction of correct answers across 25 trials)
- **Additional Metrics**: 100% correct (25/25), 90% correct (23/25), 51% correct (13/25)
- **Confidence Intervals**: 95% confidence intervals reported for all results

### Failure Modes Identified
- **Refusal Behavior**: Gemini Flash models often declined to answer when given out-of-domain expert personas
- **Over-Specialization**: Narrow role instructions caused models to under-utilize actual knowledge
- **Performance Degradation**: Toddler persona was significantly worse than Layperson in 5/6 models

## Analyse

### Persona Prompting Effectiveness
The study provides empirical evidence challenging the common practice of persona prompting:

1. **Limited Benefits**: Expert personas do not reliably improve factual accuracy across models and benchmarks
2. **Potential Harms**: Low-knowledge personas consistently reduce performance, especially "Toddler"
3. **Model Variability**: Effects are model-specific, with Gemini 2.0 Flash showing some improvements
4. **Domain Independence**: Matching personas to question domains does not provide consistent benefits

### Industry Implications

1. **Prompt Engineering Practices**: Current industry recommendations may need revision
2. **Benchmark vs Real-World**: Academic benchmarks may not reflect real-world use cases
3. **Alternative Strategies**: Organizations may get more value from task-specific instructions than personas
4. **Testing Requirements**: Multiple prompt variations should be tested for specific problems

### Methodological Contributions

1. **Rigorous Testing**: Large sample sizes (25 trials per question) provide statistical power
2. **Comprehensive Coverage**: Multiple models, benchmarks, and persona types tested
3. **Real-World Alignment**: Zero-shot prompting mirrors actual user interactions
4. **Transparency**: Detailed statistical reporting and supplementary materials provided

### Limitations and Future Research

1. **Model Coverage**: Only tested a subset of available models
2. **Benchmark Focus**: Academic benchmarks may not represent all real-world scenarios
3. **Persona Scope**: Limited number of domains and persona types tested
4. **Context Factors**: Did not examine interaction with other prompting techniques

## Conclusion

This study from Wharton's Generative AI Labs provides definitive evidence that expert personas do not reliably improve AI model accuracy on difficult factual questions. The research demonstrates:

1. **Null Results**: Across six models and two challenging benchmarks, persona prompts generally leave performance unchanged
2. **Negative Effects**: Low-knowledge personas often reduce accuracy, with "Toddler" being particularly harmful
3. **Model-Specific Exceptions**: Gemini 2.0 Flash shows some improvements, but these appear isolated
4. **Practical Recommendations**: Organizations should focus on task-specific instructions rather than persona prompts
5. **Research Direction**: Future work should explore alternative prompting strategies and real-world applications

The findings suggest that the widespread industry practice of persona prompting may be ineffective for improving factual accuracy, though personas may still serve other purposes such as altering output tone or presentation style.

## Références

- SSRN Paper: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722
- PDF Download: https://download.ssrn.com/2025/12/7/5879722.pdf
- GPQA Diamond Benchmark: Rein et al. (2024)
- MMLU-Pro Benchmark: Wang et al. (2024)
- Previous Prompting Science Reports: Meincke et al. (2025a, 2025b, 2025c)
- Anthropic Prompt Engineering Guide: https://www.anthropic.com/news/prompt-engineering-for-business-performance
- Google Vertex AI Prompt Design: https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies

## Hashtags
#AIPrompting #Personas #LLMAccuracy #AIResearch #PromptEngineering #AIBenchmarking #GenerativeAI #AIPerformance #WhartonAI #AIEvaluation