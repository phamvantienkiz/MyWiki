# Deep Learning & Computer Vision Knowledge Integration Walkthrough

> **Tài liệu Báo Cáo Hoàn Thành (Walkthrough Report)**  
> **Dự án**: Chuẩn bị kiến thức phỏng vấn Deep Learning & Computer Vision tại ATIN  
> **File triển khai chính**: [`interview/index.html`](file:///E:/MyProject/MyWiki/interview/index.html)  
> **Tuân thủ quy chuẩn**: [`AGENTS.md`](file:///E:/MyProject/MyWiki/AGENTS.md) và Skill [`lecture-visualizer`](file:///E:/MyProject/MyWiki/.agents/skills/lecture-visualizer/SKILL.md)  
> **Thư mục lưu trữ tài liệu AI**: `docs/ai/`

---

## 1. Tổng Quan Nhiệm Vụ & Cải Tiến Trực Quan

Nhiệm vụ yêu cầu nghiên cứu và trích xuất tri thức từ toàn bộ tài nguyên tài liệu trong [`resources/deep-learning/computer-vision`](file:///E:/MyProject/MyWiki/resources/deep-learning/computer-vision) và [`resources/machine-learning`](file:///E:/MyProject/MyWiki/resources/machine-learning) để bổ sung toàn diện các chủ đề lý thuyết và giải thuật Deep Learning & Computer Vision vào cẩm nang phỏng vấn [`interview/index.html`](file:///E:/MyProject/MyWiki/interview/index.html).

### Hai Cải Tiến Trực Quan Trọng Tâm Theo Yêu Cầu Người Dùng:
1. **Loại bỏ chia 2 cột (`grid-2`) tại các khu vực chứa công thức toán**: Chuyển đổi toàn bộ các card chứa biểu thức vi phân, ma trận đạo hàm chuỗi, công thức kích thước hoặc vết dò tính số học (Arithmetic Traces) sang bố cục **1 cột toàn chiều rộng (Full-Width Stacked Cards)**. Nhờ đó, các công thức toán KaTeX và các khối code monospace không bao giờ bị tràn (overflow) hay ngắt dòng gãy khúc.
2. **Bổ sung hệ thống 10 hình vẽ minh họa SVG chuẩn mực (Vector Graphics)**: Thiết kế trực tiếp bằng inline SVG responsive, không cần animation hay script phức tạp, tương thích hoàn hảo cả 2 chế độ Light & Dark mode, giúp người học chậm hiểu ngay lập tức bản chất hình học và luồng dữ liệu.

---

## 2. Chi Tiết 10 Hình Vẽ Minh Họa SVG Đã Tích Hợp

| STT | Vị Trí Section | Tên Sơ Đồ Minh Họa (Inline SVG) | Ý Nghĩa Sư Phạm Trực Giác |
| :---: | :--- | :--- | :--- |
| 1 | [Section 2.14](file:///E:/MyProject/MyWiki/interview/index.html#L2600) | **Kiến Trúc Mạng Nơ-ron & Luồng Forward - Backward** | Trực quan hóa các tầng nơ-ron: luồng mũi tên xanh lan truyền xuôi ($\mathbf{z}=\mathbf{W}\mathbf{a}+\mathbf{b}$) và mũi tên đỏ lan truyền ngược vi phân ($\mathbf{W} \leftarrow \mathbf{W} - \eta \nabla_{\mathbf{W}}\mathcal{L}$). |
| 2 | [Section 3.3](file:///E:/MyProject/MyWiki/interview/index.html#L3240) | **Phép Tích Chập Trên Thể Tích 3D (Volume)** | Trực quan hóa tensor đầu vào RGB ($W \times H \times 3$), kernel $3 \times 3 \times 3$ trượt qua toàn bộ độ sâu để sinh ra đúng 1 giá trị vô hướng (scalar) trên Feature Map 2D. |
| 3 | [Section 3.4](file:///E:/MyProject/MyWiki/interview/index.html#L3410) | **Cơ Chế Max Pooling & Phân Phối Gauss ERF** | Ma trận $4 \times 4$ với các cửa sổ $2 \times 2$ trích chọn giá trị lớn nhất; đối chiếu hình vuông RF lý thuyết với các đường đồng mức phân phối Gauss của ERF (tâm chiếm $>90\%$ gradient). |
| 4 | [Section 3.5](file:///E:/MyProject/MyWiki/interview/index.html#L3630) | **Bộ Tứ Chuẩn Hóa Trên Tensor 4 Chiều (N, C, H, W)** | 4 khối lập phương trực quan hóa trục chuẩn hóa của: BN (trục $N, H, W$), LN (trục $C, H, W$), IN (trục $H, W$), GN (nhóm kênh $C/G, H, W$). |
| 5 | [Section 3.6](file:///E:/MyProject/MyWiki/interview/index.html#L3770) | **Cơ Chế Inverted Dropout: Training vs Inference** | Pha huấn luyện tắt ngẫu nhiên nơ-ron (dấu $\times$) và nhân bù $\frac{1}{1-p}$ vs Pha suy luận mọi nơ-ron hoạt động nguyên bản với **Zero Overhead**. |
| 6 | [Section 3.7](file:///E:/MyProject/MyWiki/interview/index.html#L3840) | **Khối Phần Dư ResNet (Residual Block) & Đường Cao Tốc (+1)** | Sơ đồ khối $y = \mathcal{F}(x) + x$ với mũi tên đường tắt (Skip connection) mang số hạng $+1$ đưa gradient chảy thẳng không bao giờ bị suy hao. |
| 7 | [Section 3.7](file:///E:/MyProject/MyWiki/interview/index.html#L3880) | **Kiến Trúc Chữ U Của U-Net & Skip Connection Ghép Kênh** | Nhánh co rút Encoder (bên trái), nhánh mở rộng Decoder (bên phải) và các đường nối ngang ghép kênh `torch.cat` giúp bảo toàn đường biên phân đoạn sắc nét. |
| 8 | [Section 3.8](file:///E:/MyProject/MyWiki/interview/index.html#L4150) | **4 Kỹ Thuật Tăng Cường Dữ Liệu Nâng Cao (SOTA)** | 4 khung hình minh họa: 1. Cutout (ô vuông đen); 2. Mixup (pha trộn 2 ảnh $\lambda A + (1-\lambda)B$); 3. CutMix (dán miếng ảnh B vào A); 4. Mosaic (ghép 4 ảnh vào 1 khung YOLO). |
| 9 | [Section 3.9](file:///E:/MyProject/MyWiki/interview/index.html#L4240) | **Depthwise Separable Convolution Của MobileNet** | Đối chiếu Standard Conv ($K \times K \times C_{in} \times C_{out}$) với Depthwise Conv ($K \times K \times 1$) + Pointwise Conv ($1 \times 1 \times C_{in}$) tiết kiệm $\approx 9$ lần chi phí FLOPs. |
| 10 | [Section 3.9](file:///E:/MyProject/MyWiki/interview/index.html#L4270) | **Vision Transformer (ViT) vs Swin Transformer** | Đối chiếu ViT cắt patch $16 \times 16$ với self-attention toàn cục $O(N^2)$ vs Swin Transformer với cơ chế cửa sổ dịch chuyển Shifted Windows giảm độ phức tạp xuống tuyến tính $O(M^2 N)$. |

---

## 3. Bảng Tổng Hợp Kiến Thức Đã Tích Hợp

| Nhóm Chủ Đề | Nội Dung Chi Tiết Đã Tích Hợp | Vị Trí Trong `interview/index.html` |
| :--- | :--- | :--- |
| **Bias, Variance & Tradeoff** | Đánh đổi Bias-Variance, Underfitting vs Overfitting, đường cong học tập (Learning Curves), chiến lược khắc phục. | [Section 2.14](file:///E:/MyProject/MyWiki/interview/index.html#L2547) |
| **MLP & Dense Layer** | Phép biến đổi tuyến tính $\mathbf{z} = \mathbf{W}\mathbf{a} + \mathbf{b}$, phi tuyến hóa, từ điển 4 cột ký hiệu, sự thất bại của Dense layer trước ảnh số. | [Section 2.14](file:///E:/MyProject/MyWiki/interview/index.html#L2547) & [Section 3.3](file:///E:/MyProject/MyWiki/interview/index.html#L3154) |
| **Forward, Loss, Backprop & Update** | Lan truyền xuôi, MSE/BCE/Cross-Entropy, lan truyền ngược (Chain Rule), cập nhật $\mathbf{W} \leftarrow \mathbf{W} - \eta \nabla_{\mathbf{W}}\mathcal{L}$, vết dò số học 2 tầng full-width. | [Section 2.14](file:///E:/MyProject/MyWiki/interview/index.html#L2547) |
| **Optimizers & Momentum, Adam** | Bảng so sánh 6 thuật toán: Mini-batch SGD, Momentum, NAG, AdaGrad, RMSprop, Adam, AdamW. | [Section 2.13](file:///E:/MyProject/MyWiki/interview/index.html#L2446) |
| **CNN: Kernels, Stride, Padding & Volume** | Phép tích chập 2D/3D trên thể tích, công thức kích thước đầu ra $O = \lfloor \frac{W-K+2P}{S} \rfloor + 1$, Local Connectivity & Parameter Sharing, vết dò số học $4 \times 4$. | [Section 3.3](file:///E:/MyProject/MyWiki/interview/index.html#L3154) |
| **Pooling Layer & Receptive Field / ERF** | Bảng đối chiếu Max/Avg/GAP, công thức tích lũy $RF_l = RF_{l-1} + (K_l-1)J_{l-1}$, bản chất phân phối chuẩn Gauss của Effective Receptive Field. | [Section 3.4](file:///E:/MyProject/MyWiki/interview/index.html#L3381) |
| **Batch Normalization & Bộ Tứ Chuẩn Hóa** | Internal Covariate Shift, Loss Landscape Smoothing, 4 bước BN, Training vs Inference, Gập trọng số BN vào Conv, bảng đối chiếu BN/LN/IN/GN. | [Section 3.5](file:///E:/MyProject/MyWiki/interview/index.html#L3564) |
| **Inverted Dropout & Triệt Tiêu Gradient** | Cơ chế Inverted Dropout chia bù $(1-p)$ trong training, tích chuỗi đạo hàm Triệt tiêu / Bùng nổ Gradient và 4 trụ cột phòng ngự (ReLU, He Init, Normalization, Clipping). | [Section 3.6](file:///E:/MyProject/MyWiki/interview/index.html#L3747) |
| **Kiến Trúc Đột Phá: ResNet & U-Net** | Degradation problem, Residual Block $F(x)+x$, chứng minh đạo hàm số hạng $+1$ mở cao tốc gradient; U-Net Encoder-Decoder, Skip-Connection `torch.cat`, Combo Loss BCE+Dice. | [Section 3.7](file:///E:/MyProject/MyWiki/interview/index.html#L3800) |
| **Transfer Learning & Data Augmentation** | 3 cấp độ học chuyển giao (Feature Extraction, Partial Fine-Tuning, Full Fine-Tuning + Warmup); Kỹ thuật tăng cường hình học, quang học, Cutout, Mixup, CutMix, Mosaic. | [Section 3.8](file:///E:/MyProject/MyWiki/interview/index.html#L4081) |
| **MobileNet Edge & Vision Transformers** | MobileNet Depthwise Separable Conv ($DW + PW$) giảm $\approx 9$ lần FLOPs; ViT Patch $16 \times 16$ vs Swin Shifted Windows $O(M^2 N)$; Bảng so sánh 1-1 CNN vs ViT vs Swin. | [Section 3.9](file:///E:/MyProject/MyWiki/interview/index.html#L4172) |

---

## 4. Kiểm Tra Tính Toàn Vẹn Cú Pháp (Verification)

- [x] **Cân bằng Thẻ HTML (Tag Balance)**: Module 02 (từ dòng 575 đến 3032) và Module 03 (từ dòng 3033 đến 4411) đạt kết quả **100% cân bằng không một thẻ mở/đóng lệch hay sót** (`Stack remainder count: 0`).
- [x] **Trực tiếp thao tác (No File-Editing Scripts)**: Mọi thao tác sửa file đều thực hiện bằng `edit_file` chuẩn tắc.
- [x] **Chống Tràn Công Thức Toán**: Đã xóa bỏ các `grid-2` chật hẹp tại các khu vực chứa công thức vi phân và bảng tính số học.
- [x] **Hệ Thống Neo ScrollSpy**: Toàn bộ các ID `mod3-1` đến `mod3-9` khớp nối tuyệt đối với sidebar điều hướng.
