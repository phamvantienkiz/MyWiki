# Kế Hoạch Trích Xuất Tri Thức Wiki (Karpathy Wiki Architecture)

## 1. Mục Tiêu
Trích xuất toàn diện tri thức từ 9 tài liệu mới được thêm vào thư mục `resources/` thành các trang thực thể wiki độc lập chuẩn phong cách Karpathy trong `wiki/`, đồng thời cập nhật mạng lưới liên kết tại `wiki/index.md` và các trang liên quan.

## 2. Danh Sách Tài Liệu Nguồn & Thực Thể Wiki Tương Ứng
1. `resources/build-serving/AIO2026_[Reading]-Basic-Data-Pipeline.pdf` & `resources/build-serving/AIO2026_[Reading]-Modern-Data-Pipeline.pdf`
   - Thực thể 1: `wiki/modern-data-pipeline.md` (Mô hình chiều Kimball vs Inmon, Snowflake 3 tầng, CDC Streams & Tasks, Medallion ELT).
   - Thực thể 2: `wiki/apache-iceberg.md` (Open Table Format, Cây Metadata 4 tầng, Pruning 3 cấp độ, Hidden Partitioning, Schema Evolution qua Field IDs, Hồ dữ liệu lai S3 + Snowflake).
2. `resources/deep-learning/computer-vision/AIO2026_[Reading_v2]_Multi-label_Classification-C2AE.pdf`
   - Thực thể 3: `wiki/multi-label-classification.md` (Multi-class vs Multi-label, Binary Relevance/Label Powerset, kiến trúc C2AE, Latent Alignment, Gram Matrix Penalty, Exponential Pairwise Ranking Loss, Threshold calibration, Hamming Loss / Subset Acc / Micro-Macro F1).
3. `resources/genai/AIO2026_[Reading] - Fine_tuning_LLM_MS-SWIFT.pdf`
   - Thực thể 4: `wiki/ms-swift-llm-finetuning.md` (Vòng đời 5 bước MS-SWIFT, ChatML, công thức batch size hiệu dụng, DDP vs DeepSpeed ZeRO-2/3, Mid-adapter injection với up-projection khởi tạo 0, HF auto_map và plugin registry).
4. `resources/genai/NLP, LLM, AI agent course.pdf` & `resources/genai/RAG_Technical_Documentation.pdf`
   - Thực thể 5: `wiki/modular-rag-production.md` (Modular RAG 2-stage decoupled pipeline, 6 document loaders so sánh chi tiết, 7 chiến lược chunking + MinHash dedup, Hybrid search với RRF k=60, Cross-Encoder reranking, Lost-in-the-Middle sandwich ordering, 3-tier Redis caching, Input/Output/Retrieval Guardrails, RAGAS metrics & Latency Budget).
5. `resources/ops/AIO2026_MLOps_[Reading1]-Docker.pdf` & `resources/ops/AIO2026_MLOps_[Reading2]-Docker.pdf`
   - Thực thể 6: `wiki/docker-ai-inference-packaging.md` (Kiến trúc Docker Daemon/containerd/runc, Linux Namespaces & Cgroups, Copy-on-Write, Named Volumes vs Bind Mounts, Multi-stage builds tối ưu PyTorch CPU từ 10.36GB xuống 2.81GB, tách rời model artifacts qua one-shot prepare container, điều phối Compose với healthcheck & restart policy, least privilege non-root UID 10001).
6. `resources/ops/AIO2026_[Reading_v6]-FastAPI.pdf`
   - Thực thể 7: `wiki/fastapi-production-ml-serving.md` (5-layer clean architecture, Lifespan context manager nạp model một lần, ModelRegistry lazy load có threading.Lock, chống Train/Serve skew qua scikit-learn Pipeline, Pydantic input validation & response_model contract, giải quyết triệt để Event Loop Blocking Trap qua run_in_threadpool, domain exception hierarchy ServiceError).

## 3. Nhật Ký Hoàn Thành
- [x] Khảo sát chi tiết nội dung cả 9 tệp tài liệu PDF nguồn bằng `read_file`.
- [x] Thiết kế và biên soạn 7 trang thực thể wiki độc lập chuẩn phong cách Karpathy trong `wiki/`.
- [x] Cập nhật các liên kết 2 chiều (`wiki-links`) trong các trang wiki liên quan:
  - `wiki/rag-architecture.md`
  - `wiki/llm-fine-tuning.md`
  - `wiki/model-serving-api.md`
  - `wiki/containerization-kubernetes-ml.md`
  - `wiki/sql-vs-nosql-data-architecture.md`
- [x] Cập nhật Master Knowledge Graph (Mermaid), danh mục 7 Miền Tri thức, bảng tra cứu chữ cái A-Z và bảng quy chiếu Canonical Source Mapping trong `wiki/index.md`.
- [x] Kiểm tra trạng thái Git và tính toàn vẹn của liên kết.
