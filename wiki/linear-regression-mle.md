# Hồi Quy Tuyến Tính và Ước Lượng Hợp Lý Cực Đại (Linear Regression & MLE)

> **Khái niệm chính thống**: *Mathematics for Machine Learning* (Deisenroth et al., Cambridge), Chapter 9; *Understanding Machine Learning* (Shalev-Shwartz & Ben-David), Chapter 9; *03_LinearRegression-with-MLE.pdf*.
> **Miền kiến thức**: [[index|Machine Learning & Statistical Foundations]]
> **Tài liệu gốc liên quan**:
> - [Mathematics-for-Machine-Learning.pdf](../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) (Trang 289-320)
> - [03_LinearRegression-with-MLE.pdf](../resources/machine-learning/03_LinearRegression-with-MLE.pdf) (Trang 1-22)
> - [understanding-machine-learning-theory-algorithms.pdf](../resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf) (Trang 115-130)
> - [AIO2026_Reading-LinearRegression.pdf](../resources/machine-learning/AIO2026_Reading-LinearRegression.pdf) (Trang 1-49)

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

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & `wiki-links`)
- [[bias-variance-tradeoff]] — Đánh giá sự cân bằng giữa độ chệch và phương sai trong hồi quy.
- [[regularization-l1-l2]] — L1 Lasso và L2 Ridge khắc phục hiện tượng đa cộng tuyến và quá khớp.
- [[optimization-algorithms]] — Giải thuật Gradient Descent để tìm nghiệm hồi quy trên tập dữ liệu lớn.
- [[principal-component-analysis]] — Phương pháp chiếu giảm chiều giải quyết đa cộng tuyến trước khi hồi quy.