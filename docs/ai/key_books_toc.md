
========================================
# Encyclopedia of LLMs (genai/Encyclopedia of LLMs and Foundation Models.pdf)
========================================

--- Page 7 ---
Contents
Abstract i
Preface iii
List of Figures xvii
1 F oundations and historical development 1
1.1 Introduction to Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1.1 Definition and Scope . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1.2 Historical Context and Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2 Evolution of Language Modeling Approaches . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2.1 Statistical Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2.2 Neural Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.3 The Transformer Revolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3.1 Attention Mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3.2 Transformer Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.3.3 Impact and Adoption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.4 The Pre-training and Fine-tuning Paradigm . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4.1 Transfer Learning in NLP . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4.2 Foundational Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.4.3 The Scaling Era Begins . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2 Core architectures and mechanisms 7
2.1 The Transformer Architecture in Depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.1 Self-Attention Mechanism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.2 Position-wise Feed-Forward Networks . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.3 Positional Encoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.1.4 Layer Normalization and Residual Connections . . . . . . . . . . . . . . . . . . . . 8
2.1.5 Causal Masking for Language Modeling . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2 Architecture Variants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.1 Encoder-Only Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.2 Decoder-Only Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.3 Encoder-Decoder Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3 Scaling Laws and Emergent Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3.1 Neural Scaling Laws . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3.2 Emergent Abilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3.3 In-Context Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Attention Mechanism Variations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4.1 Sparse Attention Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4.2 Efficient Attention Mechanisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.4.3 Rotary Position Embeddings (RoPE) . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.4.4 Grouped-Query Attention (GQA) . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.5 Tokenization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.5.1 Subword Tokenization Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.5.2 Vocabulary Size Trade-offs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.5.3 Impact on Model Behavior . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
v

--- Page 8 ---
vi CONTENTS
3 Major models and families 15
3.1 GPT Series . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.1.1 GPT-1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.1.2 GPT-2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.1.3 GPT-3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.1.4 GPT-4 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.1.5 GPT-4 Turbo and GPT-4o . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2 BERT and Encoder Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2.1 BERT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.2.2 BERT Variants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.3 T5 and Encoder-Decoder Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3.1 T5 (Text-to-Text Transfer Transformer) . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3.2 BART . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.3.3 UL2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.4 LLaMA and Open Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.4.1 LLaMA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.4.2 LLaMA 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.4.3 LLaMA 3 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.4.4 Open Model Ecosystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
3.5 Claude . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6 PaLM and Gemini . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.1 PaLM (Pathways Language Model) . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
3.6.2 Gemini . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.7 Specialized and Domain-Specific Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.7.1 Code Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.7.2 Scientific and Biomedical Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.7.3 Multilingual Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8 Mixture-of-Experts Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8.1 Architectural Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.8.2 Switch Transformer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.8.3 GLaM . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
3.8.4 Mixtral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
4 T raining methodologies 25
4.1 Pre-training Objectives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.1.1 Causal Language Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.1.2 Masked Language Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.1.3 Prefix Language Modeling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.1.4 Span Corruption . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2 Training Data and Curation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.1 Data Sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
4.2.2 Data Quality and Filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.2.3 Data Scaling Considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3 Optimization and Training Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3.1 Optimizers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3.2 Learning Rate Schedules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3.3 Gradient Clipping and Stability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.3.4 Mixed Precision Training . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.3.5 Batch Size and Accumulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4 Distributed Training and Parallelism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4.1 Data Parallelism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4.2 Model Parallelism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4.3 Zero Redundancy Optimizer (ZeRO) . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.4.4 3D Parallelism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.5 Fine-tuning Techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.5.1 Full Fine-tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.5.2 Parameter-Efficient Fine-Tuning (PEFT) . . . . . . . . . . . . . . . . . . . . . . . 29
4.6 Instruction Tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

--- Page 9 ---
CONTENTS vii
4.6.1 Motivation and Approach . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.6.2 Instruction Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.6.3 Self-Instruct and Data Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.7 Reinforcement Learning from Human Feedback (RLHF) . . . . . . . . . . . . . . . . . . . 31
4.7.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.7.2 RLHF Pipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.7.3 InstructGPT and ChatGPT . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.7.4 Challenges and Limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.8 Constitutional AI and RLAIF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.8.1 Constitutional AI . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.8.2 Direct Preference Optimization (DPO) . . . . . . . . . . . . . . . . . . . . . . . . . 33
5 Prompt engineering and interaction design 35
5.1 Foundations of prompting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.1.1 The role of prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.1.2 Prompt components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.1.3 Zero-shot, few-shot, and many-shot prompting . . . . . . . . . . . . . . . . . . . . 36
5.2 Advanced prompting techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.2.1 Chain-of-thought prompting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.2.2 Self-consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
5.2.3 Tree-of-thoughts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
5.2.4 Least-to-most prompting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
5.2.5 Decomposed prompting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.2.6 Self-refinement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.2.7 Reflexion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.3 Prompt optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.3.1 Manual prompt engineering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5.3.2 Automatic prompt optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.3.3 Prompt ensembles . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.4 Prompting for specific tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.4.1 Information extraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.4.2 Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.4.3 Generation tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.4.4 Reasoning and analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5 Prompt security and robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.1 Prompt injection attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.5.2 Defense strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.5.3 Prompt robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
5.6 Evaluation of prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.6.1 Performance metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.6.2 Evaluation methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.6.3 A/B testing for prompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.7 Prompting in production systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.7.1 Prompt management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.7.2 Dynamic prompting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.7.3 Cost optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
5.7.4 Monitoring and maintenance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
6 Capabilities and applications 47
6.1 Natural language understanding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.1.1 Text Classification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.1.2 Named Entity Recognition (NER) . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.1.3 Relation Extraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
6.1.4 Question Answering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
6.1.5 Semantic Similarity and Entailment . . . . . . . . . . . . . . . . . . . . . . . . . . 48
6.2 Text Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
6.2.1 Summarization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
6.2.2 Creative Writing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49

--- Page 10 ---
viii CONTENTS
6.2.3 Content Creation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
6.3 Translation and Multilingual Capabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.3.1 Machine Translation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.3.2 Cross-Lingual Transfer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.3.3 Code-Switching and Multilingual Dialogue . . . . . . . . . . . . . . . . . . . . . . . 50
6.4 Reasoning and Problem Solving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.4.1 Mathematical Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
6.4.2 Logical Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.4.3 Commonsense Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.4.4 Chain-of-Thought Prompting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.5 Code Understanding and Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.5.1 Code Completion and Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6.5.2 Code Understanding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.5.3 Code Translation and Refactoring . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.5.4 Testing and Debugging . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.6 Multimodal Capabilities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.6.1 Vision-Language Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.6.2 Document Understanding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
6.6.3 Audio and Speech . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
6.6.4 Video Understanding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
6.7 Domain-Specific Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.7.1 Healthcare and Biomedicine . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.7.2 Legal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.7.3 Education . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.7.4 Scientific Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
6.7.5 Business and Enterprise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
7 Evaluation and benchmarks 57
7.1 Evaluation Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7.1.1 Fundamental Difficulties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7.1.2 Automatic vs. Human Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . 57
7.2 Understanding Benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.2.1 GLUE and SuperGLUE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.2.2 Question Answering Benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.2.3 Commonsense Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.3 Reasoning and Problem-Solving Benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.3.1 Mathematical Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 58
7.3.2 Code Benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
7.3.3 Multi-Step Reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
7.4 Comprehensive Evaluation Suites . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
7.4.1 MMLU (Massive Multitask Language Understanding) . . . . . . . . . . . . . . . . 61
7.4.2 HELM (Holistic Evaluation of Language Models) . . . . . . . . . . . . . . . . . . . 61
7.4.3 LMSYS Chatbot Arena . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 62
7.5 Specialized Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7.5.1 Truthfulness and Hallucination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7.5.2 Safety and Toxicity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7.5.3 Multilingual Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7.5.4 Long-Context Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 63
7.6 Evaluation Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7.6.1 Perplexity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7.6.2 Accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7.6.3 F1 Score . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7.6.4 BLEU (Bilingual Evaluation Understudy) . . . . . . . . . . . . . . . . . . . . . . . 64
7.6.5 ROUGE (Recall-Oriented Understudy for Gisting Evaluation) . . . . . . . . . . . . 64
7.6.6 BERTScore . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
7.6.7 Pass@k . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 65

--- Page 11 ---
CONTENTS ix
8 Safety , ethics, and societal impact 67
8.1 Safety Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
8.1.1 Hallucination and Factual Accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . 67
8.1.2 Harmful Content Generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
8.1.3 Jailbreaking and Adversarial Prompts . . . . . . . . . . . . . . . . . . . . . . . . . 68
8.1.4 Prompt Injection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
8.2 Bias and Fairness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
8.2.1 Sources of Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
8.2.2 Types of Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
8.2.3 Measurement and Detection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
8.2.4 Mitigation Approaches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
8.2.5 Fundamental Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
8.3 Privacy and Data Protection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
8.3.1 Training Data Privacy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
8.3.2 Usage Privacy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
8.4 Intellectual Property and Copyright . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
8.4.1 Training Data Copyright . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
8.4.2 Generated Content Ownership . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
8.4.3 Code Generation Concerns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
8.5 Misuse and Dual Use . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
8.5.1 Potential Misuse Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72
8.5.2 Mitigation Strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
8.6 Societal Impact . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
8.6.1 Labor Market Effects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 73
8.6.2 Access and Equity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.6.3 Information Ecosystem Effects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.6.4 Education and Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
8.7 Governance and Regulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
8.7.1 Regulatory Approaches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
8.7.2 Industry Self-Governance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 75
8.7.3 Research and Development Governance . . . . . . . . . . . . . . . . . . . . . . . . 76
8.8 Alignment and Value Specification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
8.8.1 The Alignment Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
8.8.2 Technical Alignment Approaches . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
8.8.3 Value Pluralism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 77
9 Infrastructure and systems for LLM training 79
9.1 Hardware infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
9.1.1 Graphics processing units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 79
9.1.2 Tensor processing units . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
9.1.3 Alternative accelerators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
9.1.4 Networking infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
9.2 Distributed training systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
9.2.1 Parallelism strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81
9.2.2 Memory optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
9.2.3 Training frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
9.3 Communication optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
9.3.1 Collective operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
9.3.2 Communication-computation overlap . . . . . . . . . . . . . . . . . . . . . . . . . . 86
9.3.3 Compression techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
9.4 Training stability and efficiency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
9.4.1 Numerical stability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
9.4.2 Learning rate scheduling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
9.4.3 Checkpointing and fault tolerance . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
9.5 Efficiency techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
9.5.1 FlashAttention . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
9.5.2 Kernel fusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
9.5.3 Operator optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

