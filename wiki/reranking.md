# Xếp Hạng Lại (Reranking & Cross-Encoders)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 13.4.2; Nogueira & Cho (2019) *"Passage Re-ranking with BERT"*; *english_GiaiThichThuatNguRAG.pdf*.
> **Miền kiến thức**: [[index|Post-Retrieval Optimization]]
> **Tài liệu gốc liên quan**:
> - [english_GiaiThichThuatNguRAG.pdf](../resources/genai/english_GiaiThichThuatNguRAG.pdf) (Trang 10-15)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 125-126)
> - [AIO2026_[Reading]-RAG-System.pdf](../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 85-98)

---

## 1. Tóm tắt (Executive Summary)
**Xếp hạng lại (Reranking)** là giai đoạn tối ưu hóa sau truy xuất (Post-Retrieval) sử dụng mô hình **Cross-Encoder** có độ chính xác cao để tính toán lại điểm số tương quan giữa câu hỏi của người dùng và danh sách các đoạn văn bản ứng viên (thường là Top 50-100) được lấy về từ bước tìm kiếm ban đầu. Trong khi Bi-Encoder (dùng trong vector search) mã hóa câu hỏi và tài liệu độc lập với nhau, Cross-Encoder cho phép câu hỏi và tài liệu tương tác chéo hoàn toàn qua cơ chế All-to-All Self-Attention, giúp lọc sạch các đoạn thông tin nhiễu và đưa những tài liệu giá trị nhất lên vị trí dẫn đầu (Top 3-5) trước khi chuyển cho LLM tạo câu trả lời.

---

## 2. Định nghĩa chính thống & Kiến trúc So sánh (Bi-Encoder vs Cross-Encoder)

### 2.1 Bản chất kiến trúc
1. **Bi-Encoder (Retrieval Stage)**:
   - Câu hỏi $q$ và văn bản $d$ được đưa vào mô hình độc lập: $u = \text{Encoder}(q)$, $v = \text{Encoder}(d)$.
   - Điểm số tương đồng: $s(q, d) = \langle u, v \rangle$.
   - *Ưu điểm*: Các vector $v$ của hàng triệu tài liệu có thể tính toán trước offline và đánh chỉ mục ANN. Thời gian tìm kiếm chỉ mất vài mili-giây.
   - *Nhược điểm*: Không có sự giao tiếp token-to-token giữa câu hỏi và văn bản; dễ bỏ sót các sắc thái ngữ cảnh tinh tế.
2. **Cross-Encoder (Reranking Stage)**:
   - Ghép cặp trực tiếp: $\text{Input} = [\text{CLS}] \circ q \circ [\text{SEP}] \circ d \circ [\text{EOS}]$.
   - Toàn bộ chuỗi được nạp qua các tầng Transformer. Mọi token trong câu hỏi $q$ được tự do tính toán ma trận Attention với mọi token trong văn bản $d$.
   - Điểm số: $s(q, d) = \text{Sigmoid}(W \cdot h_{[\text{CLS}]})$.

