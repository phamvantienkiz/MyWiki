import { DomainId, DomainInfo } from '../types/wiki';

export const DOMAINS: Record<DomainId, DomainInfo> = {
  genai: {
    id: 'genai',
    name: 'GenAI, Foundation Models & Reasoning',
    shortName: 'GenAI & LLM',
    color: '#1F5FFF',
    pastelBg: '#D9E8FF',
    textColor: '#0D3EA3',
    description: 'Kiến trúc Transformer, Huấn luyện căn bản, Alignment, Reasoning và Nén lượng tử hóa.'
  },
  rag: {
    id: 'rag',
    name: 'RAG & Retrieval Systems',
    shortName: 'RAG Systems',
    color: '#B13BF0',
    pastelBg: '#E6DDFB',
    textColor: '#6A1AA3',
    description: 'Kiến trúc RAG nâng cao, Chunking, Vector Embeddings, Hybrid Search, Reranking và Graph RAG.'
  },
  agentic: {
    id: 'agentic',
    name: 'Agentic AI & Design Patterns',
    shortName: 'Agentic AI',
    color: '#FF8A1F',
    pastelBg: '#FFE6D1',
    textColor: '#A34C00',
    description: 'Cốt lõi Agent, Vòng lặp ReAct, Reflection, Planning, Tool use, Multi-agent và Human-in-the-loop.'
  },
  deeplearning: {
    id: 'deeplearning',
    name: 'Deep Learning & Computer Vision / NLP',
    shortName: 'Deep Learning',
    color: '#1FA63A',
    pastelBg: '#D8F3E4',
    textColor: '#0E6320',
    description: 'Mạng tích chập CNN, U-Net Segmentation, YOLO Object Detection, ViT, GNN và Tối ưu TensorRT.'
  },
  mlmath: {
    id: 'mlmath',
    name: 'Machine Learning & Mathematical Foundations',
    shortName: 'ML & Math',
    color: '#0EA5E9',
    pastelBg: '#DDF4FE',
    textColor: '#0369A1',
    description: 'Hồi quy tuyến tính MLE, Phân rã Bias-Variance, Regularization, Optimization và Đánh giá mô hình.'
  },
  mlops: {
    id: 'mlops',
    name: 'MLOps & Production Engineering',
    shortName: 'MLOps',
    color: '#EC4899',
    pastelBg: '#FCE7F3',
    textColor: '#9D174D',
    description: 'Vòng đời MLOps, Experiment Tracking, Model Serving API, Docker/K8s, CI/CD và Giám sát Drift.'
  },
  software: {
    id: 'software',
    name: 'Software Engineering & Data Systems',
    shortName: 'Software Eng',
    color: '#64748B',
    pastelBg: '#E2E8F0',
    textColor: '#334155',
    description: 'Nguyên lý OOP, SOLID trong AI/ML, Indexing B-Tree, Giao dịch ACID và Kiến trúc SQL vs NoSQL.'
  }
};

export const DOMAIN_SLUG_MAP: Record<string, DomainId> = {
  // Miền 1: GenAI
  'large-language-models': 'genai',
  'transformer-architecture': 'genai',
  'llm-reasoning': 'genai',
  'llm-fine-tuning': 'genai',
  'llm-alignment': 'genai',
  'prompt-engineering': 'genai',
  'llm-evaluation': 'genai',
  'quantization-and-compression': 'genai',

  // Miền 2: RAG
  'rag-architecture': 'rag',
  'document-chunking': 'rag',
  'vector-embeddings': 'rag',
  'hybrid-search': 'rag',
  'reranking': 'rag',
  'query-transformation': 'rag',
  'graph-rag': 'rag',

  // Miền 3: Agentic
  'agentic-ai-core': 'agentic',
  'react-pattern': 'agentic',
  'reflection-and-self-correction': 'agentic',
  'planning-and-decomposition': 'agentic',
  'tool-use-and-function-calling': 'agentic',
  'multi-agent-collaboration': 'agentic',
  'agent-memory-systems': 'agentic',
  'human-in-the-loop': 'agentic',

  // Miền 4: Deep Learning
  'convolutional-neural-networks': 'deeplearning',
  'unet-architecture': 'deeplearning',
  'object-detection-yolo': 'deeplearning',
  'vision-transformers': 'deeplearning',
  'inference-optimization-tensorrt': 'deeplearning',
  'graph-neural-networks': 'deeplearning',

  // Miền 5: ML & Math
  'linear-regression-mle': 'mlmath',
  'bias-variance-tradeoff': 'mlmath',
  'regularization-l1-l2': 'mlmath',
  'gradient-vanishing-exploding': 'mlmath',
  'optimization-algorithms': 'mlmath',
  'principal-component-analysis': 'mlmath',
  'model-selection-evaluation': 'mlmath',

  // Miền 6: MLOps
  'mlops-lifecycle': 'mlops',
  'experiment-tracking-model-registry': 'mlops',
  'model-serving-api': 'mlops',
  'containerization-kubernetes-ml': 'mlops',
  'continuous-integration-cd-ml': 'mlops',
  'data-drift-model-monitoring': 'mlops',

  // Miền 7: Software
  'oop-core-principles': 'software',
  'solid-principles': 'software',
  'database-indexing-optimization': 'software',
  'acid-and-transactions': 'software',
  'sql-vs-nosql-data-architecture': 'software',
};