--- Page 12 ---
x CONTENTS
9.6 Energy efficiency and sustainability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
9.6.1 Carbon footprint . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
9.6.2 Efficiency improvements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
9.6.3 Reporting and transparency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
10 Data science for large language models 91
10.1 Training data sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.1.1 Web-scale text corpora . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91
10.1.2 Curated text sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
10.1.3 Code repositories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 92
10.1.4 Conversational and instructional data . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.2 Data curation and preprocessing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.2.1 Quality filtering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93
10.2.2 Deduplication . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
10.2.3 Data mixing and sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94
10.3 Synthetic data generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
10.3.1 Instruction generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
10.3.2 Reasoning chain synthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
10.3.3 Code generation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
10.3.4 Quality and limitations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 96
10.4 Evaluation data contamination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.4.1 Sources of contamination . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.4.2 Detection methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.4.3 Mitigation strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.5 Multilingual data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.5.1 Language distribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
10.5.2 Multilingual corpora . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.5.3 Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.5.4 Cross-lingual transfer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.6 Legal and ethical considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.6.1 Copyright and licensing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.6.2 Privacy concerns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98
10.6.3 Bias and representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
10.6.4 Documentation practices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
10.7 Data infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
10.7.1 Storage and processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
10.7.2 Data loading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
10.7.3 Preprocessing pipelines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
11 Deployment and MLOps for LLMs 101
11.1 Inference optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
11.1.1 Quantization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101
11.1.2 Key-value cache optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
11.1.3 Batching strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102
11.1.4 Speculative decoding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
11.2 Serving infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
11.2.1 Inference servers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103
11.2.2 API design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
11.2.3 Load balancing and scaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104
11.3 Operational practices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
11.3.1 Monitoring and observability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
11.3.2 Cost management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
11.3.3 Security considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
11.4 Model lifecycle management . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
11.4.1 Version control . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
11.4.2 A/B testing and experimentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 106
11.4.3 Model updates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
11.5 Edge and on-device deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107

--- Page 13 ---
CONTENTS xi
11.5.1 Mobile deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
11.5.2 Browser deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
11.5.3 Embedded systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107
11.6 Retrieval-augmented generation deployment . . . . . . . . . . . . . . . . . . . . . . . . . . 108
11.6.1 Vector database integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
11.6.2 RAG pipeline components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
11.6.3 Operational considerations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
11.7 Fine-tuning operations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
11.7.1 Training infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
11.7.2 Continuous fine-tuning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108
11.7.3 PEFT deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
12 Industry landscape and economics 111
12.1 Major industry players . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
12.1.1 Frontier model developers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
12.1.2 Cloud providers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
12.1.3 Hardware providers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
12.2 Economic analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
12.2.1 Training costs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 113
12.2.2 Inference economics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114
12.2.3 Market sizing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
12.3 Business models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
12.3.1 API-as-a-service . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
12.3.2 Platform and infrastructure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
12.3.3 Vertical applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 115
12.3.4 Open-source monetization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
12.4 Competitive dynamics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
12.4.1 Moats and differentiation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
12.4.2 Open vs closed models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116
12.4.3 Consolidation trends . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
12.5 Investment landscape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
12.5.1 Venture capital . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
12.5.2 Corporate investment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
12.5.3 Public markets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
12.6 Regulatory and policy environment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
12.6.1 Emerging regulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
12.6.2 Policy debates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 118
12.7 Workforce and labor impacts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
12.7.1 Job displacement concerns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
12.7.2 Job creation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
12.7.3 Skill transformation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
12.7.4 Productivity effects . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
12.8 Geopolitical dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
12.8.1 US-China competition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
12.8.2 Technology sovereignty . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
12.8.3 International cooperation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120
13 Retrieval-augmented generation 121
13.1 Foundations of RAG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
13.1.1 Motivation and core concepts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
13.1.2 RAG architecture patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
13.2 Text embeddings and vector representations . . . . . . . . . . . . . . . . . . . . . . . . . . 122
13.2.1 Dense retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
13.2.2 Embedding models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
13.2.3 Sparse retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
13.2.4 Hybrid retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
13.3 Vector databases and indexing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
13.3.1 Approximate nearest neighbor search . . . . . . . . . . . . . . . . . . . . . . . . . . 123

--- Page 14 ---
xii CONTENTS
13.3.2 Vector database systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
13.3.3 Indexing strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
13.4 Retrieval optimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
13.4.1 Query processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
13.4.2 Reranking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
13.4.3 Multi-hop retrieval . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.5 RAG system design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.5.1 Context construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.5.2 Generation with retrieved context . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.5.3 Evaluation of RAG systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
13.6 Advanced RAG techniques . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
13.6.1 Agentic RAG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
13.6.2 Graph RAG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
13.6.3 Multimodal RAG . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
14 Agents and autonomous systems 129
14.1 Foundations of LLM agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
14.1.1 Definition and components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
14.1.2 Agent architectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129
14.1.3 Cognitive architectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
14.2 Memory systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
14.2.1 Short-term memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
14.2.2 Long-term memory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
14.2.3 Memory retrieval and consolidation . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
14.3 Tool use and function calling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
14.3.1 Function calling interfaces . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131
14.3.2 Tool categories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
14.3.3 Tool learning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
14.4 Planning and reasoning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
14.4.1 Task decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 132
14.4.2 Planning algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
14.4.3 Verification and error recovery . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
14.5 Multi-agent systems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
14.5.1 Agent collaboration patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133
14.5.2 Multi-agent frameworks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
14.5.3 Communication protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134
14.6 Agent applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
14.6.1 Code agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
14.6.2 Research agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
14.6.3 Web agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
14.6.4 Personal assistants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
14.7 Evaluation and benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
14.7.1 Agent benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135
14.7.2 Evaluation dimensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
14.8 Safety and alignment for agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
14.8.1 Risks specific to agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
14.8.2 Mitigation strategies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136
15 Interpretability and mechanistic understanding 137
15.1 Motivation for interpretability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
15.1.1 Why interpretability matters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
15.1.2 Levels of analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
15.2 Probing and representation analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
15.2.1 Linear probing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 137
15.2.2 Representation similarity analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
15.2.3 Geometry of representations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
15.3 Attention analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
15.3.1 Attention visualization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138


========================================
# Giao Trinh RAG (genai/giao_trinh_rag.pdf)
========================================

--- Page 1 ---
Giáo trình Retrieval-Augmented Generation
(RAG)
Giới thiệu
Giáo trình này cung cấp một cái nhìn tổng quan toàn diện về Retrieval-Augmented Generation (RAG),
một kỹ thuật tiên tiến kết hợp khả năng truy xuất thông tin từ các nguồn dữ liệu bên ngoài với sức mạnh
tạo nội dung của các mô hình ngôn ngữ lớn (LLM). RAG giúp LLM cung cấp các phản hồi chính xác, đáng
tin cậy và có căn cứ hơn bằng cách bổ sung kiến thức thực tế từ các nguồn bên ngoài, khắc phục hạn chế
về kiến thức tĩnh của LLM.
Giáo trình sẽ đi sâu vào các thành phần chính của RAG, bao gồm quá trình truy xuất (Retrieval) và quá
trình tạo sinh (Generation), cùng với các kỹ thuật tối ưu hóa và những thách thức thường gặp. Ngoài ra,
giáo trình còn bao gồm một dự án thực hành để học viên có thể áp dụng kiến thức đã học vào thực tế.
Mục lục
 . Giới thiệu về RAG và các thành phần chính
 . Retrieval (Truy xuất)
 . Generation (Tạo sinh)
 . Tối ưu hóa và các thách thức trong RAG
 . Dự án thực hành RAG
 . Giới thiệu về RAG và các thành phần chính
 . . RAG là gì?
Retrieval-Augmented Generation (RAG) là một kỹ thuật tiên tiến trong lĩnh vực Trí tuệ nhân tạo (AI) và Xử
lý ngôn ngữ tự nhiên (NLP) nhằm nâng cao khả năng của các mô hình ngôn ngữ lớn (Large Language
Models - LLM) bằng cách tích hợp khả năng truy xuất thông tin từ các nguồn dữ liệu bên ngoài. Thay vì
chỉ dựa vào kiến thức đã được huấn luyện trong quá trình đào tạo, RAG cho phép LLM tìm kiếm và sử
dụng thông tin liên quan từ một kho dữ liệu (knowledge base) để tạo ra các phản hồi chính xác, cập nhật
và có căn cứ hơn [ ,  ].
Các mô hình LLM truyền thống, mặc dù có khả năng tạo văn bản ấn tượng, thường gặp phải các vấn đề
như:
"Hallucination" (Ảo giác): Tạo ra thông tin sai lệch hoặc không có thật.

--- Page 2 ---
Kiến thức lỗi thời: Kiến thức của mô hình bị giới hạn bởi dữ liệu huấn luyện, không thể cập nhật
thông tin mới nhất.
Thiếu khả năng giải thích: Khó khăn trong việc truy xuất nguồn gốc của thông tin được tạo ra.
RAG ra đời để giải quyết những hạn chế này bằng cách cung cấp cho LLM một cơ chế để "tra cứu" thông
tin bên ngoài trước khi tạo ra câu trả lời. Điều này giúp tăng cường độ chính xác, độ tin cậy và khả năng
giải thích của các phản hồi do LLM tạo ra [ ].
 . . Tại sao RAG lại quan trọng?
RAG mang lại nhiều lợi ích đáng kể, đặc biệt trong các ứng dụng yêu cầu độ chính xác cao và thông tin
cập nhật:
Tăng cường độ chính xác và tin cậy: Bằng cách truy xuất thông tin từ các nguồn đáng tin cậy, RAG
giảm thiểu hiện tượng "hallucination" và đảm bảo các phản hồi dựa trên dữ liệu thực tế.
Cập nhật kiến thức liên tục: Mô hình có thể truy cập thông tin mới nhất mà không cần phải huấn
luyện lại toàn bộ LLM, giúp hệ thống luôn được cập nhật với dữ liệu mới.
Khả năng giải thích (Explainability): RAG cho phép người dùng hoặc hệ thống kiểm tra các nguồn
thông tin đã được sử dụng để tạo ra câu trả lời, tăng tính minh bạch và khả năng giải thích.
Giảm chi phí huấn luyện: Không cần huấn luyện lại LLM với dữ liệu mới, tiết kiệm tài nguyên tính
toán và thời gian.
Xử lý thông tin chuyên biệt: Cho phép LLM trả lời các câu hỏi về các lĩnh vực chuyên môn hoặc dữ
liệu nội bộ của tổ chức mà LLM chưa từng được huấn luyện.
 . . Các thành phần chính của hệ thống RAG
Một hệ thống RAG cơ bản thường bao gồm hai thành phần chính hoạt động song song:
 . . . Retrieval Module (Mô-đun Truy xuất)
Mô-đun Retrieval chịu trách nhiệm tìm kiếm và truy xuất các đoạn văn bản hoặc tài liệu liên quan từ một
kho dữ liệu lớn (knowledge base) dựa trên truy vấn của người dùng. Quá trình này thường bao gồm các
bước sau:
 . Chuyển đổi truy vấn: Truy vấn của người dùng được chuyển đổi thành một biểu diễn vector
(embedding) bằng cách sử dụng một mô hình nhúng (embedding model).
 . Tìm kiếm tương đồng: Biểu diễn vector của truy vấn được sử dụng để tìm kiếm các đoạn văn bản
có biểu diễn vector tương tự trong kho dữ liệu. Kho dữ liệu này thường được lưu trữ dưới dạng cơ sở
dữ liệu vector (vector database) để tăng tốc độ tìm kiếm.
 . Truy xuất tài liệu: Các tài liệu hoặc đoạn văn bản có độ tương đồng cao nhất với truy vấn sẽ được
truy xuất và chuyển đến mô-đun Generation [ ].

--- Page 3 ---
 . . . Generation Module (Mô-đun Tạo sinh)
