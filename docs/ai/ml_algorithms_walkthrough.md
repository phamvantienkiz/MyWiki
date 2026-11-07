# Báo Cáo Nghiệm Thu & Walkthrough: Tích Hợp Các Thuật Toán Machine Learning Vào Bộ Tài Liệu Phỏng Vấn `interview/`

## 1. Tổng Quan Công Việc Đã Thực Hiện
Đã sử dụng toàn bộ hệ thống tri thức từ tài liệu chuyên sâu trong `resources/machine-learning/` để bổ sung và nâng cấp toàn diện các thuật toán Machine Learning kinh điển vào `interview/index.html`, `interview/script.js` và `interview/style.css`.
Toàn bộ nội dung tuân thủ nghiêm ngặt kỹ năng sư phạm `lecture-visualizer`:
- **Trực giác trước — Ký hiệu sau**: Diễn giải bằng văn phong đời thường mộc mạc, gần gũi cho người học chậm trước khi giới thiệu công thức.
- **Bảng từ điển ký hiệu 4 cột**: Ký hiệu KaTeX $\to$ Tên tiếng Anh chuẩn học thuật $\to$ Tên tiếng Việt chính xác $\to$ Nghĩa đời thường.
- **Hộp thoại "Góc Dành Cho Người Học Chậm" (`.callout.intuition`)**: Sử dụng các ẩn dụ thực tế (Tâm bia bắn cung, Căng dây chun cọc mốc, Duyệt hồ sơ vay ngân hàng, Hội đồng 100 bác sĩ, Học sinh sửa lỗi bài kiểm tra, Flycam chụp tượng 3D).
- **Trace số học từng bước (Arithmetic step-by-step trace)**: Thực hiện tính tay chi tiết từng con số trên bộ dữ liệu mẫu (Toy Dataset) để người học thấy rõ nguồn gốc từng phép tính.
- **Bảng đối chiếu 1-1 bóc tách bản chất**: So sánh trực tiếp giữa các cặp thuật toán đối ứng.
- **Thiết kế Soft Clean Cards**: Nền trắng thanh lịch, bo góc lớn, bóng mờ nhẹ, typography Inter + JetBrains Mono, KaTeX kết xuất công thức toán học sắc nét.
- **Resource Pills & Wiki Links**: Gắn badge liên kết trực tiếp tới các file PDF canonical trong `resources/machine-learning/` và các ghi chú trong `wiki/`.
- **Bộ công cụ tương tác Machine Learning Playground**: Thử nghiệm trực quan 4 thuật toán ngay trên giao diện web.

---

## 2. Danh Sách Các Thuật Toán Machine Learning Đã Tích Hợp

### 2.1 Bản Chất Học Máy, Phân Rã Toán Học Bias-Variance Tradeoff & Điều Chuẩn (L1/L2)
- **Tài liệu nguồn**: `resources/machine-learning/Bias-Variance_Tradeoff.pdf`, `resources/machine-learning/3 - Polynomial Regression and Regularizations.pdf`.
- **Nội dung bổ sung**:
  - Bảng từ điển ký hiệu 4 cột ($\mathcal{D}, f(x), \hat{f}(x), \epsilon, \sigma^2, \text{Bias}, \text{Var}, \lambda$).
  - Chứng minh toán học đầy đủ từng bước phân rã sai số bình phương kỳ vọng: $\mathbb{E}[(y - \hat{f})^2] = \text{Bias}^2 + \text{Var} + \sigma^2$, chỉ rõ lý do các số hạng tích chéo triệt tiêu về 0 do tính độc lập của nhiễu $\epsilon$.
  - Ẩn dụ sư phạm: 4 tâm bia bắn súng (Bullseye Analogy).
  - Trace số học bằng tay tính Bias & Variance trên 3 dự đoán của mô hình với chân lý $f(x_0)=20, \sigma^2=0.5$.

### 2.2 Thuật Toán Hồi Quy Tuyến Tính (Linear Regression) & MLE
- **Tài liệu nguồn**: `resources/machine-learning/03_LinearRegression-with-MLE.pdf`, `resources/machine-learning/LinearRegression-with-MLE.pdf`, `resources/machine-learning/AIO2026_Reading-LinearRegression.pdf`, `resources/machine-learning/3 - Polynomial Regression and Regularizations.pdf`.
- **Nội dung bổ sung**:
  - Nguồn gốc xác suất: Chứng minh tối thiểu hóa MSE xuất phát từ Maximum Likelihood Estimation (MLE) với giả định sai số Gauss $\epsilon \sim \mathcal{N}(0, \sigma^2)$.
  - Giải nghiệm giải tích đóng Normal Equation: $\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$ bằng đạo hàm ma trận.
  - Phân tích chi phí tính toán: Khi nào dùng Normal Equation ($O(d^3)$) vs Gradient Descent ($O(N \cdot d)$).
  - Hồi quy đa thức (Polynomial Regression), hiện tượng Runge dao động ở biên và vai trò của Regularization.
  - Trace số học bằng tay: Giải nghiệm đóng trên 3 điểm dữ liệu $(1, 2), (2, 3), (3, 5)$ ra chính xác $\hat{y} = 1.50x + 0.33$.

