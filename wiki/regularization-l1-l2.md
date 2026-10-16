# Kỹ Thuật Chính Quy Hóa L1 và L2 (Regularization: L1 Lasso & L2 Ridge)

> **Khái niệm chính thống**: *Mathematics for Machine Learning*, Chapter 9 (Section 9.3); *Understanding Machine Learning*, Chapter 13 (Regularization and Stability); *3 - Polynomial Regression and Regularizations.pdf*.
> **Miền kiến thức**: [[index|Machine Learning Optimization & Generalization]]
> **Tài liệu gốc liên quan**:
> - [3 - Polynomial Regression and Regularizations.pdf](../resources/machine-learning/3%20-%20Polynomial%20Regression%20and%20Regularizations.pdf) (Trang 1-27)
> - [Mathematics-for-Machine-Learning.pdf](../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) (Trang 305-315)
> - [understanding-machine-learning-theory-algorithms.pdf](../resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf) (Trang 165-180)

---

## 1. Tóm tắt (Executive Summary)
**Chính quy hóa (Regularization)** là tập hợp các kỹ thuật can thiệp vào hàm mục tiêu tối ưu hóa nhằm phạt độ phức tạp của mô hình, ngăn chặn hiện tượng quá khớp (Overfitting) và kiểm soát phương sai (Variance). Hai kỹ thuật chính quy hóa kinh điển và phổ quát nhất là **L1 Regularization (Lasso)** — phạt tổng giá trị tuyệt đối của trọng số, có khả năng triệt tiêu các trọng số thừa về chính xác 0 để thực hiện lựa chọn đặc trưng tự động (**Sparsity**); và **L2 Regularization (Ridge / Weight Decay)** — phạt tổng bình phương độ lớn trọng số, co cụm các trọng số về lân cận 0 để làm mượt mặt cong hàm quyết định và giải quyết hiện tượng đa cộng tuyến.

---

## 2. Định nghĩa chính thống & Bản chất Hình học (Geometry of Regularization)

### 2.1 Hàm Mục tiêu Tối ưu hóa
Cho hàm mất mát gốc $\mathcal{L}_0(\theta)$ (ví dụ MSE trong hồi quy tuyến tính):
1. **L2 Regularization (Ridge Regression / Tikhonov Regularization)**:
   $$\mathcal{L}_{\text{Ridge}}(\theta) = \frac{1}{N} \|y - X\theta\|_2^2 + \lambda \|\theta\|_2^2 = \frac{1}{N} \|y - X\theta\|_2^2 + \lambda \sum_{j=1}^D \theta_j^2$$
   - *Nghiệm giải tích đóng*:
     $$\hat{\theta}_{\text{Ridge}} = (X^T X + \lambda N I)^{-1} X^T y$$
   - Khi $\lambda > 0$, ma trận $(X^T X + \lambda N I)$ **luôn luôn xác định dương và khả nghịch tuyệt đối**, giải quyết triệt để rủi ro ma trận suy biến trong OLS.

2. **L1 Regularization (Lasso Regression - Tibshirani, 1996)**:
   $$\mathcal{L}_{\text{Lasso}}(\theta) = \frac{1}{N} \|y - X\theta\|_2^2 + \alpha \|\theta\|_1 = \frac{1}{N} \|y - X\theta\|_2^2 + \alpha \sum_{j=1}^D |\theta_j|$$
   - Hàm không khả vi tại $\theta_j = 0$; được tối ưu bằng giải thuật hạ dưới vi phân (Subgradient Descent) hoặc hạ tọa độ (Coordinate Descent).

```mermaid
flowchart LR
    subgraph L1 Geometry (Lasso)
        L1_Contour["Loss Contours (Ellipses)"] --> L1_Hit["Intersects L1 Diamond at Corners (θ₁ = 0)"]
        L1_Hit --> Sparse["Sparse Solution (Feature Selection)"]
    end
    
    subgraph L2 Geometry (Ridge)
        L2_Contour["Loss Contours (Ellipses)"] --> L2_Hit["Intersects L2 Sphere Smoothly (θ ≈ 0)"]
        L2_Hit --> Shrink["Weight Decay / Smooth Coefficients"]
    end
```

### 2.2 Tại sao L1 tạo ra Tính Thưa thớt (Sparsity) còn L2 thì không?
- Dưới góc độ bài toán tối ưu hóa ràng buộc Karush-Kuhn-Tucker (KKT):
  - Ràng buộc L1 có dạng **hình thoi (Diamond / Cross-polytope)** với các đỉnh nhọn nằm chính xác trên các trục tọa độ $\theta_j$.
  - Ràng buộc L2 có dạng **hình cầu tròn (Hypersphere)** mượt mà, không có góc nhọn.