Mô-đun Generation, thường là một mô hình ngôn ngữ lớn (LLM), nhận đầu vào là truy vấn ban đầu của
người dùng và các đoạn văn bản liên quan được truy xuất từ mô-đun Retrieval. Sau đó, LLM sẽ sử dụng
cả hai thông tin này để tạo ra một phản hồi mạch lạc, chính xác và phù hợp với ngữ cảnh [ ].
Quá trình này cho phép LLM:
Tổng hợp thông tin: Kết hợp kiến thức nội tại của mô hình với thông tin mới được truy xuất.
Tạo văn bản tự nhiên: Tạo ra câu trả lời bằng ngôn ngữ tự nhiên, dễ hiểu cho người dùng.
Cung cấp ngữ cảnh: Đảm bảo câu trả lời có liên quan trực tiếp đến truy vấn và các tài liệu đã truy
xuất.
 . . Quy trình hoạt động của RAG
Quy trình hoạt động của một hệ thống RAG có thể được tóm tắt như sau:
 . Người dùng gửi truy vấn: Người dùng đặt câu hỏi hoặc đưa ra yêu cầu.
 . Truy vấn được nhúng: Truy vấn được chuyển đổi thành một vector biểu diễn (query embedding).
 . Tìm kiếm trong kho kiến thức: Query embedding được sử dụng để tìm kiếm các đoạn văn bản liên
quan nhất trong kho kiến thức (đã được nhúng sẵn).
 . Truy xuất tài liệu: Các đoạn văn bản (chunks) có liên quan được truy xuất.
 . Tạo ngữ cảnh (Context Augmentation): Truy vấn ban đầu của người dùng và các đoạn văn bản
được truy xuất được kết hợp lại để tạo thành một ngữ cảnh đầu vào phong phú cho LLM.
 . Tạo phản hồi: LLM nhận ngữ cảnh đã được tăng cường và tạo ra câu trả lời cuối cùng cho người
dùng.
 . . Kết luận
RAG đại diện cho một bước tiến quan trọng trong việc phát triển các hệ thống AI đàm thoại và thông tin.
Bằng cách kết hợp sức mạnh của LLM với khả năng truy xuất thông tin hiệu quả, RAG mở ra nhiều ứng
dụng mới và cải thiện đáng kể hiệu suất của các hệ thống AI hiện có. Các chương tiếp theo sẽ đi sâu vào
từng thành phần của RAG, các kỹ thuật triển khai và những thách thức cần vượt qua.
Tài liệu tham khảo
[ ] AWS. (n.d.). RAG là gì? - Giải thích về AI tạo có kết hợp truy xuất thông tin ngoài. Retrieved from
https://aws.amazon.com/vi/what-is/retrieval-augmented-generation/ [ ] Viblo.asia. (n.d.). Tìm hiểu về
Retrieval Augmented Generation (RAG). Retrieved from https://viblo.asia/p/chatgpt-series- -tim-hieu-
ve-retrieval-augmented-generation-rag-Ny VGRd LPA [ ]    Lab. (    , March   ). RAG (Retrieval-
Augmented Generation) là gì? Giải thích dễ hiểu cho người mới bắt đầu. Retrieved from
https://   lab.io/blog/rag-la-gi/ [ ] Techbase.vn. (    , November   ). Retrieval Augmented Generation
(RAG) và    Thư Viện Mã Nguồn Mở Để Xây Dựng RAG. Retrieved from
https://www.techbasevn.com/blog-technical/retrieval-augmented-generation-rag-va-  -thu-vien-ma-

--- Page 4 ---
nguon-mo-de-xay-dung-rag.html [ ] FPT.AI. (    , January   ). Retrieval-Augmented Generation Cải
Thiện Phản Hồi Cho LLMs. Retrieved from https://fpt.ai/vi/bai-viet/retrieval-augmented-generation/
 . Retrieval (Truy xuất)
 . . Giới thiệu về Retrieval Module
Mô-đun Retrieval là trái tim của hệ thống RAG, chịu trách nhiệm tìm kiếm và truy xuất các thông tin liên
quan từ một kho dữ liệu lớn (knowledge base) để cung cấp ngữ cảnh cho mô hình ngôn ngữ lớn (LLM).
Mục tiêu chính của mô-đun này là đảm bảo rằng các tài liệu được truy xuất có chất lượng cao, phù hợp
và đa dạng, giúp LLM tạo ra các phản hồi chính xác và toàn diện [ ].
Quá trình truy xuất thường bao gồm việc chuyển đổi truy vấn của người dùng và các tài liệu trong kho
kiến thức thành các biểu diễn vector (embeddings), sau đó sử dụng các kỹ thuật tìm kiếm tương đồng để
xác định các tài liệu phù hợp nhất. Hiệu suất của mô-đun Retrieval ảnh hưởng trực tiếp đến chất lượng
đầu ra của toàn bộ hệ thống RAG.
 . . Các thành phần chính của Retrieval Module
 . . . Kho kiến thức (Knowledge Base)
Kho kiến thức là nơi lưu trữ tất cả các tài liệu mà hệ thống RAG có thể truy xuất. Đây có thể là:
Cơ sở dữ liệu văn bản: Các tài liệu dạng văn bản như bài viết, sách, báo cáo, tài liệu kỹ thuật, v.v.
Cơ sở dữ liệu có cấu trúc: Dữ liệu từ các bảng, cơ sở dữ liệu SQL, NoSQL.
Dữ liệu đa phương tiện: Hình ảnh, video, âm thanh (sau khi được chuyển đổi thành văn bản hoặc
biểu diễn có thể tìm kiếm).
Để tối ưu hóa quá trình truy xuất, các tài liệu trong kho kiến thức thường được chia nhỏ thành các đoạn
(chunks) nhỏ hơn và được chuyển đổi thành các vector nhúng (embeddings) trước khi lưu trữ. Kích thước
của các chunk là một yếu tố quan trọng cần cân nhắc, vì chunk quá lớn có thể chứa nhiều thông tin
không liên quan, trong khi chunk quá nhỏ có thể làm mất ngữ cảnh [ ].
 . . . Mô hình nhúng (Embedding Model)
Mô hình nhúng (embedding model) là một thành phần quan trọng có nhiệm vụ chuyển đổi văn bản (truy
vấn của người dùng và các đoạn tài liệu trong kho kiến thức) thành các vector số (embeddings) trong
một không gian đa chiều. Các vector này được thiết kế sao cho các văn bản có ý nghĩa tương tự sẽ có các
vector gần nhau trong không gian nhúng [ ].
Các loại embedding model phổ biến:
Word Embeddings: Word Vec, GloVe, FastText (biểu diễn từng từ).
Sentence Embeddings: Sentence-BERT, Universal Sentence Encoder (biểu diễn cả câu hoặc đoạn
văn).


========================================
# Giao Trinh Agentic AI (genai/giao_trinh_agentic.pdf)
========================================

--- Page 1 ---
Giáo trình Agentic AI
Giới thiệu
Giáo trình này cung cấp một cái nhìn toàn diện về Agentic AI, một lĩnh vực đang phát
triển nhanh chóng trong trí tuệ nhân tạo, tập trung vào việc phát triển các hệ thống AI
có khả năng tự chủ, lập kế hoạch, ra quyết định và thực hiện các hành động phức tạp
để đạt được mục tiêu. Khác với các mô hình AI truyền thống chỉ phản hồi theo lệnh,
Agentic AI có khả năng suy luận, học hỏi và thích nghi với môi trường thay đổi, mở ra
nhiều tiềm năng ứng dụng trong tự động hóa, robot, và các hệ thống thông minh.
Giáo trình sẽ đi sâu vào các khái niệm cốt lõi, kiến trúc, các kỹ thuật và công cụ được sử
dụng để xây dựng Agentic AI, cũng như các ứng dụng thực tế và những thách thức hiện
tại. Cuối cùng, một dự án thực hành sẽ giúp học viên áp dụng kiến thức vào việc xây
dựng một Agentic AI đơn giản.
Mục lục
 . Giới thiệu về Agentic AI và các khái niệm cốt lõi
 . Kiến trúc và các thành phần của Agentic AI
 . Các kỹ thuật và công cụ trong Agentic AI
 . Ứng dụng và Thách thức của Agentic AI
 . Dự án thực hành Agentic AI
 . Giới thiệu về Agentic AI và các khái niệm cốt lõi
 . . Agentic AI là gì?
Agentic AI, hay Trí tuệ nhân tạo hành động độc lập, là một bước tiến quan trọng trong
lĩnh vực trí tuệ nhân tạo, cho phép các hệ thống AI không chỉ phản hồi theo lệnh mà
còn có khả năng tự chủ, lập kế hoạch, ra quyết định và thực hiện các hành động phức

--- Page 2 ---
tạp để đạt được mục tiêu [ ,  ]. Khác với các mô hình AI truyền thống (như Generative
AI chỉ tạo nội dung theo lệnh), Agentic AI có khả năng suy luận, học hỏi và thích nghi
với môi trường thay đổi, mở ra nhiều tiềm năng ứng dụng trong tự động hóa, robot, và
các hệ thống thông minh [ ].
Agentic AI được xây dựng dựa trên ý tưởng về các "Agent" (tác nhân) ‒ các thực thể AI
có khả năng cảm nhận môi trường, xử lý thông tin, suy luận và thực hiện hành động để
đạt được mục tiêu đã định. Điều này đòi hỏi Agentic AI phải có khả năng quản lý trạng
thái, duy trì bộ nhớ, và học hỏi từ kinh nghiệm để cải thiện hiệu suất theo thời gian [ ].
 . . Sự khác biệt giữa Agentic AI và Generative AI
Để hiểu rõ hơn về Agentic AI, điều quan trọng là phải phân biệt nó với Generative AI (AI
tạo sinh), một lĩnh vực AI đã trở nên rất phổ biến gần đây:
Đặc điểm Generative AI (Ví dụ: ChatGPT) Agentic AI (Ví dụ: Auto-GPT, BabyAGI)
Mục tiêu
chính
Tạo ra nội dung (văn bản, hình
ảnh, âm thanh) dựa trên đầu
vào/lời nhắc.
Thực hiện các hành động tự chủ để đạt
được một mục tiêu cụ thể, thường là đa
bước và phức tạp.
Khả năng Tạo sinh, tổng hợp thông tin, trả
lời câu hỏi, dịch thuật.
Lập kế hoạch, suy luận, ra quyết định, thực
hiện hành động, tự sửa lỗi, học hỏi, thích
nghi.
Tính chất
Phản ứng (Reactive), thụ động,
cần lời nhắc rõ ràng.
Chủ động (Proactive), tự chủ, có khả năng
tự khởi tạo hành động.
Tương
tác
Nhận đầu vào, tạo đầu ra.
Tương tác với môi trường bên ngoài (công
cụ, API, hệ thống khác), thực hiện chuỗi
hành động.
Bộ nhớ Bộ nhớ ngắn hạn (trong ngữ cảnh
của phiên làm việc hiện tại).
Bộ nhớ dài hạn, có khả năng lưu trữ và truy
xuất thông tin qua nhiều phiên làm việc.
Vòng lặp Không có vòng lặp phản hồi nội tại
để tự cải thiện hành vi.
Có vòng lặp phản hồi (sense-plan-act) để tự
đánh giá và điều chỉnh hành vi.