### 2.3 Thuật Toán Hồi Quy Logistic (Logistic Regression) & Softmax Regression
- **Tài liệu nguồn**: `resources/machine-learning/AIO2026_[Description]-Exercise-Softmax-Regression.pdf`, `resources/machine-learning/Machine Learning Cheatsheet.pdf`, `resources/machine-learning/super-cheatsheet-machine-learning.pdf`.
- **Nội dung bổ sung**:
  - Phân tích tại sao không thể dùng hồi quy tuyến tính để phân loại (đầu ra vượt ngưỡng xác suất, cực kỳ nhạy cảm với ngoại lai).
  - Hàm Sigmoid, Tỷ lệ cược (Odds) $\frac{p}{1-p}$ và hàm Log-odds (Logit): $\ln(\text{Odds}) = \mathbf{w}^T\mathbf{x} + b$.
  - Suy diễn hàm mất mát Binary Cross-Entropy (BCE) từ hàm hợp lý phân phối Bernoulli.
  - Đạo hàm Gradient đẹp ngỡ ngàng: $\nabla_{\mathbf{w}} \mathcal{L} = \frac{1}{N} \mathbf{X}^T (\hat{\mathbf{y}} - \mathbf{y})$.
  - Mở rộng đa lớp: Softmax Regression (Multinomial Logistic Regression) và hàm Categorical Cross-Entropy.
  - Trace số học bằng tay: 1 bước cập nhật Gradient Descent trên 1 mẫu dữ liệu cụ thể.

### 2.4 Thuật Toán Perceptron & Định Lý Hội Tụ Novikoff
- **Tài liệu nguồn**: `resources/machine-learning/Perceptron_Learning_Algorithm_and_Convergence.pdf`, `resources/machine-learning/Machine-Learning-with-Neural-Networks.pdf`, `resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf`.
- **Nội dung bổ sung**:
  - Quy trình cập nhật Perceptron Learning Algorithm (PLA) khi phân loại sai $y_i(\mathbf{w}^T\mathbf{x}_i) \le 0 \implies \mathbf{w} \leftarrow \mathbf{w} + \eta y_i \mathbf{x}_i$.
  - Trực giác hình học: Vector pháp tuyến $\mathbf{w}$ quay dần về phía điểm bị sai để biến góc tù thành góc nhọn.
  - Chứng minh toán học định lý Novikoff (1962): Dùng Cauchy-Schwarz thiết lập chặn dưới $\mathbf{w}_k^T\mathbf{w}^* \ge k\gamma$ và chặn trên $\|\mathbf{w}_k\|^2 \le k R^2$, suy ra số bước cập nhật tối đa $k \le \frac{R^2}{\gamma^2}$.
  - Cú sốc lịch sử: Marvin Minsky chứng minh Perceptron bất lực trước hàm XOR $\to$ Mùa đông AI đầu tiên.
  - Trace số học bằng tay: 3 vòng lặp PLA học phân tách cổng logic OR.

### 2.5 Máy Vector Hỗ Trợ (Support Vector Machine - SVM) & Kernel Trick
- **Tài liệu nguồn**: `resources/machine-learning/super-cheatsheet-machine-learning.pdf`, `resources/machine-learning/ML_cheatsheets.pdf`, `resources/machine-learning/understanding-machine-learning-theory-algorithms.pdf`.
- **Nội dung bổ sung**:
  - Bản chất hình học: Tìm siêu phẳng có khoảng cách an toàn (Margin) rộng nhất $\frac{2}{\|\mathbf{w}\|}$.
  - Hard-margin SVM vs Soft-margin SVM với biến bù lỏng $\xi_i \ge 0$ và tham số điều chuẩn $C$.
  - Mối liên hệ toán học với Hinge Loss $\mathcal{L}_{\text{hinge}}(z) = \max(0, 1 - z)$.
  - Bài toán Đối ngẫu Lagrange (Dual Problem) và điều kiện bù trừ KKT (Karush-Kuhn-Tucker): Chỉ các điểm sát mép lề (Support Vectors, $\alpha_i > 0$) mới ảnh hưởng đến ranh giới quyết định.
  - Bí thuật Kernel Trick & Định lý Mercer: Linear, Polynomial, RBF / Gaussian ($K(\mathbf{x}, \mathbf{z}) = \exp(-\gamma \|\mathbf{x} - \mathbf{z}\|^2)$ ánh xạ không gian Hilbert vô hạn chiều), Sigmoid.
  - Trace số học bằng tay: Tính vector pháp tuyến $\mathbf{w}$, hệ số chặn $b$ và bề rộng lề $\text{Margin} = \sqrt{2} \approx 1.414$ trên 3 điểm dữ liệu 2D.

