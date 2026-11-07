# Báo Cáo Triển Khai Sơ Đồ Kiến Trúc Đóng Gói Theo Tiêu Chuẩn `diagram-design`

## 1. Tổng Quan & Yêu Cầu Cốt Lõi
- **Mục tiêu của người dùng:** Áp dụng skill `diagram-design` cho các phần sơ đồ kiến trúc trong tài liệu `interview/index.html`. Giữ phong cách đơn giản, chủ yếu là **đóng gói các thành phần lại thành các khung trực quan (Packaged Container Frames & Compartments)** với viền, nhãn nhận diện phân vùng, thay vì trình bày dưới dạng văn bản markdown / ASCII art rời rạc.
- **Tiêu chuẩn kỹ thuật tuân thủ (`diagram-design`):**
  1. **Khung đóng gói (Container & Zone Frames):** Mọi kiến trúc được bao bọc trong các vùng chứa viền mỏng 1px - 1.2px (`stroke="var(--border)"`), góc bo tròn chuẩn `rx="8"`, nền rửa nhẹ 2% (`fill="rgba(45,49,66,0.02)"`), có thẻ tiêu đề phân vùng (Eyebrow Tag on Mask).
  2. **Các khối thành phần (Component Nodes):** Bo góc chuẩn `rx="6"`, không dùng drop-shadow, phân cấp kiểu chữ rõ ràng (Tiêu đề in đậm, mô tả kỹ thuật chữ nhỏ / monospace).
  3. **Kết nối trực giao (Orthogonal Connectors):** 100% đường nối dùng đường thẳng hoặc góc gập vuông bo tròn $r=8\text{px}$, mũi tên có marker chuẩn xác, nhãn kết nối nằm trên mask chống đè nét.
  4. **Điểm nhấn biên tập (Editorial Focal Accent):** Giới hạn 1–2 màu điểm nhấn chủ đạo (`var(--data-emerald)`, `var(--data-blue)`, `var(--data-purple)`), giữ các khối còn lại ở tông màu trung tính sang trọng.
  5. **Chống tràn màn hình & Đáp ứng tốt (Responsive SVG):** Mọi SVG được bọc trong container `<div style="overflow-x: auto; width: 100%;">` với `min-width` khớp kích thước `viewBox`.

---

## 2. Chi Tiết 10 Sơ Đồ Kiến Trúc Được Nâng Cấp Hoàn Toàn

### 1. Khối Phần Dư ResNet (Residual Block & Gradient Highway) — [Mục 3.7](file:///E:/MyProject/MyWiki/interview/index.html#L3960)
- **Đóng gói phân vùng:**
  - Khung bao ngoài: `RESIDUAL BLOCK: y = F(x) + x` viền mỏng 1.2px bo góc `rx="8"`.
  - Phân vùng con bên trong: `NON-LINEAR MAPPING F(x)` bao bọc chuỗi mắt xích `Weight (Conv 3×3 + BN)` $\to$ `ReLU` $\to$ `Weight (Conv 3×3 + BN)`.
  - Đường cao tốc phía trên: `IDENTITY SHORTCUT HIGHWAY (+x)` chạy vòng qua toàn bộ nhánh phi tuyến, đi thẳng vào nút cộng tròn `⊕ Element-wise Add` với màu xanh ngọc bích `var(--data-emerald)`.

### 2. Kiến Trúc Chữ U Của U-Net (Phân Đoạn Ảnh Ngữ Nghĩa) — [Mục 3.7](file:///E:/MyProject/MyWiki/interview/index.html#L4040)
- **Đóng gói phân vùng:**
  - Khung trái: `ENCODER (CONTRACTING PATH)` gồm 3 tầng Conv $3\times3$ và các mũi tên MaxPool $2\times2$ hạ phân giải không gian.
  - Khung trung tâm đáy: `LATENT BOTTLENECK (ĐÁY CHỮ U)` nén thông tin ngữ nghĩa trừu tượng 512-d / 1024-d.
  - Khung phải: `DECODER (EXPANSIVE PATH)` gồm 3 tầng Transposed Conv tái tạo độ phân giải không gian về ảnh gốc.
  - Các đường nối ngang `torch.cat`: Kênh nối ngang Skip-Connection mang đặc trưng độ phân giải cao từ Encoder dán thẳng vào Decoder với nhãn phân định rõ ràng.

