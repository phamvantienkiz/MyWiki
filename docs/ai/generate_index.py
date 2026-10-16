# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

INDEX_CONTENT = r"""# 🧠 AI Engineer Knowledge Wiki (LLM Wiki Architecture)

> *"An LLM wiki is a folder of plain markdown files that an AI agent reads, writes, and maintains on your behalf. Each file is an entity page: a structured, Wikipedia-style entry for one concept, linked to related concepts using `[[wiki-links]]`... Over time, the wiki becomes a connected knowledge graph, not just a pile of documents. At 100+ pages, it can answer questions where the answer doesn't exist in any single source, because the answer lives in the relationships between pages."*  
> — **Andrej Karpathy**

Chào mừng bạn đến với **AI Engineer Personal Knowledge Wiki** — hệ thống tri thức mở được biên soạn và duy trì theo kiến trúc **LLM Wiki**. Khác với các hệ thống RAG truyền thống vốn chỉ lưu trữ các đoạn cắt rời rạc (chunks) thụ động, Wiki này là kết quả của **bước biên dịch tri thức (Compilation Step)**: đọc hiểu toàn bộ hơn 114 tài liệu nguồn trong `resources/`, chắt lọc định nghĩa chuẩn tắc từ các sách kinh điển, chỉ ra mâu thuẫn giữa lý thuyết và thực tiễn sản xuất, và kết nối các khái niệm thành một mạng lưới tri thức sống động.

---

## 🗺️ Bản Đồ Mạng Lưới Tri Thức Tổng Thể (Master Knowledge Graph)

```mermaid
graph TD
    subgraph 1. Nền Tảng Toán & Thống Kê
        Math["Toán học cho ML\n(MML Textbook)"] --> LinReg["[[linear-regression-mle|Hồi quy Tuyến tính & MLE]]"]
        Math --> PCA["[[principal-component-analysis|Phân tích Thành phần Chính (PCA)]]"]
        Math --> Opt["[[optimization-algorithms|Thuật toán Tối ưu hóa (AdamW)]]"]
    end

    subgraph 2. Lý Thuyết Học Máy & Lựa Chọn Mô Hình
        LinReg --> BiasVar["[[bias-variance-tradeoff|Đánh đổi Bias - Variance]]"]
        BiasVar --> Reg["[[regularization-l1-l2|Chính quy hóa L1 / L2]]"]
        BiasVar --> ModSel["[[model-selection-evaluation|Lựa chọn Mô hình & Tránh Data Leakage]]"]
    end

    subgraph 3. Học Sâu & Thị Giác Máy Tính / NLP
        Opt --> GradVan["[[gradient-vanishing-exploding|Triệt tiêu & Bùng nổ Gradient]]"]
        GradVan --> CNN["[[convolutional-neural-networks|Mạng Tích chập & ResNet]]"]
        CNN --> UNet["[[unet-architecture|Kiến trúc U-Net & Phân đoạn Ảnh]]"]
        CNN --> YOLO["[[object-detection-yolo|Phát hiện Vật thể YOLOv1-v10]]"]
        GradVan --> Trans["[[transformer-architecture|Kiến trúc Transformer & Attention]]"]
        Trans --> ViT["[[vision-transformers|Vision Transformer & Swin]]"]
        CNN --> GNN["[[graph-neural-networks|Mạng Nơ-ron Đồ thị (GNN)]]"]
    end

    subgraph 4. Generative AI & Mô Hình Ngôn Ngữ Lớn
        Trans --> LLM["[[large-language-models|Mô hình Ngôn ngữ Lớn (LLM)]]"]
        LLM --> Reas["[[llm-reasoning|Suy luận System 2 (CoT / o1 / R1)]]"]
        LLM --> SFT["[[llm-fine-tuning|Tinh chỉnh LoRA & QLoRA]]"]
        LLM --> Align["[[llm-alignment|Căn chỉnh An toàn (RLHF / DPO)]]"]
        LLM --> Prompt["[[prompt-engineering|Kỹ nghệ Câu lệnh & ICL]]"]
        LLM --> Quant["[[quantization-and-compression|Lượng tử hóa AWQ / GPTQ / GGUF]]"]
        LLM --> Eval["[[llm-evaluation|Đánh giá LLM-as-a-Judge & Ragas]]"]
    end

    subgraph 5. Retrieval-Augmented Generation (RAG)
        LLM --> RAG["[[rag-architecture|Kiến trúc RAG (Naive to Agentic)]]"]
        RAG --> Chunk["[[document-chunking|Chiến lược Phân đoạn (Chunking)]]"]
        RAG --> Vec["[[vector-embeddings|Vector Nhúng & HNSW Index]]"]
        RAG --> Hybrid["[[hybrid-search|Tìm kiếm Lai (Dense + BM25)]]"]
        RAG --> Rerank["[[reranking|Xếp hạng lại (Cross-Encoders)]]"]
        RAG --> QTrans["[[query-transformation|Chuyển đổi Truy vấn (HyDE)]]"]
        RAG --> GRAG["[[graph-rag|Graph RAG & Đồ thị Tri thức]]"]
    end

    subgraph 6. Agentic AI & Hệ Thống Tự Chủ
        Reas --> Agent["[[agentic-ai-core|Kiến trúc Cốt lõi Agentic AI]]"]
        Agent --> ReAct["[[react-pattern|Mô thức ReAct (Thought-Action-Obs)]]"]
        Agent --> Refl["[[reflection-and-self-correction|Phản biện & Tự sửa lỗi]]"]
        Agent --> Plan["[[planning-and-decomposition|Lập kế hoạch & Task DAG]]"]
        Agent --> Tools["[[tool-use-and-function-calling|Sử dụng Công cụ & MCP]]"]
        Agent --> Multi["[[multi-agent-collaboration|Hợp tác Đa tác nhân (Multi-Agent)]]"]
        Agent --> Mem["[[agent-memory-systems|Hệ thống Bộ nhớ Tác nhân (MemGPT)]]"]
        Agent --> HITL["[[human-in-the-loop|Con người trong Vòng lặp (HITL)]]"]
    end

    subgraph 7. MLOps & Kỹ Nghệ Sản Xuất
        Quant --> TRT["[[inference-optimization-tensorrt|Tối ưu hóa Suy luận TensorRT]]"]
        SFT --> MLOps["[[mlops-lifecycle|Vòng đời MLOps & Production Script]]"]
        MLOps --> RegHub["[[experiment-tracking-model-registry|Tracking & Model Registry]]"]
        MLOps --> Serve["[[model-serving-api|Serving API (FastAPI / Triton)]]"]
        MLOps --> K8s["[[containerization-kubernetes-ml|Docker & Kubernetes]]"]
        MLOps --> CICD["[[continuous-integration-cd-ml|CI/CD/CT cho Machine Learning]]"]
        Serve --> Drift["[[data-drift-model-monitoring|Giám sát Data & Concept Drift]]"]
    end

    subgraph 8. Kỹ Nghệ Phần Mềm & Dữ Liệu
        Serve --> OOP["[[oop-core-principles|4 Tính chất OOP & Interface]]"]
        OOP --> SOLID["[[solid-principles|5 Nguyên lý Thiết kế SOLID]]"]
        Serve --> SQL["[[database-indexing-optimization|Chỉ mục DB & Tối ưu SQL]]"]
        SQL --> ACID["[[acid-and-transactions|Giao dịch & Nguyên lý ACID]]"]
        SQL --> NoSQL["[[sql-vs-nosql-data-architecture|Kiến trúc SQL, NoSQL & Lakehouse]]"]
    end
```

---

## 💎 5 Nguyên Lý Vàng Của Senior AI Engineer (Core Architecture Principles)

Được đúc kết từ thực tiễn ngành và chuỗi bài học chuyên gia (*`resources/images/`*):

1. **Model này dùng khi nào? ([[model-selection-evaluation]])**:
   - *Junior*: Trả lời bằng tên model hot nhất hiện tại (e.g. *"Dùng GPT-4o hoặc XGBoost đi anh!"*).
   - *Senior*: Phân tích bài toán, phân bố dữ liệu, ràng buộc độ trễ (Latency SLA), ngân sách chi phí token/GPU và yêu cầu giải thích (Explainability). Biết khi nào nên dùng thống kê cổ điển hoặc rule-based thay vì nhồi nhét AI phức tạp.
2. **Dữ liệu bẩn xử lý sao? ([[model-selection-evaluation]] & [[document-chunking]])**:
   - *Junior*: Nói chung chung là "làm sạch dữ liệu" hoặc xóa trắng outliers.
   - *Senior*: Phân biệt rành mạch giữa *Thiếu dữ liệu (Missing)* và *Dữ liệu sai (Corrupted)*. Hiểu rằng trong nhiều bài toán (phát hiện gian lận, lỗi hệ thống), **Outlier chính là tín hiệu quan trọng nhất**.
3. **Khi nào KHÔNG NÊN dùng AI? ([[human-in-the-loop]])**:
   - *Junior*: Cố gắng nhét AI vào mọi ngóc ngách của ứng dụng.
   - *Senior*: Từ chối dùng AI cho các quy trình hoàn toàn xác định (Deterministic processes), bài toán có ít dữ liệu hoặc đòi hỏi độ chính xác tuyệt đối 100%. Ưu tiên tự động hóa bằng code thuần, connectors và scheduled triggers.
4. **Nếu model sai thì sao? ([[bias-variance-tradeoff]] & [[data-drift-model-monitoring]])**:
   - *Junior*: Lúng túng trả lời *"Để em train lại model!"*.
   - *Senior*: Không có model nào đúng 100%. Phân tích lỗi theo từng lát cắt dữ liệu (**Data Slicing**), thiết lập hàng rào kiểm soát rủi ro (**Fail-safe Mechanisms**) và bẫy lỗi để hệ thống không bao giờ sụp đổ trước người dùng cuối.
5. **Ai chịu trách nhiệm kết quả? ([[human-in-the-loop]])**:
   - *Junior*: Đổ lỗi cho thuật toán hoặc dữ liệu bị nhiễu.
   - *Senior*: **Trách nhiệm pháp lý và đạo đức luôn thuộc về con người và tổ chức vận hành**. AI chỉ là công cụ hỗ trợ ra quyết định. Bắt buộc phải thiết lập cơ chế **Human-in-the-Loop** cho mọi hành động nhạy cảm.

---

## 📚 Mục Lục Phân Tầng Theo 7 Miền Tri Thức

### Miền 1: Generative AI, Foundation Models & Reasoning (8 thực thể)
- [[large-language-models]] — [Mô hình Ngôn ngữ Lớn (LLM)](large-language-models.md): Bản chất xác suất, Scaling Laws, phân loại Causal Decoder-only và năng lực đột sinh.
- [[transformer-architecture]] — [Kiến trúc Transformer](transformer-architecture.md): Cơ chế Scaled Dot-Product Self-Attention, Multi-Head Attention, RoPE, GQA và phân tích bộ nhớ KV Cache.
- [[llm-reasoning]] — [Suy luận trong LLM](llm-reasoning.md): Chuyển dịch từ tư duy System 1 sang System 2 qua Chain-of-Thought, Tree-of-Thoughts, và Test-time Compute (OpenAI o1/o3, DeepSeek-R1).
- [[llm-fine-tuning]] — [Tinh chỉnh LLM (PEFT & LoRA)](llm-fine-tuning.md): Toán học phân rã hạng thấp LoRA, lượng tử hóa QLoRA 4-bit NF4 và phân định ranh giới giữa Fine-Tuning và RAG.
- [[llm-alignment]] — [Căn chỉnh An toàn (RLHF & DPO)](llm-alignment.md): Định hướng theo tiêu chuẩn HHH qua quy trình PPO, hàm mục tiêu đóng Direct Preference Optimization và Constitutional AI.
- [[prompt-engineering]] — [Kỹ nghệ Câu lệnh & ICL](prompt-engineering.md): Cơ chế In-Context Learning, bộ khung cấu trúc prompt chuẩn production, và phòng chống Prompt Injection.
- [[llm-evaluation]] — [Đánh giá & Benchmark LLM](llm-evaluation.md): Hạn chế của BLEU/ROUGE, phương pháp LLM-as-a-Judge, kiểm soát thiên kiến vị trí/độ dài và khung đánh giá Ragas.
- [[quantization-and-compression]] — [Lượng tử hóa & Nén Mô hình](quantization-and-compression.md): Toán học lượng tử hóa tuyến tính, kỹ thuật AWQ, GPTQ, GGUF và giải phóng nút thắt Memory-Bound lúc inference.

### Miền 2: RAG & Hệ Thống Truy Xuất Thông Tin (7 thực thể)
- [[rag-architecture]] — [Kiến trúc RAG Tổng thể](rag-architecture.md): Tiến hóa qua 4 thế hệ (Naive, Advanced, Modular, Agentic RAG) và giải pháp triệt tiêu Ảo giác tri thức.
- [[document-chunking]] — [Chiến lược Phân đoạn Tài liệu](document-chunking.md): Trade-off kích thước chunk, Recursive Character, Semantic Chunking và phương pháp phân tầng Parent-Document.
- [[vector-embeddings]] — [Vector Nhúng & Tìm kiếm ANN](vector-embeddings.md): Không gian vector ngữ nghĩa, độ đo Cosine/Dot-Product và thuật toán đồ thị phân tầng HNSW.
- [[hybrid-search]] — [Tìm kiếm Lai (Dense + Sparse)](hybrid-search.md): Dung hợp tìm kiếm ngữ nghĩa vector và từ khóa BM25 qua giải thuật Reciprocal Rank Fusion (RRF).
- [[reranking]] — [Xếp hạng Lại với Cross-Encoders](reranking.md): Kiến trúc hai tầng (Two-stage Retrieval), cơ chế All-to-All Attention và tối ưu hóa chi phí ngữ cảnh.
- [[query-transformation]] — [Chuyển đổi & Mở rộng Truy vấn](query-transformation.md): Cầu nối ngữ nghĩa qua HyDE (Hypothetical Document Embeddings), Sub-query Decomposition và Step-back Prompting.
- [[graph-rag]] — [Graph RAG & Đồ thị Tri thức](graph-rag.md): Khắc phục điểm mù toàn cục của Vector RAG bằng phân cụm cộng đồng Leiden và tóm tắt phân tầng Map-Reduce.

### Miền 3: Agentic AI & Các Mẫu Thiết Kế Tác Nhân (8 thực thể)
- [[agentic-ai-core]] — [Kiến trúc Cốt lõi Agentic AI](agentic-ai-core.md): Mental model "LLM là CPU, Agent là Process, Framework là OS"; chu trình khép kín Perceive-Plan-Act-Observe-Reflect.
- [[react-pattern]] — [Mô thức ReAct](react-pattern.md): Hiệp đồng giữa Suy luận (Reasoning) và Hành động (Acting) qua chuỗi Thought-Action-Observation.
- [[reflection-and-self-correction]] — [Phản biện & Tự sửa lỗi](reflection-and-self-correction.md): Mô hình Reflexion, Self-Refine và kiến trúc song tác tử Actor-Critic với phản hồi khách quan.
- [[planning-and-decomposition]] — [Lập kế hoạch & Phân rã Nhiệm vụ](planning-and-decomposition.md): Phân rã mục tiêu trừu tượng thành đồ thị DAG, thực thi song song qua LLM Compiler.
- [[tool-use-and-function-calling]] — [Sử dụng Công cụ & MCP](tool-use-and-function-calling.md): Giao thức JSON Schema, Native Function Calling và cuộc cách mạng chuẩn hóa Model Context Protocol.
- [[multi-agent-collaboration]] — [Hợp tác Đa tác nhân](multi-agent-collaboration.md): Phân chia trách nhiệm (SOPs), mô hình Supervisor-Worker, tranh luận đối kháng và tối ưu hóa ngữ cảnh cô lập.
- [[agent-memory-systems]] — [Hệ thống Bộ nhớ Tác nhân](agent-memory-systems.md): Phân tầng 4 cấp độ (Working, Episodic, Semantic, Procedural) và kiến trúc phân trang MemGPT.
- [[human-in-the-loop]] — [Con người trong Vòng lặp & Quản trị](human-in-the-loop.md): Cổng phê duyệt an toàn (Approval Gates), đặc quyền tối thiểu và phân định trách nhiệm pháp lý.

### Miền 4: Deep Learning & Computer Vision / NLP (6 thực thể)
- [[convolutional-neural-networks]] — [Mạng Tích chập & ResNet](convolutional-neural-networks.md): Toán tử tương quan chéo 2D, Receptive Field, tính bất biến tịnh tiến và bước đột phá Residual Highway.
- [[unet-architecture]] — [Kiến trúc U-Net & Phân đoạn Ảnh](unet-architecture.md): Mô hình Encoder-Decoder đối xứng, kết nối tắt Concatenation bảo toàn vị trí điểm ảnh và hàm mất mát Dice Loss.
- [[object-detection-yolo]] — [Phát hiện Vật thể & Dòng họ YOLO](object-detection-yolo.md): Single-stage regression, Anchor-free, FPN/PANet, phân tích IoU/mAP và kiến trúc NMS-free của YOLOv10.
- [[vision-transformers]] — [Vision Transformers & Swin](vision-transformers.md): Chiếu Patch Embedding, giới hạn của Attention bậc hai và giải pháp cửa sổ dịch chuyển Shifted Windows tuyến tính.
- [[inference-optimization-tensorrt]] — [Tối ưu hóa Suy luận & TensorRT](inference-optimization-tensorrt.md): Định dạng trung gian ONNX, hợp nhất tầng CBR Kernel Fusion và hiệu chuẩn lượng tử hóa INT8 KL-Divergence.
- [[graph-neural-networks]] — [Mạng Nơ-ron Đồ thị (GNN)](graph-neural-networks.md): Khung truyền tin Message Passing, kiến trúc GCN/GAT, hiện tượng Over-smoothing và mở rộng qua GraphSAGE.

### Miền 5: Machine Learning & Nền Tảng Toán Học (7 thực thể)
- [[linear-regression-mle]] — [Hồi quy Tuyến tính & MLE](linear-regression-mle.md): Phương trình chuẩn tắc Normal Equation, chứng minh toán học sự tương đương giữa OLS và Maximum Likelihood với nhiễu Gaussian.
- [[bias-variance-tradeoff]] — [Đánh đổi Bias - Variance](bias-variance-tradeoff.md): Dẫn xuất khai triển sai số dự đoán kỳ vọng, chẩn đoán Underfitting/Overfitting và hiện tượng Double Descent trong Deep Learning.
- [[regularization-l1-l2]] — [Chính quy hóa L1 & L2](regularization-l1-l2.md): Bản chất hình học hình thoi L1 (Sparsity) vs hình cầu L2 (Weight Decay), nghiệm đóng Ridge và phân phối tiên nghiệm Bayes.
- [[gradient-vanishing-exploding]] — [Triệt tiêu & Bùng nổ Gradient](gradient-vanishing-exploding.md): Toán học quy tắc chuỗi qua mạng sâu $L$ tầng, tử huyệt của Sigmoid/Tanh và giải pháp He Init/ReLU.
- [[optimization-algorithms]] — [Các Thuật toán Tối ưu hóa](optimization-algorithms.md): Từ SGD Momentum, RMSprop đến Adam và sự tách rời số hạng Weight Decay trong AdamW.
- [[principal-component-analysis]] — [Phân tích Thành phần Chính (PCA)](principal-component-analysis.md): Hai góc nhìn toán học (Tối đa hóa phương sai vs Tối thiểu hóa sai số tái tạo), phân rã SVD và Scree Plot.
- [[model-selection-evaluation]] — [Chiến lược Lựa chọn Mô hình](model-selection-evaluation.md): K-Fold Cross-Validation, tiêu chuẩn AIC/BIC, phòng chống Data Leakage và bộ 3 triết lý chọn mô hình thực chiến.

### Miền 6: MLOps & Kỹ Nghệ Sản Xuất (6 thực thể)
- [[mlops-lifecycle]] — [Vòng đời MLOps & Production Script](mlops-lifecycle.md): 3 cấp độ trưởng thành MLOps của Google, 6 bước refactor mã nguồn từ Jupyter Notebook sang Production Scripts.
- [[experiment-tracking-model-registry]] — [Theo dõi Thử nghiệm & Registry](experiment-tracking-model-registry.md): Quản trị tham số, số liệu và artifacts qua MLflow/W&B; quy trình thăng hạng mô hình Staging sang Production.
- [[model-serving-api]] — [Triển khai Dịch vụ API Mô hình](model-serving-api.md): Xây dựng API bất đồng bộ với FastAPI/Uvicorn, kiến trúc Dynamic Batching và phục vụ GPU thông lượng cao qua Triton.
- [[containerization-kubernetes-ml]] — [Docker & Điều phối Kubernetes](containerization-kubernetes-ml.md): Kỹ thuật Multi-stage build rút gọn image, quản lý GPU Driver qua NVIDIA Operator và HPA theo dõi GPU.
- [[continuous-integration-cd-ml]] — [CI/CD/CT cho Machine Learning](continuous-integration-cd-ml.md): Tự động hóa kiểm thử mã nguồn, dữ liệu và mô hình; các chiến lược phát hành Canary, Blue-Green và Shadow.
- [[data-drift-model-monitoring]] — [Giám sát Dữ liệu & Trôi dạt Mô hình](data-drift-model-monitoring.md): Phân loại Data Drift vs Concept Drift, các phép kiểm định thống kê KS-Test, Population Stability Index (PSI).

### Miền 7: Kỹ Nghệ Phần Mềm & Hệ Thống Dữ Liệu (5 thực thể)
- [[oop-core-principles]] — [4 Tính chất OOP & Vai trò Interface](oop-core-principles.md): Đóng gói, Trừu tượng, Kế thừa, Đa hình giải thích qua bài toán kỹ thuật thực tế; tại sao bắt buộc phải có Interface?
- [[solid-principles]] — [5 Nguyên lý Thiết kế SOLID](solid-principles.md): SRP, OCP, LSP, ISP và trọng tâm Dependency Inversion (chữ D) giải thích bằng ví dụ kiến trúc AI Service/Repository.
- [[database-indexing-optimization]] — [Chỉ mục DB & Tối ưu hóa Truy vấn](database-indexing-optimization.md): Cấu trúc B+Tree, phân tích EXPLAIN Execution Plan, giải quyết N+1 Query Problem, WHERE vs HAVING, TRUNCATE vs DELETE.
- [[acid-and-transactions]] — [Giao dịch & Nguyên lý ACID](acid-and-transactions.md): 4 thuộc tính ACID, 4 cấp độ cô lập giao dịch ANSI, giải quyết tranh chấp đồng thời bằng Khóa bi quan vs Khóa lạc quan.
- [[sql-vs-nosql-data-architecture]] — [Kiến trúc SQL, NoSQL & Lakehouse](sql-vs-nosql-data-architecture.md): Đối chiếu lưu trữ Dòng (Row-wise OLTP) vs Cột (Column-wise OLAP), Định lý CAP phân tán và kiến trúc Lakehouse.

---

## 🔤 Chỉ Mục Tra Cứu Chữ Cái A - Z (Alphabetical Index)

- **A**:
  - [[acid-and-transactions]] — Giao dịch và Nguyên lý ACID trong Database.
  - [[agentic-ai-core]] — Kiến trúc Cốt lõi của Agentic AI.
  - [[agent-memory-systems]] — Hệ thống Bộ nhớ của Tác nhân AI.
- **B**:
  - [[bias-variance-tradeoff]] — Sự đánh đổi giữa Độ chệch và Phương sai.
- **C**:
  - [[containerization-kubernetes-ml]] — Đóng gói Docker và Điều phối Kubernetes cho ML.
  - [[continuous-integration-cd-ml]] — Tích hợp, Triển khai và Huấn luyện Liên tục (CI/CD/CT).
  - [[convolutional-neural-networks]] — Mạng Nơ-ron Tích chập (CNN) và ResNet.
- **D**:
  - [[database-indexing-optimization]] — Đánh chỉ mục Cơ sở dữ liệu và Tối ưu hóa Query SQL.
  - [[data-drift-model-monitoring]] — Giám sát Dữ liệu và Trôi dạt Mô hình (Data & Concept Drift).
  - [[document-chunking]] — Các Chiến lược Phân đoạn Tài liệu trong RAG.
- **E**:
  - [[experiment-tracking-model-registry]] — Theo dõi Thử nghiệm và Đăng ký Mô hình (MLflow).
- **G**:
  - [[gradient-vanishing-exploding]] — Vấn đề Triệt tiêu và Bùng nổ Gradient trong Mạng sâu.
  - [[graph-neural-networks]] — Mạng Nơ-ron Đồ thị (GNN, GCN, GAT).
  - [[graph-rag]] — Graph RAG và Đồ thị Tri thức phân tầng.
- **H**:
  - [[human-in-the-loop]] — Con người trong Vòng lặp và Quản trị Tác nhân.
  - [[hybrid-search]] — Tìm kiếm Lai kết hợp Dense Vector và Sparse BM25.
- **I**:
  - [[inference-optimization-tensorrt]] — Tối ưu hóa Suy luận với ONNX và NVIDIA TensorRT.
- **L**:
  - [[large-language-models]] — Mô hình Ngôn ngữ Lớn (LLM) và Foundation Models.
  - [[linear-regression-mle]] — Hồi quy Tuyến tính và Ước lượng Hợp lý Cực đại (MLE).
  - [[llm-alignment]] — Căn chỉnh Mô hình Ngôn ngữ Lớn (RLHF, DPO, Constitutional AI).
  - [[llm-evaluation]] — Đánh giá Mô hình Ngôn ngữ Lớn và LLM-as-a-Judge.
  - [[llm-fine-tuning]] — Tinh chỉnh Mô hình Ngôn ngữ Lớn (SFT, LoRA, QLoRA).
  - [[llm-reasoning]] — Năng lực Suy luận trong LLM (CoT, ToT, Reasoning Models).
- **M**:
  - [[mlops-lifecycle]] — Vòng đời MLOps và Chuyển đổi Kịch bản Sản xuất.
  - [[model-selection-evaluation]] — Chiến lược Lựa chọn và Đánh giá Mô hình Học máy.
  - [[model-serving-api]] — Triển khai Mô hình thành Dịch vụ API (FastAPI, Triton).
  - [[multi-agent-collaboration]] — Hợp tác Đa tác nhân và Hệ thống Phối hợp.
- **O**:
  - [[object-detection-yolo]] — Phát hiện Vật thể và Dòng họ YOLO (v1 đến v10).
  - [[oop-core-principles]] — 4 Tính chất Cốt lõi của OOP và Vai trò của Interface.
  - [[optimization-algorithms]] — Các Thuật toán Tối ưu hóa (SGD, Adam, AdamW).
- **P**:
  - [[planning-and-decomposition]] — Lập kế hoạch và Phân rã Nhiệm vụ cho AI Agent.
  - [[principal-component-analysis]] — Phân tích Thành phần Chính (PCA).
  - [[prompt-engineering]] — Kỹ thuật Kỹ nghệ Câu lệnh và In-Context Learning.
- **Q**:
  - [[quantization-and-compression]] — Lượng tử hóa và Nén Mô hình (INT8/INT4, AWQ, GPTQ).
  - [[query-transformation]] — Chuyển đổi và Mở rộng Truy vấn trong RAG (HyDE, Sub-query).
- **R**:
  - [[rag-architecture]] — Kiến trúc Tạo sinh Tăng cường Truy xuất (RAG).
  - [[react-pattern]] — Mô thức ReAct: Phối hợp Suy luận và Hành động.
  - [[reflection-and-self-correction]] — Phản biện và Tự sửa lỗi trong Agentic AI.
  - [[regularization-l1-l2]] — Kỹ thuật Chính quy hóa L1 Lasso và L2 Ridge.
  - [[reranking]] — Xếp hạng Lại tài liệu sau Truy xuất (Cross-Encoders).
- **S**:
  - [[solid-principles]] — 5 Nguyên lý Thiết kế Phần mềm Bền vững SOLID.
  - [[sql-vs-nosql-data-architecture]] — Kiến trúc Dữ liệu SQL, NoSQL, Cột OLAP và Lakehouse.
- **T**:
  - [[tool-use-and-function-calling]] — Sử dụng Công cụ, Function Calling và Chuẩn MCP.
  - [[transformer-architecture]] — Kiến trúc Transformer và Cơ chế Tự chú ý (Self-Attention).
- **U**:
  - [[unet-architecture]] — Kiến trúc U-Net và Phân đoạn Ảnh Ngữ nghĩa.
- **V**:
  - [[vector-embeddings]] — Vector Nhúng và Thuật toán Tìm kiếm Tương đồng HNSW.
  - [[vision-transformers]] — Thị giác Máy tính Dựa trên Transformer (ViT & Swin).

---

## 📖 Bảng Quy Chiếu Đối Soát Nguồn Chân Lý (Canonical Ground Truth Mapping)

| Miền Tri thức | Sách Giáo Khoa Kinh Điển (Canonical Textbook) | Tài liệu Bài giảng / Thực hành tương ứng |
| :--- | :--- | :--- |
| **GenAI & LLMs** | [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) | `Vietnamese_Introduction-to-LLMs.pdf`, `LLM Interview QnA.pdf` |
| **RAG Systems** | *Encyclopedia of LLMs* (Chapter 13); Lewis et al. (2020) | `giao_trinh_rag.pdf`, `english_GiaiThichThuatNguRAG.pdf`, `AIO2025_Tutorial_RAG.pdf` |
| **Agentic AI** | [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) | `Agentic AI Design Patterns(2026 Edition).pdf`, `giao_trinh_agentic.pdf` |
| **Deep Learning** | [The-Principles-of-Deep-Learning-Theory.pdf](../../resources/deep-learning/The-Principles-of-Deep-Learning-Theory.pdf) | `Deep Learning_Computer Vision_NLP.pdf`, `AIO2025_Reading_CNNs.pdf` |
| **Machine Learning** | [Mathematics-for-Machine-Learning.pdf](../../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) | `03_LinearRegression-with-MLE.pdf`, `Bias-Variance_Tradeoff.pdf` |
| **ML Theory** | [understanding-machine-learning-theory-algorithms.pdf](../../resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf) | `Machinelearningyearning-Vi.pdf` (Andrew Ng) |
| **Graph Learning** | [Deep-Learning-on-Graphs.pdf](../../resources/deep-learning/Deep-Learning-on-Graphs.pdf) (Cambridge) | `AIO2026_[Reading]-RAG-System.pdf` (Graph RAG sections) |
| **MLOps** | Google Cloud MLOps Architecture Guidelines | `AIO2025_MLOps_CICD.pdf`, `Session 1` đến `Session 9` Bootcamp |
| **Database Systems** | [Fundamentals of Database System.pdf](../../resources/software/Fundamentals%20of%20Database%20System.pdf) | `DatabaseSQL.jpg`, `JavaOOP-Core.jpg`, `Questtion.txt` |
"""

def generate():
    output_path = Path("wiki/index.md")
    output_path.write_text(INDEX_CONTENT.strip(), encoding="utf-8")
    print(f"Created master index: {output_path}")

if __name__ == "__main__":
    generate()
