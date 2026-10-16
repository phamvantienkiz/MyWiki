# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = Path("wiki")
WIKI_DIR.mkdir(parents=True, exist_ok=True)

ENTITIES = {
    "rag-architecture.md": r"""# Kiến Trúc RAG (Retrieval-Augmented Generation Architecture)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Chapter 13 (Sections 13.1 - 13.6); Lewis et al. (2020) *"Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"*; Gao et al. (2023) *"Retrieval-Augmented Generation for Large Language Models: A Survey"*.
> **Miền kiến thức**: [[rag-overview|Retrieval-Augmented Generation & Information Retrieval]]
> **Tài liệu gốc liên quan**:
> - [giao_trinh_rag.pdf](../../resources/genai/giao_trinh_rag.pdf) (Trang 1-16)
> - [AIO2025_Tutorial_RAG.pdf](../../resources/genai/AIO2025_Tutorial_RAG.pdf) (Trang 1-33)
> - [AIO2026_[Reading]-RAG-System.pdf](../../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 1-113)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 121-128)
> - [english_GiaiThichThuatNguRAG.pdf](../../resources/genai/english_GiaiThichThuatNguRAG.pdf) (Trang 1-16)

---

## 1. Tóm tắt (Executive Summary)
**Kiến trúc Tạo sinh Tăng cường Truy xuất (Retrieval-Augmented Generation - RAG)** là mô hình kiến trúc AI kết hợp năng lực truy xuất thông tin phi tham số (non-parametric retrieval) từ các kho cơ sở dữ liệu bên ngoài với năng lực suy luận và ngôn ngữ tham số (parametric language model) của LLM. Bằng cách neo câu trả lời vào các tài liệu thực tế được truy xuất theo thời gian thực tại thời điểm suy luận, RAG giải quyết triệt để 3 tử huyệt cố hữu của LLM: **ảo giác sự thật (hallucination)**, **kiến thức lỗi thời (knowledge cutoff)**, và **thiếu minh bạch nguồn gốc (lack of explainability / citations)**.

---

## 2. Định nghĩa chính thống & Sự tiến hóa Kiến trúc (Canonical Architecture Evolution)

### 2.1 Định nghĩa nền tảng (Lewis et al., 2020)
Trong mô hình RAG chính thống, xác suất sinh chuỗi câu trả lời $y = (y_1, ..., y_N)$ dựa trên câu hỏi $x$ được mô hình hóa biên qua tập tài liệu ẩn $z \in \mathcal{Z}$ được truy xuất:
$$P(y|x) = \sum_{z \in \text{Top-K}(\mathcal{Z})} P_\eta(z|x) \prod_{i=1}^N P_\theta(y_i | x, z, y_{<i})$$
Trong đó:
- $P_\eta(z|x)$ là **Mô-đun Truy xuất (Retriever)** tham số hóa bởi $\eta$ (ví dụ: Bi-Encoder BERT/DPR), tính xác suất tài liệu $z$ liên quan tới câu hỏi $x$.
- $P_\theta(y_i | x, z, y_{<i})$ là **Mô-đun Tạo sinh (Generator)** tham số hóa bởi $\theta$ (ví dụ: BART, LLaMA, GPT), sinh token dựa trên liên kết giữa câu hỏi, tài liệu ngữ cảnh $z$ và các token đã sinh.

```mermaid
flowchart TD
    subgraph Pre-Retrieval
        RawDocs["Unstructured Raw Documents"] --> Chunking["[[document-chunking|Chunking Strategy]]"]
        Chunking --> Embed["[[vector-embeddings|Embedding Model]]"]
        Embed --> VDB[("Vector Database / ANN Index")]
    end
    
    subgraph Online Query Phase
        Query["User Query"] --> Transform["[[query-transformation|Query Transformation / HyDE]]"]
        Transform --> Search["[[hybrid-search|Hybrid Search (Dense + BM25)]]"]
        VDB -.-> Search
        Search --> TopK["Top-K Candidate Chunks"]
        TopK --> Rerank["[[reranking|Cross-Encoder Reranker]]"]
        Rerank --> TopM["Top-M Filtered Context"]
        TopM --> Prompt["Prompt Synthesis (Query + Context)"]
        Prompt --> LLM["[[large-language-models|LLM Generator]]"]
        LLM --> Out["Grounded Answer + Citations"]
    end
```

### 2.2 4 Thế hệ Kiến trúc RAG
1. **Naive RAG (RAG Nguyên thủy)**: Luồng tuần tự thô sơ: `Chunking cố định -> Embedding -> Vector Search Cosine Top-K -> Bơm vào Prompt -> Sinh kết quả`. *Nhược điểm*: Rất dễ trích xuất sai ngữ cảnh (Low Precision), trôi dạt ngữ nghĩa và nuốt chửng thông tin rải rác.
2. **Advanced RAG (RAG Nâng cao)**: Bổ sung 2 tầng then chốt:
   - *Pre-retrieval*: [[query-transformation|Query Expansion, Sub-queries, HyDE]], tối ưu hóa chunking theo cấu trúc.
   - *Post-retrieval*: [[reranking|Cross-Encoder Reranking]], Context Compression, lọc nhiễu trước khi nạp vào LLM.
3. **Modular RAG (RAG Module hóa)**: Kiến trúc phân rã thành các dịch vụ độc lập có thể cắm-rút (Pluggable modules): Search module, Memory module, Routing module, Predict module.
4. **Agentic RAG (RAG Tác nhân)**: LLM hoạt động như một bộ não điều phối ([[agentic-ai-core|Agentic AI]]), tự quyết định khi nào cần tra cứu, tra cứu ở nguồn nào (Vector DB, SQL DB hay Web Search), tự đánh giá xem tài liệu lấy về đã đủ trả lời chưa, và thực hiện truy xuất lặp nhiều chặng (Multi-hop Reasoning).

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Khía cạnh | Tài liệu giáo trình cơ bản (`giao_trinh_rag.pdf`) | Tài liệu chuyên sâu (`Encyclopedia of LLMs` & Production) | Phân tích của AI Engineer |
| :--- | :--- | :--- | :--- |
| **Công cụ tìm kiếm cốt lõi** | Coi Vector Database và Cosine Similarity là trái tim duy nhất của RAG. | Khẳng định Vector Search đơn lẻ thất bại thảm hại trong môi trường doanh nghiệp; bắt buộc phải là **Hybrid Search (Dense + BM25)** kết hợp **Reranker**. | Vector search giỏi hiểu ý nghĩa tổng quát (semantic) nhưng bất lực trước mã số, số hiệu, mã SKU hay tên riêng chính xác. Cần kết hợp từ khóa truyền thống. |
| **Giải quyết bài toán Context dài** | Khuyên dùng RAG cho mọi tình huống để tiết kiệm token và bộ nhớ. | Tranh luận với việc các mô hình mở rộng Context Window lên 1M - 2M tokens (Gemini 1.5, LLaMA 3.1): *"Context dài có giết chết RAG?"* | RAG không chết mà chuyển hóa: Context 1M token quá đắt đỏ và chậm cho hàng triệu query mỗi ngày; RAG đóng vai trò bộ lọc định tuyến (Routing Filter) để chọn ra 10k-50k token tinh túy nhất cho mô hình lớn. |
| **Trích dẫn nguồn (Attribution)** | Cho rằng có RAG là tự động loại bỏ 100% ảo giác và luôn trích dẫn đúng. | Chỉ ra nguy cơ **Attribution Hallucination**: LLM tạo ra câu trả lời dựa trên định kiến tiền huấn luyện (parametric bias) nhưng lại gắn tag trích dẫn giả mạo vào tài liệu đính kèm. | Phải có cơ chế kiểm tra chéo (Fact-Checking / Faithfulness Verification) bằng framework như Ragas hoặc Guardrails độc lập. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy tắc triển khai Production RAG (The Production Rules)
1. **Garbage In, Garbage Out**: 80% thành bại của RAG nằm ở chất lượng làm sạch dữ liệu trước khi chunking (loại bỏ header/footer lặp lại trong PDF, chuẩn hóa bảng biểu HTML/Markdown, tách bảng metadata).
2. **Kích thước Chunking**: Không bao giờ dùng một kích thước chunking cho toàn bộ tài nguyên. Hãy phối hợp kỹ thuật **Parent-Document Retrieval** (truy xuất chunk nhỏ 200 token để vector match chuẩn xác, nhưng nạp chunk cha 1.000 token vào context của LLM).
3. **Luôn sử dụng Reranker**: Thêm một Cross-Encoder nhỏ (như `bge-reranker-large` hoặc Cohere Rerank) tăng tỷ lệ Hit-Rate của hệ thống từ 60% lên trên 90%.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Khi nào hệ thống RAG nên trả về "Tôi không biết" thay vì cố gắng trả lời? Thiết kế cơ chế đó thế nào?*
  - **A**: Khi điểm số tương đồng sau bước Reranking của toàn bộ các chunk ứng viên đều thấp hơn một ngưỡng tin cậy xác định ($Score < \tau$), hoặc khi hàm đo Faithfulness phát hiện câu trả lời sinh ra không có căn cứ từ Context. Lúc này hệ thống phải kích hoạt kịch bản fallback rõ ràng để bảo toàn tính trung thực nghiệp vụ.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[document-chunking]] — Kỹ thuật phân tách tài liệu nguồn.
- [[vector-embeddings]] — Biểu diễn toán học của văn bản trong không gian vector.
- [[hybrid-search]] — Kết hợp truy xuất ngữ nghĩa và truy xuất từ khóa chính xác.
- [[reranking]] — Tầng lọc và xếp hạng lại tài liệu tối thượng.
- [[query-transformation]] — Tái cấu trúc câu hỏi người dùng trước khi truy xuất.
- [[graph-rag]] — Kết hợp đồ thị tri thức để giải quyết bài toán suy luận tổng thể toàn kho dữ liệu.
- [[llm-evaluation]] — Đánh giá RAG thông qua bộ chỉ số Ragas (Faithfulness, Context Relevance).
""",

    "document-chunking.md": r"""# Chiến Lược Phân Đoạn Tài Liệu (Document Chunking Strategies)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 13.3; *TOP RAG CHUNKING METHODS YOU SHOULD* (Mouka, 2025); *giao_trinh_rag.pdf*.
> **Miền kiến thức**: [[rag-overview|RAG Pre-processing & Data Ingestion]]
> **Tài liệu gốc liên quan**:
> - [TOP RAG CHUNKING METHODS YOU SHOULD.pdf](../../resources/genai/TOP%20RAG%20CHUNKING%20METHODS%20YOU%20SHOULD.pdf) (Trang 1-25)
> - [giao_trinh_rag.pdf](../../resources/genai/giao_trinh_rag.pdf) (Trang 4-8)
> - [AIO2026_[Reading]-RAG-System.pdf](../../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 20-38)

---

## 1. Tóm tắt (Executive Summary)
**Phân đoạn Tài liệu (Document Chunking)** là kỹ thuật phân tách các văn bản dài phi cấu trúc thành các đơn vị thông tin nhỏ hơn (chunks) có ý nghĩa ngữ nghĩa độc lập trước khi tạo vector embedding và lưu trữ vào cơ sở dữ liệu vector. Chunking quyết định trực tiếp đến **Độ chính xác truy xuất (Retrieval Precision)** và **Ngữ cảnh tạo sinh (Generation Context)**. Kỹ thuật chunking đã phát triển từ phân tách độ dài ký tự cố định thô sơ sang phân đoạn đệ quy theo cấu trúc cú pháp, phân đoạn ngữ nghĩa thích ứng (Semantic Chunking) và phân đoạn phân tầng cha-con (Parent-Document / Small-to-Big Retrieval).

---

## 2. Định nghĩa chính thống & Các phương pháp Chunking cốt lõi

### 2.1 Đánh đổi then chốt trong kích thước Chunk (The Chunk Size Trade-off)
- **Chunk quá nhỏ (50-100 tokens)**: Độ tương đồng vector với câu truy vấn rất cao vì embedding tập trung, nhưng làm mất đứt gãy ngữ cảnh xung quanh, khiến LLM không đủ thông tin để trả lời.
- **Chunk quá lớn (1000-2000 tokens)**: Ngữ cảnh phong phú nhưng vector embedding bị loãng (diluted embedding) do chứa quá nhiều chủ đề hỗn tạp, khiến thuật toán tìm kiếm tương đồng dễ bỏ qua.
- **Chunk Overlap (Độ gối đầu)**: Thường thiết lập từ 10% đến 20% kích thước chunk để tránh việc một câu văn quan trọng bị cắt đôi ngay giữa chừng.

```mermaid
flowchart TD
    Doc["Full Document / PDF"] --> Strategy{Chunking Method}
    Strategy -->|"1. Fixed-Size"| Fixed["Fixed Character / Token Length (e.g. 500 chars + 50 overlap)"]
    Strategy -->|"2. Recursive"| Recursive["Split by Hierarchy: \n\n -> \n -> Space -> Char"]
    Strategy -->|"3. Semantic"| Semantic["Calculate Embedding Distance between consecutive sentences; Split on Spikes"]
    Strategy -->|"4. Hierarchical"| Parent["Small Child Chunks (Index) linked to Parent Chunk (Context)"]
```

### 2.2 Chi tiết 5 phương pháp Chunking chuẩn mực
1. **Fixed-Size Chunking with Overlap**:
   - Cắt văn bản sau mỗi $K$ ký tự hoặc token, gối đầu $M$ token. Đơn giản nhất nhưng dễ phá vỡ cấu trúc câu và đoạn văn.
2. **Recursive Character Chunking (LangChain Standard)**:
   - Cắt đệ quy theo danh sách phân tách ưu tiên: `["\n\n", "\n", " ", ""]`. Thuật toán cố gắng giữ nguyên vẹn đoạn văn (paragraph); nếu đoạn quá dài mới cắt theo câu, nếu câu quá dài mới cắt theo từ.
3. **Document-Structure / Markdown-Aware Chunking**:
   - Tôn trọng ngữ nghĩa tài liệu: Tách theo tiêu đề Heading (`#`, `##`, `###`), phần tử bảng biểu HTML, danh sách gạch đầu dòng hoặc khối mã nguồn. Thêm breadcrumbs metadata (e.g., `Header 1 > Subheader 2`) vào đầu mỗi chunk.
4. **Semantic Chunking (Phân đoạn Ngữ nghĩa Động)**:
   - Chia văn bản thành các câu riêng biệt, tính vector embedding cho từng câu.
   - Tính khoảng cách cosine giữa câu $i$ và câu $i+1$. Khi khoảng cách vượt qua ngưỡng độ lệch chuẩn (threshold percentile), hệ thống xác định có sự chuyển đổi chủ đề (topic shift) và đặt điểm cắt đoạn tại đó.
5. **Parent-Document / Small-to-Big Chunking**:
   - Chia tài liệu thành các khối cha lớn (1.000 token). Mỗi khối cha lại được chia nhỏ thành 5-10 khối con (100-200 token).
   - Chỉ lưu vector nhúng của các khối con vào Vector DB để tìm kiếm (tối ưu hóa Retrieval Precision). Nhưng khi truy xuất trúng khối con, hệ thống nạp toàn bộ khối cha tương ứng vào context cho LLM (tối ưu hóa Generation Context).

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Phương pháp | Chi phí tính toán | Khả năng bảo toàn ngữ nghĩa | Độ phức tạp triển khai | Phù hợp nhất cho |
| :--- | :--- | :--- | :--- | :--- |
| **Fixed-Size** | Rất thấp ($\mathcal{O}(N)$ chuỗi). | Rất kém. | Tối thiểu. | Dữ liệu thô sơ, kiểm thử nhanh ban đầu (PoC). |
| **Recursive Text** | Thấp. | Tốt cho văn bản thông thường. | Thấp. | Sách truyện, bài báo tin tức thông thường. |
| **Markdown / Structure** | Thấp đến trung bình. | Rất cao với tài liệu kỹ thuật, báo cáo. | Trung bình (cần parser chuẩn). | Tài liệu hướng dẫn, API docs, báo cáo tài chính. |
| **Semantic Chunking** | Rất cao (phải gọi embedding cho từng câu). | Xuất sắc cho văn bản biến chuyển nhiều chủ đề. | Cao. | Biên bản họp, bài phát biểu, diễn đàn trao đổi. |
| **Parent-Document** | Trung bình. | Toàn diện nhất (giải quyết triệt để trade-off). | Trung bình. | **Tiêu chuẩn vàng cho Enterprise Production RAG**. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Bẫy bảng biểu và dữ liệu có cấu trúc trong PDF
- Khi xử lý bảng biểu trong PDF báo cáo tài chính: Nếu dùng Recursive Chunking thông thường, các dòng trong bảng sẽ bị xé lẻ thành các đoạn vô nghĩa (ví dụ: dòng số liệu bị tách khỏi tiêu đề cột).
- **Giải pháp**:
  - Dùng công cụ bóc tách chuyên biệt (như `Marker`, `Unstructured`, `PyMuPDF`) để nhận diện bảng và chuyển đổi nguyên vẹn bảng sang định dạng **Markdown Table** hoặc **HTML Table**.
  - Không bao giờ cắt ngang một bảng biểu nếu kích thước của bảng nhỏ hơn context window cho phép.
  - Sinh thêm một đoạn văn bản tóm tắt nội dung bảng đính kèm làm metadata để hỗ trợ tìm kiếm ngữ nghĩa.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao Semantic Chunking dù rất thông minh trên lý thuyết nhưng lại ít khi được dùng cho các kho dữ liệu hàng triệu văn bản trong thực tế?*
  - **A**: Vì rào cản chi phí và thời gian tính toán (Computational Latency): Việc phải tính embedding riêng cho hàng trăm triệu câu văn đơn lẻ và so sánh khoảng cách liên tục tiêu tốn tài nguyên GPU khổng lồ, khiến quá trình Ingestion dữ liệu bị nghẽn (bottleneck). Trong thực tế sản xuất, Recursive Chunking kết hợp Markdown Header và Parent-Document mang lại tỷ lệ chi phí/hiệu quả (ROI) vượt trội hơn hẳn.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[rag-architecture]] — Nơi chunking đóng vai trò bước xử lý tiền đề sống còn.
- [[vector-embeddings]] — Biến đổi các chunk thành vector toán học.
- [[hybrid-search]] — Truy xuất các chunk qua vector và từ khóa.
- [[reranking]] — Tinh lọc các chunk ứng viên sau khi truy xuất.
""",

    "vector-embeddings.md": r"""# Vector Nhúng và Tìm Kiếm Tương Đồng (Vector Embeddings & Similarity Search)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 13.2 - 13.3; *Mathematics for Machine Learning*, Chapter 3 (Analytic Geometry & Inner Products); Malkov & Yashunin (2018) *"Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs" (HNSW)*.
> **Miền kiến thức**: [[rag-overview|Vector Embeddings & ANN Search]]
> **Tài liệu gốc liên quan**:
> - [giao_trinh_rag.pdf](../../resources/genai/giao_trinh_rag.pdf) (Trang 8-12)
> - [Mathematics-for-Machine-Learning.pdf](../../resources/machine-learning/Mathematics-for-Machine-Learning.pdf) (Trang 70-95)
> - [AIO2026_[Reading]-RAG-System.pdf](../../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 40-60)

---

## 1. Tóm tắt (Executive Summary)
**Vector Nhúng (Vector Embeddings)** là phép ánh xạ từ các thực thể ngữ nghĩa phức tạp (từ ngữ, câu văn, hình ảnh, âm thanh) vào các vector số thực trong không gian đa chiều liên tục $\mathbb{R}^d$ ($d$ thường từ 384 đến 3072 chiều) sao cho khoảng cách hình học hoặc góc giữa các vector phản ánh chính xác mức độ tương đồng ngữ nghĩa. Để tìm kiếm siêu tốc trong kho hàng triệu đến hàng tỷ vector nhúng, các giải thuật **Tìm kiếm Láng giềng Gần đúng (Approximate Nearest Neighbors - ANN)** như **HNSW** và **IVF-Flat** được sử dụng để đánh đổi một sai số nhỏ không đáng kể lấy tốc độ truy xuất nhanh gấp hàng ngàn lần so với tìm kiếm vét cạn ($k$-NN).

---

## 2. Định nghĩa chính thống & Độ đo Hình học (Geometric Measures & Algorithms)

### 2.1 Các độ đo khoảng cách tương đồng
Cho hai vector nhúng $u, v \in \mathbb{R}^d$:
1. **Cosine Similarity**: Đo góc giữa hai vector, không phụ thuộc vào độ dài (magnitude):
   $$\text{Cosine}(u, v) = \frac{\langle u, v \rangle}{\|u\|_2 \|v\|_2} = \frac{\sum_{i=1}^d u_i v_i}{\sqrt{\sum_{i=1}^d u_i^2} \sqrt{\sum_{i=1}^d v_i^2}}$$
2. **Dot Product (Tích vô hướng)**: Khi các vector đã được chuẩn hóa độ dài đơn vị ($\|u\|_2 = \|v\|_2 = 1$), Dot Product tương đương tuyệt đối với Cosine Similarity nhưng có tốc độ tính toán nhanh hơn nhiều vì bỏ qua bước chia căn bậc hai:
   $$\text{DotProduct}(u, v) = u^T v = \sum_{i=1}^d u_i v_i$$
3. **Euclidean Distance ($L_2$ Distance)**: Khoảng cách hình học Euclid:
   $$d_{L_2}(u, v) = \sqrt{\sum_{i=1}^d (u_i - v_i)^2}$$

```mermaid
flowchart TD
    subgraph ANN Indexing Strategies
        Flat["Flat Index (Exact k-NN, O(N), 100% Recall, Very Slow)"]
        IVF["IVF (Inverted File Index: Voronoi Cells, Fast, Medium Recall)"]
        HNSW["HNSW (Multi-layer Navigable Small World Graph, O(log N), High Recall, Production Standard)"]
    end
    Query["Query Vector"] --> HNSW
    HNSW --> Result["Top-K Approximate Nearest Neighbors in < 5ms"]
```

### 2.2 Thuật toán HNSW (Hierarchical Navigable Small World)
HNSW là thuật toán ANN đồ thị phân tầng thống trị toàn bộ các Vector Database hiện đại (Milvus, Qdrant, Pinecone, pgvector):
- Xây dựng một đồ thị gồm nhiều tầng (layers) tương tự như cấu trúc dữ liệu **Skip-List**:
  - Tầng trên cùng có ít điểm nút, các cạnh liên kết rất dài, dùng để "nhảy cóc" nhanh qua các vùng không gian lớn.
  - Tầng dưới cùng chứa toàn bộ dữ liệu với các liên kết cục bộ dày đặc.
- Khi truy vấn, thuật toán thực hiện tìm kiếm tham lam (greedy search) từ tầng cao nhất, khi chạm cực tiểu cục bộ thì nhảy xuống tầng dưới tiếp tục tìm kiếm cho đến khi tới tầng đáy.
- Độ phức tạp tìm kiếm: $\mathcal{O}(\log N)$, nhanh gấp hàng vạn lần tìm kiếm tuyến tính $\mathcal{O}(N)$.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Thuật ngữ / Đặc tính | Sparse Embeddings (BM25 / SPLADE) | Dense Embeddings (OpenAI, BGE, Cohere) | Phối hợp trong AI Engineering |
| :--- | :--- | :--- | :--- |
| **Bản chất biểu diễn** | Vector số chiều cực lớn ($V \approx 30.000 - 100.000$) nhưng phần lớn là số 0. Mỗi chiều gắn liền với một từ vựng xác định. | Vector số chiều cố định ($d \in [768, 1536]$), toàn bộ các phần tử đều là số thực liên tục. | Dense embeddings nắm bắt ngữ cảnh, từ đồng nghĩa và ý niệm trừu tượng. Sparse embeddings nắm bắt mã định danh, số liệu và từ khóa hiếm. |
| **Không gian lưu trữ** | Tối ưu qua Inverted Index; rất nhẹ bộ nhớ RAM. | Đòi hỏi RAM/VRAM lớn để lưu ma trận vector phục vụ ANN search. | Kết hợp cả hai trong mô hình [[hybrid-search|Hybrid Search]] để đạt Recall tối đa. |
| **Hiện tượng sụp đổ chiều (Dimensionality Collapse)** | Không bị ảnh hưởng. | Các vector nhúng có xu hướng co cụm vào một nón hẹp (narrow cone) trong không gian, làm giảm hiệu quả phân biệt khoảng cách. | Áp dụng chuẩn hóa độ dài (Normalization) hoặc kỹ thuật Matryoshka Embeddings. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Matryoshka Representation Learning (MRL)
Các mô hình embedding thế hệ mới (như `text-embedding-3-small/large` của OpenAI, `nomic-embed-text`) được huấn luyện bằng MRL:
- Cho phép cắt ngắn vector từ 1536 chiều xuống còn 512 hoặc 256 chiều mà vẫn giữ được 95-98% độ chính xác truy xuất.
- **Lợi ích kinh tế sống còn**: Giảm 3-6 lần chi phí lưu trữ RAM trong Vector DB và tăng tốc độ tính toán dot-product tương ứng.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Khi nào nên dùng Cosine Similarity, và khi nào nên dùng Dot Product hoặc Euclidean Distance trong Vector DB?*
  - **A**: Nếu embedding model xuất ra các vector đã được chuẩn hóa độ dài ($L_2$ normalized, $\|v\| = 1$), thì thứ tự xếp hạng của Cosine Similarity, Dot Product và Euclidean Distance là **hoàn toàn giống nhau** về mặt toán học. Trong trường hợp đó, **bắt buộc chọn Dot Product** vì nó chỉ bao gồm các phép nhân-cộng ma trận không có phép chia căn, cho phép CPU/GPU tận dụng tập lệnh SIMD/Tensor Cores chạy nhanh nhất.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[document-chunking]] — Đơn vị văn bản đầu vào để sinh vector embedding.
- [[hybrid-search]] — Kết hợp Dense Vector với Sparse Inverted Index.
- [[reranking]] — Tinh chỉnh thứ tự sau khi ANN search trả về Top-K ứng viên.
- [[principal-component-analysis]] — Phương pháp toán học giảm số chiều vector cổ điển.
""",

    "hybrid-search.md": r"""# Tìm Kiếm Lai (Hybrid Search: Dense Vector + Sparse BM25)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 13.2.4; Robertson et al. (1994) *"Okapi BM25"*; Cormack et al. (2009) *"Reciprocal Rank Fusion (RRF)"*.
> **Miền kiến thức**: [[rag-overview|Advanced Retrieval Architectures]]
> **Tài liệu gốc liên quan**:
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 123-125)
> - [AIO2026_[Reading]-RAG-System.pdf](../../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 60-80)
> - [english_GiaiThichThuatNguRAG.pdf](../../resources/genai/english_GiaiThichThuatNguRAG.pdf) (Trang 8-12)

---

## 1. Tóm tắt (Executive Summary)
**Tìm kiếm Lai (Hybrid Search)** là phương pháp kết hợp đồng thời hai cơ chế truy xuất bổ trợ nhau: **Tìm kiếm Ngữ nghĩa Dày đặc (Dense Semantic Retrieval)** dựa trên vector nhúng và **Tìm kiếm Từ khóa Thưa thớt (Sparse Lexical Retrieval)** dựa trên thuật toán BM25 / Inverted Index. Bằng cách dung hợp kết quả xếp hạng từ hai luồng thông qua giải thuật **Reciprocal Rank Fusion (RRF)** hoặc kết hợp điểm tuyến tính có trọng số, Hybrid Search giải quyết hoàn hảo bài toán "điểm mù" của vector search (vốn thường bỏ sót các mã lỗi, tên riêng, thuật ngữ chuyên ngành) và điểm mù của keyword search (vốn không hiểu ngữ cảnh và từ đồng nghĩa).

---

## 2. Định nghĩa chính thống & Thuật toán Dung hợp (Algorithms & Mathematical Fusion)

### 2.1 Thuật toán BM25 (Okapi BM25)
Điểm số BM25 của tài liệu $D$ đối với truy vấn $Q = \{q_1, q_2, ..., q_n\}$ được định nghĩa:
$$\text{Score}_{BM25}(D, Q) = \sum_{i=1}^n \text{IDF}(q_i) \cdot \frac{f(q_i, D) \cdot (k_1 + 1)}{f(q_i, D) + k_1 \cdot \left(1 - b + b \cdot \frac{|D|}{\text{avgdl}}\right)}$$
Trong đó:
- $f(q_i, D)$ là tần suất xuất hiện của từ $q_i$ trong tài liệu $D$.
- $|D|$ và $\text{avgdl}$ lần lượt là độ dài tài liệu $D$ và độ dài trung bình của mọi tài liệu trong kho.
- $k_1$ (thường $1.2 - 2.0$) kiểm soát độ bão hòa tần suất từ; $b$ (thường $0.75$) kiểm soát mức độ phạt độ dài văn bản.

```mermaid
flowchart TD
    UserQuery["User Query"] --> DenseBranch["Dense Embedding (Vector Search)"]
    UserQuery --> SparseBranch["Sparse Tokenizer (BM25 / Keyword Search)"]
    
    DenseBranch --> DenseList["Dense Ranked List (Top-K)"]
    SparseBranch --> SparseList["Sparse Ranked List (Top-K)"]
    
    DenseList --> RRF["Reciprocal Rank Fusion (RRF)"]
    SparseList --> RRF
    
    RRF --> FusedOutput["Robust Unified Top-M Results"]
```

### 2.2 Thuật toán Reciprocal Rank Fusion (RRF)
RRF là giải thuật dung hợp thứ hạng không tham số tiêu chuẩn công nghiệp: Không cần chuẩn hóa điểm số khác biệt giữa thang điểm cosine $[0, 1]$ và thang điểm BM25 $[0, \infty)$, RRF chỉ quan tâm đến vị trí thứ hạng (rank) của tài liệu trong mỗi danh sách:
$$\text{RRF\_Score}(d \in \mathcal{D}) = \sum_{m \in \mathcal{M}} \frac{1}{k + r_m(d)}$$
Trong đó:
- $\mathcal{M}$ là tập hợp các bộ truy xuất (ở đây gồm Dense và Sparse).
- $r_m(d)$ là thứ hạng của tài liệu $d$ trong hệ thống truy xuất $m$ ($r \in \{1, 2, 3, ...\}$).
- $k$ là hằng số làm mượt (smoothing constant), thường chọn mặc định $k = 60$ để giảm thiểu sức ảnh hưởng thái quá của các vị trí đứng đầu bảng.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Trường hợp truy vấn | Chỉ dùng Dense Vector Search | Chỉ dùng BM25 Keyword Search | Kết quả của Hybrid Search (RRF) |
| :--- | :--- | :--- | :--- |
| **"Lỗi ngoại lệ NullPointerException tại dòng 42"** | Kém; vector bị trôi dạt vào các bài viết chung chung về lỗi Java. | Xuất sắc; tìm trúng chính xác chuỗi ký tự lỗi và số dòng. | **Thành công vượt trội**: Đưa chính xác đoạn code lỗi lên Top 1. |
| **"Cách làm dịu cơn đau đầu mà không cần dùng thuốc"** | Xuất sắc; hiểu được các ý niệm tương đồng như thư giãn, bấm huyệt, uống nước. | Kém; nếu tài liệu không chứa đúng cụm từ "làm dịu" hay "cơn đau đầu" thì bị loại bỏ. | **Thành công vượt trội**: Bao quát toàn bộ các bài viết liên quan ngữ nghĩa. |
| **Truy vấn đa ngôn ngữ hoặc từ viết tắt** | Hiểu được ngữ cảnh chéo ngôn ngữ. | Thất bại nếu không khớp từ khóa. | Cân bằng hoàn hảo giữa độ chính xác và độ bao phủ. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Trọng số Alpha Tuning (Weighted Score Fusion)
Bên cạnh RRF, một số hệ thống (như Qdrant, Elasticsearch, Weaviate) hỗ trợ dung hợp tuyến tính:
$$\text{Score}_{\text{Hybrid}} = \alpha \cdot \text{Score}_{\text{Dense}} + (1 - \alpha) \cdot \text{Score}_{\text{Sparse}}$$
- Khi $\alpha = 1.0$: Hệ thống trở thành Dense Search thuần túy.
- Khi $\alpha = 0.0$: Hệ thống trở thành Keyword Search thuần túy.
- **Kinh nghiệm thực chiến**: Với các hệ thống tài liệu nội bộ chứa nhiều mã hợp đồng, số hiệu điều luật: Hãy đặt $\alpha \in [0.4, 0.6]$. Với hệ thống hỏi đáp người dùng thông thường: Đặt $\alpha \in [0.7, 0.8]$.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao RRF lại được ưu tiên hơn Weighted Score Fusion trong các hệ thống đa nguồn tìm kiếm phức tạp?*
  - **A**: Vì điểm số (raw score) của các thuật toán khác nhau có phân phối hoàn toàn khác biệt: Cosine bị giới hạn $[-1, 1]$, Dot product không giới hạn, BM25 phụ thuộc vào độ dài văn bản và số lượng tài liệu trong corpus. Việc chuẩn hóa điểm số (Min-Max scaler hay Z-score) rất nhạy cảm với các giá trị ngoại lai (outliers). RRF hoàn toàn miễn nhiễm với vấn đề này vì nó hoạt động thuần túy trên thứ tự xếp hạng (ordinal ranking).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[rag-architecture]] — Khung kiến trúc tổng thể ứng dụng tìm kiếm lai.
- [[vector-embeddings]] — Trụ cột Dense của Hybrid Search.
- [[reranking]] — Tầng kế tiếp nhận đầu ra của Hybrid Search để tái xếp hạng chính xác.
""",

    "reranking.md": r"""# Xếp Hạng Lại (Reranking & Cross-Encoders)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 13.4.2; Nogueira & Cho (2019) *"Passage Re-ranking with BERT"*; *english_GiaiThichThuatNguRAG.pdf*.
> **Miền kiến thức**: [[rag-overview|Post-Retrieval Optimization]]
> **Tài liệu gốc liên quan**:
> - [english_GiaiThichThuatNguRAG.pdf](../../resources/genai/english_GiaiThichThuatNguRAG.pdf) (Trang 10-15)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 125-126)
> - [AIO2026_[Reading]-RAG-System.pdf](../../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 85-98)

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

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[rag-architecture]] — Tầng áp dụng Reranking trong quy trình xử lý.
- [[hybrid-search]] — Cung cấp danh sách ứng viên đầu vào cho Reranker.
- [[vector-embeddings]] — Phân định ranh giới giữa Bi-Encoder và Cross-Encoder.
- [[inference-optimization-tensorrt]] — Tối ưu hóa tốc độ suy luận của mô hình Cross-Encoder trên GPU.
""",

    "query-transformation.md": r"""# Chuyển Đổi Truy Vấn (Query Transformation & Expansion)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 13.4.1; Gao et al. (2023) *"Precise Zero-Shot Dense Retrieval without Relevance Labels" (HyDE)*; *english_GiaiThichThuatNguRAG.pdf*.
> **Miền kiến thức**: [[rag-overview|Pre-Retrieval Optimization]]
> **Tài liệu gốc liên quan**:
> - [english_GiaiThichThuatNguRAG.pdf](../../resources/genai/english_GiaiThichThuatNguRAG.pdf) (Trang 5-9)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 124-126)
> - [AIO2026_[Reading]-RAG-System.pdf](../../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 75-88)

---

## 1. Tóm tắt (Executive Summary)
**Chuyển đổi Truy vấn (Query Transformation)** là tập hợp các kỹ thuật tối ưu hóa trước truy xuất (Pre-Retrieval) nhằm viết lại, phân rã hoặc mở rộng câu hỏi ban đầu của người dùng thành một hoặc nhiều truy vấn tối ưu hơn cho bộ máy tìm kiếm. Trong thực tế, câu hỏi của người dùng thường ngắn ngủi, mơ hồ, sai chính tả hoặc chứa nhiều câu hỏi con lồng ghép. Query Transformation giúp thu hẹp khoảng cách biểu diễn ngữ nghĩa (Semantic Gap) giữa câu hỏi của người dùng và các tài liệu lưu trong kho dữ liệu thông qua các kỹ thuật đột phá như **HyDE (Hypothetical Document Embeddings)**, **Sub-Query Decomposition**, và **Step-Back Prompting**.

---

## 2. Định nghĩa chính thống & Các mô thức Chuyển đổi (Transformation Paradigms)

```mermaid
flowchart TD
    RawQuery["Raw User Query (Short / Ambiguous)"] --> Router{Transformation Strategy}
    Router -->|"HyDE"| GenDoc["LLM generates Hypothetical Answer (Doc')"]
    GenDoc --> EmbedDoc["Embed Doc' and Search VDB"]
    Router -->|"Sub-queries"| Split["Decompose into N atomic Sub-queries"]
    Split --> ParallelSearch["Parallel Search across Data Sources"]
    Router -->|"Step-Back"| Abstract["Generate High-Level Conceptual Question"]
    Abstract --> SearchAbstract["Retrieve Foundational Principles"]
```

### 2.1 Chi tiết các kỹ thuật chuyển đổi chủ đạo
1. **HyDE (Hypothetical Document Embeddings - Gao et al., 2023)**:
   - *Vấn đề*: Câu hỏi ngắn ngủi ("Chính sách hoàn tiền?") và câu trả lời trong tài liệu ("Khách hàng được quyền gửi trả hàng trong 30 ngày...") nằm ở hai vùng không gian vector khác nhau.
   - *Cơ chế*: Dùng một LLM nhỏ sinh ra một "tài liệu giả định" (Hypothetical Document) trả lời câu hỏi đó (dù có thể chứa thông tin chưa chính xác). Sau đó lấy vector nhúng của tài liệu giả định này để đi tìm kiếm trong Vector DB. Do cấu trúc của tài liệu giả định tương đồng với tài liệu thật trong kho, độ trùng khớp vector tăng vọt.
2. **Sub-Query Decomposition (Phân rã Đa truy vấn)**:
   - Áp dụng khi câu hỏi phức tạp chứa nhiều vế so sánh (e.g., *"So sánh doanh thu của Apple và Microsoft quý 3 năm 2024?"*).
   - LLM tự động phân rã thành 2 câu truy vấn độc lập:
     - Sub-query 1: *"Doanh thu Apple quý 3 năm 2024"*
     - Sub-query 2: *"Doanh thu Microsoft quý 3 năm 2024"*
   - Hệ thống tìm kiếm song song cho từng truy vấn rồi gộp kết quả lại.
3. **Step-Back Prompting (Lùi một bước để nhìn tổng thể)**:
   - Đặt một câu hỏi trừu tượng hơn về mặt nguyên lý nền tảng để lấy về các tài liệu khái quát trước khi đi vào tiểu tiết cụ thể.
4. **Query Rewriting with Multi-Turn History**:
   - Trong hội thoại liên tục, khi người dùng hỏi *"Nó giá bao nhiêu?"*, LLM sẽ kết hợp lịch sử chat để viết lại thành: *"Giá bán của sản phẩm iPhone 15 Pro Max là bao nhiêu?"*.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Kỹ thuật | Độ trễ gia tăng (Latency Overhead) | Mức độ cải thiện Recall | Rủi ro tiềm ẩn |
| :--- | :--- | :--- | :--- |
| **Raw Query (Không chuyển đổi)** | 0 ms | Thấp nếu câu hỏi mơ hồ. | Bỏ sót các tài liệu có từ vựng không trùng khớp. |
| **HyDE** | Cao (+300ms đến 1s cho bước sinh văn bản giả định). | Rất cao cho các câu hỏi mở, câu hỏi khái niệm. | Nếu LLM sinh ra tài liệu giả định bị ảo giác đi chệch hướng hoàn toàn, vector search sẽ bị kéo theo hướng sai (Drift). |
| **Sub-Query Decomposition** | Trung bình (+200ms cho phân rã, tìm kiếm chạy song song). | Xuất sắc cho các bài toán phân tích phức tạp. | Bùng nổ số lượng chunk trả về, làm quá tải bước Reranking. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Routing thông minh: Không áp dụng HyDE bừa bãi
- **Quy tắc vàng**:
  - Không bao giờ chạy HyDE cho các truy vấn tra cứu sự thật đơn giản (Factoid Queries) hoặc tra cứu mã SKU, mã nhân viên (e.g., *"Mã số thuế của công ty X"*), vì LLM sẽ bịa ra một mã số giả làm lệch kết quả tìm kiếm.
  - Thiết kế một tầng **Query Classifier / Router** (dùng rule-based hoặc model cực nhỏ 0.5B):
    - Câu hỏi khái niệm/mở $\rightarrow$ Định tuyến sang HyDE.
    - Câu hỏi so sánh đa thực thể $\rightarrow$ Định tuyến sang Sub-Query Decomposition.
    - Câu hỏi mã định danh/từ khóa $\rightarrow$ Chuyển thẳng tới [[hybrid-search|Hybrid Search]].

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao HyDE lại hiệu quả ngay cả khi câu trả lời giả định do LLM sinh ra có chứa thông tin sai sự thật (hallucination)?*
  - **A**: Vì mô hình embedding không kiểm tra tính đúng sai của sự thật, mà mã hóa **phong cách ngữ pháp, trường từ vựng và chủ đề liên quan (topical & stylistic structure)**. Một văn bản giả định về chủ đề "luật lao động" sẽ có phân phối từ vựng và cấu trúc ngữ nghĩa rất gần với văn bản luật lao động thật trong cơ sở dữ liệu, giúp vector search rơi đúng vào cụm láng giềng liên quan.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[rag-architecture]] — Tầng tiền xử lý truy vấn trong quy trình RAG.
- [[hybrid-search]] — Nơi tiếp nhận các câu truy vấn đã được chuyển đổi.
- [[vector-embeddings]] — Cơ chế đo khoảng cách mà HyDE tác động trực tiếp.
- [[prompt-engineering]] — Kỹ thuật thiết kế prompt để viết lại câu hỏi và phân rã truy vấn.
""",

    "graph-rag.md": r"""# Graph RAG và Đồ Thị Tri Thức (Graph RAG & Knowledge Graphs)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 13.6.2; Edge et al. (2024, Microsoft Research) *"From Local to Global: A Graph RAG Approach to Query-Focused Summarization"*; *Deep-Learning-on-Graphs* (Ma & Tang, Cambridge).
> **Miền kiến thức**: [[rag-overview|Advanced Knowledge Representation & Graph Systems]]
> **Tài liệu gốc liên quan**:
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 126-128)
> - [Deep-Learning-on-Graphs.pdf](../../resources/deep-learning/Deep-Learning-on-Graphs.pdf) (Trang 1-45)
> - [AIO2026_[Reading]-RAG-System.pdf](../../resources/genai/AIO2026_%5BReading%5D-RAG-System.pdf) (Trang 95-113)

---

## 1. Tóm tắt (Executive Summary)
**Graph RAG** là kiến trúc RAG thế hệ mới tích hợp **Đồ thị Tri thức (Knowledge Graph - KG)** vào quy trình lập chỉ mục và truy xuất thông tin của LLM. Trong khi Vector RAG truyền thống hoạt động dựa trên sự tương đồng cục bộ của từng đoạn văn bản riêng lẻ (phù hợp cho câu hỏi tìm kiếm điểm hẹp - "Point Queries"), nó hoàn toàn thất bại trước các câu hỏi tổng thể đòi hỏi kết nối thông tin toàn kho dữ liệu (như: *"Các chủ đề chính trong tập tài liệu này là gì?"*). Graph RAG trích xuất các thực thể (Entities), mối quan hệ (Relationships) và phân cụm cộng đồng (Community Detection) để tạo ra các bản tóm tắt phân tầng, cho phép hệ thống thực hiện cả truy xuất suy luận đa chặng (Multi-hop) và tóm tắt toàn cục (Global Sensemaking).

---

## 2. Định nghĩa chính thống & Kiến trúc Microsoft Graph RAG

### 2.1 Quy trình Lập chỉ mục Đồ thị (Graph Indexing Pipeline)
1. **Source Text Chunking**: Phân nhỏ văn bản thành các text units lớn (~1200 tokens).
2. **Entity & Relation Extraction**: Sử dụng LLM để trích xuất toàn bộ các thực thể (Nodes) và quan hệ giữa chúng (Edges), cùng mô tả chi tiết cho từng phần tử:
   $$(E_{\text{source}}, \text{Relationship Description}, E_{\text{target}})$$
3. **Entity Resolution (Giải quyết đồng thực thể)**: Hợp nhất các biến thể tên gọi cùng chỉ một đối tượng (ví dụ: "Bộ Y tế", "BYT", "MOH").
4. **Hierarchical Community Detection (Leiden Algorithm)**: Áp dụng thuật toán Leiden để phát hiện các phân cụm cộng đồng mạng lưới từ vi mô đến vĩ mô.
5. **Community Summarization**: LLM tạo ra các báo cáo tóm tắt toàn diện cho từng cụm cộng đồng ở từng cấp độ phân tầng.

```mermaid
flowchart TD
    RawDocs["Raw Documents"] --> Extract["LLM Entity & Relationship Extraction"]
    Extract --> Graph[("Knowledge Graph: Nodes & Edges")]
    Graph --> Leiden["Leiden Community Detection Algorithm"]
    Leiden --> C1["Community Level 1 Summaries"]
    Leiden --> C2["Community Level 2 Summaries"]
    Leiden --> C3["Community Level 3 Summaries"]
    
    UserQuery["Global Sensemaking Query"] --> MapReduce["Map-Reduce over Community Summaries"]
    C1 --> MapReduce
    C2 --> MapReduce
    MapReduce --> GlobalAnswer["Comprehensive Global Synthesis"]
```

### 2.2 Global Search vs Local Search trong Graph RAG
- **Local Search (Tìm kiếm Cục bộ)**: Dành cho câu hỏi về các thực thể cụ thể (e.g., *"Ai là giám đốc dự án Apollo và họ có mối quan hệ gì với công ty X?"*). Hệ thống tìm kiếm nút thực thể trong đồ thị, lan truyền láng giềng k-hop để lấy các quan hệ liên kết và đoạn văn bản gốc tương ứng.
- **Global Search (Tìm kiếm Toàn cục)**: Dành cho câu hỏi tổng thể (e.g., *"Những rủi ro địa chính trị lớn nhất được nhắc tới trong kho hồ sơ này là gì?"*). Hệ thống thực hiện quy trình Map-Reduce trên các bản tóm tắt cộng đồng (Community Summaries) mà không cần quét qua hàng triệu văn bản gốc.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Tiêu chí | Vector RAG truyền thống | Microsoft Graph RAG | Đánh giá kiến trúc AI Engineering |
| :--- | :--- | :--- | :--- |
| **Chi phí lập chỉ mục (Indexing Cost)** | Cực rẻ. Chỉ cần gọi mô hình embedding 1 lần cho mỗi chunk. | Rất đắt. Phải gọi LLM hàng ngàn lần để trích xuất thực thể, quan hệ và sinh tóm tắt cộng đồng. | Chỉ đầu tư Graph RAG khi dữ liệu có tính kết nối cao và giá trị thông tin khai thác biện minh được cho chi phí. |
| **Khả năng trả lời câu hỏi tổng quát** | Gần như bằng 0. Vector search chỉ kéo về được vài chunk rời rạc ngẫu nhiên. | Xuất sắc. Bản tóm tắt phân tầng bao quát toàn bộ bức tranh dữ liệu. | Graph RAG là giải pháp duy nhất hiện nay giải quyết triệt để bài toán "Global Corpus Understanding". |
| **Độ trễ truy vấn (Query Latency)** | Thấp (< 50ms cho vector search). | Trung bình đến cao (Local search ~1-2s; Global search cần luồng Map-Reduce đa bước). | Cần lưu cache các bản tóm tắt và câu trả lời thường gặp. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Kiến trúc Graph-Vector Hybrid
Trong thực tế sản xuất, không ai dùng Graph RAG thuần túy mà luôn triển khai kiến trúc lai (**Hybrid Graph-Vector System**):
- Sử dụng **Neo4j** hoặc **AWS Neptune** để lưu trữ Graph Triples.
- Nhúng vector vào chính các nút thực thể và bản tóm tắt cộng đồng trong Vector DB.
- Khi người dùng hỏi:
  - Vector search tìm ra các nút thực thể khởi đầu (Seed Entities).
  - Graph traversal mở rộng mạng lưới tri thức 1-2 bước (1-hop / 2-hop subgraphs).
  - Nạp thông tin cấu trúc đồ thị vào ngữ cảnh của LLM.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Khi nào hệ thống nên dùng Graph RAG thay vì Vector RAG truyền thống?*
  - **A**: Dùng Graph RAG khi:
    1. Tác vụ đòi hỏi suy luận xuyên văn bản qua nhiều bước kết nối thực thể (Multi-hop Reasoning: A liên quan B, B sở hữu C, tìm mối quan hệ giữa A và C).
    2. Dữ liệu có cấu trúc mạng lưới quan hệ chằng chịt: Hồ sơ điều tra chống gian lận tài chính, phả hệ y sinh/dược phẩm, chuỗi cung ứng logistics.
    3. Cần trả lời các câu hỏi tóm tắt tổng thể toàn bộ kho tri thức mà Vector search thông thường bị mù cục bộ.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[rag-architecture]] — Bức tranh tổng thể nơi Graph RAG đại diện cho thế hệ tiên tiến nhất.
- [[vector-embeddings]] — Kết hợp vector nhúng trên các nút thực thể đồ thị.
- [[graph-neural-networks]] — Cơ sở toán học nền tảng về xử lý học sâu trên cấu trúc đồ thị.
- [[llm-evaluation]] — Đo lường độ bao phủ tri thức và tính trung thực của các câu trả lời tổng hợp.
"""
}

def generate():
    for filename, content in ENTITIES.items():
        filepath = WIKI_DIR / filename
        filepath.write_text(content.strip(), encoding="utf-8")
        print(f"Created: {filepath.name}")

if __name__ == "__main__":
    generate()
