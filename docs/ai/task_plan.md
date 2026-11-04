# Kế Hoạch & Báo Cáo Tiến Độ Nâng Cấp Bộ Tài Liệu Phỏng Vấn AI Engineer - ATIN (Computer Vision & Serving Focus)

## 1. Mục Tiêu & Bối Cảnh
- **Doanh nghiệp tuyển dụng**: Công ty Cổ phần Sáng tạo Công nghệ ATIN (ATIN Advanced Technology Innovations - `https://atin.com.vn/vi/`).
- **Trụ sở**: TT3D.70 Khu đô thị Phùng Khoang Nam Cường, phường Thanh Xuân, TP. Hà Nội.
- **Lĩnh vực cốt lõi**: Trí tuệ Nhân tạo (AI), Thị giác Máy tính (Computer Vision - Camera AI giám sát an ninh trật tự, nhận diện khuôn mặt, nhận diện biển số xe ANPR, IOC điều hành thông minh, tự động hóa cảng biển & logistics container), Tác nhân thông minh (Agent AI), Phát triển phần mềm theo yêu cầu.
- **Vị trí**: AI Engineer (Trọng tâm: Computer Vision từ cơ bản đến nâng cao, từ Notebook đến Production Serving; bên cạnh đó là Nền tảng ML/DL, LLM/AI Agent, Software Engineering, CSDL & MLOps).

---

## 2. Trạng Thái Hoàn Thành Các Hạng Mục (100% DONE)

### ✅ Bước 1: Khảo Sát & Khai Thác Nguồn Chân Lý (Done)
- Khai thác toàn diện tài liệu từ `resources/deep-learning/computer-vision/`, `resources/machine-learning/`, `resources/ops/`, `resources/genai/`, `resources/software/`, `resources/database/` và `wiki/`.
- Tích hợp các badge liên kết `.resource-pill` trỏ trực tiếp đến tài liệu PDF canonical và wiki.

### ✅ Bước 2: Cập Nhật `interview/script.js` & `interview/style.css` (Done)
- Đổi theme key từ `baha_interview_theme` thành `atin_interview_theme`.
- Cập nhật ReAct Simulator sang bài toán phân tích luồng RTSP Camera ANPR & TensorRT của ATIN.
- Cập nhật 3D Digital Twin Studio sang mô hình Smart City IOC & Port Logistics Digital Twin của ATIN.
- Cập nhật bộ tính toán thông lượng GPU Inference & VRAM Calculator cho luồng camera RTSP.
- Bổ sung CSS class `.resource-pill` và tinh chỉnh typography.

### ✅ Bước 3: Cải Tạo Toàn Diện 9 Module Trong `interview/index.html` (5,071 Dòng Sư Phạm Chuyên Sâu) (Done)
- **Header & Sidebar Navigation**: Thiết lập kiến trúc 9 module rõ ràng, navigation anchor links đồng bộ 100% với các section và subsection.
- **Module 01: Doanh Nghiệp ATIN, Bóc Tách JD & 3 Đại Pipeline CV Thực Tế**:
  - 1.1 Chân dung ATIN & hệ sinh thái sản phẩm công nghệ.
  - 1.2 Bóc tách nhu cầu tuyển dụng AI Engineer thực tế tại ATIN.
  - 1.3 Từ điển thuật ngữ chuyên ngành CV & Serving thực chiến.
  - 1.4 **Kiến trúc 3 Đại Pipeline CV Thực Tế Tại ATIN**:
    - *Pipeline 1:* Giám sát giao thông & Phạt nguội (ANPR + Vượt đèn đỏ/Lấn làn).
    - *Pipeline 2:* Tự động hóa cảng biển & Logistics Container (ISO 6346 OCR + U-Net hư hại + Transaction TOS).
    - *Pipeline 3:* Kiểm soát ra vào khuôn mặt tốc độ cao (RetinaFace + 5 Landmarks Affine Alignment + ArcFace Loss + HNSW).