--- Page 3 ---
 . . Các khái niệm cốt lõi trong Agentic AI
 . . . Agent (Tác nhân)
Agent là một thực thể có khả năng cảm nhận môi trường thông qua các cảm biến, xử lý
thông tin, và thực hiện các hành động thông qua các bộ phận chấp hành (actuators) để
đạt được mục tiêu. Một Agent có thể là một phần mềm, một robot, hoặc một hệ thống
phức hợp [ ].
 . . . Môi trường (Environment)
Môi trường là thế giới mà Agent tương tác. Nó bao gồm tất cả các đối tượng, quy tắc và
các Agent khác mà Agent đang xem xét. Môi trường có thể là một thế giới ảo (ví dụ: môi
trường phần mềm, trò chơi) hoặc thế giới vật lý (ví dụ: môi trường robot) [ ].
 . . . Cảm nhận (Perception)
Khả năng cảm nhận cho phép Agent thu thập thông tin từ môi trường. Điều này có thể
bao gồm việc đọc dữ liệu từ cảm biến, phân tích văn bản, hình ảnh, hoặc lắng nghe
phản hồi từ người dùng [ ].
 . . . Hành động (Action)
Hành động là những gì Agent thực hiện để tác động lên môi trường. Các hành động có
thể là vật lý (ví dụ: di chuyển robot) hoặc ảo (ví dụ: gửi email, gọi API, viết mã) [ ].
 . . . Mục tiêu (Goal)
Mục tiêu là trạng thái mong muốn mà Agent cố gắng đạt được. Mục tiêu có thể được
định nghĩa rõ ràng (ví dụ: "đặt vé máy bay") hoặc trừu tượng hơn (ví dụ: "tối ưu hóa lợi
nhuận") [ ].
 . . . Lập kế hoạch (Planning)
Lập kế hoạch là quá trình Agent xác định một chuỗi các hành động cần thiết để đạt
được mục tiêu. Điều này thường liên quan đến việc phân rã mục tiêu lớn thành các
nhiệm vụ nhỏ hơn và xác định thứ tự thực hiện chúng [  ].

--- Page 4 ---
 . . . Suy luận (Reasoning)
Suy luận là khả năng của Agent để xử lý thông tin, rút ra kết luận và đưa ra quyết định.
Điều này có thể bao gồm suy luận logic, suy luận xác suất, hoặc suy luận dựa trên tri
thức [  ].
 . . . Bộ nhớ (Memory)
Bộ nhớ là nơi Agent lưu trữ thông tin về môi trường, các hành động đã thực hiện, và các
mục tiêu. Bộ nhớ có thể là ngắn hạn (ví dụ: ngữ cảnh hiện tại) hoặc dài hạn (ví dụ: kiến
thức tích lũy, kinh nghiệm) [  ].
 . . . Học hỏi (Learning)
Học hỏi là khả năng của Agent để cải thiện hiệu suất của mình theo thời gian dựa trên
kinh nghiệm. Điều này có thể thông qua học tăng cường (reinforcement learning), học
giám sát (supervised learning), hoặc học không giám sát (unsupervised learning) [  ].
 . . Lợi ích của Agentic AI
Tự động hóa phức tạp: Khả năng tự động hóa các quy trình đa bước, phức tạp
mà trước đây cần sự can thiệp của con người.
Thích nghi và linh hoạt: Agentic AI có thể thích nghi với các tình huống mới và
thay đổi, đưa ra các quyết định linh hoạt.
Hiệu quả và năng suất: Tăng cường hiệu quả hoạt động và năng suất bằng cách
giảm thiểu công việc thủ công.
Giải quyết vấn đề sáng tạo: Khả năng suy luận và lập kế hoạch cho phép Agentic
AI giải quyết các vấn đề mới một cách sáng tạo.
 . . Kết luận
Agentic AI đại diện cho một hướng đi mới đầy hứa hẹn trong lĩnh vực trí tuệ nhân tạo,
chuyển từ các hệ thống phản ứng sang các hệ thống chủ động và tự chủ. Việc hiểu rõ
các khái niệm cốt lõi này là nền tảng để khám phá sâu hơn về kiến trúc, kỹ thuật và ứng
dụng của Agentic AI. Các chương tiếp theo sẽ đi sâu vào từng khía cạnh này.


========================================
# Agentic AI Design Patterns 2026 (genai/Agentic AI Design Patterns(2026 Edition).pdf)
========================================

--- Page 1 ---
Agentic AI Design Patterns(2026 Edition)
4 min read · Jan 13, 2026
Dewasheesh Rana Follow
Listen Share More
Open in app
2/2/26, 8:29 AM Agentic AI Design Patterns(2026 Edition) | by Dewasheesh Rana | Jan, 2026 | Medium
https://medium.com/@dewasheesh.rana/agentic-ai-design-patterns-2026-ed-e3a5125162c5 1/24
2/2/26, 8:29 AM Agentic AI Design Patterns(2026 Edition) | by Dewasheesh Rana | Jan, 2026 | Medium
https://medium.com/@dewasheesh.rana/agentic-ai-design-patterns-2026-ed-e3a5125162c5 2/24

--- Page 2 ---
The Definitive Architect’s Guide (Jan 2026)
2/2/26, 8:29 AM Agentic AI Design Patterns(2026 Edition) | by Dewasheesh Rana | Jan, 2026 | Medium
https://medium.com/@dewasheesh.rana/agentic-ai-design-patterns-2026-ed-e3a5125162c5 3/24
2/2/26, 8:29 AM Agentic AI Design Patterns(2026 Edition) | by Dewasheesh Rana | Jan, 2026 | Medium
https://medium.com/@dewasheesh.rana/agentic-ai-design-patterns-2026-ed-e3a5125162c5 4/24

--- Page 3 ---
1. Architect’s Reality Check (Why This Matters)
Agentic AI is not a feature — it is an architectural paradigm shift.
Most AI failures in production (2024 – 2026) did not fail due to model quality.
They failed because of:
Unbounded autonomy
No state control
No failure recovery
No observability
No governance
Agentic patterns exist to solve architectural risks, not just improve reasoning.
2. From LLM →  Agent →  System (Mental Model)
❌  Old Mental Model
Use r →  Prompt →  LLM →  Response
✅  Architect-Grade Mental Model (2026)
Use r
 ↓
Intent Router
 ↓
Agent Orchestrator
 ├─  Planner
 ├─  Tool Executor
 ├─  Reflector
 ├─  Memory / State
 ├─  Other Agents
2/2/26, 8:29 AM Agentic AI Design Patterns(2026 Edition) | by Dewasheesh Rana | Jan, 2026 | Medium
https://medium.com/@dewasheesh.rana/agentic-ai-design-patterns-2026-ed-e3a5125162c5 5/24
 ↓
Validated Output
LLMs are CPUs.
Agents are processes.
Agentic frameworks are operating systems.
3. Canonical Agentic Architecture (2026 Reference Model)
2/2/26, 8:29 AM Agentic AI Design Patterns(2026 Edition) | by Dewasheesh Rana | Jan, 2026 | Medium
https://medium.com/@dewasheesh.rana/agentic-ai-design-patterns-2026-ed-e3a5125162c5 6/24


========================================
# Master All 20 Agentic AI Design Patterns (genai/Master All 20 Agentic AI Design Patterns.pdf)
========================================

--- Page 1 ---
Master All 20 Agentic AI Design
Patterns
A Complete Guide to Production-Ready AI Agent Architectures
Comprehensive Technical Report
Designed for AI Engineers & Architects
2025 Edition

--- Page 2 ---
Table of Contents
1. Introduction to Agentic AI Design Patterns
2. Pattern 1: Prompt Chaining
3. Pattern 2: Routing
4. Pattern 3: Parallelization
5. Pattern 4: Reflection
6. Pattern 5: Tool Use
7. Pattern 6: Planning
8. Pattern 7: Multi-Agent Collaboration
9. Pattern 8: Memory Management
10. Pattern 9: Learning & Adaptation
11. Pattern 10: Goal Setting & Monitoring
12. Pattern 11: Exception Handling & Recovery
13. Pattern 12: Human-in-the-Loop
14. Pattern 13: Retrieval (RAG)
15. Pattern 14: Inter-Agent Communication
16. Pattern 15: Resource-Aware Optimization
17. Pattern 16: Reasoning Techniques
18. Pattern 17: Evaluation & Monitoring
19. Pattern 18: Guardrails & Safety
20. Pattern 19: Prioritization
21. Pattern 20: Exploration & Discovery
22. Conclusion
23. References

--- Page 3 ---
Introduction to Agentic AI Design Patterns
As Large Language Models (LLMs) evolve from simple chatbots to autonomous agents
capable of executing complex workflows, the need for robust engineering architectures
has become paramount. "Agentic AI Design Patterns" represent the crystallized wisdom
of the AI engineering community—standardized, proven approaches to solving
common problems in building autonomous systems.
Building a prototype agent is easy; building a production-ready agent that is reliable,
cost-effective, and safe is exponentially harder. Without structured patterns, developers
often create "spaghetti code" workflows that are brittle, hard to debug, and prone to
hallucinations. These patterns provide the scaffolding necessary to move from
experimental notebooks to enterprise-grade deployments.
This guide categorizes 20 essential patterns into a cohesive framework. These patterns
span the entire lifecycle of an agent's operation: from how it receives and processes a
task (Routing, Prompt Chaining), to how it thinks (Reasoning, Reflection), acts (Tool
Use, Collaboration), and improves (Learning, Evaluation). By mastering these
architectures, engineers can assemble sophisticated systems that leverage the best
capabilities of LLMs while mitigating their inherent limitations.
How to Use This Guide
Each section functions as a standalone reference but builds upon the others. Beginners
should start with foundational patterns like Prompt Chaining and Tool Use. Advanced
architects should focus on Multi-Agent Collaboration and Resource-Aware Optimization. Use
the "Implementation Considerations" to weigh tradeoffs before writing code.

--- Page 4 ---
1. Prompt Chaining
Clear Definition
Prompt Chaining is the foundational design pattern where a complex task is
decomposed into a series of smaller, sequential sub-tasks. Instead of asking an LLM to
perform a massive operation in a single prompt (a "mega-prompt"), the output of one
LLM call becomes the input for the next.
This approach transforms a probabilistic, opaque process into an assembly-line
workflow. It allows for intermediate checkpoints where logic can be validated, formats
can be corrected, and context can be refined before passing it to the next stage.
How It Works
Decomposition: Break the user's request into logical steps (e.g., Step 1: Extract
Data, Step 2: Analyze Sentiment, Step 3: Format Response).
Sequential Execution: Execute Step 1. The output is captured in a variable.
Transformation: (Optional) Code middleware cleans or reformats the output of Step
1.
Chaining: The output of Step 1 is inserted into the prompt template for Step 2.
Validation: Gates are placed between steps to ensure quality before proceeding.
Key Benefits
Higher Reliability: Smaller tasks reduce the cognitive load on the model,
leading to fewer errors.
Debuggability: You can inspect the output at every stage to identify exactly
where the failure occurred.
Context Management: Prevents context window overflow by only passing
necessary information to the next step.
Model Specialization: Different steps can use different models (e.g., a fast
model for formatting, a smart model for reasoning).


========================================
# Mathematics for Machine Learning (machine-learning/Mathematics-for-Machine-Learning.pdf)
========================================

--- Page 6 ---


