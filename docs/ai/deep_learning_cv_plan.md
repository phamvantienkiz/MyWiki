# Kế Hoạch Nâng Cấp Toàn Diện Kiến Thức Deep Learning & Computer Vision Cho `interview/`

## 1. Mục Tiêu & Yêu Cầu
- Tích hợp toàn diện các tài nguyên từ `resources/deep-learning/computer-vision/` và `resources/machine-learning/` vào bộ tài liệu phỏng vấn trong `interview/index.html`.
- Bao quát đầy đủ tất cả các chủ đề Deep Learning cốt lõi theo yêu cầu:
  1. **Bias - Underfitting - Variance - Overfitting trong Neural Networks**
  2. **Fully Connected layer (Dense layer)**: Kiến trúc, biểu diễn ma trận $\mathbf{z} = \mathbf{W}\mathbf{x} + \mathbf{b}$.
  3. **Forward propagation, Loss function, Backpropagation, Gradient, Optimization function, How parameters are updated?** ($\mathbf{w} \leftarrow \mathbf{w} - \eta \nabla_{\mathbf{w}} \mathcal{L}$).
  4. **Momentum & Adaptive Gradient Descent**: Mini-batch SGD, Momentum, Nesterov (NAG), AdaGrad, RMSprop, Adam, AdamW (Weight Decay tách rời).
  5. **Mạng Tích Chập (CNNs)**:
     - Convolutional layer, filters/kernels, size ($k \times k$), stride ($S$), padding ($P$), channel ($C$).
     - Convolutional operation, convolutional operation on volume (3D tensor $\mathbb{R}^{H \times W \times C}$).
     - Output size formula: $O = \lfloor \frac{W - K + 2P}{S} \rfloor + 1$.
     - Local connectivity (kết nối cục bộ) & Parameter sharing (chia sẻ tham số) giúp giảm số lượng trọng số từ hàng tỷ xuống vài ngàn.
  6. **Pooling Layer**:
     - Max Pooling, Average Pooling, Global Average Pooling (GAP thay thế Dense layer cuối).
  7. **Internal Covariate Shift & Các Tầng Chuẩn Hóa (Normalization Layers)**:
     - Khái niệm Internal Covariate Shift (sự trôi dạt phân phối kích hoạt qua các tầng).
     - Batch Normalization (BN): Tại sao chuẩn hóa giúp tăng tốc hội tụ và ổn định loss landscape?
     - Chi tiết 2 pha của BN: Pha huấn luyện (Training: tính mean $\mu_B$, var $\sigma_B^2$, scale $\gamma$, shift $\beta$, cập nhật running mean/var) vs Pha suy luận (Inference: dùng running mean/var cố định, kỹ thuật Fold Batch Normalization vào Conv).
     - Bộ 4 chuẩn hóa: Batch Normalization (BN), Layer Normalization (LN), Instance Normalization (IN), Group Normalization (GN) với bảng đối chiếu hình học trên tensor 4D $(N, C, H, W)$ và bối cảnh ứng dụng.
  8. **Dropout Layer**: Cơ chế Inverted Dropout (tỉ lệ $p$, chia cho $1-p$ ở forward để inference không tốn chi phí).
  9. **Receptive Field (RF) & Effective Receptive Field (ERF)**: Công thức tính toán $RF_{l} = RF_{l-1} + (k_l - 1) \times J_{l-1}$, phân phối Gauss thực tế của ERF tập trung ở trung tâm.
  10. **ResNet & Skip-Connection**: Căn bệnh suy thoái (Degradation), khối Residual Block $y = \mathcal{F}(x) + x$, đạo hàm $+1$ giữ dòng chảy gradient thông suốt không bị triệt tiêu.
  11. **U-Net**: Kiến trúc đối xứng Encoder-Decoder, Skip connections dạng Concatenation giữ chi tiết không gian mức pixel, Transposed Conv vs Bilinear Upsampling, Combo Loss (BCE + Dice).
  12. **Triệt tiêu / Bùng nổ Gradient (Vanishing / Exploding Gradients)**: Chuỗi vi phân Chain rule, đạo hàm của hàm Sigmoid $\le 0.25$, giải pháp khởi tạo He/Xavier, Gradient Clipping, Skip connections.
  13. **Transfer Learning & Fine-tuning**: 3 cấp độ (Feature Extraction, Partial Fine-tuning, Full Fine-tuning), Learning Rate Warmup, đóng băng/rã đông backbone.
  14. **Data Augmentation**: Biến đổi hình học (Geometric), quang học (Photometric), Cutout, Mixup, CutMix, Mosaic Augmentation.