### 2.6 Cây Quyết Định (Decision Tree), Entropy, Gini Impurity & Cắt Tỉa Pruning
- **Tài liệu nguồn**: `resources/machine-learning/Data Science_Machine Learning course (1).pdf`, `resources/machine-learning/Machine Learning Cheatsheet.pdf`, `resources/machine-learning/super-cheatsheet-machine-learning.pdf`.
- **Nội dung bổ sung**:
  - Trực giác 20 câu hỏi và độ bừa bộn của căn phòng.
  - 3 độ đo độ tinh khiết: Shannon Entropy $H(S) = -\sum p_c \log_2 p_c$, Information Gain $IG(S, A)$, Gain Ratio (C4.5) và Gini Impurity $Gini(S) = 1 - \sum p_c^2$ (CART).
  - Cây hồi quy (Regression Tree): Giảm phương sai (Variance Reduction), giá trị dự đoán là trung bình cộng tại lá $\bar{y}$.
  - Chiến lược cắt tỉa: Pre-pruning (max_depth, min_samples_split) vs Post-pruning (Cost-Complexity Pruning $\mathcal{R}_\alpha(T) = \mathcal{R}(T) + \alpha |T|$).
  - Trace số học bằng tay: Tính Entropy, Information Gain và Gini Impurity trên 6 mẫu dữ liệu dự đoán Chơi Golf.

### 2.7 Rừng Ngẫu Nhiên (Random Forest), Bagging & Out-of-Bag (OOB)
- **Tài liệu nguồn**: `resources/machine-learning/super-cheatsheet-machine-learning.pdf`, `resources/machine-learning/ML_cheatsheets.pdf`, `resources/machine-learning/Data Science_Machine Learning course (1).pdf`.
- **Nội dung bổ sung**:
  - Toán học phân rã phương sai tập hợp: $\text{Var}(\bar{X}) = \rho \sigma^2 + \frac{1-\rho}{B}\sigma^2$. Khi $B \to \infty$, phương sai chỉ phụ thuộc vào hệ số tương quan $\rho$.
  - 2 tầng ngẫu nhiên hóa: Bootstrap Sampling (dòng) và Random Feature Subspace (cột, $m = \sqrt{d}$) giúp triệt tiêu tương quan $\rho \to 0$.
  - Chứng minh toán học tỷ lệ Out-of-Bag: $\lim_{N \to \infty}(1 - 1/N)^N = 1/e \approx 36.8\%$.
  - Đánh giá độ quan trọng đặc trưng: MDI (Mean Decrease Impurity) vs MDA (Permutation Importance).
  - Bảng đối chiếu 1-1: Single Decision Tree vs Random Forest.

### 2.8 Thuật Toán XGBoost & Gradient Boosting Decision Trees (GBDT)
- **Tài liệu nguồn**: `resources/machine-learning/super-cheatsheet-machine-learning.pdf`, `resources/machine-learning/ML_cheatsheets.pdf`, `resources/machine-learning/Machinelearningyearning-Vi.pdf`.
- **Nội dung bổ sung**:
  - Khác biệt bản chất: Bagging (giảm Variance, học song song) vs Boosting (giảm Bias, học chuỗi nối tiếp sửa lỗi).
  - Tiến trình lịch sử: AdaBoost $\to$ GBDT (fit gradient âm) $\to$ XGBoost.
  - Đột phá toán học XGBoost: Khai triển Taylor bậc 2 quanh $\hat{y}_i^{(t-1)}$:
    $$\tilde{\mathcal{L}}^{(t)} \approx \sum_{i=1}^n \left[ g_i f_t(\mathbf{x}_i) + \frac{1}{2} h_i f_t^2(\mathbf{x}_i) \right] + \gamma T + \frac{1}{2}\lambda \sum_{j=1}^T w_j^2$$
  - Trọng số lá tối ưu $w_j^* = -\frac{G_j}{H_j + \lambda}$ và công thức tính Split Gain có điều chuẩn $\gamma$.
  - Kỹ thuật công nghiệp: Sparsity-aware Split Finding (tự động phân nhánh cho dữ liệu NaN/missing value), Weighted Quantile Sketch, Cache-aware block.
  - Bảng đối chiếu 1-1: Bagging (Random Forest) vs Boosting (XGBoost).
  - Trace số học bằng tay: Tính trọng số lá tối ưu với hàm loss MSE có điều chuẩn $\lambda = 1.0$.

