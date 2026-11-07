# Kế Hoạch Nâng Cấp Sơ Đồ Kiến Trúc Theo Tiêu Chuẩn `diagram-design`

## 1. Mục Tiêu
Chuyển hóa toàn bộ các sơ đồ kiến trúc trong `interview/index.html` từ dạng text/markdown/ascii `<pre>` hoặc sơ đồ rời rạc thành các sơ đồ kiến trúc đồ họa SVG chuẩn mực theo skill `diagram-design`:
- **Đóng gói phân vùng (Zone Packaging):** Sử dụng các khung container viền 1px (`rx="8"`), có dải thẻ định danh (Eyebrow Tag on Mask), gom nhóm các mắt xích theo ranh giới chức năng rõ ràng.
- **Không dùng phong cách markdown/ascii:** Thay thế toàn bộ các khối `<pre>` sơ đồ luồng thành SVG trực quan, phân tầng rõ rệt.
- **Chuẩn kết nối Orthogonal:** Không dùng đường xiên chéo bừa bãi, sử dụng góc uốn vuông bo tròn $r=8\text{px}$, mũi tên có marker chuẩn, nhãn có mask nền chống đè nét.
- **Tiêu chuẩn màu sắc biên tập (Editorial Accent):** Tối đa 1–2 điểm nhấn nổi bật (Emerald / Blue / Purple), nền và khung trung tính tinh tế.
- **Chống tràn màn hình:** Bao bọc bằng thẻ `<div style="overflow-x: auto; width: 100%;">` với `min-width` khớp `viewBox`, đảm bảo hiển thị hoàn hảo trên mọi thiết bị.

---

## 2. Danh Sách Các Sơ Đồ Kiến Trúc Cần Đóng Gói
1. **Module 1 - Đại Pipeline 1: Giám Sát Giao Thông & Phạt Nguội** (Thay thế `<pre>` dòng 358-391)
   - Khung 1: *Thu Nạp & Tiền Xử Lý (Ingestion & NVDEC GPU Demuxing)*
   - Khung 2: *Thị Giác Máy Tính Cốt Lõi (Core Vision & Perception: YOLO + Tracker)*
   - Khung 3: *Phân Tích Song Song (State Machine Vi Phạm || Module ANPR)*
   - Khung 4: *Đóng Gói Bằng Chứng & Phục Vụ (Evidence Package -> Kafka / DB / IOC)*
2. **Module 1 - Đại Pipeline 2: Tự Động Hóa Cảng Biển & Logistics Container** (Thay thế `<pre>` dòng 437-472)
   - Khung 1: *Cảm Biến & Kích Hoạt Đồng Thời 4 Camera Cảng*
   - Khung 2: *Bộ Ba Kiểm Soát Song Song (OCR ISO 6346 Modulo 11 | U-Net Hư Hại Thùng | ANPR Đầu Kéo)*
   - Khung 3: *Hợp Nhất Giao Dịch & Tích Hợp TOS Điều Khiển Barie (2.5s)*
3. **Module 1 - Đại Pipeline 3: Kiểm Soát Ra Vào Khuôn Mặt Tốc Độ Cao** (Thay thế `<pre>` dòng 509-541)
   - Khung 1: *Thu Nạp Song Quang (Dual RGB + IR Sensor) & RetinaFace (BBox + 5 Landmarks)*
   - Khung 2: *Bảo Mật & Căn Chỉnh Song Song (FASNet Liveness || Affine 112x112)*
   - Khung 3: *Nhận Diện & Điều Khiển Tức Thời (ArcFace 512-d -> HNSW Index -> Relay Mở Cửa <300ms)*
4. **Module 2 - Section 2.14: Kiến Trúc C2AE Multi-Label** (Thay thế `<pre>` dòng 2833-2837)
   - Khung 1: *Feature Encoding Pipeline ($X \to F_X \to z_x$)*
   - Khung 2: *Label AutoEncoder & Orthogonal Reconstruction ($Y \to F_Y \to z_y \to D_Y \to \hat{Y}$)*
   - Khung 3: *Shared Latent Space & Frobenius Alignment ($\|z_x - z_y\|_F^2$)*
5. **Module 3 - Section 3.7: Kiến Trúc Khối Phần Dư ResNet (Residual Block)** (Nâng cấp SVG dòng 3882-3945)
   - Đóng gói toàn bộ khối vào khung container `Residual Block [F(x) + x]`
   - Phân chia rõ phân vùng biến đổi phi tuyến $\mathcal{F}(x)$ và đường cao tốc Gradient Bypass $+1$
6. **Module 3 - Section 3.7: Kiến Trúc U-Net Phân Đoạn Ảnh Ngữ Nghĩa** (Nâng cấp SVG dòng 3950-4015)
   - Đóng gói thành 3 khung phân vùng kiến trúc: Khung Encoder (Co rút), Khung Bottleneck, Khung Decoder (Mở rộng)
   - Các kênh Skip-Connection ngang nối tầng `torch.cat` với nhãn chú thích rõ ràng
7. **Module 3 - Section 3.9: MobileNet Depthwise Separable Convolution** (Nâng cấp SVG dòng 4229-4267)
   - Đóng gói khung so sánh A: *Standard Convolutional Block*
   - Đóng gói khung so sánh B: *Depthwise Separable Block (Stage 1 Depthwise + Stage 2 Pointwise)*
8. **Module 3 - Section 3.9: ViT vs Swin Transformer** (Nâng cấp SVG dòng 4290-4334)
   - Khung A: *Vision Transformer Pipeline ($16 \times 16$ Patches $\to$ Global Attention $O(N^2)$)*
   - Khung B: *Swin Transformer Hierarchical Stage (W-MSA & Shifted Window SW-MSA $O(M^2 N)$)*
9. **Module 7 - Section 7.4: Kiến Trúc Agent Harness 9 Thành Phần** (Thay thế `<pre>` dòng 5704-5717)
   - Khung Outer: *Agent Harness Enterprise Runtime Frame*
   - Khung Phân Vùng 1: *Core Loop & Context Management (Bắt buộc)*
   - Khung Phân Vùng 2: *Tool Registry & Isolation Perimeter (Tools, Sub-agents, Skills, Session)*
   - Khung Phân Vùng 3: *Governance & Orchestration (Prompt Assembly, Hooks, Permission Gate)*
10. **Module 8 - Section 8.2: Clean Architecture Củ Hành / Lục Giác** (Thay thế `<pre>` dòng 5931-5934)
    - Hệ thống 4 khung đồng tâm / phân tầng lồng ghép: Core Entities $\to$ Use Cases $\to$ Interface Adapters $\to$ Frameworks & Drivers.