## 2. Phương Pháp Sư Phạm `lecture-visualizer` ("Dành Cho Người Học Chậm")
- **Trực giác trước — Ký hiệu sau**: Diễn giải bằng ví dụ đời sống (Kính lúp quét trang sách, chiếc máy ép nước mía, hội đồng bác sĩ, đường cao tốc không tắc đường, người sao chép tranh nghệ thuật).
- **Bảng từ điển ký hiệu 4 cột** cho từng chủ đề.
- **Hộp thoại "Góc Dành Cho Người Học Chậm" (`.callout.intuition`)**.
- **Trace số học từng bước (Arithmetic trace)** trên Toy Dataset nhỏ gọn (tính tay ma trận tích chập, tính BN training & inference, tính Receptive Field, tính 1 bước backpropagation).
- **Bảng đối chiếu 1-1** (BN vs LN vs IN vs GN, Plain Net vs ResNet, Feature Extraction vs Fine-tuning).
- **KaTeX** chuẩn mực, không lỗi raw text.
- **Resource Pills & Wiki Links** trỏ tới các file PDF trong `resources/deep-learning/computer-vision/`.

## 3. Kiến Trúc Cấu Trúc Các File Cần Chỉnh Sửa
1. `interview/index.html`:
   - Hoàn thiện và làm sâu sắc thêm phần Mạng Nơ-ron, Backprop & Optimizers trong Module 02 (2.13, 2.14).
   - Tái cấu trúc Module 03 (Thị giác máy tính & CNNs) thành hệ thống chuyên đề chuẩn mực:
     - **3.1** Biểu Diễn Ảnh Số & Bộ Lọc Không Gian
     - **3.2** Xử Lý Hình Thái Học & Biến Đổi Hình Học (Homography)
     - **3.3** Mạng Tích Chập (CNNs): Kernels, Stride, Padding, Operation On Volume & Parameter Sharing
     - **3.4** Pooling Layer (Max, Avg, GAP) & Receptive Field vs Effective Receptive Field (ERF)
     - **3.5** Khắc Phục Internal Covariate Shift: Batch Normalization Toàn Tập (Training vs Inference) & Bộ Tứ Chuẩn Hóa (BN, LN, IN, GN)
     - **3.6** Kỹ Thuật Điều Chuẩn: Inverted Dropout & Triệt Tiêu Gradient (Vanishing Gradients)
     - **3.7** Kiến Trúc Đột Phá: ResNet (Skip-Connection $+1$) & U-Net (Encoder-Decoder Concatenation)
     - **3.8** Transfer Learning, Fine-Tuning Thực Chiến & Kỹ Thuật Tăng Cường Dữ Liệu (Data Augmentation)
     - **3.9** MobileNet Cho Thiết Bị Biên (Edge) & Vision Transformers (ViT / Swin)
   - Cập nhật Sidebar Navigation tương ứng.
2. `interview/script.js`:
   - Thêm bộ công cụ tương tác CNN / Convolution & Normalization Explorer nếu cần để người học thử nghiệm tính toán kích thước output hoặc Batch Norm.
3. `interview/style.css`:
   - Tinh chỉnh style hỗ trợ các bảng đối chiếu và thẻ Soft Clean Cards.