- **Module 02: Nền Tảng Học Máy & Học Sâu Toàn Tập (ML & DL Core Foundations)**:
  - 2.1 Bản chất học máy, 4 trường phái, phân rã toán học Bias-Variance Tradeoff, Điều chuẩn L1 (Lasso - sinh ma trận thưa) vs L2 (Ridge/Weight Decay), Overfitting/Underfitting, Early Stopping, Inverted Dropout, Data Augmentation.
  - 2.2 **Toàn tập Hàm Kích Hoạt (Activation Functions)**: Sigmoid, Tanh, ReLU, LeakyReLU, PReLU, ELU, GELU (chuẩn Transformer), Swish/SiLU (chuẩn YOLO), Softmax (công thức, miền giá trị, đạo hàm, hiện tượng bão hòa và căn bệnh Dead ReLU).
  - 2.3 **Toàn tập Hàm Mất Mát (Loss Functions)**: Hồi quy (MSE, MAE, Huber/Smooth L1), Phân loại (BCE, CCE, **Focal Loss toán học triệt tiêu mất cân bằng lớp 1000:1 trong RetinaNet**, Label Smoothing), Phân đoạn (Dice Loss, Combo Loss), Metric Learning (Triplet Loss, ArcFace Additive Angular Margin), Bounding Box Regression (IoU, GIoU, DIoU, CIoU, EIoU).
  - 2.4 **Toàn tập Độ Đo Đánh Giá (Evaluation Metrics)**: Ma trận nhầm lẫn (Confusion Matrix), Accuracy, Precision, Recall, Specificity, F1-Score, Phân biệt sống còn Macro-F1 vs Micro-F1 vs Weighted-F1, ROC-AUC vs PR-AUC, Object Detection AP & mAP@0.5:0.95 (COCO), Tracking MOTA, MOTP, IDF1, HOTA.
  - 2.5 **Thuật toán Tối Ưu (Optimizers) & Bùng nổ/Triệt tiêu Gradient**: Mini-batch SGD, Momentum, NAG, AdaGrad, RMSprop, Adam, AdamW (Weight Decay tách rời); Phân tích chuỗi vi phân Chain Rule triệt tiêu gradient, Khởi tạo trọng số Xavier vs He/Kaiming, Batch Normalization vs Layer Normalization, Gradient Clipping.
  - 2.6 **Mạng Nơ-ron Cơ Bản & Chuỗi Tuần Hoàn**: Perceptron, MLP, Lan truyền ngược (Backpropagation), RNN & vấn đề mất trí nhớ dài hạn BPTT, LSTM (3 cổng $f_t, i_t, o_t$ & Cell State Highway giải quyết vanishing gradient), GRU (2 cổng tinh gọn).
  - 2.7 **Phân Loại Đa Nhãn (Multi-Label Classification) & Kiến Trúc C2AE**: Multi-Class vs Multi-Label (Softmax vs Independent Sigmoids), Problem Transformation (Binary Relevance, Classifier Chains, Label Powerset), Asymmetric Loss (ASL), Kiến trúc C2AE (Canonical Correlated AutoEncoder với chuẩn Frobenius căn chỉnh không gian tiềm ẩn chung và ràng buộc trực giao ma trận Gram), Độ đo Hamming Loss & Subset Accuracy.
- **Module 03: Thị Giác Máy Tính Nền Tảng & Mạng Tích Chập (CV & CNNs)**:
  - 3.1 Biểu diễn ảnh số, không gian màu (RGB/HSV/YCrCb), lọc làm mịn (Gaussian vs Median), Canny Edge Detection 4 bước toán học nghiêm ngặt.
  - 3.2 Xử lý hình thái học (Dilation, Erosion, Opening, Closing) & Biến đổi phối cảnh Homography $3\times3$ nắn phẳng biển số.
  - 3.3 Mạng tích chập (CNNs), phép tính Conv2D toán học, Stride, Padding, Receptive Field mở rộng, ResNet Skip Connection toán học $+1$.
  - 3.4 MobileNet Depthwise Separable Convolution (tiết kiệm tính toán $8-9$ lần), Vision Transformers (ViT) & Swin Transformer (Shifted Windows).
- **Module 04: Tác Vụ CV Chuyên Sâu Tại ATIN (Detection, Segmentation, Face, Tracking)**:
  - 4.1 Two-Stage Detection: R-CNN, Fast R-CNN, Faster R-CNN (RPN, Anchor boxes), **Đột phá RoIAlign trong Mask R-CNN triệt tiêu 100% sai số lượng tử hóa bằng Nội suy song tuyến (Bilinear Interpolation)**.
  - 4.2 One-Stage Detection: **Gia phả họ YOLO toàn tập từ v1 đến v10 (NMS-free Dual Label Assignment, CIB, PSA)**.
  - 4.3 Phân đoạn ảnh ngữ nghĩa: U-Net đối xứng (Encoder-Decoder, Skip Connections), Combo Loss (BCE + Dice).
  - 4.4 Nhận diện khuôn mặt: RetinaFace + 5 facial landmarks Affine alignment + ArcFace Additive Angular Margin Loss + HNSW Vector Search.
  - 4.5 Bám vết đa đối tượng: **Kalman Filter tuyến tính 8 chiều**, Hungarian Algorithm, So sánh SORT vs DeepSORT vs ByteTrack (2-stage association) vs BoT-SORT (Camera Motion Compensation), Thuật toán đếm vạch Virtual Tripwire (Tích có hướng vector & Debounce Cache).
