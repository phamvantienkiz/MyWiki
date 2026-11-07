# Kế Hoạch Bổ Sung Các Thuật Toán Machine Learning Cốt Lõi Vào `interview/`

## 1. Mục Tiêu & Yêu Cầu
- Tích hợp toàn diện các thuật toán Machine Learning kinh điển: **Linear Regression, Logistic Regression, Perceptron, SVM, Decision Tree, Random Forest, XGBoost, PCA, Bias-Variance Tradeoff** vào bộ tài liệu phỏng vấn `interview/index.html`.
- Áp dụng triệt để phương pháp sư phạm của skill `lecture-visualizer`:
  - **Trực giác trước - Ký hiệu sau** (ngôn ngữ tự nhiên mộc mạc cho người học chậm, ví dụ đời sống).
  - **Bảng từ điển ký hiệu 4 cột** (Ký hiệu, Tên tiếng Anh, Tên tiếng Việt, Nghĩa đời thường).
  - **Hộp thoại "Góc Dành Cho Người Học Chậm"** (`.callout.intuition`) bóc tách bản chất, ẩn dụ trực quan.
  - **Trace số học từng bước (Arithmetic step-by-step trace)** trên bộ dữ liệu mẫu (Toy Dataset) để người đọc thấy rõ từng phép tính.
  - **Bảng đối chiếu 1-1** (Linear vs Logistic, Hard vs Soft SVM, Bagging vs Boosting, PCA vs Feature Selection).
  - **Soft Clean Cards design system** đồng bộ với giao diện hiện có của `interview/`.
  - **KaTeX** toán học chuẩn mực cho mọi công thức.
  - **Resource Pills & Wiki Links** trỏ trực tiếp đến toàn bộ tài liệu canonical trong `resources/machine-learning/` và `wiki/`.
- Sửa trực tiếp các file `interview/index.html`, `interview/script.js`, `interview/style.css` (không dùng script python để sửa file).
- Tạo tất cả các file công việc phụ trợ (kế hoạch, task log, preview...) trực tiếp trong `docs/ai/`.

## 2. Danh Sách Tài Liệu Canonical Khai Thác Từ `resources/machine-learning/`
1. `03_LinearRegression-with-MLE.pdf` & `LinearRegression-with-MLE.pdf` & `AIO2026_Reading-LinearRegression.pdf`
2. `3 - Polynomial Regression and Regularizations.pdf`
3. `AIO2026_[Description]-Exercise-Softmax-Regression.pdf`
4. `Perceptron_Learning_Algorithm_and_Convergence.pdf`
5. `Bias-Variance_Tradeoff.pdf`
6. `Principal Component Analysis.pdf`
7. `super-cheatsheet-machine-learning.pdf` & `ML_cheatsheets.pdf` & `Machine Learning Cheatsheet.pdf`
8. `Data Science_Machine Learning course (1).pdf`
9. `understanding-machine-learning-theory-algorithms.pdf`
10. `Algorithmic-Aspects-of-Machine-Learning.pdf`
11. `Mathematics-for-Machine-Learning.pdf`
12. `Mathematical-Analysis-of-Machine-Learning-Algorithms.pdf`
13. `Machinelearningyearning-Vi.pdf`
14. `Machine-Learning-with-Neural-Networks.pdf`

## 3. Kiến Trúc Cấu Trúc Module 02 Mới
- **2.1** Bản Chất Học Máy, Phân Rã Toán Học Bias-Variance Tradeoff & Kỹ Thuật Điều Chuẩn (L1/L2)
- **2.2** Hồi Quy Tuyến Tính (Linear Regression) & Ước Lượng Hợp Lý Cực Đại (MLE)
- **2.3** Hồi Quy Logistic (Logistic Regression) & Phân Loại Softmax (Softmax Regression)
- **2.4** Thuật Toán Perceptron & Định Lý Hội Tụ Novikoff
- **2.5** Máy Vector Hỗ Trợ (Support Vector Machine - SVM, Hard/Soft Margin, Hinge Loss, Kernel Trick)
- **2.6** Cây Quyết Định (Decision Tree, Entropy, Information Gain, Gini Impurity, Cắt Tỉa Pruning)
- **2.7** Rừng Ngẫu Nhiên (Random Forest, Bagging, Out-of-Bag OOB, Feature Importance)
- **2.8** Thuật Toán XGBoost & Gradient Boosting Decision Trees (Khai triển Taylor bậc 2, Gain Split, Regularization)
- **2.9** Phân Tích Thành Phần Chính (Principal Component Analysis - PCA, Covariance, Eigenvalues, SVD)
- **2.10** Toàn Tập Các Hàm Kích Hoạt (Activation Functions)
- **2.11** Toàn Tập Các Hàm Mất Mát (Loss Functions)
- **2.12** Toàn Tập Các Độ Đo Đánh Giá (Evaluation Metrics)
- **2.13** Thuật Toán Tối Ưu (Optimizers) & Bùng Nổ / Triệt Tiêu Gradient
- **2.14** Mạng Nơ-ron Cơ Bản & Chuỗi Tuần Hoàn (MLP, Backpropagation, RNN, LSTM, GRU)
- **2.15** Phân Loại Đa Nhãn (Multi-Label Classification) & Kiến Trúc C2AE

## 4. Các Bước Thực Hiện
- [x] Bước 1: Khảo sát tài liệu `resources/machine-learning/` và mã nguồn `interview/index.html`, `script.js`, `style.css`.
- [ ] Bước 2: Thiết kế nội dung chi tiết cho từng thuật toán ML theo chuẩn `lecture-visualizer` (Từ điển ký hiệu, Trực giác, Công thức toán KaTeX, Trace số học trên Toy Dataset, Hộp thoại người học chậm, Bảng đối chiếu, Resource pills).
- [ ] Bước 3: Cập nhật Sidebar Navigation trong `interview/index.html` (đánh số 2.1 -> 2.15).
- [ ] Bước 4: Chèn các khối nội dung ML chất lượng cao (2.2 -> 2.9) và tinh chỉnh 2.1 trong `interview/index.html`.
- [ ] Bước 5: Cập nhật các ID mục sau đó (2.10 -> 2.15) để đồng bộ neo liên kết và ScrollSpy.
- [ ] Bước 6: Cập nhật `interview/script.js` và `interview/style.css` nếu cần cho widget tương tác thuật toán ML (ví dụ: Interactive ML Playground / Decision Boundary / PCA variance calculator).
- [ ] Bước 7: Kiểm tra tính toàn vẹn cú pháp HTML, kiểm tra KaTeX rendering, kiểm tra liên kết neo (anchors) và tài nguyên.