--- Page 7 ---
Foreword
Machine learning is the latest in a long line of attempts to distill human
knowledge and reasoning into a form that is suitable for constructing ma-
chines and engineering automated systems. As machine learning becomes
more ubiquitous and its software packages become easier to use, it is nat-
ural and desirable that the low-level technical details are abstracted away
and hidden from the practitioner. However, this brings with it the danger
that a practitioner becomes unaware of the design decisions and, hence,
the limits of machine learning algorithms.
The enthusiastic practitioner who is interested to learn more about the
magic behind successful machine learning algorithms currently faces a
daunting set of pre-requisite knowledge:
Programming languages and data analysis tools
Large-scale computation and the associated frameworks
Mathematics and statistics and how machine learning builds on it
At universities, introductory courses on machine learning tend to spend
early parts of the course covering some of these pre-requisites. For histori-
cal reasons, courses in machine learning tend to be taught in the computer
science department, where students are often trained in the first two areas
of knowledge, but not so much in mathematics and statistics.
Current machine learning textbooks primarily focus on machine learn-
ing algorithms and methodologies and assume that the reader is com-
petent in mathematics and statistics. Therefore, these books only spend
one or two chapters on background mathematics, either at the beginning
of the book or as appendices. We have found many people who want to
delve into the foundations of basic machine learning methods who strug-
gle with the mathematical knowledge required to read a machine learning
textbook. Having taught undergraduate and graduate courses at universi-
ties, we find that the gap between high school mathematics and the math-
ematics level required to read a standard machine learning textbook is too
big for many people.
This book brings the mathematical foundations of basic machine learn-
ing concepts to the fore and collects the information in a single place so
that this skills gap is narrowed or even closed.
1
This material is published by Cambridge University Press asMathematics for Machine Learning by
Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong (2020). This version is free to view
and download for personal use only . Not for re-distribution, re-sale, or use in derivative works.
©by M. P. Deisenroth, A. A. Faisal, and C. S. Ong, 2024. https://mml-book.com.

--- Page 8 ---
2 Foreword
Why Another Book on Machine Learning?
Machine learning builds upon the language of mathematics to express
concepts that seem intuitively obvious but that are surprisingly difficult
to formalize. Once formalized properly , we can gain insights into the task
we want to solve. One common complaint of students of mathematics
around the globe is that the topics covered seem to have little relevance
to practical problems. We believe that machine learning is an obvious and
direct motivation for people to learn mathematics.
This book is intended to be a guidebook to the vast mathematical lit-
erature that forms the foundations of modern machine learning. We mo-“Math is linked in
the popular mind
with phobia and
anxiety . You’d think
we’re discussing
spiders.” (Strogatz,
2014, page 281)
tivate the need for mathematical concepts by directly pointing out their
usefulness in the context of fundamental machine learning problems. In
the interest of keeping the book short, many details and more advanced
concepts have been left out. Equipped with the basic concepts presented
here, and how they fit into the larger context of machine learning, the
reader can find numerous resources for further study , which we provide at
the end of the respective chapters. For readers with a mathematical back-
ground, this book provides a brief but precisely stated glimpse of machine
learning. In contrast to other books that focus on methods and models
of machine learning (MacKay, 2003; Bishop, 2006; Alpaydin, 2010; Bar-
ber, 2012; Murphy, 2012; Shalev-Shwartz and Ben-David, 2014; Rogers
and Girolami, 2016) or programmatic aspects of machine learning (M¨uller
and Guido, 2016; Raschka and Mirjalili, 2017; Chollet and Allaire, 2018),
we provide only four representative examples of machine learning algo-
rithms. Instead, we focus on the mathematical concepts behind the models
themselves. We hope that readers will be able to gain a deeper understand-
ing of the basic questions in machine learning and connect practical ques-
tions arising from the use of machine learning with fundamental choices
in the mathematical model.
We do not aim to write a classical machine learning book. Instead, our
intention is to provide the mathematical background, applied to four cen-
tral machine learning problems, to make it easier to read other machine
learning textbooks.
Who Is the Target Audience?
As applications of machine learning become widespread in society , we
believe that everybody should have some understanding of its underlying
principles. This book is written in an academic mathematical style, which
enables us to be precise about the concepts behind machine learning. We
encourage readers unfamiliar with this seemingly terse style to persevere
and to keep the goals of each topic in mind. We sprinkle comments and
remarks throughout the text, in the hope that it provides useful guidance
with respect to the big picture.
The book assumes the reader to have mathematical knowledge commonly
Draft (2024-01-15) of “Mathematics for Machine Learning”. Feedback:https://mml-book.com.

--- Page 9 ---
Foreword 3
covered in high school mathematics and physics. For example, the reader
should have seen derivatives and integrals before, and geometric vectors
in two or three dimensions. Starting from there, we generalize these con-
cepts. Therefore, the target audience of the book includes undergraduate
university students, evening learners and learners participating in online
machine learning courses.
In analogy to music, there are three types of interaction that people
have with machine learning:
Astute Listener The democratization of machine learning by the pro-
vision of open-source software, online tutorials and cloud-based tools al-
lows users to not worry about the specifics of pipelines. Users can focus on
extracting insights from data using off-the-shelf tools. This enables non-
tech-savvy domain experts to benefit from machine learning. This is sim-
ilar to listening to music; the user is able to choose and discern between
different types of machine learning, and benefits from it. More experi-
enced users are like music critics, asking important questions about the
application of machine learning in society such as ethics, fairness, and pri-
vacy of the individual. We hope that this book provides a foundation for
thinking about the certification and risk management of machine learning
systems, and allows them to use their domain expertise to build better
machine learning systems.
Experienced Artist Skilled practitioners of machine learning can plug
and play different tools and libraries into an analysis pipeline. The stereo-
typical practitioner would be a data scientist or engineer who understands
machine learning interfaces and their use cases, and is able to perform
wonderful feats of prediction from data. This is similar to a virtuoso play-
ing music, where highly skilled practitioners can bring existing instru-
ments to life and bring enjoyment to their audience. Using the mathe-
matics presented here as a primer, practitioners would be able to under-
stand the benefits and limits of their favorite method, and to extend and
generalize existing machine learning algorithms. We hope that this book
provides the impetus for more rigorous and principled development of
machine learning methods.
Fledgling Composer As machine learning is applied to new domains,
developers of machine learning need to develop new methods and extend
existing algorithms. They are often researchers who need to understand
the mathematical basis of machine learning and uncover relationships be-
tween different tasks. This is similar to composers of music who, within
the rules and structure of musical theory , create new and amazing pieces.
We hope this book provides a high-level overview of other technical books
for people who want to become composers of machine learning. There is
a great need in society for new researchers who are able to propose and
explore novel approaches for attacking the many challenges of learning
from data.
©2024 M. P. Deisenroth, A. A. Faisal, C. S. Ong. Published by Cambridge University Press (2020).

--- Page 10 ---
4 Foreword
Acknowledgments
We are grateful to many people who looked at early drafts of the book
and suffered through painful expositions of concepts. We tried to imple-
ment their ideas that we did not vehemently disagree with. We would
like to especially acknowledge Christfried Webers for his careful reading
of many parts of the book, and his detailed suggestions on structure and
presentation. Many friends and colleagues have also been kind enough
to provide their time and energy on different versions of each chapter.
We have been lucky to benefit from the generosity of the online commu-
nity , who have suggested improvements viahttps://github.com, which
greatly improved the book.
The following people have found bugs, proposed clarifications and sug-
gested relevant literature, either via https://github.com or personal
communication. Their names are sorted alphabetically .
Abdul-Ganiy Usman
Adam Gaier
Adele Jackson
Aditya Menon
Alasdair Tran
Aleksandar Krnjaic
Alexander Makrigiorgos
Alfredo Canziani
Ali Shafti
Amr Khalifa
Andrew Tanggara
Angus Gruen
Antal A. Buss
Antoine Toisoul Le Cann
Areg Sarvazyan
Artem Artemev
Artyom Stepanov
Bill Kromydas
Bob Williamson
Boon Ping Lim
Chao Qu
Cheng Li
Chris Sherlock
Christopher Gray
Daniel McNamara
Daniel Wood
Darren Siegel
David Johnston
Dawei Chen
Ellen Broad
Fengkuangtian Zhu
Fiona Condon
Georgios Theodorou
He Xin
Irene Raissa Kameni
Jakub Nabaglo
James Hensman
Jamie Liu
Jean Kaddour
Jean-Paul Ebejer
Jerry Qiang
Jitesh Sindhare
John Lloyd
Jonas Ngnawe
Jon Martin
Justin Hsi
Kai Arulkumaran
Kamil Dreczkowski
Lily Wang
Lionel Tondji Ngoupeyou
Lydia Kn¨ufing
Mahmoud Aslan
Mark Hartenstein
Mark van der Wilk
Markus Hegland
Martin Hewing
Matthew Alger
Matthew Lee
Draft (2024-01-15) of “Mathematics for Machine Learning”. Feedback:https://mml-book.com.

--- Page 11 ---
Foreword 5
Maximus McCann
Mengyan Zhang
Michael Bennett
Michael Pedersen
Minjeong Shin
Mohammad Malekzadeh
Naveen Kumar
Nico Montali
Oscar Armas
Patrick Henriksen
Patrick Wieschollek
Pattarawat Chormai
Paul Kelly
Petros Christodoulou
Piotr Januszewski
Pranav Subramani
Quyu Kong
Ragib Zaman
Rui Zhang
Ryan-Rhys Griffiths
Salomon Kabongo
Samuel Ogunmola
Sandeep Mavadia
Sarvesh Nikumbh
Sebastian Raschka
Senanayak Sesh Kumar Karri
Seung-Heon Baek
Shahbaz Chaudhary
Shakir Mohamed
Shawn Berry
Sheikh Abdul Raheem Ali
Sheng Xue
Sridhar Thiagarajan
Syed Nouman Hasany
Szymon Brych
Thomas B¨uhler
Timur Sharapov
Tom Melamed
Vincent Adam
Vincent Dutordoir
Vu Minh
Wasim Aftab
Wen Zhi
Wojciech Stokowiec
Xiaonan Chong
Xiaowei Zhang
Yazhou Hao
Yicheng Luo
Young Lee
Yu Lu
Yun Cheng
Yuxiao Huang
Zac Cranko
Zijian Cao
Zoe Nolan
Contributors through GitHub, whose real names were not listed on their
GitHub profile, are:
SamDataMad
bumptiousmonkey
idoamihai
deepakiim
insad
HorizonP
cs-maillist
kudo23
empet
victorBigand
17SKYE
jessjing1995
We are also very grateful to Parameswaran Raman and the many anony-
mous reviewers, organized by Cambridge University Press, who read one
or more chapters of earlier versions of the manuscript, and provided con-
structive criticism that led to considerable improvements. A special men-
tion goes to Dinesh Singh Negi, our LATEX support, for detailed and prompt
advice about LATEX-related issues. Last but not least, we are very grateful
to our editor Lauren Cowles, who has been patiently guiding us through
the gestation process of this book.
©2024 M. P. Deisenroth, A. A. Faisal, C. S. Ong. Published by Cambridge University Press (2020).