- Các đường đồng mức elip của hàm mất mát $\mathcal{L}_0$ khi phình to ra từ tâm nghiệm OLS có xác suất hình học cực cao chạm vào **các đỉnh nhọn của hình thoi L1 trước tiên**. Tại các đỉnh nhọn này, một hoặc nhiều tọa độ $\theta_j$ có giá trị bằng 0 tuyệt đối. Ngược lại, quả cầu L2 chỉ tiếp xúc tại các điểm mượt mà, khiến các trọng số bị thu nhỏ nhưng hầu như không bao giờ triệt tiêu về 0 hoàn toàn.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Tiêu chí | L1 Regularization (Lasso) | L2 Regularization (Ridge) | Elastic Net |
| :--- | :--- | :--- | :--- |
| **Chỉ tiêu phạt** | Chuẩn $L_1$: $\sum |\theta_j|$. | Chuẩn $L_2^2$: $\sum \theta_j^2$. | Kết hợp lồi: $r L_1 + (1-r) L_2$. |
| **Tính chất nghiệm** | Thưa thớt (Sparse). Tự động loại bỏ feature vô dụng. | Dày đặc (Dense). Giữ lại mọi feature nhưng ép nhỏ hệ số. | Cân bằng: Vừa tạo sparsity vừa nhóm các feature tương quan. |
| **Độ nhạy với dữ liệu đa cộng tuyến** | Thường chọn ngẫu nhiên 1 feature trong nhóm feature tương quan cao và bỏ qua các feature còn lại. | Giữ lại toàn bộ nhóm feature tương quan và chia đều trọng số cho chúng. | Khắc phục điểm yếu của Lasso: Chọn toàn bộ nhóm feature tương quan cùng nhau. |
| **Trong Deep Learning** | Ít dùng trực tiếp lên trọng số mạng nơ-ron sâu. | **Tiêu chuẩn vàng**: Được biết đến với tên gọi **Weight Decay**. | Tùy biến trong một số kiến trúc chuyên biệt. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Weight Decay vs L2 Regularization trong PyTorch / Adam
Một chi tiết kỹ thuật mà rất nhiều kỹ sư bị nhầm lẫn trong các buổi phỏng vấn:
- Trong thuật toán **SGD chuẩn**, L2 Regularization và Weight Decay tương đương toán học tuyệt đối.
- Nhưng trong **Adam (Adaptive Moment Estimation)**, việc cộng thêm đạo hàm của L2 vào gradient làm sai lệch việc ước lượng moment bậc 2 ($v_t$), khiến các trọng số có gradient lịch sử lớn bị phạt ít hơn các trọng số có gradient nhỏ (phản trực giác).
- **Giải pháp**: Phải sử dụng **AdamW (Loshchilov & Hutter, 2019)**: Tách rời (Decoupled) số hạng Weight Decay trực tiếp ra khỏi bước cập nhật gradient thích ứng:
  $$\theta_{t+1} = \theta_t - \eta_t \cdot \lambda \theta_t - \frac{\eta_t}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Dưới góc nhìn Xác suất Bayes (Bayesian Perspective), L1 và L2 Regularization tương đương với việc đặt phân phối tiên nghiệm (Prior Distribution) nào lên trọng số?*
  - **A**:
    - **L2 Regularization (Ridge)** tương đương với ước lượng Maximum A Posteriori (**MAP**) với phân phối tiên nghiệm là **Phân phối Chuẩn Gaussian Prior**: $\theta \sim \mathcal{N}(0, \tau^2)$.
    - **L1 Regularization (Lasso)** tương đương với ước lượng **MAP** với phân phối tiên nghiệm là **Phân phối Laplace Prior**: $\theta \sim \text{Laplace}(0, b)$. Đồ thị phân phối Laplace có đỉnh nhọn sắc bén tại 0, giải thích nguồn gốc xác suất vì sao L1 thúc đẩy các trọng số tập trung về 0 tuyệt đối.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & `wiki-links`)
- [[linear-regression-mle]] — Nền tảng áp dụng chính quy hóa L1/L2.
- [[bias-variance-tradeoff]] — Regularization là công cụ trực tiếp để giảm Variance và kiểm soát Overfitting.
- [[optimization-algorithms]] — Sự khác biệt giữa L2 trong Adam vs AdamW.
- [[principal-component-analysis]] — Phương pháp giảm số chiều thay thế cho L1 feature selection.