### 3. Tích Chập Phân Tách MobileNet (Depthwise Separable Conv) — [Mục 3.9](file:///E:/MyProject/MyWiki/interview/index.html#L4360)
- **Đóng gói phân vùng:**
  - Khung A: `STANDARD CONVOLUTION (NGUYÊN KHỐI 3D CỰC NẶNG)` biểu diễn phép quét 3D đồng thời $K \times K \times C_{in} \times C_{out}$.
  - Khung B: `MOBILENET DEPTHWISE SEPARABLE (PHÂN TÁCH 2 PHÂN VÙNG)` chia thành:
    - *Sub-Frame 1:* `STAGE 1: DEPTHWISE` (Bộ lọc $K \times K \times 1$ cho từng kênh độc lập).
    - *Sub-Frame 2:* `STAGE 2: POINTWISE` (Bộ lọc $1 \times 1 \times C_{in}$ tổ hợp liên kênh).
    - Huy hiệu nổi bật: Tiết kiệm gần 9 lần FLOPs ($\approx 1/9$).

### 4. Vision Transformer (ViT) vs Swin Transformer — [Mục 3.9](file:///E:/MyProject/MyWiki/interview/index.html#L4420)
- **Đóng gói phân vùng:**
  - Khung A: `VISION TRANSFORMER (ViT)` trực quan hóa lưới mảnh vá ảnh 16×16 $\to$ Linear Projection $\to$ Global Multi-Head Attention với độ phức tạp bậc hai $O(N^2)$.
  - Khung B: `SWIN TRANSFORMER (SHIFTED WINDOWS)` trực quan hóa cửa sổ cố định W-MSA $\to$ cửa sổ dịch chuyển SW-MSA đạt độ phức tạp tuyến tính $O(M^2 \cdot HW)$.

### 5. Đại Pipeline 1: Giám Sát Giao Thông & Phạt Nguội — [Mục 1.2](file:///E:/MyProject/MyWiki/interview/index.html#L356)
- **Thay thế hoàn toàn khối text/markdown `<pre>`:**
  - Khung 1: `PHÂN VÙNG 1: THU NẠP & GIẢI MÃ GPU` (Camera RTSP $\to$ NVDEC Hardware Decoder $\to$ Decimation Buffer).
  - Khung 2: `PHÂN VÙNG 2: THỊ GIÁC & PHÂN TÍCH HÀNH VI` (YOLO TensorRT $\to$ ByteTrack $\to$ Rẽ nhánh song song sang State Machine Vượt Vạch & Module ANPR).
  - Khung 3: `PHÂN VÙNG 3: BẰNG CHỨNG & SERVING` (Evidence Package Generator $\to$ Message Queue Kafka $\to$ PostgreSQL/MinIO & Dashboard IOC).

### 6. Đại Pipeline 2: Tự Động Hóa Cổng Cảng Container — [Mục 1.2](file:///E:/MyProject/MyWiki/interview/index.html#L526)
- **Thay thế hoàn toàn khối text/markdown `<pre>`:**
  - Khung 1: `PHÂN VÙNG 1: KÍCH HOẠT & ĐA CAMERA` (Laser Scanner / Vòng từ $\to$ Chụp đồng bộ 4 Camera đầu kéo, sườn, cửa sau).
  - Khung 2: `PHÂN VÙNG 2: BỘ BA THỊ GIÁC PHÂN TÍCH SONG SONG` (OCR ISO 6346 Modulo 11 + U-Net Hư hại vỏ + ANPR kép đầu kéo & rơ-moóc).
  - Khung 3: `PHÂN VÙNG 3: HỢP NHẤT & TOS CẢNG` (Transaction Aggregator $\to$ Hệ thống TOS $\to$ Mở Barie & In EIR $\le 2.5\text{s}$).