```mermaid
flowchart TD
    subgraph Bi-Encoder Architecture (Fast Retrieval)
        Q1["Query q"] --> EncQ["Encoder"] --> VecQ["Vector u"]
        D1["Doc d"] --> EncD["Encoder"] --> VecD["Vector v"]
        VecQ --> Dot["Dot Product"]
        VecD --> Dot
        Dot --> Score1["Approximate Similarity Score"]
    end
    
    subgraph Cross-Encoder Architecture (Deep Reranking)
        Pair["[CLS] Query [SEP] Document [EOS]"] --> FullTrans["Full Transformer Layers (All-to-All Self Attention)"]
        FullTrans --> CLS["[CLS] Hidden State"]
        CLS --> Classifier["Linear Layer + Sigmoid"]
        Classifier --> DeepScore["Precise Relevance Score (0.0 to 1.0)"]
    end
```

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Đặc tính | Bi-Encoder (Embedding Retrieval) | Cross-Encoder (Reranker) | Nhận định kiến trúc hệ thống |
| :--- | :--- | :--- | :--- |
| **Độ phức tạp thời gian** | $\mathcal{O}(1)$ tìm kiếm láng giềng gần đúng qua ANN Index. | $\mathcal{O}(K \cdot L^2)$ với $K$ là số chunk ứng viên, $L$ là tổng độ dài cặp text. | Không thể dùng Cross-Encoder để tìm kiếm trên toàn bộ triệu tài liệu vì độ trễ sẽ lên tới hàng chục giây. |
| **Độ chính xác tương quan** | Trung bình khá (khoảng 60-70% MRR). | Cực kỳ cao (> 85-90% MRR). | Mô hình hai tầng (Two-Stage Retrieval: Bi-Encoder kéo Top-100 $\rightarrow$ Cross-Encoder lọc lấy Top-5) là tiêu chuẩn vàng tối ưu giữa tốc độ và độ chính xác. |
| **Khả năng nhận diện ngữ cảnh phủ định** | Rất kém (dễ nhầm lẫn câu mang nghĩa đối lập vì cùng từ vựng). | Xuất sắc (cơ chế Attention phân tích rõ câu phủ định và điều kiện biên). | Reranker giải quyết triệt để vấn đề "bẫy từ đồng âm khác nghĩa" và phủ định trong văn bản luật/y tế. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Lựa chọn Reranker Model trong Thực tế
1. **Mô hình mã nguồn mở (Self-hosted)**:
   - `BAAI/bge-reranker-large` / `bge-reranker-v2-m3`: Hỗ trợ đa ngôn ngữ xuất sắc (bao gồm tiếng Việt), có thể chạy mượt mà trên 1 GPU nhỏ hoặc qua ONNX Runtime trên CPU.
2. **Mô hình thương mại (SaaS API)**:
   - `Cohere Rerank-v3`: Hỗ trợ nén ngữ cảnh và tính toán độ tương quan cao cấp, thích hợp cho doanh nghiệp không muốn duy trì hạ tầng GPU riêng.

### 4.2 Tối ưu hóa Context Window & Giảm chi phí LLM
Thay vì nạp 20 chunks (khoảng 8.000 token) lấy từ vector search vào LLM:
- Reranker lọc danh sách xuống còn 3 chunks xuất sắc nhất (khoảng 1.200 token).
- **Kết quả**:
  - Giảm 85% chi phí gọi API LLM.
  - Giảm độ trễ Time-to-First-Token của LLM.
  - Loại bỏ hoàn toàn hiện tượng **Lost-in-the-Middle** (LLM bị nhiễu loạn khi nhồi quá nhiều văn bản thừa).

### 4.3 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao không huấn luyện Bi-Encoder tốt hơn nữa để thay thế hoàn toàn Cross-Encoder nhằm tiết kiệm thời gian?*
  - **A**: Về mặt lý thuyết thông tin, Bi-Encoder buộc phải nén toàn bộ ngữ nghĩa phong phú của một đoạn văn bản phức tạp thành một vector có số chiều hữu hạn cố định (như 768 hoặc 1536 float). Sự nén thông tin độc lập này làm mất đi khả năng đối chiếu từng từ giữa câu hỏi và câu trả lời. Chỉ có cơ chế All-to-All Attention của Cross-Encoder mới có thể nắm bắt được sự phụ thuộc phức tạp này. Do đó, mô hình hai tầng (Two-Stage Pipeline) là nguyên lý kiến trúc tối ưu không thể thay thế.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & `wiki-links`)
- [[rag-architecture]] — Tầng áp dụng Reranking trong quy trình xử lý.
- [[hybrid-search]] — Cung cấp danh sách ứng viên đầu vào cho Reranker.
- [[vector-embeddings]] — Phân định ranh giới giữa Bi-Encoder và Cross-Encoder.
- [[inference-optimization-tensorrt]] — Tối ưu hóa tốc độ suy luận của mô hình Cross-Encoder trên GPU.