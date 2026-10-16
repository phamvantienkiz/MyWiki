# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = Path("wiki")
WIKI_DIR.mkdir(parents=True, exist_ok=True)

ENTITIES = {
    "convolutional-neural-networks.md": r"""# Mạng Nơ-ron Tích Chập (Convolutional Neural Networks - CNN & ResNet)

> **Khái niệm chính thống**: *The Principles of Deep Learning Theory* (Roberts & Yaida, Cambridge), Chapter 1 & 2; LeCun et al. (1998) *"Gradient-Based Learning Applied to Document Recognition"*; He et al. (2016) *"Deep Residual Learning for Image Recognition"*.
> **Miền kiến thức**: [[deep-learning-overview|Deep Learning Foundations & Computer Vision]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_Reading_CNNs.pdf](../../resources/deep-learning/computer-vision/AIO2025_Reading_CNNs.pdf) (Trang 1-19)
> - [Classification - CNN.pdf](../../resources/deep-learning/computer-vision/Classification%20-%20CNN.pdf) (Trang 1-73)
> - [Deep Learning_Computer Vision_NLP.pdf](../../resources/deep-learning/Deep%20Learning_Computer%20Vision_NLP.pdf) (Trang 45-110)
> - [The-Principles-of-Deep-Learning-Theory.pdf](../../resources/deep-learning/The-Principles-of-Deep-Learning-Theory.pdf) (Trang 1-40)

---

## 1. Tóm tắt (Executive Summary)
**Mạng Nơ-ron Tích chập (Convolutional Neural Networks - CNN)** là lớp kiến trúc học sâu chuyên biệt được thiết kế để xử lý dữ liệu dạng lưới không gian (như ảnh 2D, âm thanh phổ tần spectrogram và video). Dựa trên hai nguyên lý quy nạp toán học then chốt là **tính bất biến tịnh tiến (Translation Invariance)** và **tính cục bộ không gian (Spatial Locality)** thông qua cơ chế chia sẻ trọng số (Parameter Sharing) và trường thụ cảm (Receptive Field), CNN giải phóng mạng nơ-ron khỏi sự bùng nổ số lượng tham số của mạng kết nối đầy đủ (MLP). Sự ra đời của kiến trúc **ResNet với kết nối tắt (Skip / Residual Connections)** đã giải quyết triệt để vấn đề suy biến gradient, mở đường cho việc huấn luyện các mạng sâu hàng trăm tầng.

---

## 2. Định nghĩa chính thống & Cơ chế Toán học (Mathematical Foundations)

### 2.1 Toán tử Tích chập 2D rời rạc (Discrete Cross-Correlation)
Trong học sâu, phép tính tích chập giữa ảnh đầu vào $I \in \mathbb{R}^{H \times W \times C_{in}}$ và bộ lọc (Kernel/Filter) $K \in \mathbb{R}^{k_h \times k_w \times C_{in}}$ tại vị trí $(i, j)$ được tính theo công thức tương quan chéo:
$$S(i, j) = (I * K)(i, j) = \sum_{m=0}^{k_h-1} \sum_{n=0}^{k_w-1} \sum_{c=0}^{C_{in}-1} I(i \cdot s + m, \; j \cdot s + n, \; c) \cdot K(m, n, c) + b$$
Trong đó:
- $s$ là bước trượt (Stride).
- Kích thước chiều không gian đầu ra sau tích chập với phần đệm (Padding) $p$:
  $$H_{out} = \left\lfloor \frac{H_{in} - k_h + 2p}{s} \right\rfloor + 1, \quad W_{out} = \left\lfloor \frac{W_{in} - k_w + 2p}{s} \right\rfloor + 1$$

```mermaid
flowchart LR
    Input["Input Image (H x W x C)"] --> Conv["Conv2D (Locality & Weight Sharing)"]
    Conv --> BN["BatchNorm / LayerNorm"]
    BN --> Act["ReLU / SiLU Activation"]
    Act --> Pool["MaxPooling / Strided Conv"]
    Pool --> ResBlock["Residual Block with Skip Connection: F(x) + x"]
    ResBlock --> GlobalPool["Global Average Pooling"]
    GlobalPool --> Dense["Dense Layer / Classification Head"]
```

### 2.2 Đột phá Residual Learning (ResNet - He et al., 2016)
Khi mạng nơ-ron trở nên quá sâu, việc tối ưu hóa gặp hiện tượng suy thoái (Degradation Problem): lỗi huấn luyện tăng lên dù không phải do quá khớp (overfitting).
ResNet tái cấu trúc phép ánh xạ mục tiêu $H(x)$ thành ánh xạ thặng dư:
$$H(x) = \mathcal{F}(x, \{W_i\}) + x$$
$$\text{Output } y = \sigma(\mathcal{F}(x) + x)$$
- Thay vì bắt các tầng nơ-ron học một hàm ánh xạ trực tiếp $H(x)$, mạng chỉ cần học phần sai khác $\mathcal{F}(x) = H(x) - x$.
- Nếu hàm đồng nhất (Identity Mapping) là tối ưu, bộ tối ưu hóa chỉ cần đẩy các trọng số của $\mathcal{F}(x)$ về 0, việc này dễ dàng hơn nhiều về mặt toán học.
- Đạo hàm theo lan truyền ngược:
  $$\frac{\partial \mathcal{E}}{\partial x} = \frac{\partial \mathcal{E}}{\partial y} \left( \frac{\partial \mathcal{F}}{\partial x} + 1 \right)$$
  Thành phần $+1$ đảm bảo gradient luôn có một "đường cao tốc" (gradient highway) truyền ngược thẳng về các tầng đầu tiên mà không bị triệt tiêu dù mạng sâu hàng trăm tầng.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Kiến trúc | Điểm mạnh cốt lõi | Điểm yếu cốt lõi | Mối quan hệ trong Thị giác Hiện đại |
| :--- | :--- | :--- | :--- |
| **CNN truyền thống (VGG, ResNet)** | Hiểu tính cục bộ cực nhanh, ít tốn dữ liệu (Strong Inductive Bias), chi phí tính toán thấp trên ảnh phân giải nhỏ. | Tầm nhìn bị hạn chế bởi Receptive Field; khó mô hình hóa các mối quan hệ ngữ cảnh toàn cục xa nhau trên bức ảnh. | Vẫn là xương sống (Backbone) trong các thiết bị nhúng và mô hình Mobile edge. |
| **Vision Transformer (ViT)** | Cơ chế Global Self-Attention giúp nhìn bao quát toàn bộ bức ảnh từ tầng đầu tiên. | Yếu về Inductive Bias; đòi hỏi tập dữ liệu khổng lồ (JFT-300M, ImageNet-22k) mới huấn luyện tốt. | Thống trị các tác vụ phân tích thị giác quy mô lớn khi có đủ dữ liệu. |
| **Swin Transformer / ConvNeXt** | Dung hợp: Đưa cấu trúc phân tầng và cục bộ của CNN vào cơ chế Attention của Transformer. | Độ phức tạp mã nguồn và tối ưu hóa phần cứng cao hơn. | Trở thành tiêu chuẩn SOTA cân bằng giữa hai trường phái. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy tắc thiết kế Receptive Field và Kernel Size
- **Tại sao nên dùng chuỗi các bộ lọc $3 \times 3$ thay vì dùng một bộ lọc $7 \times 7$?**
  - Hai tầng Conv $3 \times 3$ liên tiếp có cùng Effective Receptive Field là $5 \times 5$. Ba tầng Conv $3 \times 3$ có cùng Receptive Field là $7 \times 7$.
  - *Lợi ích*: Số lượng tham số giảm mạnh: $3 \times (3 \times 3 \times C^2) = 27 C^2$ so với $1 \times (7 \times 7 \times C^2) = 49 C^2$ (tiết kiệm gần một nửa tham số và FLOPs).
  - Đồng thời xen kẽ được 3 hàm kích hoạt phi tuyến tính thay vì 1, giúp tăng khả năng biểu diễn của mạng.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Batch Normalization (BN) hoạt động thế nào và tại sao cần chuyển sang chế độ `eval()` khi inference?*
  - **A**: Trong quá trình huấn luyện, BN chuẩn hóa từng kênh đặc trưng dựa trên giá trị trung bình $\mu_B$ và phương sai $\sigma_B^2$ được tính trực tiếp từ mini-batch hiện tại. Khi sang môi trường inference (chế độ phục vụ sản xuất), kích thước batch có thể chỉ là 1 ảnh duy nhất (không thể tính phương sai batch). Khi gọi `model.eval()`, BN sẽ cố định và sử dụng các giá trị trung bình và phương sai động (Running Mean & Running Variance) đã tích lũy trong toàn bộ quá trình huấn luyện, đảm bảo tính tất định và ổn định của mô hình.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[unet-architecture]] — Ứng dụng kiến trúc tích chập và skip connection vào phân đoạn ảnh.
- [[object-detection-yolo]] — Sử dụng CNN backbone để phát hiện và định vị vật thể.
- [[vision-transformers]] — Bước tiến hóa vượt qua giới hạn không gian của CNN.
- [[gradient-vanishing-exploding]] — Nền tảng toán học giải thích lý do ResNet thành công.
- [[inference-optimization-tensorrt]] — Tối ưu hóa nhân Conv2D và hợp nhất lớp (Conv + BN + ReLU Fusion).
""",

    "unet-architecture.md": r"""# Kiến Trúc U-Net và Phân Đoạn Ảnh (U-Net Architecture & Image Segmentation)

> **Khái niệm chính thống**: Ronneberger et al. (MICCAI 2015) *"U-Net: Convolutional Networks for Biomedical Image Segmentation"*; *Deep Learning for Computer Vision*, Chapter 6.
> **Miền kiến thức**: [[deep-learning-overview|Computer Vision & Semantic Segmentation]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_Reading-UNet.pdf](../../resources/deep-learning/computer-vision/AIO2025_Reading-UNet.pdf) (Trang 1-45)
> - [Classification - CNN.pdf](../../resources/deep-learning/computer-vision/Classification%20-%20CNN.pdf) (Trang 50-73)
> - [Deep Learning_Computer Vision_NLP.pdf](../../resources/deep-learning/Deep%20Learning_Computer%20Vision_NLP.pdf) (Trang 120-150)

---

## 1. Tóm tắt (Executive Summary)
**Kiến trúc U-Net** là mô hình mạng nơ-ron tích chập dạng Bộ mã hóa - Bộ giải mã đối xứng (**Encoder-Decoder**) được thiết kế chuyên biệt cho bài toán **Phân đoạn ngữ nghĩa (Semantic Segmentation)** và xử lý ảnh y sinh. Đặc trưng đột phá của U-Net là các **kết nối tắt xuyên tầng (Long Skip Connections)** nối trực tiếp các bản đồ đặc trưng có độ phân giải cao ở nhánh co (Contracting / Encoder path) sang các tầng giải mã tương ứng ở nhánh mở rộng (Expansive / Decoder path). Cơ chế này cho phép mô hình vừa nắm bắt ngữ cảnh ngữ nghĩa trừu tượng cấp cao, vừa tái tạo chính xác từng đường viền và ranh giới không gian chi tiết đến từng điểm ảnh (Pixel-level localization).

---

## 2. Định nghĩa chính thống & Sơ đồ Cấu trúc Chữ U (Architecture & Loss Functions)

### 2.1 Cấu trúc hai nhánh đối xứng
1. **Nhánh Co (Contracting / Encoder Path)**:
   - Cấu trúc gồm các khối lặp lại: `Conv 3x3 -> ReLU -> Conv 3x3 -> ReLU -> MaxPooling 2x2`.
   - Giảm dần kích thước không gian ($H, W$) để tăng trường thụ cảm và tăng số lượng kênh đặc trưng (Channels) để học thông tin "Vật thể đó là gì?" (**What**).
2. **Nhánh Mở rộng (Expansive / Decoder Path)**:
   - Sử dụng phép tích chập chuyển vị (Transposed Convolution / Up-Convolution 2x2) để tăng gấp đôi kích thước không gian.
   - **Skip Connection Concatenation**: Ghép nối (concatenate) bản đồ đặc trưng từ Encoder sang Decoder theo trục kênh:
     $$X_{\text{decoder\_input}} = \text{Concat}(X_{\text{up-sampled}}, \; X_{\text{encoder\_skip}})$$
   - Khôi phục chính xác thông tin "Vật thể đó nằm ở đâu?" (**Where**).

```mermaid
flowchart TD
    Input["Input Image (H x W x C)"] --> Enc1["Encoder Block 1 (High Res, Low Semantics)"]
    Enc1 --> Pool1["MaxPool 2x2"]
    Pool1 --> Enc2["Encoder Block 2"]
    Enc2 --> Pool2["MaxPool 2x2"]
    Pool2 --> Bottleneck["Bottleneck (Deepest Semantics, Low Res)"]
    
    Bottleneck --> Up1["Transposed Conv 2x2"]
    Enc2 -.->|"Skip Connection (Fine Spatial Details)"| Cat1["Concat"]
    Up1 --> Cat1
    Cat1 --> Dec1["Decoder Block 2"]
    
    Dec1 --> Up2["Transposed Conv 2x2"]
    Enc1 -.->|"Skip Connection"| Cat2["Concat"]
    Up2 --> Cat2
    Cat2 --> Dec2["Decoder Block 1"]
    
    Dec2 --> Head["Conv 1x1 + Sigmoid / Softmax"]
    Head --> Mask["Pixel-wise Segmentation Mask"]
```

### 2.2 Hàm mất mát chuyên biệt: Dice Loss & Focal Loss
Trong bài toán phân đoạn ảnh, số lượng điểm ảnh hậu cảnh (background) thường áp đảo hoàn toàn số điểm ảnh vùng tổn thương/vật thể (Class Imbalance nghiêm trọng). Hàm Cross-Entropy truyền thống bị tê liệt.
- **Sørensen–Dice Coefficient**:
  $$\text{Dice} = \frac{2 |X \cap Y|}{|X| + |Y|} = \frac{2 \sum_i p_i y_i}{\sum_i p_i + \sum_i y_i + \epsilon}$$
- **Soft Dice Loss (Khả vi để lan truyền ngược)**:
  $$\mathcal{L}_{\text{Dice}} = 1 - \frac{2 \sum_{i=1}^N p_i g_i + \epsilon}{\sum_{i=1}^N p_i^2 + \sum_{i=1}^N g_i^2 + \epsilon}$$
- Trong thực tế, kỹ sư thường kết hợp **Combo Loss**: $\mathcal{L} = \alpha \mathcal{L}_{\text{BCE}} + \beta \mathcal{L}_{\text{Dice}}$.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Thành phần | U-Net nguyên thủy (2015) | Các biến thể hiện đại (U-Net++, nnU-Net, TransUNet) | Ghi chú kiến trúc |
| :--- | :--- | :--- | :--- |
| **Phép kết nối Skip** | Nối thẳng thô sơ (Direct Concatenation). Vì tích chập không có padding nên phải cắt xén (crop) biên ảnh. | Dùng **Same Padding** và bổ sung các nút mạng lồng nhau (Dense Nested Skip Pathways) trong U-Net++ để thu hẹp khoảng cách ngữ nghĩa giữa Encoder và Decoder. | U-Net++ giải quyết hiện tượng lệch tầng ngữ nghĩa giữa biểu diễn mức thấp và mức cao. |
| **Up-sampling Method** | Transposed Convolution (Tích chập chuyển vị). | Chuyển dịch sang **Bilinear Interpolation + Conv 3x3**. | Transposed Conv thường gây ra hiện tượng mắt lưới bàn cờ (Checkerboard Artifacts) trên ảnh đầu ra; phép nội suy tuyến tính triệt tiêu hoàn toàn lỗi này. |
| **Ứng dụng ngoài y tế** | Chỉ nhắc tới phân đoạn tế bào y sinh. | Trở thành xương sống (Backbone) trong các mô hình **Diffusion sinh ảnh (Stable Diffusion)** để dự đoán nhiễu (Noise Predictor). | U-Net là kiến trúc khử nhiễu hoàn hảo nhất vì bảo toàn được kích thước ảnh đầu vào và đầu ra tương đương. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy tắc đánh giá: IoU vs Dice Coefficient
- **IoU (Intersection over Union / Jaccard Index)**:
  $$\text{IoU} = \frac{|A \cap B|}{|A \cup B|} = \frac{\text{Dice}}{2 - \text{Dice}}$$
- Điểm IoU luôn khắt khe hơn Dice score (IoU $\le$ Dice). Trong các cuộc thi Kaggle hoặc nghiệm thu dự án y tế, hãy làm rõ khách hàng yêu cầu nghiệm thu theo chuẩn IoU hay Dice để tránh hiểu lầm chỉ số.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao Skip Connection trong U-Net lại dùng phép Concatenate (ghép kênh), trong khi Skip Connection của ResNet lại dùng phép Addition (cộng phần tử)?*
  - **A**:
    - Trong **ResNet**, mục tiêu là giải quyết vấn đề suy thoái gradient trong mạng sâu phân loại; phép cộng $F(x) + x$ giữ nguyên số chiều kênh, cho phép gradient truyền ngược thẳng về mà không làm tăng kích thước tham số.
    - Trong **U-Net**, mục tiêu là định vị điểm ảnh (localization); thông tin từ Encoder là chi tiết không gian thô sơ (edges, corners), còn Decoder là thông tin ngữ nghĩa trừu tượng. Phép Concatenate ghép 2 luồng này vào các kênh độc lập, cho phép các tầng tích chập phía sau tự do học cách kết hợp cả hai loại thông tin mà không làm ép buộc hay phá hủy phân phối giá trị của nhau.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[convolutional-neural-networks]] — Nền tảng xây dựng nên các khối Encoder/Decoder của U-Net.
- [[object-detection-yolo]] — So sánh giữa bài toán phân đoạn (Pixel-level) và phát hiện vật thể (Box-level).
- [[vision-transformers]] — TransUNet tích hợp Transformer vào nút cổ chai Bottleneck của U-Net.
""",

    "object-detection-yolo.md": r"""# Phát Hiện Vật Thể và Dòng Họ YOLO (Object Detection & YOLO Evolution)

> **Khái niệm chính thống**: Redmon et al. (CVPR 2016) *"You Only Look Once: Unified, Real-Time Object Detection"*; Wang et al. (2024) *"YOLOv10: Real-Time End-to-End Object Detection"*; *AIO2025 Series: YOLO Tutorial*.
> **Miền kiến thức**: [[deep-learning-overview|Computer Vision & Real-time Object Detection]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_YOLO-Tutorial.pdf](../../resources/deep-learning/computer-vision/AIO2025_YOLO-Tutorial.pdf) (Trang 1-88)
> - [AIO2025_Object-Detection-Quiz.pdf](../../resources/deep-learning/computer-vision/AIO2025_Object-Detection-Quiz.pdf) (Trang 1-27)
> - [Object Detection.pdf](../../resources/deep-learning/computer-vision/Object%20Detection.pdf) (Trang 1-47)
> - [Deep Learning_Computer Vision_NLP.pdf](../../resources/deep-learning/Deep%20Learning_Computer%20Vision_NLP.pdf) (Trang 80-120)

---

## 1. Tóm tắt (Executive Summary)
**Phát hiện Vật thể (Object Detection)** là bài toán thị giác máy tính cốt lõi đồng thời xác định vị trí biên tọa độ (Bounding Box) và phân loại nhãn (Classification) của nhiều vật thể xuất hiện trong ảnh. Cuộc cách mạng **YOLO (You Only Look Once)** đã tái định nghĩa bài toán từ quy trình hai giai đoạn chậm chạp (Two-Stage Detectors như R-CNN/Faster R-CNN) thành bài toán hồi quy đơn giai đoạn (**Single-Stage Regression**), dự đoán trực tiếp tọa độ hộp và xác suất lớp chỉ qua một lượt truyền xuôi duy nhất (Single Forward Pass). Trải qua từ YOLOv1 đến YOLOv10/v11, dòng họ YOLO đã tích hợp các cơ chế Anchor-free, Path Aggregation, và gần đây nhất là loại bỏ hoàn toàn thuật toán hậu xử lý NMS (NMS-free training) để đạt tốc độ xử lý thời gian thực hàng trăm FPS.

---

## 2. Định nghĩa chính thống & Kiến trúc Phát hiện Vật thể

### 2.1 Mô hình Kiến trúc 3 Thành phần Chuẩn mực
Mọi mô hình phát hiện vật thể hiện đại đều được cấu thành từ 3 phần:
1. **Backbone**: Mạng tích chập sâu (DarkNet, CSPDarknet, HGNet) trích xuất các bản đồ đặc trưng đa tỷ lệ từ ảnh đầu vào.
2. **Neck**: Mạng kết hợp đặc trưng phân tầng (**FPN - Feature Pyramid Network**, **PANet - Path Aggregation Network**), trộn các đặc trưng ngữ nghĩa mức cao với đặc trưng vị trí mức thấp để phát hiện vật thể ở nhiều kích thước khác nhau (nhỏ, vừa, lớn).
3. **Head**: Dự đoán các hộp giới hạn (Bounding Boxes), độ tin cậy chứa vật thể (Objectness Score), và phân phối xác suất lớp (Class Probabilities).

```mermaid
flowchart LR
    Input["Input Image (640x640x3)"] --> Backbone["Backbone (CSPDarkNet / RepVGG)"]
    Backbone --> Neck["Neck (PANet: Feature Pyramid Fusion)"]
    Neck --> P3["P3 Head (Detect Small Objects)"]
    Neck --> P4["P4 Head (Detect Medium Objects)"]
    Neck --> P5["P5 Head (Detect Large Objects)"]
    P3 --> NMS{"Dual-Label Assignment / NMS"}
    P4 --> NMS
    P5 --> NMS
    NMS --> Detections["Final Bounding Boxes + Classes"]
```

### 2.2 Các độ đo chất lượng then chốt
1. **IoU (Intersection over Union)**:
   $$\text{IoU} = \frac{\text{Area of Overlap}}{\text{Area of Union}} = \frac{|B_p \cap B_{gt}|}{|B_p \cup B_{gt}|}$$
2. **mAP (Mean Average Precision)**:
   - Tính diện tích dưới đường cong Precision-Recall (AUC-PR) cho từng lớp, sau đó lấy trung bình trên toàn bộ các lớp đối tượng.
   - **mAP@50**: Độ chính xác trung bình khi ngưỡng IoU $\ge 0.50$.
   - **mAP@50:95 (Chuẩn COCO)**: Lấy trung bình của mAP tại 10 ngưỡng IoU khác nhau từ 0.50 đến 0.95 với bước nhảy 0.05.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Thế hệ YOLO | Cơ chế Anchor | Đột phá kiến trúc then chốt | Điểm nghẽn khắc phục |
| :--- | :--- | :--- | :--- |
| **YOLOv1 - v3** | Anchor-based (Sử dụng K-means phân cụm kích thước hộp neo cố định). | DarkNet, FPN, đa tỷ lệ (3 scale outputs). | Tốc độ cao nhưng khó bắt vật thể nhỏ và vật thể đứng sát nhau. |
| **YOLOv4 - v7** | Anchor-based / CSPNet. | Mosaic Data Augmentation, CSPNet (Cross-Stage Partial), E-ELAN. | Tối ưu hóa việc sử dụng bộ nhớ và tính toán trên phần cứng GPU tiêu dùng. |
| **YOLOv8** | **Anchor-free**. | Tách biệt nhánh phân loại và hồi quy hộp (Decoupled Head); loại bỏ hoàn toàn khái niệm Anchor box. | Loại bỏ sự phụ thuộc vào việc tinh chỉnh thủ công kích thước anchor boxes cho từng tập dữ liệu mới. |
| **YOLOv10 (2024)** | **NMS-Free (End-to-End)**. | Huấn luyện nhãn kép (Consistent Dual Assignments: One-to-Many cho training, One-to-One cho inference). | **Loại bỏ hoàn toàn NMS**: Triệt tiêu độ trễ hậu xử lý, giảm độ trễ inference xuống mức tối thiểu. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Tử huyệt NMS trong Edge Deployment
- Thuật toán **Non-Maximum Suppression (NMS)** truyền thống:
  - Lặp qua hàng ngàn hộp dự đoán, sắp xếp theo điểm tin cậy, tính IoU để loại bỏ các hộp trùng lặp có $\text{IoU} > \text{threshold}$.
  - *Vấn đề trong Production*: NMS chạy tuần tự trên CPU hoặc cần nhân CUDA phức tạp, có thể chiếm tới 30-50% tổng độ trễ của toàn bộ pipeline khi trên ảnh có hàng trăm vật thể chen chúc.
  - *Giải pháp 2025-2026*: Chuyển dịch sang các kiến trúc **End-to-End không cần NMS** (như YOLOv10 hoặc RT-DETR).

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Sự khác biệt cốt lõi giữa hàm mất mát GIoU, DIoU, CIoU trong hồi quy hộp giới hạn là gì?*
  - **A**:
    - **IoU Loss**: Bằng 0 khi hai hộp không giao nhau, khiến gradient bị triệt tiêu hoàn toàn.
    - **GIoU (Generalized IoU)**: Thêm hệ số phạt dựa trên diện tích hộp bao nhỏ nhất chứa cả 2 hộp, giúp đẩy 2 hộp lại gần nhau ngay cả khi không giao nhau.
    - **DIoU (Distance IoU)**: Thêm thành phần khoảng cách Euclid giữa hai tâm hộp chuẩn hóa theo đường chéo của hộp bao, tăng tốc độ hội tụ cực nhanh.
    - **CIoU (Complete IoU)**: Hoàn thiện bằng cách bổ sung thêm ràng buộc về tỷ lệ khung hình (Aspect Ratio consistency) giữa hộp dự đoán và hộp nhãn gốc, là hàm mất mát tiêu chuẩn trong các bản YOLO hiện đại.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[convolutional-neural-networks]] — Xương sống trích xuất đặc trưng của YOLO.
- [[unet-architecture]] — So sánh đối chiếu giữa phân đoạn điểm ảnh và bounding box.
- [[inference-optimization-tensorrt]] — Quy trình bắt buộc để deploy YOLO thời gian thực trên camera giao thông/robotics.
""",

    "vision-transformers.md": r"""# Thị Giác Máy Tính Dựa Trên Transformer (Vision Transformers & Swin Transformer)

> **Khái niệm chính thống**: Dosovitskiy et al. (ICLR 2021) *"An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale"*; Liu et al. (ICCV 2021) *"Swin Transformer: Hierarchical Vision Transformer using Shifted Windows"*; *Deep Learning for Computer Vision*, Chapter 8.
> **Miền kiến thức**: [[deep-learning-overview|Modern Vision Architectures & Attention]]
> **Tài liệu gốc liên quan**:
> - [AIO_Solution_Swin_CNN.pdf](../../resources/deep-learning/computer-vision/AIO_Solution_Swin_CNN.pdf) (Trang 1-10)
> - [Deep Learning_Computer Vision_NLP.pdf](../../resources/deep-learning/Deep%20Learning_Computer%20Vision_NLP.pdf) (Trang 220-250)
> - [Classification - CNN.pdf](../../resources/deep-learning/computer-vision/Classification%20-%20CNN.pdf) (Trang 60-73)

---

## 1. Tóm tắt (Executive Summary)
**Vision Transformers (ViT)** đánh dấu bước ngoặt lịch sử khi áp dụng trực tiếp kiến trúc Transformer nguyên bản của xử lý ngôn ngữ tự nhiên vào thị giác máy tính mà hầu như không cần chỉnh sửa cấu trúc. Bằng cách chia nhỏ bức ảnh thành chuỗi các mảnh vá (**Patches**) có kích thước cố định (ví dụ $16 \times 16$) và xem mỗi patch như một "token từ ngữ", ViT khai thác sức mạnh của cơ chế Global Self-Attention để mô hình hóa mối quan hệ giữa mọi vùng trên ảnh. Tiếp nối ViT, kiến trúc **Swin Transformer (Shifted Windows)** đã giải quyết bài toán độ phức tạp tính toán bậc hai bằng cách tính toán Attention trong các cửa sổ cục bộ phân tầng và hoán vị cửa sổ, đưa Vision Transformer trở thành xương sống (Backbone) đa năng cho mọi tác vụ từ phân loại, phát hiện vật thể đến phân đoạn ảnh.

---

## 2. Định nghĩa chính thống & Cơ chế Patch Embedding

### 2.1 Từ Bức ảnh đến Chuỗi Token (ViT Ingestion)
Cho ảnh $I \in \mathbb{R}^{H \times W \times C}$ với kích thước patch là $P \times P$:
1. Số lượng patch thu được: $N = \frac{HW}{P^2}$.
2. Mỗi patch được duỗi phẳng (flatten) thành vector kích thước $P^2 \cdot C$, sau đó chiếu tuyến tính qua ma trận $E \in \mathbb{R}^{(P^2 \cdot C) \times D}$ để thu được vector nhúng có số chiều $D$:
   $$z_0 = [x_{\text{class}}; \; x_p^1 E; \; x_p^2 E; ...; \; x_p^N E] + E_{pos}$$
3. Thêm một token học được đặc biệt $[x_{\text{class}}]$ vào đầu chuỗi (tương tự token `[CLS]` của BERT) và cộng vector mã hóa vị trí 1D học được ($E_{pos} \in \mathbb{R}^{(N+1) \times D}$).
4. Chuỗi vector được đưa qua các khối Transformer Encoder chuẩn mực. Trạng thái ẩn cuối cùng của token `[CLS]` được dùng làm đầu vào cho bộ phân loại (MLP Head).

```mermaid
flowchart TD
    Img["Input Image (224x224x3)"] --> Patch["Patch Extraction (16x16 Patches -> N = 196)"]
    Patch --> Linear["Linear Projection to Dimension D (Patch Embedding)"]
    Linear --> Prepend["Prepend [CLS] Token & Add 1D Positional Embeddings"]
    Prepend --> Blocks["Standard Transformer Encoder Layers (MHA + MLP)"]
    Blocks --> CLSOut["Output State of [CLS] Token"]
    CLSOut --> Classifier["MLP Classification Head"]
```

### 2.2 Đột phá Swin Transformer: Shifted Window Attention
ViT nguyên bản có độ phức tạp tính toán $\mathcal{O}((HW)^2)$ theo độ phân giải ảnh, khiến nó bất khả thi cho các ảnh độ phân giải cao trong phát hiện vật thể.
Swin Transformer giải quyết vấn đề này qua hai cơ chế:
1. **Window Multi-Head Self-Attention (W-MSA)**: Chia ảnh thành các cửa sổ kích thước $M \times M$ không chồng lấn (thường $M=7$). Chỉ tính Self-Attention bên trong từng cửa sổ, đưa độ phức tạp về mức tuyến tính $\mathcal{O}(HW \cdot M^2)$.
2. **Shifted Window Multi-Head Self-Attention (SW-MSA)**: Ở tầng tiếp theo, dịch chuyển vị trí các cửa sổ đi $\left(\lfloor \frac{M}{2} \rfloor, \lfloor \frac{M}{2} \rfloor\right)$ pixels. Cơ chế dịch chuyển này cho phép thông tin giao tiếp xuyên qua ranh giới của các cửa sổ cũ mà vẫn giữ nguyên chi phí tính toán tuyến tính.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Tiêu chí | Convolutional Neural Network (ResNet) | Vision Transformer (ViT) | Swin Transformer |
| :--- | :--- | :--- | :--- |
| **Định kiến quy nạp (Inductive Bias)** | Rất mạnh (giả định tính cục bộ và bất biến tịnh tiến). | Rất yếu (mô hình phải tự học cấu trúc hình học từ dữ liệu). | Trung bình khá (đưa tính cục bộ phân tầng trở lại). |
| **Yêu cầu dữ liệu huấn luyện** | Học tốt trên tập dữ liệu nhỏ và vừa (ImageNet-1k). | Cần dữ liệu khổng lồ (JFT-300M) nếu không sẽ bị underfit/overfit nghiêm trọng. | Học tốt trên ImageNet-1k nhờ cấu trúc cửa sổ. |
| **Độ phức tạp theo phân giải ảnh** | Tuyến tính $\mathcal{O}(HW)$. | Bậc hai $\mathcal{O}((HW)^2)$. | Tuyến tính $\mathcal{O}(HW)$. |
| **Độ đa năng cho bài toán Downstream** | Tốt cho mọi bài toán (Dense Prediction). | Kém trên Object Detection/Segmentation vì độ phân giải cố định. | **Xuất sắc nhất**; làm backbone thay thế ResNet trong toàn bộ mô hình SOTA. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Triển khai ViT trong Môi trường Hạn chế Tài nguyên
- Không bao giờ huấn luyện ViT từ đầu (from scratch) trên tập dữ liệu đặc thù của công ty nếu số lượng ảnh dưới 100.000 mẫu.
- Luôn sử dụng kỹ thuật **Transfer Learning**: Lấy checkpoint tiền huấn luyện (pretrained weights từ HuggingFace/timm) và chỉ tinh chỉnh (fine-tuning) các tầng cuối cùng hoặc áp dụng LoRA trên các ma trận $W_Q, W_V$ của Transformer.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao phép trích xuất Patch Embedding trong ViT lại có thể được cài đặt tương đương tuyệt đối bằng một lớp Convolution 2D duy nhất?*
  - **A**: Phép trích xuất patch kích thước $P \times P$ và chiếu tuyến tính sang vector $D$ chiều chính là một lớp `nn.Conv2d(in_channels=3, out_channels=D, kernel_size=P, stride=P)`. Do bước trượt `stride` bằng đúng kích thước nhân `kernel_size = P`, các cửa sổ tích chập hoàn toàn không gối lên nhau, tạo ra chính xác $\frac{H}{P} \times \frac{W}{P}$ vector biểu diễn có số chiều $D$. Cách cài đặt này tận dụng tối đa nhân tăng tốc GPU thay vì phải cắt mảng thủ công.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[transformer-architecture]] — Bản thiết kế gốc của cơ chế Self-Attention.
- [[convolutional-neural-networks]] — Hệ quy chiếu đối chiếu của ViT trong thị giác máy tính.
- [[object-detection-yolo]] — Swin Transformer làm backbone cho các bộ phát hiện vật thể tiên tiến.
- [[inference-optimization-tensorrt]] — Kỹ thuật biên dịch nhân Attention tối ưu cho ViT trên GPU.
""",

    "inference-optimization-tensorrt.md": r"""# Tối Ưu Hóa Suy Luận và TensorRT (Inference Optimization & TensorRT)

> **Khái niệm chính thống**: NVIDIA TensorRT Developer Guide; *AIO2025 Series: Tối ưu hiệu suất mô hình với ONNX và TensorRT*; *Encyclopedia of LLMs*, Chapter 11.
> **Miền kiến thức**: [[deep-learning-overview|Model Deployment & Hardware Acceleration]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_Reading_ONNX_TensorRT.pdf](../../resources/deep-learning/computer-vision/AIO2025_Reading_ONNX_TensorRT.pdf) (Trang 1-42)
> - [AIO2025_M08W05-Reading_ONNX_TensorRT.pdf](../../resources/deep-learning/computer-vision/AIO2025_M08W05-Reading_ONNX_TensorRT.pdf) (Trang 1-42)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 101-105)

---

## 1. Tóm tắt (Executive Summary)
**Tối ưu hóa Suy luận (Inference Optimization)** là quá trình chuyển đổi, biên dịch và tinh gọn một mô hình học sâu sau huấn luyện (từ PyTorch/TensorFlow) sang một công cụ thực thi tối ưu hóa ở cấp độ phần cứng (Hardware-specific Execution Engine) nhằm đạt **thời gian phản hồi thấp nhất (Latency Minimization)** và **thông lượng cao nhất (Throughput Maximization)**. Tiêu chuẩn vàng trong hệ sinh thái NVIDIA là chuyển đổi mô hình qua định dạng trung gian **ONNX (Open Neural Network Exchange)**, sau đó nạp vào trình biên dịch **TensorRT** để thực hiện hợp nhất toán tử (Kernel Fusion), lượng tử hóa bán chính xác (FP16/INT8 Calibration) và tự động lựa chọn nhân CUDA tối ưu nhất trên kiến trúc vi xử lý mục tiêu.

---

## 2. Định nghĩa chính thống & Các kỹ thuật Tối ưu hóa TensorRT

```mermaid
flowchart TD
    PyTorch["PyTorch / TensorFlow Trained Model"] --> Export["Export to ONNX Graph (.onnx)"]
    Export --> Simplify["ONNX Simplifier (Constant Folding)"]
    Simplify --> TRTBuilder["NVIDIA TensorRT Builder"]
    
    subgraph TensorRT Optimizations
        TRTBuilder --> Fusion["Layer & Tensor Fusion (Conv+BN+ReLU -> Single CUDA Kernel)"]
        TRTBuilder --> Precision["Precision Calibration (FP32 -> FP16 / INT8 PTQ)"]
        TRTBuilder --> KernelAuto["Kernel Auto-Tuning (Select Fastest Algorithms for GPU)"]
        TRTBuilder --> MemOpt["Dynamic Tensor Memory Management"]
    end
    
    Precision --> Engine["Optimized Serialized Engine (.engine / .plan)"]
    Engine --> Runtime["TensorRT C++ / Python Runtime Server"]
```

### 2.1 4 Kỹ thuật tối ưu hóa cốt lõi của TensorRT
1. **Hợp nhất Tầng và Toán tử (Layer & Tensor Fusion)**:
   - Trong đồ thị PyTorch thông thường, chuỗi `Convolution -> BatchNorm -> ReLU` đòi hỏi GPU phải thực thi 3 CUDA kernels riêng biệt, ghi dữ liệu trung gian ra bộ nhớ VRAM (HBM) rồi đọc lại 3 lần.
   - TensorRT hợp nhất 3 thao tác này thành **một nhân tính toán duy nhất (CBR Fused Kernel)**: Dữ liệu được giữ trong thanh ghi nội bộ của chip (Registers/SRAM), giảm thiểu 66% băng thông đọc/ghi bộ nhớ.
2. **Hiệu chuẩn Lượng tử hóa INT8 (INT8 Post-Training Calibration)**:
   - Chuyển đổi trọng số và ma trận kích hoạt từ 32-bit sang số nguyên 8-bit.
   - Sử dụng thuật toán đo phân kỳ Kullback-Leibler (**KL Divergence**) trên một tập dữ liệu hiệu chuẩn nhỏ (Calibration Dataset) để tìm ngưỡng cắt (Threshold clipping) tối ưu, đảm bảo thông tin ngữ nghĩa bị mất đi là nhỏ nhất.
3. **Kernel Auto-Tuning (Tự động tinh chỉnh nhân CUDA)**:
   - TensorRT chạy thử nghiệm thực tế hàng chục giải thuật nhân ma trận khác nhau (GEMM, Winograd, Direct Convolution) trực tiếp trên dòng card GPU đang chạy (ví dụ RTX 4090, A100 hay T4) và chọn ra thuật toán có tốc độ thực thi nhanh nhất tương ứng với batch size chỉ định.
4. **Tái sử dụng Bộ nhớ Động (Dynamic Memory Management)**:
   - Cấp phát lại các vùng đệm bộ nhớ (Memory footprint) dùng chung cho các tensor không tồn tại đồng thời, giảm đáng kể dung lượng VRAM tổng thể.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Môi trường Thực thi | Độ trễ (Latency) | Khả năng mở rộng phần cứng | Mức độ phức tạp triển khai |
| :--- | :--- | :--- | :--- |
| **PyTorch Native (`model(x)`)** | Cao (chứa overhead của Python runtime, CUDA kernel launches rời rạc). | Rất linh hoạt (chạy được trên mọi thiết bị). | Thấp nhất (sẵn sàng ngay sau huấn luyện). |
| **ONNX Runtime (CPU / GPU)** | Nhanh hơn PyTorch 1.5 - 2.5 lần; tối ưu hóa đồ thị nền tảng. | Đa nền tảng (Intel CPU, AMD, NVIDIA, ARM). | Trung bình; dễ debug bằng Netron viewer. |
| **TensorRT Engine** | **Nhanh nhất (Nhanh hơn PyTorch 3 - 8 lần)**; khai thác tối đa Tensor Cores. | Độc quyền phần cứng NVIDIA GPU. Checkpoint `.engine` biên dịch trên card nào chỉ chạy được trên card đó! | Cao; đòi hỏi cài đặt CUDA/cuDNN/TensorRT tương thích phiên bản nghiêm ngặt. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy tắc triển khai TensorRT trong Production
1. **Quy tắc "Hardware Binding"**: Không bao giờ biên dịch TensorRT engine trên máy tính cá nhân (ví dụ GPU RTX 3060) rồi copy file `.engine` lên máy chủ Cloud (GPU NVIDIA T4 hoặc A10G). File engine gắn chặt với kiến trúc Compute Capability của phần cứng; bắt buộc phải biên dịch file engine ngay trên chính môi trường phần cứng máy chủ phục vụ.
2. **Hỗ trợ Dynamic Shape**: Khi xuất ONNX và build TensorRT, phải khai báo dải kích thước linh hoạt (`min_shape`, `opt_shape`, `max_shape`) cho batch size và sequence length để engine có thể phục vụ cả các request đơn lẻ (batch=1) lẫn các đợt request dồn dập (batch=16, 32).

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao quy trình INT8 Calibration trong TensorRT lại sử dụng phân kỳ KL (Kullback-Leibler Divergence) thay vì chỉ lấy giá trị Max đơn thuần (Max-Range)?*
  - **A**: Nếu chỉ lấy giá trị Max tuyệt đối của ma trận kích hoạt làm ngưỡng lượng tử hóa, các giá trị ngoại lai cực đoan (outliers - có thể chỉ chiếm 0.01% số lượng điểm ảnh nhưng có độ lớn gấp 100 lần) sẽ kéo dãn thang đo $S$, khiến 99.99% các giá trị bình thường còn lại bị co cụm vào chỉ một vài giá trị số nguyên INT8 lân cận 0, làm phá hủy hoàn toàn độ chính xác của mạng. Phương pháp phân kỳ KL đo lường sự mất mát thông tin giữa phân phối liên tục gốc và phân phối lượng tử hóa rời rạc, từ đó tìm ra ngưỡng cắt tối ưu để bão hòa các outlier nhưng bảo toàn tối đa độ phân giải cho khối dữ liệu chủ đạo.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[convolutional-neural-networks]] — Mô hình đối tượng hưởng lợi trực tiếp từ hợp nhất lớp CBR.
- [[object-detection-yolo]] — Triển khai TensorRT là chuẩn mực bắt buộc để chạy YOLO 60+ FPS.
- [[quantization-and-compression]] — Nền tảng lý thuyết lượng tử hóa INT8 và FP16.
- [[model-serving-api]] — Tích hợp TensorRT engine vào Triton Inference Server hoặc FastAPI backend.
""",

    "graph-neural-networks.md": r"""# Mạng Nơ-ron Đồ Thị (Graph Neural Networks - GNN & GCN)

> **Khái niệm chính thống**: *Deep Learning on Graphs* (Yao Ma & Jiliang Tang, Cambridge 2021); Kipf & Welling (ICLR 2017) *"Semi-Supervised Classification with Graph Convolutional Networks"*; Veličković et al. (ICLR 2018) *"Graph Attention Networks (GAT)"*.
> **Miền kiến thức**: [[deep-learning-overview|Geometric Deep Learning & Non-Euclidean Data]]
> **Tài liệu gốc liên quan**:
> - [Deep-Learning-on-Graphs.pdf](../../resources/deep-learning/Deep-Learning-on-Graphs.pdf) (Trang 1-60; 100-145)
> - [Deep Learning_Computer Vision_NLP.pdf](../../resources/deep-learning/Deep%20Learning_Computer%20Vision_NLP.pdf) (Trang 160-185)

---

## 1. Tóm tắt (Executive Summary)
**Mạng Nơ-ron Đồ thị (Graph Neural Networks - GNN)** là lớp mô hình học sâu được thiết kế để xử lý dữ liệu phi cấu trúc Euclid dạng đồ thị $\mathcal{G} = (\mathcal{V}, \mathcal{E})$, nơi các thực thể (nút - Nodes) liên kết với nhau qua các mối quan hệ (cạnh - Edges) bất đối xứng và không có trật tự cố định. Khác với CNN hay Transformer xử lý dữ liệu dạng mảng hay chuỗi tuần tự, GNN vận hành dựa trên cơ chế **Truyền tin (Message Passing Paradigm)**: mỗi nút tổng hợp thông tin đặc trưng từ tập hợp các nút láng giềng để cập nhật biểu diễn trạng thái của chính mình. GNN đóng vai trò cốt lõi trong phân tích mạng xã hội, hệ thống gợi ý (Recommender Systems), phát hiện gian lận tài chính, và thiết kế cấu trúc phân tử sinh hóa.

---

## 2. Định nghĩa chính thống & Khung Truyền tin (Message Passing Framework)

### 2.1 Khung Thông điệp Tổng quát (Gilmer et al., 2017)
Tại tầng thứ $k$ của mạng GNN, biểu diễn ẩn $h_u^{(k)}$ của nút $u$ được tính toán qua 3 bước:
1. **Message Function**: Tạo thông điệp từ nút láng giềng $v \in \mathcal{N}(u)$:
   $$m_{u,v}^{(k)} = \text{MSG}^{(k)}\left(h_u^{(k-1)}, \; h_v^{(k-1)}, \; e_{u,v}\right)$$
2. **Aggregation Function**: Tổng hợp các thông điệp từ toàn bộ láng giềng bằng một toán tử bất biến hoán vị (Permutation Invariant: Sum, Mean, Max):
   $$m_u^{(k)} = \text{AGG}^{(k)}\left( \left\{ m_{u,v}^{(k)} : v \in \mathcal{N}(u) \right\} \right)$$
3. **Update Function**: Cập nhật trạng thái mới của nút $u$:
   $$h_u^{(k)} = \text{UPDATE}^{(k)}\left( h_u^{(k-1)}, \; m_u^{(k)} \right)$$

```mermaid
flowchart TD
    N1["Neighbor Node v1"] --> M1["Message v1->u"]
    N2["Neighbor Node v2"] --> M2["Message v2->u"]
    N3["Neighbor Node v3"] --> M3["Message v3->u"]
    
    M1 --> Agg["Permutation Invariant Aggregator (Sum / Mean / Attention)"]
    M2 --> Agg
    M3 --> Agg
    
    Agg --> AggMsg["Aggregated Message m_u"]
    OldH["Old Node State h_u^(k-1)"] --> Update["Update Function (MLP + Non-linearity)"]
    AggMsg --> Update
    Update --> NewH["New Node Representation h_u^(k)"]
```

### 2.2 Các kiến trúc GNN tiêu biểu
1. **GCN (Graph Convolutional Networks - Kipf & Welling, 2017)**:
   - Xấp xỉ cấp 1 của tích chập phổ trên đồ thị:
     $$H^{(k+1)} = \sigma\left( \tilde{D}^{-\frac{1}{2}} \tilde{A} \tilde{D}^{-\frac{1}{2}} H^{(k)} W^{(k)} \right)$$
   - Trong đó $\tilde{A} = A + I_N$ là ma trận kề có thêm vòng tự liên kết (Self-loops), và $\tilde{D}_{ii} = \sum_j \tilde{A}_{ij}$ là ma trận bậc (Degree Matrix).
2. **GAT (Graph Attention Networks - Veličković et al., 2018)**:
   - Không coi mọi láng giềng đều có tầm quan trọng như nhau; GAT sử dụng cơ chế Self-Attention để học trọng số $\alpha_{ij}$ tự động giữa nút $i$ và nút $j$:
     $$\alpha_{ij} = \frac{\exp\left(\text{LeakyReLU}\left(\mathbf{a}^T [\mathbf{W}h_i \,\|\, \mathbf{W}h_j]\right)\right)}{\sum_{k \in \mathcal{N}(i)} \exp\left(\text{LeakyReLU}\left(\mathbf{a}^T [\mathbf{W}h_i \,\|\, \mathbf{W}h_k]\right)\right)}$$

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Thách thức lý thuyết | Bản chất kỹ thuật | Triệu chứng trong mô hình | Giải pháp của Kỹ sư AI |
| :--- | :--- | :--- | :--- |
| **Hiện tượng Làm mịn Quá mức (Over-smoothing)** | Khi số tầng GNN tăng lên quá sâu ($k > 4 - 8$), cơ chế truyền tin liên tục làm biểu diễn của mọi nút trong đồ thị hội tụ về cùng một vector trung bình giống hệt nhau. | Mô hình mất hoàn toàn khả năng phân biệt giữa các nút khác nhau; độ chính xác phân loại sụp đổ. | Sử dụng **Residual/Jumping Connections**, DropEdge, hoặc giới hạn độ sâu mạng chỉ từ 2 đến 3 tầng. |
| **Hiện tượng Nghẽn cổ chai Thông tin (Over-squashing)** | Khi đồ thị có cấu trúc hình học mở rộng theo hàm mũ (lượng láng giềng tăng vọt sau mỗi hop), việc nén thông tin từ hàng ngàn nút vào một vector kích thước cố định gây nghẽn thông tin. | Các nút ở khoảng cách xa không thể truyền tín hiệu hữu ích cho nhau. | Biến đổi cấu trúc đồ thị (Graph Rewiring), bổ sung các cạnh ảo (Virtual Nodes). |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy mô lớn (Scalability) trong Hệ thống Gợi ý (GraphSAGE)
- Trong các đồ thị thực tế (mạng xã hội hàng tỷ nút), phép nhân ma trận toàn cục của GCN là bất khả thi vì không thể nhét toàn bộ đồ thị vào RAM/GPU.
- **Giải pháp**: Thuật toán **GraphSAGE (Sample and Aggregate)**:
  - Thay vì lấy toàn bộ láng giềng, chỉ lấy mẫu ngẫu nhiên một số lượng láng giềng cố định (Uniform Sampling: e.g., lấy 10 láng giềng ở hop 1, 25 láng giềng ở hop 2).
  - Cho phép huấn luyện GNN theo từng mini-batch độc lập như mạng nơ-ron thông thường, mở khóa khả năng mở rộng trên các đồ thị quy mô Internet (Pinterest, Uber Eats).

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao toán tử tổng hợp (Aggregation Function) trong GNN bắt buộc phải là một hàm bất biến hoán vị (Permutation Invariant)?*
  - **A**: Đồ thị toán học là một tập hợp các nút và cạnh không có thứ tự tự nhiên (khác với câu văn có thứ tự từ trái sang phải, hoặc bức ảnh có tọa độ trên dưới). Nếu đổi chỗ vị trí của các hàng/cột trong ma trận kề (đổi tên nhãn nút), bản chất đồ thị vẫn không đổi (Graph Isomorphism). Do đó, toán tử tổng hợp từ tập láng giềng $\mathcal{N}(u)$ bắt buộc phải cho ra kết quả giống nhau bất kể thứ tự duyệt qua các láng giềng là gì (phép Sum, Mean, Max thỏa mãn điều này, trong khi hàm nối Concat hay LSTM phụ thuộc thứ tự sẽ thất bại).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[graph-rag]] — Ứng dụng đồ thị tri thức để mở rộng năng lực truy xuất của RAG.
- [[transformer-architecture]] — Transformer là trường hợp đặc biệt của GNN trên đồ thị đầy đủ (Fully-connected Graph).
- [[convolutional-neural-networks]] — So sánh đối chiếu giữa tích chập trên lưới Euclid và tích chập trên đồ thị phi Euclid.
"""
}

def generate():
    for filename, content in ENTITIES.items():
        filepath = WIKI_DIR / filename
        filepath.write_text(content.strip(), encoding="utf-8")
        print(f"Created: {filepath.name}")

if __name__ == "__main__":
    generate()