--- Page 12 ---
6 Foreword
Table of Symbols
Symbol Typical meaning
a, b, c, α, β, γScalars are lowercase
x, y, z Vectors are bold lowercase
A, B, C Matrices are bold uppercase
x⊤, A⊤ Transpose of a vector or matrix
A−1 Inverse of a matrix
⟨x, y⟩ Inner product of x and y
x⊤y Dot product of x and y
B = (b1, b2, b3) (Ordered) tuple
B = [b1, b2, b3] Matrix of column vectors stacked horizontally
B = {b1, b2, b3} Set of vectors (unordered)
Z, N Integers and natural numbers, respectively
R, C Real and complex numbers, respectively
Rn n-dimensional vector space of real numbers
∀x Universal quantifier: for all x
∃x Existential quantifier: there exists x
a := b a is defined as b
a =: b b is defined as a
a ∝ b a is proportional to b, i.e., a = constant · b
g ◦ f Function composition: “g after f”
⇐ ⇒ If and only if
=⇒ Implies
A, C Sets
a ∈ A a is an element of set A
∅ Empty set
A\B A without B: the set of elements in A but not in B
D Number of dimensions; indexed by d = 1, . . . , D
N Number of data points; indexed by n = 1, . . . , N
I m Identity matrix of size m × m
0m,n Matrix of zeros of size m × n
1m,n Matrix of ones of size m × n
ei Standard/canonical vector (where i is the component that is 1)
dim Dimensionality of vector space
rk(A) Rank of matrix A
Im(Φ) Image of linear mapping Φ
ker(Φ) Kernel (null space) of a linear mapping Φ
span[b1] Span (generating set) of b1
tr(A) Trace of A
det(A) Determinant of A
| · | Absolute value or determinant (depending on context)
∥·∥ Norm; Euclidean, unless specified
λ Eigenvalue or Lagrange multiplier
Eλ Eigenspace corresponding to eigenvalue λ
Draft (2024-01-15) of “Mathematics for Machine Learning”. Feedback:https://mml-book.com.


========================================
# Understanding Machine Learning (machine-learning/understanding-machine-learning-theory-algorithms.pdf)
========================================

--- Page 7 ---
vii
Preface
The term machine learning refers to the automated detection of meaningful
patterns in data. In the past couple of decades it has become a common tool in
almost any task that requires information extraction from large data sets. We are
surrounded by a machine learning based technology: search engines learn how
to bring us the best results (while placing proﬁtable ads), anti-spam software
learns to ﬁlter our email messages, and credit card transactions are secured by
a software that learns how to detect frauds. Digital cameras learn to detect
faces and intelligent personal assistance applications on smart-phones learn to
recognize voice commands. Cars are equipped with accident prevention systems
that are built using machine learning algorithms. Machine learning is also widely
used in scientiﬁc applications such as bioinformatics, medicine, and astronomy.
One common feature of all of these applications is that, in contrast to more
traditional uses of computers, in these cases, due to the complexity of the patterns
that need to be detected, a human programmer cannot provide an explicit, ﬁne-
detailed speciﬁcation of how such tasks should be executed. Taking example from
intelligent beings, many of our skills are acquired or reﬁned throughlearning from
our experience (rather than following explicit instructions given to us). Machine
learning tools are concerned with endowing programs with the ability to “learn”
and adapt.
The ﬁrst goal of this book is to provide a rigorous, yet easy to follow, intro-
duction to the main concepts underlying machine learning: What is learning?
How can a machine learn? How do we quantify the resources needed to learn a
given concept? Is learning always possible? Can we know if the learning process
succeeded or failed?
The second goal of this book is to present several key machine learning algo-
rithms. We chose to present algorithms that on one hand are successfully used
in practice and on the other hand give a wide spectrum of diﬀerent learning
techniques. Additionally, we pay speciﬁc attention to algorithms appropriate for
large scale learning (a.k.a. “Big Data”), since in recent years, our world has be-
come increasingly “digitized” and the amount of data available for learning is
dramatically increasing. As a result, in many applications data is plentiful and
computation time is the main bottleneck. We therefore explicitly quantify both
the amount of data and the amount of computation time needed to learn a given
concept.
The book is divided into four parts. The ﬁrst part aims at giving an initial
rigorous answer to the fundamental questions of learning. We describe a gen-
eralization of Valiant’s Probably Approximately Correct (PAC) learning model,
which is a ﬁrst solid answer to the question “what is learning?”. We describe
the Empirical Risk Minimization (ERM), Structural Risk Minimization (SRM),
and Minimum Description Length (MDL) learning rules, which shows “how can
a machine learn”. We quantify the amount of data needed for learning using
the ERM, SRM, and MDL rules and show how learning might fail by deriving

--- Page 8 ---
viii
a “no-free-lunch” theorem. We also discuss how much computation time is re-
quired for learning. In the second part of the book we describe various learning
algorithms. For some of the algorithms, we ﬁrst present a more general learning
principle, and then show how the algorithm follows the principle. While the ﬁrst
two parts of the book focus on the PAC model, the third part extends the scope
by presenting a wider variety of learning models. Finally, the last part of the
book is devoted to advanced theory.
We made an attempt to keep the book as self-contained as possible. However,
the reader is assumed to be comfortable with basic notions of probability, linear
algebra, analysis, and algorithms. The ﬁrst three parts of the book are intended
for ﬁrst year graduate students in computer science, engineering, mathematics, or
statistics. It can also be accessible to undergraduate students with the adequate
background. The more advanced chapters can be used by researchers intending
to gather a deeper theoretical understanding.
Acknowledgements
The book is based on Introduction to Machine Learning courses taught by Shai
Shalev-Shwartz at the Hebrew University and by Shai Ben-David at the Univer-
sity of Waterloo. The ﬁrst draft of the book grew out of the lecture notes for
the course that was taught at the Hebrew University by Shai Shalev-Shwartz
during 2010–2013. We greatly appreciate the help of Ohad Shamir, who served
as a TA for the course in 2010, and of Alon Gonen, who served as a TA for the
course in 2011–2013. Ohad and Alon prepared few lecture notes and many of
the exercises. Alon, to whom we are indebted for his help throughout the entire
making of the book, has also prepared a solution manual.
We are deeply grateful for the most valuable work of Dana Rubinstein. Dana
has scientiﬁcally proofread and edited the manuscript, transforming it from
lecture-based chapters into ﬂuent and coherent text.
Special thanks to Amit Daniely, who helped us with a careful read of the
advanced part of the book and also wrote the advanced chapter on multiclass
learnability. We are also grateful for the members of a book reading club in
Jerusalem that have carefully read and constructively criticized every line of
the manuscript. The members of the reading club are: Maya Alroy, Yossi Arje-
vani, Aharon Birnbaum, Alon Cohen, Alon Gonen, Roi Livni, Ofer Meshi, Dan
Rosenbaum, Dana Rubinstein, Shahar Somin, Alon Vinnikov, and Yoav Wald.
We would also like to thank Gal Elidan, Amir Globerson, Nika Haghtalab, Shie
Mannor, Amnon Shashua, Nati Srebro, and Ruth Urner for helpful discussions.
Shai Shalev-Shwartz, Jerusalem, Israel
Shai Ben-David, Waterloo, Canada

--- Page 9 ---
Contents
Preface page vii
1 Introduction 19
1.1 What Is Learning? 19
1.2 When Do We Need Machine Learning? 21
1.3 Types of Learning 22
1.4 Relations to Other Fields 24
1.5 How to Read This Book 25
1.5.1 Possible Course Plans Based on This Book 26
1.6 Notation 27
Part I Foundations 31
2 A Gentle Start 33
2.1 A Formal Model – The Statistical Learning Framework 33
2.2 Empirical Risk Minimization 35
2.2.1 Something May Go Wrong – Overﬁtting 35
2.3 Empirical Risk Minimization with Inductive Bias 36
2.3.1 Finite Hypothesis Classes 37
2.4 Exercises 41
3 A Formal Learning Model 43
3.1 PAC Learning 43
3.2 A More General Learning Model 44
3.2.1 Releasing the Realizability Assumption – Agnostic PAC
Learning 45
3.2.2 The Scope of Learning Problems Modeled 47
3.3 Summary 49
3.4 Bibliographic Remarks 50
3.5 Exercises 50
4 Learning via Uniform Convergence 54
4.1 Uniform Convergence Is Suﬃcient for Learnability 54
4.2 Finite Classes Are Agnostic PAC Learnable 55
Understanding Machine Learning, c© 2014 by Shai Shalev-Shwartz and Shai Ben-David
Published 2014 by Cambridge University Press.
Personal use only. Not for distribution. Do not post.
Please link to http://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning

--- Page 10 ---
x Contents
4.3 Summary 58
4.4 Bibliographic Remarks 58
4.5 Exercises 58
5 The Bias-Complexity Tradeoﬀ 60
5.1 The No-Free-Lunch Theorem 61
5.1.1 No-Free-Lunch and Prior Knowledge 63
5.2 Error Decomposition 64
5.3 Summary 65
5.4 Bibliographic Remarks 66
5.5 Exercises 66
6 The VC-Dimension 67
6.1 Inﬁnite-Size Classes Can Be Learnable 67
6.2 The VC-Dimension 68
6.3 Examples 70
6.3.1 Threshold Functions 70
6.3.2 Intervals 71
6.3.3 Axis Aligned Rectangles 71
6.3.4 Finite Classes 72
6.3.5 VC-Dimension and the Number of Parameters 72
6.4 The Fundamental Theorem of PAC learning 72
6.5 Proof of Theorem 6.7 73
6.5.1 Sauer’s Lemma and the Growth Function 73
6.5.2 Uniform Convergence for Classes of Small Eﬀective Size 75
6.6 Summary 78
6.7 Bibliographic remarks 78
6.8 Exercises 78
7 Nonuniform Learnability 83
7.1 Nonuniform Learnability 83
7.1.1 Characterizing Nonuniform Learnability 84
7.2 Structural Risk Minimization 85
7.3 Minimum Description Length and Occam’s Razor 89
7.3.1 Occam’s Razor 91
7.4 Other Notions of Learnability – Consistency 92
7.5 Discussing the Diﬀerent Notions of Learnability 93
7.5.1 The No-Free-Lunch Theorem Revisited 95
7.6 Summary 96
7.7 Bibliographic Remarks 97
7.8 Exercises 97
8 The Runtime of Learning 100
8.1 Computational Complexity of Learning 101

--- Page 11 ---
Contents xi
8.1.1 Formal Deﬁnition* 102
8.2 Implementing the ERM Rule 103
8.2.1 Finite Classes 104
8.2.2 Axis Aligned Rectangles 105
8.2.3 Boolean Conjunctions 106
8.2.4 Learning 3-Term DNF 107
8.3 Eﬃciently Learnable, but Not by a Proper ERM 107
8.4 Hardness of Learning* 108
8.5 Summary 110
8.6 Bibliographic Remarks 110
8.7 Exercises 110
Part II From Theory to Algorithms 115
9 Linear Predictors 117
9.1 Halfspaces 118
9.1.1 Linear Programming for the Class of Halfspaces 119
9.1.2 Perceptron for Halfspaces 120
9.1.3 The VC Dimension of Halfspaces 122
9.2 Linear Regression 123
9.2.1 Least Squares 124
9.2.2 Linear Regression for Polynomial Regression Tasks 125
9.3 Logistic Regression 126
9.4 Summary 128
9.5 Bibliographic Remarks 128
9.6 Exercises 128
10 Boosting 130
10.1 Weak Learnability 131
10.1.1 Eﬃcient Implementation of ERM for Decision Stumps 133
10.2 AdaBoost 134
10.3 Linear Combinations of Base Hypotheses 137
10.3.1 The VC-Dimension of L(B,T ) 139
10.4 AdaBoost for Face Recognition 140
10.5 Summary 141
10.6 Bibliographic Remarks 141
10.7 Exercises 142
11 Model Selection and Validation 144
11.1 Model Selection Using SRM 145
11.2 Validation 146
11.2.1 Hold Out Set 146
11.2.2 Validation for Model Selection 147
11.2.3 The Model-Selection Curve 148