### 7. Đại Pipeline 3: Kiểm Soát Vào Ra Khuôn Mặt & Anti-Spoofing — [Mục 1.2](file:///E:/MyProject/MyWiki/interview/index.html#L670)
- **Thay thế hoàn toàn khối text/markdown `<pre>`:**
  - Khung 1: `PHÂN VÙNG 1: THU NẠP & PHÁT HIỆN` (Camera kép RGB+NIR $\to$ RetinaFace TensorRT BBox & 5 Landmarks).
  - Khung 2: `PHÂN VÙNG 2: BẢO MẬT & CĂN CHỈNH TỌA ĐỘ` (FASNet Liveness || Affine Alignment 112×112 $\to$ Cổng duyệt bảo mật).
  - Khung 3: `PHÂN VÙNG 3: ARCFACE & MỞ BARIE` (ArcFace 512-d $\to$ HNSW Milvus $\ge 0.65 \to$ Relay mở barie $\le 300\text{ms}$).

### 8. Kiến Trúc C2AE Multi-Label — [Mục 2.15](file:///E:/MyProject/MyWiki/interview/index.html#L3070)
- **Thay thế hoàn toàn khối text/markdown `<pre>`:**
  - Khung 1 (Trên): `PHÂN VÙNG 1: FEATURE EMBEDDING PATHWAY` ($X \to F_X(X) \to z_x$).
  - Khung 2 (Dưới): `PHÂN VÙNG 2: LABEL AUTOENCODER` ($Y \to F_Y \to z_y \to D_Y \to \hat{Y}$ kèm ràng buộc trực giao Gram).
  - Vùng trung tâm: Căn chỉnh chuẩn Frobenius $\|z_x - z_y\|_F^2$ và đường dẫn tắt khi suy luận thực tế (Inference Shortcut).

### 9. Kiến Trúc 9 Thành Phần Của Agent Harness — [Mục 7.4](file:///E:/MyProject/MyWiki/interview/index.html#L6179)
- **Thay thế hoàn toàn khối box ASCII `<pre>┌───`:**
  - Khung Outer: `AGENT HARNESS ENTERPRISE RUNTIME CONTAINER`.
  - Phân vùng 1: `LÕI ĐIỀU KHIỂN & BỘ NHỚ (BẮT BUỘC)` gồm While Loop và Context Management.
  - Phân vùng 2: `VÀNH ĐAI CÔNG CỤ & CÁCH LY` gồm Tool Registry, Sub-Agents, Dynamic Skills, Session Persistence.
  - Phân vùng 3: `ĐIỀU PHỐI PAYLOAD, HOOKS & CỔNG PHÂN QUYỀN` gồm Prompt Assembly, Lifecycle Hooks, Permission Gate.

### 10. Clean Architecture Củ Hành / Lục Giác — [Mục 8.2](file:///E:/MyProject/MyWiki/interview/index.html#L6460)
- **Thay thế hoàn toàn khối text markdown `<pre>`:**
  - Hệ thống 4 khung đồng tâm lồng nhau từ ngoài vào trong:
    - *Layer 4:* Frameworks & Drivers (FastAPI, TensorRT, Docker, PostgreSQL).
    - *Layer 3:* Interface Adapters (CameraRouters, ANPRController, Repositories).
    - *Layer 2:* Use Cases / Application (Nghiệp vụ ứng dụng).
    - *Core Layer 1:* Domain Entities & Invariants (Trọng tâm thuần Python không phụ thuộc thư viện ngoài).
  - Mũi tên Quy tắc phụ thuộc (Dependency Rule) hướng dứt khoát vào trọng tâm lõi.
