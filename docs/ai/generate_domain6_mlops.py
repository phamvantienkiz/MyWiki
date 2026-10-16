# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = Path("wiki")
WIKI_DIR.mkdir(parents=True, exist_ok=True)

ENTITIES = {
    "mlops-lifecycle.md": r"""# Vòng Đời MLOps và Chuyển Đổi Kịch Bản Sản Xuất (MLOps Lifecycle & Production Engineering)

> **Khái niệm chính thống**: Google Cloud MLOps Maturity Framework; *Session 1: From Notebook to Production Script*; *AIO2025 Series: MLOps Tutorial*.
> **Miền kiến thức**: [[mlops-overview|Machine Learning Operations & Production Systems]]
> **Tài liệu gốc liên quan**:
> - [Sesion 1_ From Notebook to Production Script.pdf](../../resources/ops/Sesion%201_%20From%20Notebook%20to%20Production%20Script.pdf) (Trang 1-23)
> - [AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf](../../resources/ops/AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf) (Trang 1-71)
> - [Session 5_ First Cloud Deployment.pdf](../../resources/ops/Session%205_%20First%20Cloud%20Deployment.pdf) (Trang 1-28)

---

## 1. Tóm tắt (Executive Summary)
**MLOps (Machine Learning Operations)** là sự giao thoa và kết hợp thực hành giữa Machine Learning, DevOps và Kỹ nghệ Dữ liệu (Data Engineering) nhằm chuẩn hóa, tự động hóa và giám sát toàn bộ vòng đời của hệ thống học máy từ giai đoạn thử nghiệm (PoC) đến vận hành sản xuất quy mô lớn. Vấn đề nan giải lớn nhất của các nhà khoa học dữ liệu là "bẫy Jupyter Notebook" (mã nguồn thử nghiệm lộn xộn, biến toàn cục, không có kiểm thử, khó tái lập). MLOps thiết lập các cấp độ trưởng thành (Maturity Levels) để chuyển hóa mã nguồn thành các kịch bản module hóa sản xuất (**Production Scripts**), tích hợp đường ống tự động hóa (**CI/CD/CT**) và giám sát liên tục (**Continuous Monitoring**).

---

## 2. Định nghĩa chính thống & Các cấp độ Trưởng thành MLOps (Google Framework)

```mermaid
flowchart TD
    subgraph Level 0: Manual Process
        NB["Jupyter Notebooks"] --> ManualTrain["Manual Training"]
        ManualTrain --> Pkl["Artifact .pkl / .pt"]
        Pkl --> ManualDeploy["Manual Deployment"]
    end
    
    subgraph Level 1: Automated Pipeline (MLOps Level 1)
        Trigger["Data / Code Trigger"] --> AutoTrain["Automated Training Pipeline"]
        AutoTrain --> ModelReg[("Model Registry")]
        ModelReg --> CD["Automated Deployment (CI/CD)"]
        CD --> Serving["Live Serving"]
        Serving --> Monitor["Data & Drift Monitoring"]
        Monitor -.->|"CT Trigger"| AutoTrain
    end
```

### 2.1 3 Cấp độ Trưởng thành MLOps
1. **Level 0: Thủ công hoàn toàn (Manual Process)**:
   - Dành cho các nhóm mới bắt đầu; mã nguồn nằm trong notebook.
   - Quá trình tiền xử lý, huấn luyện và xuất model ra file `.pkl` được thực hiện thủ công bằng tay.
   - Không có theo dõi thử nghiệm; việc triển khai phụ thuộc hoàn toàn vào kỹ sư DevOps viết lại code từ notebook.
2. **Level 1: Tự động hóa Pipeline Huấn luyện (Continuous Training - CT)**:
   - Toàn bộ quy trình từ Ingestion, Validation, Training, Evaluation được module hóa thành pipeline có thể tái lập (sử dụng Kubeflow Pipelines hoặc Airflow).
   - Khi có dữ liệu mới hoặc phát hiện suy thoái mô hình (Drift), pipeline tự động kích hoạt huấn luyện lại mà không cần can thiệp thủ công.
3. **Level 2: Tự động hóa CI/CD Toàn diện (CI/CD Pipeline Automation)**:
   - Mọi thay đổi về mã nguồn mô hình, mã nguồn dữ liệu và hạ tầng đều được kiểm thử tự động qua CI/CD, tự động đóng gói Docker container và deploy lên cụm Kubernetes.

---

## 3. So sánh & Mâu thuẫn / Sắc thái: Notebook vs Production Script

| Tiêu chí | Jupyter Notebook (Data Science) | Production Script (MLOps Engineering) |
| :--- | :--- | :--- |
| **Cấu trúc mã nguồn** | Các ô cell chạy lộn xộn không theo thứ tự; phụ thuộc biến toàn cục (Global state). | Module hóa thành các package rõ ràng: `src/data/`, `src/models/`, `src/pipelines/`. |
| **Quản lý cấu hình** | Hard-code tham số, đường dẫn file và API keys trực tiếp trong code. | Quản lý cấu hình tập trung qua tệp `.yaml`, `.env` hoặc hệ thống như Hydra / Pydantic Settings. |
| **Xử lý lỗi & Logging** | Dùng lệnh `print()` thô sơ; không có try-catch; crash toàn bộ chương trình khi gặp ngoại lệ. | Sử dụng thư viện `logging` chuẩn mực với phân cấp (DEBUG, INFO, ERROR), ghi log có cấu trúc (JSON logs). |
| **Kiểm thử tự động** | Dùng mắt thường nhìn biểu đồ matplotlib để kết luận. | Bắt buộc có **Unit Tests** (với `pytest`), **Data Validation** (với `Great Expectations` hoặc `Pydantic`). |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Bộ quy chuẩn 6 bước "Refactor Notebook sang Production Script"
Theo giáo trình *Sesion 1: From Notebook to Production Script*:
1. **Tách biệt Logic và Cấu hình**: Chuyển toàn bộ hyperparameters, đường dẫn thư mục vào tệp `config.yaml`.
2. **Loại bỏ Side-effects & Hàm thuần khiết (Pure Functions)**: Mọi thao tác xử lý dữ liệu phải được bọc trong hàm có input và output rõ ràng, không đọc ghi biến toàn cục.
3. **CLI Interface hóa**: Sử dụng `argparse` hoặc `click` để script có thể chạy dễ dàng qua dòng lệnh:
   `python train.py --config configs/production.yaml --epochs 50`
4. **Kiểm soát Dependency**: Cố định phiên bản thư viện qua `requirements.txt` có lockfile hoặc dùng `uv / Poetry`.
5. **Đóng gói Docker**: Xây dựng Dockerfile chuẩn để cô lập hoàn toàn môi trường chạy.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Nợ kỹ thuật (Technical Debt) lớn nhất trong các hệ thống học máy sản xuất là gì?*
  - **A**: Theo bài báo kinh điển của Sculley et al. (Google - *"Hidden Technical Debt in Machine Learning Systems"*), code thuật toán ML thực sự chỉ chiếm một phần nhỏ bé (khoảng 5%) ở trung tâm của toàn bộ hệ thống. 95% còn lại là các phần mềm phụ trợ khổng lồ: thu thập dữ liệu, xác minh dữ liệu, trích xuất đặc trưng, quản lý tài nguyên, giám sát drift và serving infrastructure. Nợ kỹ thuật lớn nhất nằm ở hiện tượng "Glue Code" (viết mã chắp vá giữa các công cụ) và "Pipeline Jungles" (các đường ống tiền xử lý dữ liệu phức tạp đan xen không có tài liệu).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[experiment-tracking-model-registry]] — Hệ thống ghi nhận dấu vết thử nghiệm trong vòng đời MLOps.
- [[model-serving-api]] — Tầng triển khai mô hình thành dịch vụ sau khi hoàn tất pipeline.
- [[containerization-kubernetes-ml]] — Hạ tầng đóng gói và điều phối container cho MLOps.
- [[continuous-integration-cd-ml]] — Tự động hóa kiểm thử và phát hành mô hình.
- [[data-drift-model-monitoring]] — Giám sát chất lượng mô hình khi chạy thực tế.
""",

    "experiment-tracking-model-registry.md": r"""# Theo Dõi Thử Nghiệm và Đăng Ký Mô Hình (Experiment Tracking & Model Registry)

> **Khái niệm chính thống**: *Session 2: Experiment Tracking & Model Management*; Zaharia et al. (2018) *"Accelerating the Machine Learning Lifecycle with MLflow"*; Biewald (2020) *"Experiment Tracking with Weights & Biases"*.
> **Miền kiến thức**: [[mlops-overview|MLOps Governance & Artifact Management]]
> **Tài liệu gốc liên quan**:
> - [Session 2_ Experiment Tracking & Model Management.pdf](../../resources/ops/Session%202_%20Experiment%20Tracking%20%26%20Model%20Management.pdf) (Trang 1-29)
> - [AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf](../../resources/ops/AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf) (Trang 25-40)

---

## 1. Tóm tắt (Executive Summary)
**Theo dõi Thử nghiệm và Đăng ký Mô hình (Experiment Tracking & Model Registry)** là hai thành phần xương sống của quản trị MLOps đảm bảo tính minh bạch, có thể tái lập (Reproducibility) và kiểm soát phiên bản trong suốt quá trình nghiên cứu phát triển mô hình. **Experiment Tracking** (sử dụng MLflow Tracking, W&B) tự động ghi lại toàn bộ siêu tham số, số liệu đánh giá (metrics theo từng epoch), mã nguồn git commit và môi trường phần cứng. **Model Registry** đóng vai trò là một kho lưu trữ tập trung (Central Hub) quản lý vòng đời của các artifact mô hình đã được xác thực, kiểm soát việc thăng hạng phiên bản qua các giai đoạn: `Staging -> Production -> Archived`.

---

## 2. Định nghĩa chính thống & Kiến trúc MLflow

```mermaid
flowchart TD
    subgraph Training Runs
        Run1["Run 1: lr=0.01, AdamW"] --> MLflowServer["MLflow Tracking Server"]
        Run2["Run 2: lr=0.001, SGD"] --> MLflowServer
        Run3["Run 3: lr=0.0005, Cosine"] --> MLflowServer
    end
    
    subgraph Storage Backends
        MLflowServer --> DB[("Backend Store (PostgreSQL / SQLite)\nParameters, Metrics, Tags")]
        MLflowServer --> S3[("Artifact Store (AWS S3 / MinIO / GCS)\nModel Weights, Plots, Scalers")]
    end
    
    MLflowServer --> BestModel["Select Best Run (Lowest Val Loss)"]
    BestModel --> Registry["Model Registry: 'fraud_detector'"]
    
    subgraph Model Lifecycle Stages
        Registry --> V1["Version 1 (Archived)"]
        Registry --> V2["Version 2 (Staging)"]
        Registry --> V3["Version 3 (Production - Active Serving)"]
    end
```

### 2.1 4 Trụ cột Thông tin bắt buộc ghi lại của một Run
1. **Code Version**: Git commit hash chính xác của lần chạy thử nghiệm đó.
2. **Parameters & Hyperparameters**: Tệp cấu hình đầu vào (learning rate, batch size, model architecture, random seed).
3. **Metrics (Time-series data)**: Training loss, validation accuracy, F1 score ghi nhận tại từng step hoặc epoch.
4. **Artifacts (Binary Files)**: Trọng số mô hình (`model.bin`), ma trận nhầm lẫn (`confusion_matrix.png`), bộ tiền xử lý (`preprocessor.pkl`), tệp mô tả môi trường (`conda.yaml` / `requirements.txt`).

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các công cụ

| Tiêu chí | Git LFS / DVC (Data Version Control) | MLflow | Weights & Biases (W&B) |
| :--- | :--- | :--- | :--- |
| **Bản chất cốt lõi** | Quản lý phiên bản dữ liệu lớn và file nhị phân qua cơ chế con trỏ Git. | Nền tảng MLOps toàn diện mã nguồn mở (Tracking, Models, Registry, Projects). | Nền tảng SaaS thương mại trực quan hóa và giám sát thử nghiệm cao cấp. |
| **Môi trường triển khai** | Chạy CLI cục bộ, lưu trữ trên S3/GCS. | Dễ dàng tự host (Self-hosted) trên máy chủ nội bộ hoặc Kubernetes. | Đám mây công cộng (Cloud-hosted) hoặc Enterprise On-premise đắt đỏ. |
| **Thế mạnh đặc thù** | Versioning các tập dataset hàng chục GB. | **Model Registry** độc lập, tích hợp mượt mà với API Serving. | Trực quan hóa tương tác 3D, biểu đồ phân tích chuyên sâu cho LLM/Computer Vision. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy trình Thăng hạng Mô hình (Model Promotion Workflow)
Tuyệt đối không bao giờ cho phép mô hình mới train xong deploy thẳng vào Production:
1. **Candidate Registration**: Mô hình tốt nhất trong đợt huấn luyện được đẩy vào Registry với nhãn trạng thái `Stage: Staging`.
2. **Automated Integration Testing**: Hệ thống CI/CD kích hoạt kiểm thử ngầm trên tập dữ liệu kiểm định độc lập (Golden Evaluation Dataset), đo độ trễ suy luận và kiểm tra lỗ hổng bảo mật.
3. **Human Approval / Canary Transition**: Chuyên gia AI duyệt thăng hạng `Stage: Production`. Hệ thống điều phối hạ tầng tự động cập nhật API server trỏ sang phiên bản mới mà không gây gián đoạn dịch vụ (Zero-Downtime Deployment).

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao việc lưu trữ hạt giống ngẫu nhiên (Random Seed) trong Experiment Tracking là cần thiết nhưng vẫn chưa đủ để đảm bảo tính tái lập 100% trên GPU?*
  - **A**: Mặc dù đã cố định seed trong Python (`random.seed`), NumPy (`np.random.seed`) và PyTorch (`torch.manual_seed`), trên GPU NVIDIA các thuật toán tính toán tích chập và giảm trừ của thư viện cuDNN/CUDA mặc định sử dụng cơ chế bất định (Non-deterministic atomic operations) để tối ưu hóa tốc độ. Để đạt tính tái lập tuyệt đối, kỹ sư bắt buộc phải bật cờ:
    `torch.use_deterministic_algorithms(True)` và `torch.backends.cudnn.deterministic = True` (chấp nhận đánh đổi tốc độ chậm hơn một chút).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[mlops-lifecycle]] — Khung vận hành MLOps tổng thể.
- [[model-serving-api]] — Nơi tiếp nhận artifact mô hình từ Model Registry để phục vụ API.
- [[continuous-integration-cd-ml]] — Kích hoạt pipeline kiểm thử tự động khi model thăng hạng.
- [[data-drift-model-monitoring]] — Đối chiếu phiên bản model trong Registry với dữ liệu drift thực tế.
""",

    "model-serving-api.md": r"""# Triển Khai Mô Hình Thành Dịch Vụ API (Model Serving & High-Performance APIs)

> **Khái niệm chính thống**: *Session 3: Serving Models as a Live API*; NVIDIA Triton Inference Server Architecture; *Encyclopedia of LLMs*, Section 11.2 (Serving Infrastructure).
> **Miền kiến thức**: [[mlops-overview|Backend Engineering & Inference Serving]]
> **Tài liệu gốc liên quan**:
> - [Session 3_ Serving Models as a Live API.pdf](../../resources/ops/Session%203_%20Serving%20Models%20as%20a%20Live%20API.pdf) (Trang 1-29)
> - [AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf](../../resources/ops/AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf) (Trang 45-60)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 103-105)

---

## 1. Tóm tắt (Executive Summary)
**Triển khai Mô hình thành Dịch vụ API (Model Serving)** là bước chuyển hóa mô hình học máy từ các tệp nhị phân tĩnh (Artifacts) thành một dịch vụ mạng (Web Service) hoạt động bền bỉ, có khả năng tiếp nhận yêu cầu dự đoán và trả về kết quả qua các giao thức chuẩn (**HTTP REST**, **gRPC**) với độ trễ thấp và độ tin cậy cao. Đối với các tác vụ thông thường, **FastAPI** kết hợp máy chủ bất đồng bộ **Uvicorn** là tiêu chuẩn công nghiệp hiện đại nhờ hiệu năng cao và tự động kiểm thực dữ liệu qua Pydantic. Đối với các hệ thống AI quy mô lớn đòi hỏi thông lượng cao trên GPU, các máy chủ suy luận chuyên dụng như **NVIDIA Triton Inference Server** hoặc **vLLM** được sử dụng để tối ưu hóa việc xếp hàng lô động (**Dynamic Batching**) và tận dụng tối đa phần cứng.

---

## 2. Định nghĩa chính thống & Kiến trúc Máy chủ Suy luận (Inference Server Architecture)

```mermaid
flowchart TD
    Client1["Client Request 1 (HTTP)"] --> DynamicBatcher["Dynamic Batching Queue (Window: 5ms)"]
    Client2["Client Request 2 (gRPC)"] --> DynamicBatcher
    Client3["Client Request 3 (HTTP)"] --> DynamicBatcher
    
    DynamicBatcher --> BatchTensor["Fused Batched Tensor (Batch Size = 3)"]
    BatchTensor --> Triton["Model Execution Engine (TensorRT / ONNX)"]
    Triton --> MultiGPU["Multi-GPU Parallel Compute"]
    MultiGPU --> SplitResult["Split Results"]
    SplitResult --> Client1
    SplitResult --> Client2
    SplitResult --> Client3
```

### 2.1 Cơ chế Gom lô Động (Dynamic Batching)
Trong môi trường thực tế, các yêu cầu suy luận từ người dùng gửi tới máy chủ độc lập từng cái một (Batch size = 1):
- *Vấn đề*: Chạy mô hình với Batch size = 1 làm lãng phí 80-90% năng lực tính toán song song khổng lồ của GPU.
- *Giải pháp Dynamic Batching*: Máy chủ giữ một hàng đợi ngắn với cửa sổ thời gian trễ tối đa (ví dụ `max_queue_delay_microseconds = 5000` — 5 mili-giây). Toàn bộ các request gửi tới trong 5ms này được tự động ghép lại thành một Tensor Batch duy nhất để đẩy vào GPU tính toán một lần, sau đó tách kết quả trả về cho từng client riêng biệt.
- *Kết quả*: Tăng thông lượng hệ thống (Throughput - RPS) lên gấp 5-10 lần mà độ trễ chỉ tăng thêm vài mili-giây không đáng kể.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các Framework Serving

| Tiêu chí | Flask (Legacy) | FastAPI + Uvicorn (Chuẩn hiện đại) | NVIDIA Triton Inference Server |
| :--- | :--- | :--- | :--- |
| **Mô hình lập trình** | Đồng bộ (Synchronous / Blocking WSGI). | Bất đồng bộ (**Async / Await ASGI**). | Máy chủ nhị phân viết bằng C++ chuyên dụng cho GPU. |
| **Tốc độ & Thông lượng** | Thấp; dễ bị nghẽn I/O khi chịu tải. | Rất cao cho các bài toán trung bình và I/O-bound. | **Cao nhất (Tối ưu hóa cấp độ phần cứng)**. |
| **Hỗ trợ Dynamic Batching** | Không có (phải tự code hàng đợi). | Phải tự xây dựng qua Redis/Celery. | **Tích hợp sẵn gốc (Native feature)**. |
| **Giao thức mạng** | Chỉ hỗ trợ HTTP/1.1 REST. | HTTP/1.1, WebSockets, Server-Sent Events (SSE). | **Hỗ trợ song song cả HTTP REST và gRPC**. |
| **Đa ngôn ngữ & Đa framework** | Chỉ chạy Python. | Chỉ chạy Python. | Chạy song song PyTorch, TensorFlow, TensorRT, ONNX, vLLM trên cùng 1 server. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Phân biệt CPU-Bound vs I/O-Bound trong FastAPI AI Server
Một sai lầm kinh điển của kỹ sư Python khi viết API cho AI:
- Thao tác mạng/database (đọc file ảnh từ S3, truy vấn Vector DB) là **I/O-Bound**: Viết hàm bất đồng bộ `async def` để luồng event loop không bị khóa.
- Thao tác tính toán mô hình (`model.predict(tensor)`) là **CPU/GPU-Bound**:
  - *Cảnh báo nguy hiểm*: Nếu viết `async def predict(...)` rồi gọi trực tiếp `model(x)` bên trong, luồng Event Loop của FastAPI sẽ bị block đứng hình hoàn toàn trong suốt thời gian GPU tính toán! Toàn bộ các request khác gửi tới server sẽ bị đóng băng.
  - *Giải pháp*: Với tác vụ nặng, định nghĩa hàm đồng bộ `def predict(...)` thông thường (FastAPI sẽ tự động đẩy hàm này ra một thread pool riêng biệt `threadpool`), hoặc sử dụng tiến trình nền phân tán (Celery / RabbitMQ).

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao trong các hệ thống suy luận thời gian thực (như giao dịch tài chính hay xe tự hành), giao thức gRPC lại được ưu tiên vượt trội so với HTTP REST JSON?*
  - **A**:
    1. **Định dạng nhị phân siêu nhẹ (Protocol Buffers)**: gRPC tuần tự hóa dữ liệu tensor thành nhị phân thay vì chuỗi văn bản JSON, tiết kiệm băng thông và giảm 70% thời gian đóng gói/giải mã (Serialization overhead).
    2. **HTTP/2 Multiplexing**: Cho phép truyền nhiều luồng dữ liệu song song trên cùng một kết nối TCP duy nhất, loại bỏ việc bắt tay thiết lập kết nối (Head-of-Line blocking) của HTTP/1.1.
    3. **Hỗ trợ Streaming hai chiều (Bidirectional Streaming)**: Rất phù hợp cho các bài toán truyền dữ liệu liên tục như video stream hoặc audio chunking thời gian thực.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[mlops-lifecycle]] — Giai đoạn biến đổi từ kịch bản sang dịch vụ API.
- [[inference-optimization-tensorrt]] — Nhân tính toán phía sau các Inference Server hiệu năng cao.
- [[containerization-kubernetes-ml]] — Đóng gói API server vào Docker và scale trên Kubernetes.
- [[continuous-integration-cd-ml]] — Chiến lược triển khai Blue-Green và Canary cho API.
""",

    "containerization-kubernetes-ml.md": r"""# Đóng Gói Container và Điều Phối Kubernetes (Containerization & Kubernetes for ML)

> **Khái niệm chính thống**: *Session 4: Docker Theory - Full Class Structure*; *AIO2025 Series: Kubernetes, Kubeflow, Spark Streaming và Kafka*; Cloud Native Computing Foundation (CNCF).
> **Miền kiến thức**: [[mlops-overview|Cloud Infrastructure & Container Orchestration]]
> **Tài liệu gốc liên quan**:
> - [Session 4_ Docker Theory - Full Class Structure.pdf](../../resources/ops/Session%204_%20Docker%20Theory%20-%20Full%20Class%20Structure.pdf) (Trang 1-25)
> - [AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf](../../resources/ops/AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf) (Trang 1-35)
> - [Sesion 5 - Setup.pdf](../../resources/ops/Sesion%205%20-%20Setup.pdf) (Trang 1-3)

---

## 1. Tóm tắt (Executive Summary)
**Đóng gói Container và Điều phối (Containerization & Orchestration)** là công nghệ nền tảng loại bỏ vĩnh viễn lời than phiền kinh điển: *"Mô hình chạy hoàn hảo trên máy em nhưng không chạy được trên server"*. Bằng cách sử dụng **Docker**, toàn bộ mã nguồn, thư viện phụ thuộc, phiên bản CUDA và tệp cấu hình được đóng gói thành các hình ảnh bất biến (**Immutable Container Images**). Để vận hành hàng trăm container mô hình trên cụm máy chủ phân tán có gắn GPU, **Kubernetes (K8s)** đóng vai trò là hệ điều hành đám mây tự động hóa việc lập lịch tài nguyên, tự phục hồi lỗi (**Self-healing**), và mở rộng quy mô tự động (**Horizontal Pod Autoscaling - HPA**).

---

## 2. Định nghĩa chính thống & Kiến trúc Docker & Kubernetes

```mermaid
flowchart TD
    subgraph Multi-Stage Dockerfile
        Stage1["Builder Stage (Compile C++, Install Build Tools)"] --> Copy["Copy only built wheels & minimal runtime"]
        Copy --> Stage2["Final Slim Stage (Production Minimal Image < 500MB)"]
    end
    
    Stage2 --> Push["Push to Container Registry (ECR / DockerHub)"]
    Push --> K8sMaster["Kubernetes Control Plane (API Server & Scheduler)"]
    
    subgraph K8s Worker Nodes with GPUs
        K8sMaster --> Node1["Node 1 (NVIDIA GPU A100)"]
        K8sMaster --> Node2["Node 2 (NVIDIA GPU A100)"]
        Node1 --> Pod1["Pod: Model Serving (Triton / FastAPI)"]
        Node1 --> Pod2["Pod: Model Serving"]
        Node2 --> Pod3["Pod: Model Serving"]
    end
    
    Traffic["Incoming Traffic Spike"] --> HPA["K8s HPA (GPU Metric Trigger)"]
    HPA --> Pod3
```

### 2.1 Kỹ thuật Multi-Stage Build trong Docker cho AI
Hình ảnh Docker cho Deep Learning thường bị phình to khủng khiếp (10GB - 20GB) do chứa trình biên dịch GCC, CUDA toolkit đầy đủ và rác cache.
Kỹ thuật **Multi-stage Build** chia Dockerfile thành 2 giai đoạn:
1. **Builder Stage**: Dùng image đầy đủ (`devel`) để cài đặt thư viện và biên dịch.
2. **Final Stage**: Chỉ dùng image rút gọn (`runtime-slim`), copy các thư viện đã biên dịch sang và loại bỏ toàn bộ công cụ dev. Kích thước image giảm từ 15GB xuống dưới 1.5GB, giúp tăng tốc độ tải và triển khai Pod trên Kubernetes gấp 10 lần.

### 2.2 Quản lý Tài nguyên GPU trong Kubernetes
Kubernetes quản lý phần cứng GPU thông qua plugin **NVIDIA GPU Operator**:
Kỹ sư khai báo tài nguyên trong tệp cấu hình Pod manifest (`deployment.yaml`):
```yaml
resources:
  limits:
    nvidia.com/gpu: 1 # Yêu cầu đúng 1 GPU vật lý
    memory: "16Gi"
    cpu: "4"
  requests:
    memory: "8Gi"
    cpu: "2"
```

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Thành phần | Máy Ảo truyền thống (Virtual Machines) | Docker Container | Đánh giá Kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Cơ chế cô lập** | Ảo hóa toàn bộ phần cứng (Hardware-level Virtualization); mỗi VM chạy một hệ điều hành khách (Guest OS) riêng. | Cô lập ở cấp độ hệ điều hành qua **Linux cgroups** và **namespaces**; chia sẻ chung nhân Linux Kernel với máy chủ vật lý. | Container khởi động trong vài giây (so với vài phút của VM) và tiêu hao tài nguyên CPU/RAM tối thiểu. |
| **Tương tác Driver GPU** | Đòi hỏi cấu hình GPU Passthrough phức tạp. | Dùng chung **NVIDIA Container Toolkit (nvidia-docker)**; ứng dụng trong container gọi trực tiếp tới driver GPU của máy chủ vật lý. | Hiệu năng tính toán đạt 99.5% tương đương chạy trực tiếp trên bare-metal. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Các thực hành tốt nhất (Best Practices) cho Docker AI
1. **Tuyệt đối không chạy container dưới quyền `root`**: Luôn tạo một user không có quyền quản trị:
   `RUN useradd -m appuser && USER appuser` để phòng chống tấn công chiếm quyền máy chủ (Container Escape).
2. **Sử dụng tệp `.dockerignore`**: Loại bỏ thư mục `.git`, `.venv`, `__pycache__` và các tệp dữ liệu huấn luyện nặng để tránh làm nặng Docker build context.
3. **Cài đặt Liveness và Readiness Probes trong Kubernetes**:
   - `readinessProbe`: Đảm bảo K8s không chuyển traffic vào Pod chừng nào mô hình chưa nạp xong toàn bộ trọng số vào VRAM GPU (tránh lỗi 502/503 khi vừa khởi động).
   - `livenessProbe`: Tự động khởi động lại container nếu tiến trình bị treo (`Deadlock`).

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Làm thế nào Kubernetes có thể tự động mở rộng (Autoscale) số lượng Pod mô hình dựa trên mức độ sử dụng GPU thay vì chỉ CPU thông thường?*
  - **A**: Theo mặc định, bộ điều phối Kubernetes Horizontal Pod Autoscaler (HPA) chỉ đọc được số liệu CPU và RAM từ metrics-server. Để scale theo GPU:
    1. Cài đặt **NVIDIA DCGM Exporter** (Data Center GPU Manager) trên cụm để thu thập số liệu phần cứng GPU (GPU Utilization %, VRAM Usage).
    2. Đẩy các số liệu này vào **Prometheus**.
    3. Cài đặt **Prometheus Adapter** để chuyển đổi metric này thành **Custom Metrics API** trong Kubernetes.
    4. Cấu hình HPA theo dõi custom metric: `container_gpu_utilization > 75%` để tự động tạo thêm Pod mới khi hệ thống chịu tải nặng.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[mlops-lifecycle]] — Môi trường đóng gói phần mềm trong chu trình MLOps.
- [[model-serving-api]] — Ứng dụng được chứa đựng bên trong các container.
- [[continuous-integration-cd-ml]] — CI/CD tự động xây dựng Docker image và deploy lên cụm K8s.
- [[data-drift-model-monitoring]] — Giám sát hạ tầng container và Pods qua Prometheus.
""",

    "continuous-integration-cd-ml.md": r"""# Tích Hợp và Triển Khai Liên Tục Cho Học Máy (CI/CD/CT for Machine Learning)

> **Khái niệm chính thống**: *AIO2025 Series: Tutorial CI/CD với GitHub Actions, Jenkins và GitLab CI*; *Session 6: CICD_1*; Google Cloud Architecture Center *"MLOps: Continuous delivery and automation pipelines in machine learning"*.
> **Miền kiến thức**: [[mlops-overview|DevOps for AI & Automated Pipelines]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_MLOps_CICD.pdf](../../resources/ops/AIO2025_MLOps_CICD.pdf) (Trang 1-40)
> - [Session 6_CICD_1.pdf](../../resources/ops/Session%206_CICD_1.pdf) (Trang 1-31)
> - [AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf](../../resources/ops/AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf) (Trang 35-50)

---

## 1. Tóm tắt (Executive Summary)
**Tích hợp và Triển khai Liên tục cho Học máy (CI/CD/CT for ML)** là sự mở rộng toàn diện của các nguyên lý DevOps truyền thống sang lĩnh vực trí tuệ nhân tạo. Trong khi phần mềm truyền thống chỉ kiểm soát một chiều là **Mã nguồn (Code)**, hệ thống Machine Learning là sự kết hợp hữu cơ của 3 thành phần động: **Mã nguồn (Code)**, **Dữ liệu (Data)**, và **Mô hình (Model)**. Do đó, quy trình CI/CD trong MLOps không chỉ kiểm thử cú pháp code mà còn bao gồm kiểm thử chất lượng dữ liệu (**Data Testing**), kiểm định độ chính xác mô hình (**Model Quality Gate**), triển khai an toàn không gián đoạn (**Canary / Blue-Green Deployments**) và vòng lặp tự động huấn luyện lại (**Continuous Training - CT**).

---

## 2. Định nghĩa chính thống & Vòng lặp Tam hợp CI/CD/CT

```mermaid
flowchart TD
    GitPush["Git Commit / Data Change"] --> CI["1. Continuous Integration (CI)"]
    
    subgraph CI Stage
        CI --> Lint["Linting & Security (Ruff, Bandit)"]
        Lint --> DataTest["Data Validation (Great Expectations)"]
        DataTest --> Unit["Unit Tests (Pytest)"]
    end
    
    Unit --> CT["2. Continuous Training (CT)"]
    
    subgraph CT Stage
        CT --> Train["Train Model on GPU Cluster"]
        Train --> Eval["Evaluate on Hold-out Benchmark"]
        Eval --> QualityGate{"Pass Quality Gate? (Accuracy > Baseline)"}
    end
    
    QualityGate -->|"No: Alert Slack"| Fail["Block Deployment"]
    QualityGate -->|"Yes"| CD["3. Continuous Delivery (CD)"]
    
    subgraph CD Stage
        CD --> BuildDocker["Build & Push Docker Image"]
        BuildDocker --> Strategy{Deployment Strategy}
        Strategy --> Canary["Canary Deployment (10% Traffic)"]
        Strategy --> BlueGreen["Blue-Green Deployment"]
    end
```

### 2.1 Ba thành phần cốt lõi của CI/CD/CT
1. **Continuous Integration (CI)**:
   - Tự động chạy khi kỹ sư tạo Pull Request: Kiểm tra format code (Flake8, Black, Ruff), kiểm tra bảo mật (Bandit), chạy Unit Tests cho các hàm xử lý dữ liệu và kiểm tra cấu trúc schema dữ liệu.
2. **Continuous Training (CT - Điểm đặc thù của ML)**:
   - Tự động kích hoạt pipeline huấn luyện lại trên cụm GPU khi có luồng dữ liệu mới được nạp vào kho hoặc khi hệ thống phát hiện Concept Drift.
   - **Quality Gate Check**: So sánh mô hình mới (Challenger) với mô hình đang chạy thực tế (Champion). Chỉ thăng hạng khi mô hình mới vượt trội hơn trên tập benchmark chuẩn.
3. **Continuous Deployment (CD)**:
   - Tự động đóng gói mô hình vào Docker container và cập nhật cấu hình triển khai Kubernetes qua luồng GitOps (ArgoCD).

---

## 3. So sánh & Mâu thuẫn / Sắc thái: Các Chiến Lược Triển Khai (Deployment Strategies)

| Chiến lược | Cơ chế điều phối giao thông | Mức độ rủi ro gián đoạn | Chi phí hạ tầng |
| :--- | :--- | :--- | :--- |
| **Recreate / Big Bang** | Tắt toàn bộ phiên bản cũ (v1) rồi mới bật phiên bản mới (v2). | Rất cao; hệ thống bị sập dịch vụ (Downtime) trong thời gian container v2 khởi động. | Thấp nhất (không tốn thêm server). |
| **Blue-Green Deployment** | Duy trì 2 môi trường song song giống hệt nhau: Môi trường Blue (v1 đang chạy) và Green (v2 mới deploy). Sau khi kiểm thử Green ổn định, bộ cân bằng tải Router chuyển 100% traffic từ Blue sang Green tức thì. | Rất thấp; nếu có lỗi xảy ra, chỉ cần gạt router quay lại Blue trong 1 giây (**Instant Rollback**). | Gấp đôi chi phí server/GPU trong giai đoạn chuyển giao. |
| **Canary Deployment** | Điều hướng một tỷ lệ nhỏ traffic thực tế (e.g., 5% - 10%) sang phiên bản mới v2, trong khi 90% người dùng vẫn dùng v1. Sau vài giờ nếu không có lỗi ngoại lệ hoặc drift, tăng dần lên 25%, 50% và 100%. | **An toàn nhất trong sản xuất**. Nếu model mới có lỗi tiềm ẩn, chỉ có 5% người dùng bị ảnh hưởng. | Trung bình; đòi hỏi bộ định tuyến thông minh (như Istio / NGINX Ingress). |
| **Shadow / Dark Launching** | Toàn bộ request được nhân bản (Forked traffic): gửi đồng thời tới cả v1 và v2, nhưng **chỉ trả kết quả của v1 cho người dùng**. Kết quả của v2 được ghi vào log để phân tích hiệu năng và độ trễ ngầm. | Không có rủi ro nào cho trải nghiệm người dùng cuối. | Tốn tài nguyên tính toán gấp đôi cho mọi request. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Xây dựng GitHub Actions Pipeline mẫu cho MLOps
Tệp `.github/workflows/mlops-pipeline.yml`:
```yaml
name: MLOps Production Pipeline
on: [push, pull_request]

jobs:
  code-and-data-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install uv
          uv pip install -r requirements-test.txt
      - name: Run Linters & Security
        run: |
          ruff check src/
          bandit -r src/
      - name: Run Unit Tests & Data Integrity
        run: |
          pytest tests/ --cov=src/
```

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Sự khác biệt cốt lõi giữa Kiểm thử Phần mềm truyền thống (Traditional Software Testing) và Kiểm thử Hệ thống Học máy (ML System Testing) là gì?*
  - **A**:
    - Phần mềm truyền thống có tính tất định (Deterministic): Với cùng input $x$, logic code cố định sẽ luôn cho ra output $y$ chính xác. Kiểm thử tập trung vào tính đúng đắn của logic (Unit test).
    - Hệ thống ML mang tính xác suất (Probabilistic): Dù mã nguồn không có bất kỳ lỗi cú pháp nào, mô hình vẫn có thể thất bại thảm hại nếu dữ liệu huấn luyện bị trôi dạt (Data Drift), bị mất cân bằng nhãn hoặc bị thiên kiến. Kiểm thử ML bắt buộc phải có thêm 3 chiều: **Data Testing** (kiểm tra phân phối, giá trị null, định dạng), **Model Behavioral Testing** (kiểm tra tính bất biến - Invariance test, kiểm tra biên độ nhạy cảm - Directional Expectation test), và **Fairness/Bias Testing**.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[mlops-lifecycle]] — Nền tảng quy trình mà CI/CD/CT tự động hóa.
- [[experiment-tracking-model-registry]] — Điểm kích hoạt (Trigger) cho luồng CD khi model đổi trạng thái.
- [[containerization-kubernetes-ml]] — Môi trường đích tiếp nhận các bản phát hành tự động.
- [[data-drift-model-monitoring]] — Cung cấp tín hiệu kích hoạt ngược cho vòng lặp CT.
""",

    "data-drift-model-monitoring.md": r"""# Giám Sát Dữ Liệu và Trôi Dạt Mô Hình (Data Drift & Model Monitoring)

> **Khái niệm chính thống**: *Session 9: Model Monitoring*; Google Cloud Architecture Center *"Monitoring Machine Learning Systems"*; *847762397...jpg* ("2. Dữ liệu bẩn xử lý sao?"); *847999051...jpg* ("4. Nếu model sai thì sao?").
> **Miền kiến thức**: [[mlops-overview|Production Observability & Reliability Engineering]]
> **Tài liệu gốc liên quan**:
> - [Session 9_ Model Monitoring.pdf](../../resources/ops/Session%209_%20Model%20Monitoring.pdf) (Trang 1-39)
> - [847762397_122320901834195094_274771350129520392_n.jpg](../../resources/images/847762397_122320901834195094_274771350129520392_n.jpg) (Infographic 2: Phân loại dữ liệu bẩn)
> - [847999051_122320901954195094_4534131503073995411_n.jpg](../../resources/images/847999051_122320901954195094_4534131503073995411_n.jpg) (Infographic 4: Xử lý model sai)

---

## 1. Tóm tắt (Executive Summary)
**Giám sát Mô hình và Phát hiện Trôi dạt (Model Monitoring & Drift Detection)** là phòng tuyến phòng thủ cuối cùng bảo vệ hệ thống AI trong môi trường sản xuất. Ngay sau khi được đưa vào phục vụ thực tế, hiệu năng của mọi mô hình học máy đều có xu hướng suy thoái âm thầm theo thời gian (**Silent Model Degradation**) do thế giới thực luôn thay đổi không ngừng. Khác với lỗi sập phần mềm truyền thống (Crash / HTTP 500), mô hình bị drift vẫn trả về mã 200 OK bình thường nhưng kết quả dự đoán hoàn toàn sai lệch. Hệ thống giám sát MLOps theo dõi liên tục 4 tầng: **Hạ tầng (System Health)**, **Chất lượng Dữ liệu (Data Quality)**, **Trôi dạt Dữ liệu (Data Drift / Covariate Shift)**, và **Trôi dạt Khái niệm (Concept Drift)**.

---

## 2. Định nghĩa chính thống & Phân loại Các Dạng Trôi Dạt (Taxonomy of Drift)

Theo lý thuyết xác suất Bayes, mối quan hệ giữa biến đầu vào $X$ và nhãn mục tiêu $Y$ được mô tả qua phân phối đồng thời:
$$P(X, Y) = P(X) \cdot P(Y \mid X) = P(Y) \cdot P(X \mid Y)$$

```mermaid
flowchart TD
    Drift["Types of Production Drift"] --> DataDrift["1. Data Drift / Covariate Shift\nP(X) changes, P(Y|X) stays same"]
    Drift --> ConceptDrift["2. Concept Drift\nP(Y|X) changes, P(X) may stay same"]
    Drift --> PriorDrift["3. Prior Probability Shift\nP(Y) changes (e.g. Fraud rate spikes)"]
    
    DataDrift --> Detect1["Statistical Tests: KS-Test, PSI, Wasserstein Distance"]
    ConceptDrift --> Detect2["Performance Decay: Precision / Recall drops (Requires Ground Truth)"]
    
    Detect1 --> Trigger["Trigger Automated Retraining (CT Pipeline)"]
    Detect2 --> Trigger
```

### 2.1 Chi tiết 3 dạng trôi dạt
1. **Data Drift (Covariate Shift - Trôi dạt biến đầu vào)**:
   - Phân phối của dữ liệu đầu vào $P(X)$ thay đổi, nhưng quan hệ ánh xạ giữa đầu vào và đầu ra $P(Y \mid X)$ không đổi.
   - *Ví dụ*: Ứng dụng vay tiền mở rộng sang phục vụ nhóm khách hàng sinh viên trẻ tuổi (phân phối thu nhập và độ tuổi $P(X)$ dịch chuyển rõ rệt so với tập train ban đầu gồm người đi làm).
2. **Concept Drift (Trôi dạt Khái niệm)**:
   - Bản chất ý nghĩa mối quan hệ nghiệp vụ $P(Y \mid X)$ thay đổi, ngay cả khi phân phối đầu vào $P(X)$ trông có vẻ như cũ.
   - *Ví dụ*: Hành vi mua sắm trước và trong đại dịch COVID-19. Cùng một người dùng $X$, nhưng hành vi mua hàng tiêu dùng và khẩu trang $Y$ thay đổi hoàn toàn.
3. **Prior Probability Shift (Trôi dạt Nhãn mục tiêu)**:
   - Tỷ lệ phân phối $P(Y)$ thay đổi (ví dụ: tỷ lệ gian lận trong mùa mua sắm Black Friday tăng vọt gấp 10 lần ngày thường).

---

## 3. Các Phương Pháp Thống Kê Định Lượng Trôi Dạt (Statistical Testing)

### 3.1 Kolmogorov-Smirnov Test (KS-Test)
Dành cho các biến số liên tục (Numerical features):
- So sánh hai hàm phân phối tích lũy thực nghiệm (ECDF): $F_{\text{baseline}}(x)$ và $F_{\text{production}}(x)$.
- Thống kê kiểm định $D$:
  $$D = \sup_x |F_{\text{baseline}}(x) - F_{\text{production}}(x)|$$
- Nếu p-value $< 0.05$, bác bỏ giả thuyết $H_0$, kết luận thuộc tính đã bị trôi dạt có ý nghĩa thống kê.

### 3.2 Population Stability Index (PSI - Tiêu chuẩn ngành Ngân hàng & Tài chính)
Dành cho việc so sánh phân phối xác suất giữa tập tham chiếu (Baseline/Expected) và tập thực tế (Actual):
Chia dữ liệu thành $K$ giỏ (bins):
$$\text{PSI} = \sum_{i=1}^K \left( \text{Actual}_i - \text{Expected}_i \right) \times \ln\left( \frac{\text{Actual}_i}{\text{Expected}_i} \right)$$
- **Thang đánh giá chuẩn mực của PSI**:
  - $\text{PSI} < 0.1$: Phân phối ổn định, không có thay đổi đáng kể.
  - $0.1 \le \text{PSI} < 0.25$: Bắt đầu có sự dịch chuyển; cần đưa vào danh sách theo dõi cảnh báo.
  - $\text{PSI} \ge 0.25$: **Trôi dạt nghiêm trọng (Significant Drift)**; bắt buộc phải kích hoạt pipeline huấn luyện lại mô hình!

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Thách thức "Độ trễ Nhãn Thực tế" (Ground Truth Latency)
- Trong hầu hết các bài toán kinh doanh (chấm điểm tín dụng, dự đoán khách hàng rời bỏ - Churn), nhãn thực tế $Y$ phải mất vài tuần hoặc vài tháng sau mới xuất hiện (khách hàng có trả nợ hay không sau 90 ngày).
- **Hệ quả sống còn**: Kỹ sư **không thể đợi có nhãn $Y$ mới đo Accuracy hay F1 score để biết model bị hỏng hay chưa**!
- **Giải pháp**: Bắt buộc phải dựa vào **Data Drift Metrics (PSI, KS-Test)** trên dữ liệu đầu vào $X$ và phân phối của giá trị dự đoán $\hat{Y}$ (Prediction Drift) như một tín hiệu cảnh báo sớm (Early-warning proxy) theo thời gian thực.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Khi hệ thống cảnh báo PSI của một thuộc tính quan trọng nhảy lên 0.35 (Drift nghiêm trọng), bạn sẽ xử lý thế nào? Có nên tự động kích hoạt train lại model ngay lập tức không?*
  - **A**: **Tuyệt đối không huấn luyện lại một cách mù quáng ngay lập tức**! Quy trình chuẩn của Senior AI Engineer gồm 3 bước:
    1. **Kiểm tra tính toàn vẹn dữ liệu (Data Quality Check)**: Kiểm tra xem có lỗi pipeline kỹ thuật không (ví dụ: API upstream bị lỗi đổi đơn vị từ mét sang milimet, hoặc có một lượng lớn giá trị NULL bất thường). Nếu train lại trên dữ liệu bị lỗi kỹ thuật, mô hình sẽ bị phá hủy.
    2. **Phân tích bối cảnh kinh doanh**: Nếu drift phản ánh sự kiện thực tế ngắn hạn (ví dụ: đợt khuyến mãi bùng nổ 3 ngày Black Friday), dữ liệu này có thể là ngoại lai tạm thời, không nên làm méo mô hình dài hạn.
    3. **Huấn luyện lại an toàn (Safe Retraining)**: Sau khi xác nhận dữ liệu mới phản ánh xu thế chuyển dịch thực tế bền vững, kích hoạt pipeline CT, huấn luyện mô hình Challenger và tiến hành kiểm định chất lượng (Quality Gate) trước khi thăng hạng.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[mlops-lifecycle]] — Tầng giám sát vận hành trong vòng đời MLOps.
- [[continuous-integration-cd-ml]] — Phát tín hiệu kích hoạt ngược cho vòng lặp Continuous Training (CT).
- [[model-selection-evaluation]] — Phân tích lỗi theo lát cắt (Slicing Analysis) và phân loại dữ liệu bẩn.
- [[experiment-tracking-model-registry]] — Đối chiếu phiên bản mô hình cần cập nhật.
"""
}

def generate():
    for filename, content in ENTITIES.items():
        filepath = WIKI_DIR / filename
        filepath.write_text(content.strip(), encoding="utf-8")
        print(f"Created: {filepath.name}")

if __name__ == "__main__":
    generate()