--- Page 12 ---
xii Contents
11.2.4 k-Fold Cross Validation 149
11.2.5 Train-Validation-Test Split 150
11.3 What to Do If Learning Fails 151
11.4 Summary 154
11.5 Exercises 154
12 Convex Learning Problems 156
12.1 Convexity, Lipschitzness, and Smoothness 156
12.1.1 Convexity 156
12.1.2 Lipschitzness 160
12.1.3 Smoothness 162
12.2 Convex Learning Problems 163
12.2.1 Learnability of Convex Learning Problems 164
12.2.2 Convex-Lipschitz/Smooth-Bounded Learning Problems 166
12.3 Surrogate Loss Functions 167
12.4 Summary 168
12.5 Bibliographic Remarks 169
12.6 Exercises 169
13 Regularization and Stability 171
13.1 Regularized Loss Minimization 171
13.1.1 Ridge Regression 172
13.2 Stable Rules Do Not Overﬁt 173
13.3 Tikhonov Regularization as a Stabilizer 174
13.3.1 Lipschitz Loss 176
13.3.2 Smooth and Nonnegative Loss 177
13.4 Controlling the Fitting-Stability Tradeoﬀ 178
13.5 Summary 180
13.6 Bibliographic Remarks 180
13.7 Exercises 181
14 Stochastic Gradient Descent 184
14.1 Gradient Descent 185
14.1.1 Analysis of GD for Convex-Lipschitz Functions 186
14.2 Subgradients 188
14.2.1 Calculating Subgradients 189
14.2.2 Subgradients of Lipschitz Functions 190
14.2.3 Subgradient Descent 190
14.3 Stochastic Gradient Descent (SGD) 191
14.3.1 Analysis of SGD for Convex-Lipschitz-Bounded Functions 191
14.4 Variants 193
14.4.1 Adding a Projection Step 193
14.4.2 Variable Step Size 194
14.4.3 Other Averaging Techniques 195

--- Page 13 ---
Contents xiii
14.4.4 Strongly Convex Functions* 195
14.5 Learning with SGD 196
14.5.1 SGD for Risk Minimization 196
14.5.2 Analyzing SGD for Convex-Smooth Learning Problems 198
14.5.3 SGD for Regularized Loss Minimization 199
14.6 Summary 200
14.7 Bibliographic Remarks 200
14.8 Exercises 201
15 Support Vector Machines 202
15.1 Margin and Hard-SVM 202
15.1.1 The Homogenous Case 205
15.1.2 The Sample Complexity of Hard-SVM 205
15.2 Soft-SVM and Norm Regularization 206
15.2.1 The Sample Complexity of Soft-SVM 208
15.2.2 Margin and Norm-Based Bounds versus Dimension 208
15.2.3 The Ramp Loss* 209
15.3 Optimality Conditions and “Support Vectors”* 210
15.4 Duality* 211
15.5 Implementing Soft-SVM Using SGD 212
15.6 Summary 213
15.7 Bibliographic Remarks 213
15.8 Exercises 214
16 Kernel Methods 215
16.1 Embeddings into Feature Spaces 215
16.2 The Kernel Trick 217
16.2.1 Kernels as a Way to Express Prior Knowledge 221
16.2.2 Characterizing Kernel Functions* 222
16.3 Implementing Soft-SVM with Kernels 222
16.4 Summary 224
16.5 Bibliographic Remarks 225
16.6 Exercises 225
17 Multiclass, Ranking, and Complex Prediction Problems 227
17.1 One-versus-All and All-Pairs 227
17.2 Linear Multiclass Predictors 230
17.2.1 How to Construct Ψ 230
17.2.2 Cost-Sensitive Classiﬁcation 232
17.2.3 ERM 232
17.2.4 Generalized Hinge Loss 233
17.2.5 Multiclass SVM and SGD 234
17.3 Structured Output Prediction 236
17.4 Ranking 238


========================================
# Principles of Deep Learning Theory (deep-learning/The-Principles-of-Deep-Learning-Theory.pdf)
========================================

--- Page 8 ---
exploring diﬀerent kinds of idealized theoretical limits. However, our interests are ﬁxed
ﬁrmly on providing explanations for the tools and approaches used by practitioners, in
an eﬀort to shed light on what makes them work so well.
Fourth, a large part of the book is focused on deep multilayer perceptrons. We made
this choice in order to pedagogically illustrate the power of the eﬀective theory framework
– not due to any technical obstruction – and along the way we give pointers for how this
formalism can be extended to other architectures of interest. In fact, we expect that
many of our results have a broad applicability, and we’ve tried to focus on aspects that
we expect to have lasting and universal value to the deep learning community.
Fifth, while much of the material is novel and appears for the ﬁrst time in this
book, and while much of our framing, notation, language, and emphasis breaks with
the historical line of development, we’re also very much indebted to the deep learning
community. With that in mind, throughout the book we will try to reference important
prior contributions, with an emphasis on recent seminal deep-learning results rather than
on being completely comprehensive. Additional references for those interested can easily
be found within the work that we cite.
Sixth, this book initially grew out of a research project in collaboration with Boris
Hanin. To account for his eﬀort and then support, we’ve accordingly commemorated him
on the cover. More broadly, we’ve variously appreciated the artwork, discussions, en-
couragement, epigraphs, feedback, management, refereeing, reintroduction, and support
from Rafael Araujo, L´ eon Bottou, Paul Dirac, Ethan Dyer, John Frank, Ross Girshick,
Vince Higgs, Yoni Kahn, Yann LeCun, Kyle Mahowald, Eric Mintun, Xiaoliang Qi,
Mike Rabbat, David Schwab, Stephen Shenker, Eva Silverstein, PJ Steiner, DJ Strouse,
and Jesse Thaler. Organizationally, we’re grateful to FAIR and Facebook, Diﬀeo and
Salesforce, MIT and IAIFI, and Cambridge University Press and the arXiv.
Seventh, given intense (and variously uncertain) spacetime and energy-momentum
commitment that writing this book entailed, Dan is grateful to Aya, Lumi, and Lisa
Yaida; from the dual sample-space perspective, Sho is grateful to Adrienne Rothschilds
and would be retroactively grateful to any hypothetical future Mark or Emily that would
have otherwise been thanked in this paragraph.
Eighth, we hope that this book spreads our optimism that it is possible to have
a general theory of deep learning, one that’s both derived from ﬁrst principles and at
the same time focused on describing how realistic models actually work: nearly-simple
phenomena in practice should correspond to nearly-simple eﬀective theories. We dream
that this type of thinking will not only lead to more [redacted] AI models but also guide
us towards a unifying framework for understanding universal aspects of intelligence.
As if that eightfold way of prefacing the book wasn’t nearly-enough already, please
note: this book has a website, deeplearningtheory.com, and you may want to visit
it in order to determine whether the error that you just discovered is already common
knowledge. If it’s not, please let us know. There may be pie.
Dan Roberts & Sho Yaida
Remotely Located
June, 2021
viii

--- Page 9 ---
Chapter 0
Initialization
The simulation is such that [one] generally perceives the sum of many billions of
elementary processes simultaneously, so that the leveling law of large numbers
completely obscures the real nature of the individual processes.
John von Neumann [2]
Thanks to substantial investments into computer technology, modern artiﬁcial intel-
ligence (AI) systems can now come equipped with many billions of elementary com-
ponents. When these components are properly initialized and then trained, AI can ac-
complish tasks once considered so incredibly complex that philosophers have previously
argued that only natural intelligence systems – i.e. humans – could perform them.
Behind much of this success in AI is deep learning . Deep learning uses artiﬁcial
neural networks as an underlying model for AI: while loosely based onbiological neural
networks such as your brain, artiﬁcial neural networks are probably best thought of as
an especially nice way of specifying a ﬂexible set of functions, built out of many basic
computational blocks called neurons. This model of computation is actually quite
diﬀerent from the one used to power the computer you’re likely using to read this book.
In particular, rather than programming a speciﬁc set of instructions to solve a problem
directly, deep learning models are trained on data from the real world and learn how to
solve problems.
The real power of the deep learning framework comes from deep neural networks,
with many neurons in parallel organized into sequential computational layers, learning
useful representations of the world. Such representation learning transforms data
into increasingly reﬁned forms that are helpful for solving an underlying task, and is
thought to be a hallmark of success in intelligence, both artiﬁcial and biological.
Despite these successes and the intense interest they created, deep learning theory
is still in its infancy. Indeed, there is a serious disconnect between theory and prac-
tice: while practitioners have reached amazing milestones, they have far outpaced the
theorists, whose analyses often involve assumptions so unrealistic that they lead to con-
clusions that are irrelevant to understanding deep neural networks as they are typically
1

--- Page 10 ---
used. More importantly, very little theoretical work directly confronts the deep of deep
learning, despite a mass of empirical evidence for its importance in the success of the
framework.
The goal of this book is to put forth a set ofprinciples that enable us to theoretically
analyze deep neural networks of actual relevance. To initialize you to this task, in the
rest of this chapter we’ll explain at a very high-level both (i) why such a goal is even
attainable in theory and (ii) how we are able to get there in practice.
0.1 An Eﬀective Theory Approach
Steam navigation brings nearer together the most distant nations. . . . their theory is
very little understood, and the attempts to improve them are still directed almost by
chance. . . . We propose now to submit these questions to a deliberate examination.
Sadi Carnot, commenting on the need for a theory of deep learning [3].
While modern deep learning models are built up from seemingly innumerable elementary
computational components, a ﬁrst-principles microscopic description of how a trained
neural network computes a function from these low-level components is entirely manifest.
This microscopic description is just the set of instructions for transforming an input
through the many layers of components into an output. Importantly, during the training
process, these components become very ﬁnely-tuned, and knowledge of the particular
tunings is necessary for a system to produce useful output.
Unfortunately, the complexity of these tunings obscures any ﬁrst-principles macro-
scopic understanding of why a deep neural network computes a particular function and
not another. With many neurons performing diﬀerent tasks as part of such a computa-
tion, it seems hopeless to think that we can use theory to understand these models at
all, and silly to believe that a small set of mathematical principles will be suﬃcient for
that job.
Fortunately, theoretical physics has a long tradition of ﬁnding simple eﬀective
theories of complicated systems with a large number of components. The immense
success of the program of physics in modeling our physical universe suggests that per-
haps some of the same tools may be useful for theoretically understanding deep neural
networks. To motivate this connection, let’s very brieﬂy reﬂect on the successes of
thermodynamics and statistical mechanics, physical theories that together explain from
microscopic ﬁrst principles the macroscopic behavior of systems with many elementary
constituents.
A scientiﬁc consequence of the Industrial Age, thermodynamics arose out of an
eﬀort to describe and innovate upon the steam engine – a system consisting of many many
particles and perhaps the original black box. The laws of thermodynamics, derived from
careful empirical observations, were used to codify the mechanics of steam, providing a
high-level understanding of these macroscopic artiﬁcial machines that were transforming
society. While the advent of thermodynamics led to tremendous improvements in the
2