- **Module 05: MLOps CV & Model Serving Toàn Diện (AIO Sessions 1-9)**:
  - 5.1 Vòng đời MLOps 9 giai đoạn chuẩn doanh nghiệp & 6 bước Refactor Notebook sang Production Script.
  - 5.2 Quản lý thực nghiệm (MLflow Tracking & Model Registry) & Phiên bản hóa dữ liệu (DVC trên S3/MinIO).
  - 5.3 Tối ưu hóa suy luận mô hình: ONNX Export, NVIDIA TensorRT (Layer CBR Fusion, Lượng tử hóa INT8 PTQ KL-Divergence Calibration).
  - 5.4 Serving Real-Time Streaming: FastAPI Async (Hóa giải triệt để Event Loop Blocking Trap bằng ThreadPoolExecutor), NVIDIA Triton Inference Server (Dynamic Batching, Concurrent Execution, Model Ensemble gRPC).
  - 5.5 Đóng gói Docker GPU Multi-stage Build (< 2.5GB), Kubernetes Triển khai & Giám sát Data Drift / Concept Drift (KS-Test, PSI, Evidently AI, Prometheus + Grafana).
- **Module 06: Transformer Architecture & LLMs / Reasoning**: Scaled Dot-Product Attention, MHA/MQA/GQA, RoPE, KV Cache & PagedAttention, SFT, LoRA/QLoRA NF4, System 1 vs System 2 Reasoning (CoT / o1 / R1), Tokenization BPE.
- **Module 07: Prompt Engineering, RAG Toàn Diện & Agent Harness**: Kỹ nghệ prompt RICE & Delimiters, Hybrid Search (BM25 + Dense Vector) & Cross-Encoder Reranker, Chu trình ReAct & 20 mẫu thiết kế Agent, 9 thành phần kiến trúc Agent Harness chịu tải bền bỉ.
- **Module 08: Kỹ Nghệ Phần Mềm & CSDL Toàn Diện**:
  - 8.1 Python nâng cao (Asyncio, GIL, Pydantic V2), OOP 4 trụ cột, 5 nguyên lý SOLID, Bảng tra cứu Design Patterns cho AI.
  - 8.2 Clean Architecture 3 tầng (Router - Service - Repository) & FastAPI Microservices.
  - 8.3 CSDL quan hệ, DDL/DML/DQL, Thứ tự thực thi logic SQL, JOIN, CTE, Window Functions, Transaction ACID & 4 cấp độ cô lập, Đánh Index B+Tree (Seq Scan vs Index Scan).
  - 8.4 NoSQL (Document, Key-Value, Columnar, Graph) & CSDL Vector (`pgvector` HNSW vs Milvus chuyên dụng).
- **Module 09: Trắc Nghiệm Sẵn Sàng & Bộ 42 Kịch Bản Phỏng Vấn Sống Còn Tại ATIN**:
  - 9.1 CV Inference Throughput & Latency Calculator cho luồng camera RTSP.
  - 9.2 Bảng trắc nghiệm 25 tiêu chí sẵn sàng AI Engineer.
  - 9.3 **Tuyển tập 42 kịch bản phỏng vấn thực chiến chuẩn Senior/Staff AI Engineer** phân theo 7 nhóm chuyên đề bao quát toàn bộ câu hỏi kỹ thuật từ ATIN.

### ✅ Bước 4: Kiểm Định & Xác Minh Chất Lượng (Done)
- `Select-String -Path "interview\*" -Pattern "BAHA|baha"` $\to$ **0 matches (Clean)**.
- `Select-String -Path "interview\*" -Pattern "vinhomes|Vinhomes"` $\to$ **0 matches (Clean)**.
- Script `docs/ai/validate_anchors.ps1` kiểm tra tất cả anchor links từ sidebar $\to$ **ALL_SIDEBAR_LINKS_PERFECT (100% khớp element id)**.
- Tổng số dòng file `interview/index.html`: **5,071 dòng** nội dung chi tiết, không tóm tắt sơ sài, tích hợp đầy đủ công thức KaTeX, bảng biểu đối sánh và ví dụ thực tế.
