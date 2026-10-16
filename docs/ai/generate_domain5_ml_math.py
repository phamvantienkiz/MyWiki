# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = Path("wiki")
WIKI_DIR.mkdir(parents=True, exist_ok=True)

ENTITIES = {
    "linear-regression-mle.md": r"""# Hồi Quy Tuyến Tính và Ước Lượng Hợp Lý Cực Đại (Linear Regression & MLE)

> **Khái niệm chính thống**: *Mathematics for Machine Learning* (Deisenroth et al., Cambridge), Chapter 9; *Understanding Machine Learning* (Shalev-Shwartz & Ben-David), Chapter 9; *03_LinearRegression-with-MLE.pdf*.
> **Miền kiến thức**: [[ml-math-overview|Machine Learning & Statistical Foundations]]
> **Tài liệu gốc liên quan**:
> - [Mathematics-for-Machine-Learning.pdf](../../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) (Trang 289-320)
> - [03_LinearRegression-with-MLE.pdf](../../resources/machine-learning/03_LinearRegression-with-MLE.pdf) (Trang 1-22)
> - [understanding-machine-learning-theory-algorithms.pdf](../../resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf) (Trang 115-130)
> - [AIO2026_Reading-LinearRegression.pdf](../../resources/machine-learning/AIO2026_Reading-LinearRegression.pdf) (Trang 1-49)

---

## 1. Tóm tắt (Executive Summary)
**Hồi quy Tuyến tính (Linear Regression)** là mô hình học có giám sát nền tảng thiết lập mối quan hệ tuyến tính giữa biến đầu vào $x \in \mathbb{R}^D$ và biến mục tiêu liên tục $y \in \mathbb{R}$. Về mặt hình học, hồi quy tìm kiếm siêu phẳng tối ưu hóa khoảng cách bình phương nhỏ nhất (**Ordinary Least Squares - OLS**). Về mặt xác suất thống kê, OLS được chứng minh tương đương toán học tuyệt đối với việc tìm kiếm bộ tham số tối đa hóa hàm hợp lý (**Maximum Likelihood Estimation - MLE**) dưới giả định rằng nhiễu quan sát tuân theo phân phối chuẩn Gaussian với kỳ vọng bằng 0.

---

## 2. Định nghĩa chính thống & Dẫn xuất Toán học (Mathematical Derivation)

### 2.1 Mô hình Xác suất và Giả định Nhiễu Gaussian
Mô hình quan sát thực tế được biểu diễn bởi:
$$y = x^T \theta + \epsilon, \quad \epsilon \sim \mathcal{N}(0, \sigma^2)$$
Do đó, phân phối có điều kiện của biến mục tiêu $y$ khi biết $x$ là:
$$P(y \mid x; \theta, \sigma^2) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( - \frac{(y - x^T \theta)^2}{2\sigma^2} \right)$$

Cho tập dữ liệu gồm $N$ mẫu độc lập cùng phân phối (i.i.d.) $\mathcal{D} = \{(x_n, y_n)\}_{n=1}^N$, hàm hợp lý (Likelihood Function) là:
$$L(\theta) = \prod_{n=1}^N P(y_n \mid x_n; \theta) = \left( \frac{1}{\sqrt{2\pi \sigma^2}} \right)^N \exp\left( - \frac{1}{2\sigma^2} \sum_{n=1}^N (y_n - x_n^T \theta)^2 \right)$$

Lấy logarit tự nhiên để thu được hàm Log-Likelihood:
$$\log L(\theta) = - \frac{N}{2} \log(2\pi \sigma^2) - \frac{1}{2\sigma^2} \sum_{n=1}^N (y_n - x_n^T \theta)^2$$
Để tối đa hóa $\log L(\theta)$ theo $\theta$, ta cần tối thiểu hóa phần dư bình phương:
$$\hat{\theta}_{\text{MLE}} = \arg\min_\theta \sum_{n=1}^N (y_n - x_n^T \theta)^2 = \arg\min_\theta \|y - X\theta\|_2^2$$
*(Chứng minh hoàn tất: MLE với nhiễu Gaussian đồng nhất với phương pháp bình phương tối thiểu OLS).*

```mermaid
flowchart LR
    Prob["Gaussian Noise Assumption: ε ~ N(0, σ²)"] --> LogL["Log-Likelihood Maximization"]
    LogL --> NegMSE["Minimize Sum of Squared Residuals ||y - Xθ||²"]
    NegMSE --> NormalEq["Closed-form Normal Equation: θ* = (XᵀX)⁻¹ Xᵀy"]
    NormalEq --> Grad["Or Iterative Gradient Descent for Big Data"]
```

### 2.2 Nghiệm đóng Phương trình Chuẩn tắc (Normal Equation)
Đặt gradient của hàm mất mát $\|y - X\theta\|_2^2$ theo $\theta$ bằng 0:
$$\nabla_\theta \left( y^T y - 2 \theta^T X^T y + \theta^T X^T X \theta \right) = -2 X^T y + 2 X^T X \theta = 0$$
$$\Rightarrow X^T X \theta = X^T y$$
Khi ma trận Gram $X^T X$ khả nghịch (các thuộc tính độc lập tuyến tính):
$$\hat{\theta}_{\text{OLS}} = (X^T X)^{-1} X^T y$$

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Phương pháp giải | Độ phức tạp thời gian | Khả năng mở rộng (Scalability) | Yêu cầu chuẩn hóa thuộc tính (Feature Scaling) |
| :--- | :--- | :--- | :--- |
| **Nghiệm đóng (Normal Equation)** | $\mathcal{O}(D^3)$ do phép nghịch đảo ma trận $D \times D$. | Rất kém khi số thuộc tính $D > 10.000$ (tràn RAM). | **Không cần**. Cho ra kết quả giải tích chính xác tức thì. |
| **Gradient Descent (GD / SGD)** | $\mathcal{O}(k \cdot N \cdot D)$ với $k$ là số vòng lặp. | Xuất sắc cho Big Data (hàng triệu mẫu $N$ lớn). | **Bắt buộc**. Nếu không chuẩn hóa, mặt cong hàm mất mát sẽ bị méo elip khiến gradient dao động dữ dội và chậm hội tụ. |
| **Phân tích SVD / Pseudo-inverse** | $\mathcal{O}(N D^2)$. | Ổn định số học hơn Normal Equation khi $X^T X$ suy biến (Singular / Collinear). | Khuyến nghị cho bài toán đa cộng tuyến. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Bẫy Đa cộng tuyến (Multicollinearity Trap)
- Khi hai hay nhiều biến giải thích có tương quan rất cao với nhau (ví dụ: `chiều cao (cm)` và `chiều cao (m)`), ma trận $X^T X$ có định thức $\det(X^T X) \approx 0$ (gần như suy biến).
- **Hậu quả**: Nghiệm nghịch đảo $(X^T X)^{-1}$ có phương sai cực đại; các trọng số $\theta$ bị thổi phồng lên hàng triệu lần và đổi dấu bất thường, khiến mô hình mất hoàn toàn tính ổn định.
- **Giải pháp**:
  1. Kiểm tra hệ số phóng đại phương sai **VIF (Variance Inflation Factor)**; loại bỏ biến có $\text{VIF} > 5 - 10$.
  2. Bổ sung số hạng chính quy hóa [[regularization-l1-l2|L2 Ridge Regularization]]: $(X^T X + \lambda I)^{-1}$ luôn luôn khả nghịch!

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Định lý Gauss-Markov khẳng định điều gì về ước lượng OLS trong Hồi quy Tuyến tính?*
  - **A**: Định lý Gauss-Markov chứng minh rằng: Dưới các giả định cổ điển (sai số có kỳ vọng bằng 0, phương sai đồng nhất - homoscedasticity, và không tự tương quan), ước lượng OLS là **BLUE (Best Linear Unbiased Estimator)** — nghĩa là trong tất cả các ước lượng tuyến tính và không chệch, ước lượng OLS có phương sai nhỏ nhất (tối ưu nhất về độ phân tán).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[bias-variance-tradeoff]] — Đánh giá sự cân bằng giữa độ chệch và phương sai trong hồi quy.
- [[regularization-l1-l2]] — L1 Lasso và L2 Ridge khắc phục hiện tượng đa cộng tuyến và quá khớp.
- [[optimization-algorithms]] — Giải thuật Gradient Descent để tìm nghiệm hồi quy trên tập dữ liệu lớn.
- [[principal-component-analysis]] — Phương pháp chiếu giảm chiều giải quyết đa cộng tuyến trước khi hồi quy.
""",

    "bias-variance-tradeoff.md": r"""# Sự Đánh Đổi Giữa Độ Chệch và Phương Sai (Bias-Variance Tradeoff)

> **Khái niệm chính thống**: *Understanding Machine Learning* (Shalev-Shwartz & Ben-David), Chapter 5; *Mathematics for Machine Learning*, Chapter 8; *Bias-Variance_Tradeoff.pdf*.
> **Miền kiến thức**: [[ml-math-overview|Learning Theory & Generalization]]
> **Tài liệu gốc liên quan**:
> - [Bias-Variance_Tradeoff.pdf](../../resources/machine-learning/Bias-Variance_Tradeoff.pdf) (Trang 1-71)
> - [understanding-machine-learning-theory-algorithms.pdf](../../resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf) (Trang 45-65)
> - [Machinelearningyearning-Vi.pdf](../../resources/machine-learning/Machinelearningyearning-Vi.pdf) (Trang 15-40)
> - [847999051_122320901954195094_4534131503073995411_n.jpg](../../resources/images/847999051_122320901954195094_4534131503073995411_n.jpg) (Infographic 4: Xử lý khi model sai)

---

## 1. Tóm tắt (Executive Summary)
**Sự đánh đổi giữa Độ chệch và Phương sai (Bias-Variance Tradeoff)** là định luật bảo toàn cốt lõi trong lý thuyết học máy mô tả mối quan hệ mâu thuẫn giữa hai nguồn sai số có thể kiểm soát được cấu thành nên lỗi kỳ vọng tổng thể của mô hình. **Độ chệch cao (High Bias)** phản ánh một mô hình quá đơn giản, bỏ sót các quy luật tiềm ẩn trong dữ liệu (**Hiện tượng Chưa khớp - Underfitting**). Ngược lại, **Phương sai cao (High Variance)** phản ánh một mô hình quá phức tạp, học vẹt cả các biến động ngẫu nhiên và nhiễu của tập huấn luyện (**Hiện tượng Quá khớp - Overfitting**). Mục tiêu của kỹ sư học máy là điều chỉnh độ phức tạp mô hình để tối thiểu hóa tổng sai số tổng quát hóa (Generalization Error).

---

## 2. Định nghĩa chính thống & Khai triển Toán học (Mathematical Decomposition)

### 2.1 Khai triển Sai số Dự đoán Kỳ vọng (Expected Prediction Error)
Giả sử dữ liệu sinh ra từ quan hệ: $y = f(x) + \epsilon$, với nhiễu $\mathbb{E}[\epsilon] = 0$ và $\text{Var}(\epsilon) = \sigma^2$.
Cho mô hình ước lượng $\hat{f}(x)$ được huấn luyện trên tập dữ liệu ngẫu nhiên $\mathcal{D}$.
Sai số bình phương kỳ vọng (Mean Squared Error - MSE) tại điểm kiểm tra $x_0$:
$$\text{MSE}(x_0) = \mathbb{E}_{\mathcal{D}, \epsilon} \left[ \left( y - \hat{f}(x_0) \right)^2 \right]$$

Khai triển đại số:
$$\text{MSE}(x_0) = \mathbb{E} \left[ \left( (f(x_0) + \epsilon) - \hat{f}(x_0) \right)^2 \right]$$
$$= \mathbb{E} \left[ \left( (f(x_0) - \mathbb{E}[\hat{f}(x_0)]) + (\mathbb{E}[\hat{f}(x_0)] - \hat{f}(x_0)) + \epsilon \right)^2 \right]$$

Do $\epsilon$ độc lập với $\hat{f}$, các số hạng tích chéo có kỳ vọng bằng 0, dẫn tới công thức phân rã tam phân kinh điển:
$$\text{MSE}(x_0) = \underbrace{\left( f(x_0) - \mathbb{E}[\hat{f}(x_0)] \right)^2}_{\text{Bias}^2(\hat{f}(x_0))} + \underbrace{\mathbb{E}\left[ \left( \hat{f}(x_0) - \mathbb{E}[\hat{f}(x_0)] \right)^2 \right]}_{\text{Variance}(\hat{f}(x_0))} + \underbrace{\sigma^2}_{\text{Irreducible Error}}$$

```mermaid
flowchart TD
    TotalError["Total Expected Error = Bias² + Variance + Noise"]
    TotalError --> Bias["Bias² (Underfitting / High Training Error)"]
    TotalError --> Variance["Variance (Overfitting / High Val-Train Gap)"]
    TotalError --> Noise["Irreducible Noise σ² (Inherent Data Noise)"]
    
    subgraph Diagnosis & Remedies
        Bias -->|"Fix High Bias"| FixB["Increase Capacity, Add Features, Weaken Regularization"]
        Variance -->|"Fix High Variance"| FixV["Add Data, Feature Selection, L1/L2 Regularization, Dropout"]
    end
```

---

## 3. So sánh & Mâu thuẫn / Sắc thái: Hiện tượng "Double Descent" trong Học Sâu

| Khía cạnh | Học máy Thống kê Cổ điển (Classical ML) | Học sâu Hiện đại (Deep Learning - Double Descent) |
| :--- | :--- | :--- |
| **Đường cong sai số kiểm tra** | **Dạng chữ U (U-shaped Curve)**: Khi tăng số tham số, sai số giảm đến điểm tối ưu rồi tăng vọt trở lại do Overfitting. | **Suy giảm Kép (Double Descent - Belkin et al., 2019)**: Vượt qua ngưỡng nội suy (Interpolation Threshold), sai số kiểm tra **giảm lần thứ hai**! |
| **Cơ chế hoạt động** | Cần giới hạn số tham số $P < N$ (số tham số nhỏ hơn số mẫu dữ liệu) để tránh Overfitting. | Mạng cực lớn (Overparameterized Regimes: $P \gg N$ như LLM) tìm thấy nghiệm có chuẩn nhỏ nhất (Minimum-norm interpolator), giúp tổng quát hóa vượt trội. |
| **Ứng dụng thực tiễn** | Bắt buộc phải cân bằng chặt chẽ siêu tham số $k$ trong k-NN, độ sâu cây quyết định. | Với Deep Learning, việc mở rộng quy mô (Scale up model size) thường mang lại hiệu năng cao hơn mô hình vừa vặn. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy trình Chẩn đoán của Andrew Ng (Machine Learning Yearning)
Khi đánh giá mô hình, hãy so sánh:
1. **Lỗi con người (Human-level / Bayes Error)**: Giả sử $1\%$.
2. **Lỗi tập Train (Training Error)**:
   - Nếu Train Error = $15\% \rightarrow$ **High Bias (Underfitting)**. *Hành động*: Tăng kích thước mạng, thêm feature mới, giảm regularization.
3. **Lỗi tập Dev / Val (Validation Error)**:
   - Nếu Train Error = $2\%$, nhưng Val Error = $12\% \rightarrow$ **High Variance (Overfitting)**. *Hành động*: Thu thập thêm dữ liệu gán nhãn, thêm [[regularization-l1-l2|L1/L2]], áp dụng Data Augmentation.

### 4.2 Triết lý "Nếu Model sai thì sao?" (Từ Infographic 847999051)
- **Người yếu**: Thường vội vã trả lời *"Train lại model đi anh!"*.
- **Người giỏi**: Hỏi ngược lại: *Sai ở mức nào và sai số đó có chấp nhận được trong bối cảnh nghiệp vụ không?*
  - **Slicing Data**: Phân tích lỗi theo từng phân khúc khách hàng (Error Analysis by Slices). Model có thể đạt độ chính xác chung 85% nhưng lại sai tới 60% trên nhóm khách hàng VIP.
  - **Fail-safe Mechanism**: Không có model nào đúng 100%. Cần xây dựng cơ chế kiểm soát rủi ro (Risk Control) và bẫy lỗi tự động thay vì né tránh sự thật.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[linear-regression-mle]] — Ví dụ minh họa trực quan nhất cho sự phân rã sai số.
- [[regularization-l1-l2]] — Vũ khí kỹ thuật trực tiếp để ghìm cương Variance.
- [[model-selection-evaluation]] — Chiến lược chia tách dữ liệu để đo lường chính xác Bias và Variance.
- [[gradient-vanishing-exploding]] — Rào cản ngăn cản mô hình giảm Bias khi tăng chiều sâu mạng.
""",

    "regularization-l1-l2.md": r"""# Kỹ Thuật Chính Quy Hóa L1 và L2 (Regularization: L1 Lasso & L2 Ridge)

> **Khái niệm chính thống**: *Mathematics for Machine Learning*, Chapter 9 (Section 9.3); *Understanding Machine Learning*, Chapter 13 (Regularization and Stability); *3 - Polynomial Regression and Regularizations.pdf*.
> **Miền kiến thức**: [[ml-math-overview|Machine Learning Optimization & Generalization]]
> **Tài liệu gốc liên quan**:
> - [3 - Polynomial Regression and Regularizations.pdf](../../resources/machine-learning/3%20-%20Polynomial%20Regression%20and%20Regularizations.pdf) (Trang 1-27)
> - [Mathematics-for-Machine-Learning.pdf](../../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) (Trang 305-315)
> - [understanding-machine-learning-theory-algorithms.pdf](../../resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf) (Trang 165-180)

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

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[linear-regression-mle]] — Nền tảng áp dụng chính quy hóa L1/L2.
- [[bias-variance-tradeoff]] — Regularization là công cụ trực tiếp để giảm Variance và kiểm soát Overfitting.
- [[optimization-algorithms]] — Sự khác biệt giữa L2 trong Adam vs AdamW.
- [[principal-component-analysis]] — Phương pháp giảm số chiều thay thế cho L1 feature selection.
""",

    "gradient-vanishing-exploding.md": r"""# Vấn Đề Triệt Tiêu và Bùng Nổ Gradient (Vanishing & Exploding Gradients)

> **Khái niệm chính thống**: *The Principles of Deep Learning Theory* (Roberts & Yaida, Cambridge), Chapter 3; Bengio et al. (1994) *"Learning long-term dependencies with gradient descent is difficult"*; Glorot & Bengio (AISTATS 2010) *"Xavier Initialization"*; He et al. (ICCV 2015) *"He / Kaiming Initialization"*.
> **Miền kiến thức**: [[ml-math-overview|Deep Learning Theory & Backpropagation Dynamics]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_GradientVanishing.pdf](../../resources/deep-learning/computer-vision/AIO2025_GradientVanishing.pdf) (Trang 1-35)
> - [\[Description_v1\]-Project-Vanishing-gradient-problem.pdf](../../resources/machine-learning/%5BDescription_v1%5D-Project-Vanishing-gradient-problem.pdf) (Trang 1-38)
> - [The-Principles-of-Deep-Learning-Theory.pdf](../../resources/deep-learning/The-Principles-of-Deep-Learning-Theory.pdf) (Trang 35-50)

---

## 1. Tóm tắt (Executive Summary)
**Vấn đề Triệt tiêu Gradient (Vanishing Gradient)** và **Bùng nổ Gradient (Exploding Gradient)** là hai căn bệnh kinh niên cản trở việc huấn luyện các mạng nơ-ron sâu trong nhiều thập kỷ. Xuất phát từ bản chất toán học của **Quy tắc Chuỗi (Chain Rule)** trong thuật toán Lan truyền ngược (Backpropagation), gradient của hàm mất mát truyền ngược từ tầng cuối về các tầng đầu tiên là tích liên tiếp của các ma trận trọng số và đạo hàm hàm kích hoạt. Khi các thành phần nhân tử nhỏ hơn 1, gradient suy giảm theo hàm mũ về 0 khiến các tầng đầu tiên ngừng học hoàn toàn. Ngược lại, khi các nhân tử lớn hơn 1, gradient bùng nổ vô tận làm mất ổn định số học (`NaN/Inf`).

---

## 2. Định nghĩa chính thống & Dẫn xuất Toán học (Mathematical Analysis)

### 2.1 Bản chất Quy tắc Chuỗi trong Mạng Sâu $L$ Tầng
Xét mạng nơ-ron truyền thẳng gồm $L$ tầng: $z^{(l)} = W^{(l)} a^{(l-1)} + b^{(l)}$, với $a^{(l)} = \sigma(z^{(l)})$.
Đạo hàm của hàm mất mát $\mathcal{L}$ đối với trọng số của tầng đầu tiên $W^{(1)}$:
$$\frac{\partial \mathcal{L}}{\partial W^{(1)}} = \frac{\partial \mathcal{L}}{\partial z^{(L)}} \left[ \prod_{l=2}^L \frac{\partial z^{(l)}}{\partial z^{(l-1)}} \right] \frac{\partial z^{(1)}}{\partial W^{(1)}}$$

Trong đó ma trận Jacobian chuyển tiếp giữa hai tầng liên tiếp là:
$$\frac{\partial z^{(l)}}{\partial z^{(l-1)}} = W^{(l)} \cdot \text{diag}\left( \sigma'(z^{(l-1)}) \right)$$
Do đó, độ lớn của gradient chịu sự chi phối của tích ma trận:
$$\frac{\partial \mathcal{L}}{\partial W^{(1)}} \propto \prod_{l=2}^L W^{(l)} \cdot \sigma'(z^{(l-1)})$$

```mermaid
flowchart RL
    Loss["Loss L"] -->|"dL/dzL"| LayerL["Layer L"]
    LayerL -->|"x W^L * σ'"| LayerMid["Intermediate Layers..."]
    LayerMid -->|"Product of L-1 Terms"| Layer1["Layer 1"]
    
    subgraph Collapse Modes
        Layer1 -->|"If Terms < 1: Exponential Decay"| Vanish["Vanishing Gradient (dL/dW1 -> 0, Early Layers Freeze)"]
        Layer1 -->|"If Terms > 1: Exponential Growth"| Explode["Exploding Gradient (dL/dW1 -> Inf/NaN, Weight Oscillation)"]
    end
```

### 2.2 Tử huyệt của Hàm Kích hoạt Sigmoid và Tanh
- Đạo hàm của hàm Sigmoid $\sigma(z) = \frac{1}{1 + e^{-z}}$ là:
  $$\sigma'(z) = \sigma(z)(1 - \sigma(z))$$
  Giá trị cực đại của $\sigma'(z)$ đạt được tại $z = 0$, nhưng cũng chỉ bằng **$0.25$**.
- Khi mạng có 10 tầng sử dụng Sigmoid: $(0.25)^{10} \approx 9.5 \times 10^{-7}$.
- Tín hiệu gradient truyền về tầng đầu tiên bị teo nhỏ gần một triệu lần, khiến việc cập nhật trọng số ở các tầng trích xuất đặc trưng cơ sở hoàn toàn bị đóng băng!

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Phương diện | Giải pháp Lịch sử (Trước 2015) | Giải pháp Kiến trúc Hiện đại (2016-2026) | Nhận định Kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Hàm kích hoạt (Activations)** | Sigmoid, Tanh (bị bão hòa ở hai đầu cực trị). | **ReLU, LeakyReLU, GeLU, SwiGLU**. | $\text{ReLU}'(z) = 1$ khi $z > 0$, triệt tiêu hoàn toàn sự suy hao gradient qua hàm kích hoạt. |
| **Khởi tạo trọng số (Weight Init)** | Khởi tạo ngẫu nhiên nhỏ $\mathcal{N}(0, 0.01^2)$ hoặc đồng đều thô sơ. | **He (Kaiming) Normal** cho ReLU; **Xavier (Glorot)** cho Sigmoid/Tanh. | Bảo toàn phương sai của kích hoạt và gradient qua từng tầng: $\text{Var}(W) = \frac{2}{n_{in}}$ cho He Init. |
| **Cấu trúc mạng (Architecture)** | Mạng truyền thẳng tuần tự đơn thuần. | **Residual Skip Connections (ResNet)** và **LayerNorm / RMSNorm**. | Skip connection tạo ra đường truyền tắt với gradient bằng 1; LayerNorm tái chuẩn hóa kích hoạt về phân phối chuẩn ổn định. |
| **Chống bùng nổ gradient** | Giảm learning rate xuống cực nhỏ khiến mạng học rất chậm. | **Gradient Clipping** ($\|\mathbf{g}\| \leftarrow \min(1, \frac{c}{\|\mathbf{g}\|}) \mathbf{g}$). | Cắt tỉa biên độ vector gradient khi vượt ngưỡng mà không làm thay đổi hướng vector. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 "Dying ReLU" và cách khắc phục
- **Vấn đề "ReLU Chết"**: Nếu một neuron bị rơi vào trạng thái $z < 0$ với toàn bộ tập dữ liệu, đạo hàm của nó luôn bằng 0: $\text{ReLU}'(z) = 0$. Trọng số không bao giờ được cập nhật nữa và neuron đó "chết vĩnh viễn".
- **Giải pháp**:
  1. Sử dụng **LeakyReLU** ($\sigma(z) = \max(\alpha z, z)$ với $\alpha = 0.01$) hoặc **GELU / SiLU** trong các mô hình Transformer hiện đại.
  2. Tuyệt đối không đặt Learning Rate quá lớn ở giai đoạn đầu; luôn sử dụng kỹ thuật **Learning Rate Warmup**.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao phép khởi tạo Xavier Init lại thất bại đối với hàm kích hoạt ReLU, và công thức He (Kaiming) Init đã sửa đổi điều đó như thế nào?*
  - **A**: Xavier Init dựa trên giả định hàm kích hoạt là tuyến tính quanh 0 với đạo hàm bằng 1, từ đó suy ra phương sai cần thiết là $\text{Var}(W) = \frac{2}{n_{in} + n_{out}}$. Tuy nhiên, ReLU triệt tiêu hoàn toàn nửa trục âm ($z < 0$), tức là làm biến mất 50% số lượng neuron ở mỗi tầng. Kaiming He nhận ra điều này và bù đắp bằng cách nhân đôi phương sai: $\text{Var}(W) = \frac{2}{n_{in}}$, giúp duy trì phương sai của tín hiệu truyền xuôi và gradient truyền ngược ổn định không đổi qua hàng trăm tầng mạng.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[convolutional-neural-networks]] — ResNet được thiết kế trực tiếp để khắc phục vanishing gradient.
- [[transformer-architecture]] — Sử dụng Pre-LN và Residual Connections để huấn luyện mạng sâu.
- [[optimization-algorithms]] — Các bộ tối ưu hóa thích ứng kết hợp Gradient Clipping.
- [[linear-regression-mle]] — Trường hợp tuyến tính đơn giản không gặp vấn đề triệt tiêu gradient.
""",

    "optimization-algorithms.md": r"""# Các Thuật Toán Tối Ưu Hóa (Optimization: SGD, Adam, AdamW & Schedules)

> **Khái niệm chính thống**: *Mathematics for Machine Learning*, Chapter 7 (Continuous Optimization); *Understanding Machine Learning*, Chapter 14; Kingma & Ba (ICLR 2015) *"Adam: A Method for Stochastic Optimization"*; Loshchilov & Hutter (ICLR 2019) *"Decoupled Weight Decay Regularization (AdamW)"*.
> **Miền kiến thức**: [[ml-math-overview|Optimization & Deep Learning Training]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_[Description]_Optimizer.pdf](../../resources/machine-learning/AIO2025_%5BDescription%5D_Optimizer.pdf) (Trang 1-29)
> - [Mathematics-for-Machine-Learning.pdf](../../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) (Trang 230-265)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 27-28; 86-88)

---

## 1. Tóm tắt (Executive Summary)
**Các thuật toán Tối ưu hóa (Optimization Algorithms)** là động cơ thúc đẩy toàn bộ quá trình học máy và học sâu, có nhiệm vụ điều chỉnh trọng số mô hình $\theta$ để tìm kiếm cực tiểu của hàm mất mát thực nghiệm $\mathcal{L}(\theta)$. Bắt đầu từ thuật toán cổ điển **Hạ Gradient Ngẫu nhiên (SGD)** với nhược điểm hội tụ chậm ở vùng yên ngựa và thung lũng hẹp, các giải thuật tích lũy động lượng (**Momentum**, **Nesterov**) và tốc độ học thích ứng theo từng tham số (**RMSprop**, **Adam**) đã ra đời. Trong kỷ nguyên LLM hiện đại, **AdamW (Decoupled Weight Decay)** kết hợp với biểu đồ tốc độ học **Cosine Annealing with Warmup** đã trở thành tiêu chuẩn vàng không thể thay thế.

---

## 2. Định nghĩa chính thống & Dẫn xuất Thuật toán (Algorithmic Formulations)

### 2.1 Cây phả hệ tiến hóa của các Bộ tối ưu hóa
1. **SGD with Momentum**:
   Tích lũy vận tốc động lượng theo moment bậc 1 để vượt qua các cực tiểu cục bộ và giảm rung lắc:
   $$v_t = \beta v_{t-1} + (1 - \beta) g_t$$
   $$\theta_t = \theta_{t-1} - \eta v_t$$
2. **RMSprop (Root Mean Square Propagation - Hinton, 2012)**:
   Điều chỉnh learning rate riêng cho từng tham số bằng cách chia cho căn bậc hai của trung bình trượt bình phương gradient (moment bậc 2):
   $$s_t = \gamma s_{t-1} + (1 - \gamma) g_t^2$$
   $$\theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{s_t} + \epsilon} \odot g_t$$
3. **Adam (Adaptive Moment Estimation - Kingma & Ba, 2015)**:
   Kết hợp cả Momentum (quán tính) và RMSprop (thích ứng từng chiều), kèm bước hiệu chỉnh thiên kiến (Bias Correction) ở các bước đầu:
   $$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t, \quad v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$
   $$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}, \quad \hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$
   $$\theta_t = \theta_{t-1} - \frac{\eta}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$

```mermaid
flowchart TD
    Grad["Gradient g_t"] --> Mom["First Moment m_t (Momentum: Direction)"]
    Grad --> Var["Second Moment v_t (RMSprop: Adaptive Scale)"]
    Mom --> CorrectM["Bias Correction m_hat"]
    Var --> CorrectV["Bias Correction v_hat"]
    CorrectM --> Combine["Adaptive Update Step"]
    CorrectV --> Combine
    WeightDecay["Decoupled Weight Decay (-η * λ * θ)"] --> FinalUpdate["AdamW Weight Update"]
    Combine --> FinalUpdate
```

### 2.2 Đột phá AdamW (Loshchilov & Hutter, 2019)
Trong Adam truyền thống, số hạng L2 Regularization được cộng thẳng vào gradient ($g_t \leftarrow g_t + \lambda \theta$). Khi đi qua phép chia $\sqrt{\hat{v}_t}$, tham số nào có gradient lớn sẽ bị phạt chính quy hóa ít hơn, làm mất đi ý nghĩa toán học của Weight Decay.
**AdamW sửa sai**: Tách rời hoàn toàn bước phạt suy giảm trọng số khỏi bước gradient thích ứng:
$$\theta_t = \theta_{t-1} - \eta_t \lambda \theta_{t-1} - \frac{\eta_t}{\sqrt{\hat{v}_t} + \epsilon} \hat{m}_t$$

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Thuật toán | Tốc độ hội tụ lúc đầu | Khả năng tổng quát hóa (Generalization) cuối cùng | Bộ nhớ GPU tiêu thụ | Lĩnh vực thống trị |
| :--- | :--- | :--- | :--- | :--- |
| **SGD + Momentum** | Chậm; đòi hỏi tinh chỉnh learning rate rất khắt khe. | **Rất cao**. Thường tìm được các cực tiểu phẳng (Flat Minima) tổng quát hóa tốt hơn Adam. | Thấp (chỉ lưu thêm 1 trạng thái vận tốc $v$: 4 byte/param). | Thị giác máy tính cổ điển (ResNet trên ImageNet). |
| **Adam** | Rất nhanh; ít nhạy cảm với việc chọn learning rate ban đầu. | Kém hơn SGD một chút trên một số bài toán Computer Vision. | Cao (lưu cả $m$ và $v$: 8 byte/param). | Thập kỷ 2015-2019. |
| **AdamW** | Cực nhanh; ổn định số học vượt trội. | **Xuất sắc**. Bắt kịp và vượt qua SGD nhờ cơ chế Weight Decay tách rời chuẩn mực. | Cao (8 byte/param cho optimizer state). | **Tiêu chuẩn tuyệt đối cho toàn bộ LLMs, Transformers và Diffusion Models**. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Chiến lược Biểu đồ Tốc độ học (Learning Rate Schedules)
Không bao giờ dùng một Learning Rate cố định từ đầu đến cuối khi huấn luyện mạng sâu hoặc fine-tuning LLM:
1. **Warmup Phase (Khởi động)**: Tăng tuyến tính learning rate từ $0$ lên $\eta_{\max}$ trong $1\% - 5\%$ số bước đầu tiên. Giúp các moment $\hat{m}_t, \hat{v}_t$ thoát khỏi các giá trị ban đầu thiếu ổn định mà không làm nổ trọng số.
2. **Cosine Annealing Decay**: Hạ dần learning rate theo đường cong cosin từ $\eta_{\max}$ về $\eta_{\min} \approx 0.1 \times \eta_{\max}$. Giúp mô hình lắng đọng nhẹ nhàng vào đáy của thung lũng cực tiểu tối ưu.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao trong huấn luyện LLM phân tán, trạng thái của AdamW (Optimizer States) lại chiếm tới 50-60% dung lượng VRAM GPU chứ không phải bản thân trọng số mô hình?*
  - **A**: Với mô hình nạp ở độ chính xác FP16/BF16:
    - Trọng số mô hình chiếm: $2 \times N$ bytes.
    - Gradient chiếm: $2 \times N$ bytes.
    - Nhưng Optimizer AdamW bắt buộc phải duy trì độ chính xác cao **FP32 Master Weights** ($4 \times N$ bytes) để tránh mất mát số học khi cộng giá trị nhỏ, cộng thêm **Moment bậc 1 $m_t$ (FP32)** ($4 \times N$ bytes), và **Moment bậc 2 $v_t$ (FP32)** ($4 \times N$ bytes).
    - Tổng cộng trạng thái AdamW chiếm tới **$12 \times N$ bytes** (gấp 6 lần kích thước trọng số FP16 của mô hình!). Đây là lý do ra đời các kỹ thuật ZeRO (DeepSpeed) và 8-bit Adam (bitsandbytes).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[gradient-vanishing-exploding]] — Động lực thúc đẩy việc cải tiến các bộ tối ưu hóa thích ứng.
- [[regularization-l1-l2]] — Bản chất toán học phân biệt Adam và AdamW.
- [[large-language-models]] — AdamW là xương sống huấn luyện mọi LLM hàng đầu.
- [[quantization-and-compression]] — Nén trạng thái optimizer (Paged / 8-bit Optimizers) để tiết kiệm VRAM.
""",

    "principal-component-analysis.md": r"""# Phân Tích Thành Phần Chính (Principal Component Analysis - PCA)

> **Khái niệm chính thống**: *Mathematics for Machine Learning*, Chapter 10 (Dimensionality Reduction with Principal Component Analysis); *Principal Component Analysis.pdf* (Ngoc Hoang Luong, UIT).
> **Miền kiến thức**: [[ml-math-overview|Unsupervised Learning & Linear Algebra]]
> **Tài liệu gốc liên quan**:
> - [Principal Component Analysis.pdf](../../resources/machine-learning/Principal%20Component%20Analysis.pdf) (Trang 1-26)
> - [Mathematics-for-Machine-Learning.pdf](../../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) (Trang 321-355)
> - [Data Science_Machine Learning course (1).pdf](../../resources/machine-learning/Data%20Science_Machine%20Learning%20course%20%281%29.pdf) (Trang 110-135)

---

## 1. Tóm tắt (Executive Summary)
**Phân tích Thành phần Chính (Principal Component Analysis - PCA)** là thuật toán học không giám sát kinh điển dùng để giảm số chiều dữ liệu từ không gian ban đầu $\mathbb{R}^D$ xuống không gian con tuyến tính $\mathbb{R}^M$ ($M < D$) trong khi vẫn bảo toàn tối đa lượng thông tin (độ biến thiên / phương sai) của dữ liệu gốc. Về mặt hình học, PCA tìm kiếm một hệ trục tọa độ trực giao mới sao cho trục thứ nhất (First Principal Component) định hướng theo phương có phương sai lớn nhất, và các trục tiếp theo trực giao với các trục trước đó và bảo toàn phương sai giảm dần. Về mặt toán học, các thành phần chính chính là các **Vector riêng (Eigenvectors)** của ma trận hiệp phương sai mẫu.

---

## 2. Định nghĩa chính thống & Hai góc nhìn Toán học Tương đương

### 2.1 Góc nhìn 1: Tối đa hóa Phương sai Chiếu (Maximum Variance Perspective)
Cho tập dữ liệu đã chuẩn hóa trừ trung bình: $\sum_{n=1}^N x_n = 0$.
Ma trận hiệp phương sai mẫu $S \in \mathbb{R}^{D \times D}$:
$$S = \frac{1}{N} \sum_{n=1}^N x_n x_n^T = \frac{1}{N} X^T X$$
Xét vector đơn vị $u_1 \in \mathbb{R}^D$ ($\|u_1\|_2 = 1$). Phương sai của dữ liệu khi chiếu lên $u_1$:
$$\text{Var}(X u_1) = \frac{1}{N} \sum_{n=1}^N (u_1^T x_n)^2 = u_1^T S u_1$$

Bài toán tối ưu hóa với nhân tử Lagrange:
$$\max_{u_1} u_1^T S u_1 \quad \text{s.t.} \quad u_1^T u_1 = 1$$
$$\mathcal{L}(u_1, \lambda_1) = u_1^T S u_1 - \lambda_1 (u_1^T u_1 - 1)$$
Lấy đạo hàm theo $u_1$ và đặt bằng 0:
$$\nabla_{u_1} \mathcal{L} = 2 S u_1 - 2 \lambda_1 u_1 = 0 \implies S u_1 = \lambda_1 u_1$$
*(Đây chính là phương trình định nghĩa trị riêng và vector riêng! Phương sai lớn nhất đạt được chính là trị riêng lớn nhất $\lambda_1$).*

```mermaid
flowchart LR
    Data["Data Matrix X (N x D)"] --> Center["Mean Centering (X - μ)"]
    Center --> SVD["Singular Value Decomposition (SVD): X = U Σ Vᵀ"]
    Center --> Cov["Sample Covariance Matrix S = (1/N) XᵀX"]
    Cov --> Eig["Eigen-decomposition: S v_i = λ_i v_i"]
    SVD -.->|"Equivalent"| Eig
    Eig --> Sort["Sort Eigenvalues: λ₁ ≥ λ₂ ≥ ... ≥ λ_D"]
    Sort --> Project["Project to Top-M Components: Z = X V_M"]
```

### 2.2 Góc nhìn 2: Tối thiểu hóa Sai số Tái tạo (Minimum Reconstruction Error)
PCA đồng thời là phép chiếu tuyến tính tối ưu hóa việc tái dựng lại dữ liệu gốc với sai số bình phương nhỏ nhất:
$$\min_{U_M} \frac{1}{N} \sum_{n=1}^N \|x_n - U_M U_M^T x_n\|_2^2$$
Hai góc nhìn Tối đa hóa Phương sai và Tối thiểu hóa Sai số Tái tạo là **tương đương tuyệt đối về mặt toán học**.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Tiêu chí | PCA qua Phân rã Ma trận Hiệp phương sai (Eigen-decomposition) | PCA qua Phân rã Giá trị Kỳ dị (SVD) | Ý nghĩa Kỹ thuật Thực chiến |
| :--- | :--- | :--- | :--- |
| **Công thức** | Tính $S = \frac{1}{N} X^T X$, sau đó phân rã $S = V \Lambda V^T$. | Phân rã trực tiếp ma trận dữ liệu: $X = U \Sigma V^T$. | Giá trị kỳ dị $\sigma_i$ của $X$ liên hệ với trị riêng của $S$: $\lambda_i = \frac{\sigma_i^2}{N}$. |
| **Ổn định Số học** | Kém; phép tính $X^T X$ làm bình phương số điều kiện (Condition Number), gây mất độ chính xác dấu phẩy động. | **Rất cao**. Không bao giờ phải tính trực tiếp ma trận $X^T X$. | `scikit-learn` và mọi thư viện chuẩn đều dùng SVD để cài đặt PCA thay vì tính ma trận hiệp phương sai. |
| **Độ phức tạp bộ nhớ** | Tốn $\mathcal{O}(D^2)$ lưu ma trận hiệp phương sai. | Tối ưu; có thể chạy dạng dòng dữ liệu (Incremental PCA). | Áp dụng được cho kho dữ liệu lớn không vừa RAM. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy tắc Tỷ lệ Phương sai Tích lũy (Explained Variance Ratio)
Để chọn số chiều $M$ tối ưu, kỹ sư vẽ biểu đồ **Scree Plot** và chọn $M$ sao cho tỷ lệ phương sai giải thích tích lũy vượt ngưỡng mong muốn (thường là 90% hoặc 95%):
$$\text{Cumulative Explained Variance}(M) = \frac{\sum_{i=1}^M \lambda_i}{\sum_{j=1}^D \lambda_j} \ge 0.95$$

### 4.2 Bẫy Bắt buộc Chuẩn hóa Dữ liệu (Standardization Prerequisite)
- **Cạm bẫy chết người**: Nếu không chuẩn hóa độ lệch chuẩn (StandardScaler: đưa về trung bình 0, phương sai 1) trước khi chạy PCA:
  - Một thuộc tính có đơn vị đo lớn (ví dụ: `Lương tính bằng VNĐ`, dao động hàng chục triệu) sẽ hoàn toàn áp đảo thuộc tính có đơn vị đo nhỏ (ví dụ: `Tuổi`, dao động 20-60).
  - Trục thành phần chính thứ nhất sẽ bị bẻ cong đi theo hướng của thuộc tính có thang đo lớn nhất một cách giả tạo, làm biến dạng toàn bộ cấu trúc dữ liệu.

### 4.3 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao PCA là phép giảm chiều tuyến tính không giám sát, và sự khác biệt cốt lõi giữa PCA với t-SNE / UMAP là gì?*
  - **A**: PCA chỉ tìm kiếm các siêu phẳng chiếu tuyến tính trực giao toàn cục và tối đa hóa phương sai; nó bảo toàn cấu trúc vĩ mô toàn cục (Global Structure) nhưng hoàn toàn thất bại trong việc phân tách các đa tạp phi tuyến tính phức tạp (Non-linear Manifolds như cuộn Swiss Roll). Ngược lại, **t-SNE** và **UMAP** là các giải thuật giảm chiều phi tuyến tính dựa trên đồ thị xác suất láng giềng, xuất sắc trong việc bảo toàn cấu trúc cục bộ (Local Neighborhoods) để trực quan hóa cụm dữ liệu 2D/3D.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[linear-regression-mle]] — Sử dụng PCA để nén thuộc tính trước khi hồi quy nhằm triệt tiêu đa cộng tuyến.
- [[vector-embeddings]] — Sử dụng PCA/SVD để nén số chiều của vector embeddings (Dimensionality Reduction).
- [[regularization-l1-l2]] — So sánh giữa trích xuất đặc trưng mới (PCA) và chọn lọc đặc trưng cũ (L1).
""",

    "model-selection-evaluation.md": r"""# Chiến Lược Lựa Chọn và Đánh Giá Mô Hình (Model Selection & Evaluation)

> **Khái niệm chính thống**: *Understanding Machine Learning*, Chapter 11 (Model Selection and Validation); *Mathematics for Machine Learning*, Chapter 8; *848563711...jpg* ("1. Model này dùng khi nào?"); *847762397...jpg* ("2. Dữ liệu bẩn xử lý sao?"); *847999051...jpg* ("4. Nếu model sai thì sao?").
> **Miền kiến thức**: [[ml-math-overview|Methodology, Validation & Production Thinking]]
> **Tài liệu gốc liên quan**:
> - [848563711_122320900772195094_1553865876902100027_n.jpg](../../resources/images/848563711_122320900772195094_1553865876902100027_n.jpg) (Infographic 1: Model Selection & Context)
> - [847762397_122320901834195094_274771350129520392_n.jpg](../../resources/images/847762397_122320901834195094_274771350129520392_n.jpg) (Infographic 2: Dữ liệu bẩn)
> - [847999051_122320901954195094_4534131503073995411_n.jpg](../../resources/images/847999051_122320901954195094_4534131503073995411_n.jpg) (Infographic 4: Xử lý lỗi model)
> - [Learning_Phases.pdf](../../resources/machine-learning/Learning_Phases.pdf) (Trang 1-39)

---

## 1. Tóm tắt (Executive Summary)
**Lựa chọn và Đánh giá Mô hình (Model Selection & Evaluation)** là quy trình khoa học mang tính hệ thống nhằm so sánh, định lượng và thẩm định tính bền vững của các thuật toán ứng viên trên dữ liệu chưa từng thấy trước khi đưa vào vận hành thực tế. Không có mô hình nào là tối ưu tuyệt đối cho mọi tình huống (**No Free Lunch Theorem**). Quy trình này bao gồm việc thiết lập chiến lược kiểm tra chéo (**K-Fold Cross-Validation**, **Stratified Splits**), sử dụng các tiêu chuẩn thông tin xác suất (**AIC, BIC**), ngăn chặn triệt để hiện tượng rò rỉ dữ liệu (**Data Leakage**), và quan trọng nhất là năng lực tư duy kỹ sư: **chọn mô hình gắn liền với ngữ cảnh bài toán, độ trễ, chi phí và khả năng giải thích**.

---

## 2. Định nghĩa chính thống & Hai trường phái Lựa chọn Mô hình (From Infographic 848563711)

```mermaid
flowchart TD
    ModelSel["Model Selection Architecture"] --> Resample["1. Resampling Techniques (Empirical)"]
    ModelSel --> Prob["2. Probabilistic Techniques (Analytical)"]
    
    Resample --> CV["K-Fold Cross-Validation / Stratified"]
    Resample --> Boot["Bootstrapping (Sampling with Replacement)"]
    Resample --> Split["Train / Validation / Test Split"]
    
    Prob --> AIC["AIC = 2k - 2 ln(L) (Akaike Info Criterion)"]
    Prob --> BIC["BIC = k ln(n) - 2 ln(L) (Bayesian Info Criterion)"]
    Prob --> BMA["Bayesian Model Averaging (BMA)"]
```

### 2.1 Chi tiết hai trường phái
1. **Resampling Techniques (Trường phái Thực nghiệm)**:
   - Dùng sức mạnh tính toán để chia tập dữ liệu nhiều lần:
     - **K-Fold Cross-Validation**: Chia $K$ phần bằng nhau, luân phiên dùng $K-1$ phần để train và 1 phần để test.
     - **Stratified K-Fold**: Bắt buộc giữ nguyên tỷ lệ phân phối các lớp mục tiêu trong từng fold (tối quan trọng khi dữ liệu mất cân bằng).
     - **Time-Series Purged / Blocked Split**: Với dữ liệu chuỗi thời gian, tuyệt đối không dùng K-Fold ngẫu nhiên mà phải chia tuần tự theo trục thời gian (Walk-forward Validation) để ngăn rò rỉ thông tin tương lai về quá khứ.
2. **Probabilistic Techniques (Trường phái Xác suất Lý thuyết)**:
   - Đánh giá mô hình dựa trên hàm hợp lý cực đại kết hợp số hạng phạt số lượng tham số $k$:
     - **AIC (Akaike Information Criterion)**: $\text{AIC} = 2k - 2\ln(\hat{L})$. Hướng tới mô hình dự đoán tốt nhất khi kích thước mẫu tiến tới vô cùng.
     - **BIC (Bayesian Information Criterion)**: $\text{BIC} = k\ln(n) - 2\ln(\hat{L})$. Phạt độ phức tạp nặng hơn AIC theo $\ln(n)$, hướng tới việc tìm ra mô hình chân lý thực sự đã sinh ra dữ liệu.

---

## 3. Tư duy Kỹ sư AI Thực chiến: Bài học từ Bộ 3 Infographics Chuyên gia

### 3.1 "Model này dùng khi nào?" (Infographic 848563711)
- **Người yếu**: Thường trả lời bằng tên model (e.g., *"Bài này cứ tương XGBoost hoặc LLM vào là xong!"*), không quan tâm bối cảnh.
- **Người có trình độ (Senior)**: Luôn hỏi lại bài toán, phân bố dữ liệu và ràng buộc hệ thống:
  1. *Kích thước dữ liệu là bao nhiêu?*
  2. *Yêu cầu độ trễ (Latency SLA) là bao nhiêu mili-giây?*
  3. *Hệ thống có cần khả năng giải thích (Explainability / White-box) cho cơ quan pháp lý không?*
  4. *Chi phí hạ tầng và ngân sách vận hành là bao nhiêu?*
  - **Quy tắc vàng**: Không phải model mạnh nhất là dùng được trong mọi tình huống. Có những bài toán dùng mô hình thống kê cổ điển hoặc Rule-based còn tốt và bền vững hơn AI ngàn lần!

### 3.2 "Dữ liệu bẩn xử lý sao?" (Infographic 847762397)
- **Người mới**: Hay nói chung chung là "làm sạch dữ liệu".
- **Người giỏi**: Phân loại rành mạch bản chất của dữ liệu bẩn:
  1. **Thiếu dữ liệu (Missing)** khác hoàn toàn với **Dữ liệu sai (Corrupted)**.
  2. **Ngoại lai (Outlier)**: Có lúc là lỗi đo đạc, nhưng có lúc lại là **tín hiệu quan trọng nhất** của toàn bộ bài toán (ví dụ: giao dịch lừa đảo gian lận tín dụng chính là các outliers!).
  3. Không phải lúc nào cũng vội vàng xóa bỏ dữ liệu ngoại lai.
  4. Xử lý dữ liệu luôn gắn chặt với nghiệp vụ kinh doanh (Business Context).

### 3.3 "Nếu Model sai thì sao?" (Infographic 847999051)
- **Slicing Analysis**: Không đánh giá mô hình bằng một con số trung bình duy nhất (như Accuracy = 73.8%). Phải mổ xẻ sai số theo từng lát cắt vùng miền/nhóm đối tượng.
- **Thiết kế Cơ chế Dự phòng (Fail-safes)**: Xây dựng hàng rào kiểm soát rủi ro, phân ngưỡng tin cậy để chuyển giao cho con người xử lý ([[human-in-the-loop]]) khi model không chắc chắn.

---

## 4. Các cạm bẫy sống còn: Data Leakage (Rò rỉ Dữ liệu)

### 4.1 3 Dạng Rò rỉ Dữ liệu phổ biến nhất
1. **Feature Preprocessing Leakage**: Fit bộ chuẩn hóa `StandardScaler` hoặc `Imputer` trên toàn bộ tập dữ liệu trước khi thực hiện `train_test_split`. *Hậu quả*: Thông tin về giá trị trung bình và độ lệch chuẩn của tập Test đã bị rò rỉ vào tập Train, khiến kết quả kiểm thử cao giả tạo.
   - *Cách khắc phục*: Bắt buộc dùng `Pipeline` trong scikit-learn để fit scaler **chỉ trên tập train** và transform trên tập test.
2. **Temporal Leakage**: Sử dụng các đặc trưng trong tương lai để dự đoán quá khứ.
3. **Group / Identity Leakage**: Mẫu ảnh của cùng một bệnh nhân xuất hiện ở cả tập Train và tập Test.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Khi gặp bài toán phân loại gian lận thẻ tín dụng với tỷ lệ gian lận chỉ chiếm 0.1%, chỉ số Accuracy đạt 99.9% có ý nghĩa gì không? Bạn sẽ dùng bộ chỉ số nào để đánh giá và lựa chọn mô hình?*
  - **A**: Accuracy = 99.9% là vô nghĩa (Dummy model chỉ cần dự đoán tất cả đều là "Không gian lận" đã đạt 99.9% nhưng hệ thống hoàn toàn vô dụng).
  - Phải sử dụng:
    1. **Precision-Recall Curve (PR-AUC)** thay vì ROC-AUC (vì ROC-AUC bị lạc quan giả tạo khi số lượng mẫu âm tính áp đảo).
    2. **Recall tại một mức Precision cố định** (ví dụ: Tìm được bao nhiêu % ca gian lận với điều kiện tỷ lệ báo động giả không vượt quá 5%).
    3. **Ma trận Chi phí Doanh nghiệp (Cost-Benefit Matrix)**: Gán trọng số thiệt hại tài chính cụ thể cho lỗi False Negative (bỏ lọt gian lận, mất tiền) so với False Positive (chặn nhầm khách hàng thật, gây phiền toái).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[bias-variance-tradeoff]] — Nền tảng lý thuyết phân tích lỗi để lựa chọn mô hình.
- [[linear-regression-mle]] — Ứng dụng AIC/BIC để lựa chọn biến trong hồi quy.
- [[regularization-l1-l2]] — Kỹ thuật kiểm soát mô hình được chọn.
- [[human-in-the-loop]] — Thiết kế cổng kiểm soát an toàn khi mô hình sai trong thực tế.
"""
}

def generate():
    for filename, content in ENTITIES.items():
        filepath = WIKI_DIR / filename
        filepath.write_text(content.strip(), encoding="utf-8")
        print(f"Created: {filepath.name}")

if __name__ == "__main__":
    generate()