--- Page 11 ---
eﬃciency of steam power, its laws were in no way fundamental.
It wasn’t until much later that Maxwell, Boltzmann, and Gibbs provided the missing
link between experimentally-derived eﬀective description on the one hand and a ﬁrst-
principles theory on the other hand. Their statistical mechanics explains how the
macroscopic laws of thermodynamics describing human-scale machines could arise sta-
tistically from the deterministic dynamics of many microscopic elementary constituents.
From this perspective, the laws of thermodynamics were emergent phenomena that only
appear from the collective statistical behavior of a very large number of microscopic
particles. In fact, it was the detailed theoretical predictions derived from statistical
mechanics that ultimately led to the general scientiﬁc acceptance that matter is really
comprised of molecules and atoms. Relentless application of statistical mechanics led
to the discovery of quantum mechanics , which is a precursor to the invention of the
transistor that powers the Information Age, and – taking the long view – is what has
allowed us to begin to realize artiﬁcial machines that can think intelligently.
Notably, these physical theories originated from a desire to understand artiﬁcial
human-engineered objects, such as the steam engine. Despite a potential misconception,
physics doesn’t make a distinction between natural and artiﬁcial phenomena. Most
fundamentally, it’s concerned with providing a uniﬁed set of principles that account
for past empirical observations and predict the result of future experiments; the point
of theoretical calculations is to connect measurable outcomes or observables directly
to the fundamental underlying constants or parameters that deﬁne the theory. This
perspective also implies a tradeoﬀ between the predictive accuracy of a model and its
mathematical tractability, and the former must take precedence over the latter for any
theory to be successful: a short tether from theory to physical reality is essential. When
successful, such theories provide a comprehensive understanding of phenomena and em-
power practical advances in technology, as exempliﬁed by the statistical-physics bridge
from the Age of Steam to the Age of Information.
For our study of deep learning, the key takeaway from this discussion is that a theo-
retical matter simpliﬁes when it is made up of many elementary constituents. Moreover,
unlike the molecules of water contained in a box of steam – with their existence once
being a controversial conjecture in need of experimental veriﬁcation – the neurons com-
prising a deep neural network are put in (the box) by hand. Indeed, in this case we
already understand the microscopic laws – how a network computes – and so instead
our task is to understand the new types of regularity that appear at the macroscopic
scale – why it computes one particular function rather than another – that emerge from
the statistical properties of these gigantic deep learning models.
3

--- Page 12 ---
Figure 1: A graph of a simple multilayer neural network, depicting how the input x is
transformed through a sequence of intermediate signals, s(1),s(2), and s(3), into the out-
putf(x;θ). The white circles represent the neurons, the black dot at the top represents
the network output, and the parameters θ are implicit; they weight the importance of
the diﬀerent arrows carrying the signals and bias the ﬁring threshold of each neuron.
0.2 The Theoretical Minimum
The method is more important than the discovery, because the correct method of
research will lead to new, even more valuable discoveries.
Lev Landau [4].
In this section, we’ll give a high-level overview of our method, providing a minimal
explanation for why we should expect a ﬁrst-principles theoretical understanding of deep
neural networks to be possible. We’ll then ﬁll in all the details in the coming chapters.
In essence, a neural network is a recipe for computing a function built out of many
computational units called neurons. Each neuron is itself a very simple function that
considers a weighted sum of incoming signals and then ﬁres in a characteristic way by
comparing the value of that sum against some threshold. Neurons are then organized
in parallel into layers, and deep neural networks are those composed of multiple layers
in sequence. The network is parametrized by the ﬁring thresholds and the weighted
connections between the neurons, and, to give a sense of the potential scale, current
state-of-the-art neural networks can have over 100 billion parameters. A graph depicting
the structure of a much more reasonably-sized neural network is shown in Figure 1.
For a moment, let’s ignore all that structure and simply think of a neural network
4

--- Page 13 ---
as a parameterized function
f(x;θ), (0.1)
wherex is the input to the function and θ is a vector of a large number of parameters
controlling the shape of the function. For such a function to be useful, we need to
somehow tune the high-dimensional parameter vector θ. In practice, this is done in two
steps:
• First, we initialize the network by randomly sampling the parameter vectorθ from
a computationally simple probability distribution,
p(θ). (0.2)
We’ll later discuss the theoretical reason why it is a good strategy to have an
initialization distributionp(θ) but, more importantly, this corresponds to what
is done in practice, and our approach in this book is to have our theoretical analysis
correspond to realistic deep learning scenarios.
• Second, we adjust the parameter vector as θ→θ⋆, such that the resulting network
function f(x;θ⋆) is as close as possible to a desired target function f(x):
f(x;θ⋆)≈f(x). (0.3)
This is called function approximation . To ﬁnd these tunings θ⋆, we ﬁt the
network function f(x;θ) to training data, consisting of many pairs of the form(
x,f (x)
{
observed from the desired – but only partially observable – target function
f(x). Overall, making these adjustments to the parameters is called training, and
the particular procedure used to tune them is called a learning algorithm.
Our goal is to understand this trained network function:
f(x;θ⋆). (0.4)
In particular, we’d like to understand the macroscopic behavior of this function from
a ﬁrst-principles microscopic description of the network in terms of these trained pa-
rameters θ⋆. We’d also like to understand how the function approximation (0.3) works
and evaluate how f(x;θ⋆) uses the training data (x,f (x){ in its approximation of f(x).
Given the high dimensionality of the parametersθ and the degree of ﬁne-tuning required
for the approximation (0.3), this goal might seem naive and beyond the reach of any
realistic theoretical approach.
One way to more directly see the kinds of technical problems that we’ll encounter is
to Taylor expand our trained network function f(x;θ⋆) around the initialized value of
the parameters θ. Being schematic and ignoring for a moment that θ is a vector and
that the derivatives of f(x;θ) are tensors, we see
f(x;θ⋆) =f(x;θ) + (θ⋆−θ)dfdθ + 12 (θ⋆−θ)2d2fdθ2 +... , (0.5)
where f(x;θ) and its derivatives on the right-hand side are all evaluated at initialized
value of the parameters. This Taylor representation illustrates our three main problems:
5

--- Page 14 ---
Problem 1
In general, the series (0.5) contains an inﬁnite number of terms
f, dfdθ, d2fdθ2 , d3fdθ3 , d4fdθ4 , ... , (0.6)
and to use this Taylor representation of the function (0.5), in principle we need
to compute them all. More speciﬁcally, as the diﬀerence between the trained and
initialized parameters, (θ⋆−θ), becomes large, so too does the number of terms
needed to get a good approximation of the trained network function f(x;θ⋆).
Problem 2
Since the parameters θ are randomly sampled from the initialization distribution,
p(θ), each time we initialize our network we get a diﬀerent function f(x;θ). This
means that each termf,df/dθ,d2f/dθ 2, . . . , from (0.6) is really arandom function
of the input x. Thus, the initialization induces a distribution over the network
function and its derivatives, and we need to determine the mapping,
p(θ)→p
(
f, dfdθ,d2fdθ2, ...( , (0.7)
that takes us from the distribution of initial parameters θ to the joint distribution
of the network function,f(x;θ), its gradient,df/dθ, its Hessian,d2f/dθ 2, and so
on. This is a joint distribution comprised of an inﬁnite number of random functions,
and in general such functions will have an intricate statistical dependence. Even if
we set aside this inﬁnity of functions for a moment and consider just the marginal
distribution of the network function only, p(f), there’s still no reason to expect
that it’s analytically tractable.
Problem 3
The learned value of the parameters, θ⋆, is the result of a complicated training
process. In general, θ⋆ is not unique and can depend on everything:
θ⋆≡ [θ⋆]
(
θ, f,dfdθ, d2fdθ2, ... ; learning algorithm; training data( . (0.8)
In practice, the learning algorithm is iterative, accumulating changes over many
steps, and the dynamics are nonlinear. Thus, the trained parametersθ⋆ will depend
in a very complicated way on all the quantities at initialization – such as the
speciﬁc random sample of the parameters θ, the network function f(x;θ) and all
of its derivatives, df/dθ, d2f/dθ 2, . . . – as well as on the details of the learning
algorithm and also on the particular pairs,
(
x,f (x)
{
, that comprise the training
data. Determining an analytical expression for θ⋆ must involve taking all of this
into account.
6


========================================
# Fundamentals of Database Systems (software/Fundamentals of Database System.pdf)
========================================

--- Page 1 ---
Fundamentals of Database Systems
for Data Scientist
Lê Thiện Hòa
2025

--- Page 2 ---
Nội dung
● SQL vs. No-SQL, Row-wise & Column-wise DB
● OLTP vs. OLAP
● ACID & BASE principles
● Data Warehouse, Data Mart
● Dimensional Modeling, Facts, Dimensions, Slowly Changing Dimensions (SCD)
● Normalization vs. Denormalization, Star Schema, Snowflake Schema
● Extract - Transform - Load (ETL), ELT
● Data Lake, Lakehouse
● Distributed Databases (HBase, Cassandra), CAP theorem

--- Page 3 ---
SQL databases
● Có cấu trúc (Structured): dữ liệu lưu trong 
bảng (table), hàng (row), cột (column).
● Ngôn ngữ chuẩn (SQL): dùng SQL để query, 
join, filter, aggregate.
● Quan hệ (Relational): hỗ trợ liên kết giữa 
nhiều bảng bằng khóa chính/ngoại.
● Tuân thủ ACID: đảm bảo tính toàn vẹn dữ liệu 
trong giao dịch.
● Phù hợp OLTP: xử lý giao dịch nhanh, nhiều 
truy vấn nhỏ.
● Schema cố định: dữ liệu phải tuân theo thiết 
kế trước (schema-first).
● Ví dụ: MySQL, PostgreSQL, Oracle, SQL 
Server.

--- Page 4 ---
No-SQL databases
● Linh hoạt schema: không cần định nghĩa cố định trước 
(schema-less hoặc schema-flexible).
● Đa dạng mô hình dữ liệu: document, key-value, 
column-family, graph.
● Khả năng scale-out: phân tán theo chiều ngang, dễ 
mở rộng với dữ liệu lớn.
● Tối ưu cho dữ liệu phi cấu trúc / bán cấu trúc 
(JSON, log, sensor, mạng xã hội).
● Hiệu năng cao cho workload đặc thù (write-intensive, 
real-time query).
● Không phải lúc nào cũng ACID, thường theo BASE
● Ví dụ: MongoDB (document), Cassandra (column), 
Redis (key-value), Neo4j (graph).

--- Page 5 ---
When to choose SQL / No-SQL ?


--- Page 6 ---
Row-wise vs. Column-wise Databases
Row-wise (hàng):
● Lưu dữ liệu theo dòng → đọc/ghi cả 
record.
● Phù hợp OLTP: nhiều transaction nhỏ, 
insert/update nhanh.
Column-wise (cột):
● Lưu dữ liệu theo cột → đọc/ghi tập trung 
theo từng thuộc tính.
● Phù hợp OLAP: phân tích, aggregate trên 
cột, truy vấn khối lượng lớn.
● Nén dữ liệu tốt, tăng tốc query analytic.
