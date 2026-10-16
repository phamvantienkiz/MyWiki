# Vòng Đời MLOps và Chuyển Đổi Kịch Bản Sản Xuất (MLOps Lifecycle & Production Engineering)

> **Khái niệm chính thống**: Google Cloud MLOps Maturity Framework; *Session 1: From Notebook to Production Script*; *AIO2025 Series: MLOps Tutorial*.
> **Miền kiến thức**: [[index|Machine Learning Operations & Production Systems]]
> **Tài liệu gốc liên quan**:
> - [Sesion 1_ From Notebook to Production Script.pdf](../resources/ops/Sesion%201_%20From%20Notebook%20to%20Production%20Script.pdf) (Trang 1-23)
> - [AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf](../resources/ops/AIO2025_MLOps-Tutorial_K8s_Kubeflow_Spark_Streaming_Kafka.pdf) (Trang 1-71)
> - [Session 5_ First Cloud Deployment.pdf](../resources/ops/Session%205_%20First%20Cloud%20Deployment.pdf) (Trang 1-28)

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

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & `wiki-links`)
- [[experiment-tracking-model-registry]] — Hệ thống ghi nhận dấu vết thử nghiệm trong vòng đời MLOps.
- [[model-serving-api]] — Tầng triển khai mô hình thành dịch vụ sau khi hoàn tất pipeline.
- [[containerization-kubernetes-ml]] — Hạ tầng đóng gói và điều phối container cho MLOps.
- [[continuous-integration-cd-ml]] — Tự động hóa kiểm thử và phát hành mô hình.
- [[data-drift-model-monitoring]] — Giám sát chất lượng mô hình khi chạy thực tế.