### 2.9 Phân Tích Thành Phần Chính (Principal Component Analysis - PCA) & SVD
- **Tài liệu nguồn**: `resources/machine-learning/Principal Component Analysis.pdf`, `resources/machine-learning/Mathematics-for-Machine-Learning.pdf`, `resources/machine-learning/super-cheatsheet-machine-learning.pdf`, `resources/machine-learning/Algorithmic-Aspects-of-Machine-Learning.pdf`.
- **Nội dung bổ sung**:
  - Bản chất hình học: Tìm góc quay sao cho cái bóng chiếu có phương sai lớn nhất (bảo toàn nhiều thông tin nhất) hoặc sai số tái tạo nhỏ nhất.
  - Chứng minh toán học bằng nhân tử Lagrange: $\boldsymbol{\Sigma} \mathbf{u}_1 = \lambda \mathbf{u}_1$, phương sai chính bằng trị riêng $\lambda$.
  - Mối quan hệ mật thiết với SVD: $\mathbf{X}_c = \mathbf{U} \mathbf{S} \mathbf{V}^T$, các cột của $\mathbf{V}$ chính là các thành phần chính, tọa độ chiếu $\mathbf{Z} = \mathbf{X}_c \mathbf{V}_k = \mathbf{U}_k \mathbf{S}_k$.
  - Explained Variance Ratio $r_k = \frac{\lambda_k}{\sum \lambda_j}$ và Biểu đồ Scree Plot.
  - Bảng đối chiếu 1-1: PCA (Unsupervised) vs LDA (Supervised) vs Feature Selection.
  - Trace số học bằng tay: PCA trên ma trận 4 mẫu 2 chiều nén về 1 chiều mà không làm mất thông tin ($\lambda_2 = 0$).

### 2.16 Bộ Khám Phá Trực Quan Thuật Toán Machine Learning (Interactive Simulator)
- Tích hợp widget tương tác 4 tab trực quan:
  1. **Bias-Variance Tradeoff Simulator**: Thanh trượt bậc đa thức $p=1 \to 9$, tính và hiển thị ngay $\text{Bias}^2$, $\text{Variance}$, $\text{Total MSE}$ và trạng thái Underfitting / Sweet Spot / Overfitting.
  2. **Gini & Entropy Impurity Explorer**: Thanh trượt số mẫu Lớp 1 và Lớp 0, tính tức thì Shannon Entropy $H(S)$ và Gini Impurity $Gini(S)$ cùng thanh đo Purity level.
  3. **PCA Explained Variance Calculator**: Nhập 4 trị riêng $\lambda_1, \lambda_2, \lambda_3, \lambda_4$, tính tỷ lệ phần trăm phương sai từng trục, tỷ lệ tích lũy và đưa ra khuyến nghị số chiều $k$ cần giữ lại ($\ge 90\%$).
  4. **Logistic Regression Logit & Odds Probe**: Kéo điểm số $z = \mathbf{w}^T\mathbf{x} + b \in [-6, +6]$, tính tức thì xác suất $P(y=1) = \sigma(z)$, tỷ lệ cược $\text{Odds} = e^z$ và hiển thị quyết định phân loại.

---

## 3. Kiểm Thử & Xác Nhận Chất Lượng
- **HTML Syntax Validation**: Đã chạy parser kiểm tra toàn bộ cấu trúc thẻ từ dòng 570 đến 2855 của Module 02. Kết quả: **Module 02 HTML is 100% perfectly balanced!**
- **Sidebar & ScrollSpy Links**: Toàn bộ 16 liên kết neo từ `mod2-1` đến `mod2-16` đều khớp 1-1 với các thẻ `div.scroll-target` tương ứng.
- **JavaScript Engine**: Các hàm mô phỏng `switchMLTab`, `updateBVSim`, `updateTreeSim`, `updatePCASim`, `updateLogisticSim` được kết nối an toàn vào sự kiện `DOMContentLoaded`.
- **CSS Design System**: Các class `.ml-tab-btn`, `.ml-tab-content`, `.resource-pill`, `.wiki-link` tuân thủ nguyên lý Soft Clean Cards.
