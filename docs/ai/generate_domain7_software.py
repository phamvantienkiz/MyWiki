# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = Path("wiki")
WIKI_DIR.mkdir(parents=True, exist_ok=True)

ENTITIES = {
    "oop-core-principles.md": r"""# 4 Tính Chất Cốt Lõi Của Lập Trình Hướng Đối Tượng (OOP Core Pillars & Interfaces)

> **Khái niệm chính thống**: Booch et al. *"Object-Oriented Analysis and Design with Applications"*; Gamma et al. *"Design Patterns: Elements of Reusable Object-Oriented Software"*; *JavaOOP-Core.jpg*; *Questtion.txt*.
> **Miền kiến thức**: [[software-data-overview|Software Engineering Foundations for AI]]
> **Tài liệu gốc liên quan**:
> - [Questtion.txt](../../resources/software/Questtion.txt) (Trang 1: Yêu cầu thực tế về OOP & Interface)
> - [JavaOOP-Core.jpg](../../resources/software/JavaOOP-Core.jpg) (Sơ đồ phỏng vấn Java Core / OOP)
> - [Backend Engineering (Phần 1) - LeThienHoa.pdf](../../resources/software/Backend%20Engineering%20%28Ph%E1%BA%A7n%201%29%20-%20LeThienHoa.pdf) (Trang 15-45)

---

## 1. Tóm tắt (Executive Summary)
**Lập trình Hướng đối tượng (Object-Oriented Programming - OOP)** là mô thức kiến trúc phần mềm tổ chức mã nguồn xoay quanh các "Đối tượng" (Objects) đóng gói trạng thái (State / Attributes) và hành vi (Behavior / Methods) tương ứng, thay vì các hàm xử lý dữ liệu rời rạc. Bốn trụ cột cốt lõi của OOP bao gồm: **Tính Đóng gói (Encapsulation)**, **Tính Kế thừa (Inheritance)**, **Tính Đa hình (Polymorphism)**, và **Tính Trừu tượng (Abstraction)**. Trong kỹ nghệ phần mềm và hệ thống AI thực tế, việc làm chủ OOP không dừng lại ở các ví dụ trường học kinh điển mà nằm ở khả năng thiết kế giao diện (**Interface**) chuẩn mực, phân tách vai trò và làm chủ nguyên lý cắm-rút module.

---

## 2. Định nghĩa chính thống & 4 Trụ Cột Thực Chiến (Production-Grade Pillars)

*(Cảnh báo từ `Questtion.txt`: Tuyệt đối không dùng các ví dụ sáo rỗng như con chó, con mèo; phải giải thích bằng ví dụ hệ thống thực tế)*:

### 2.1 Tính Đóng gói (Encapsulation)
- **Bản chất**: Che giấu trạng thái nội tại bên trong của đối tượng và chỉ cho phép tương tác ra bên ngoài thông qua các phương thức công khai được kiểm soát chặt chẽ (Public API / Getters & Setters / Properties).
- **Ví dụ Kỹ thuật Thực tế**:
  Trong một `LLMTokenBucketRateLimiter`, biến `current_tokens` và `last_refill_timestamp` được khai báo `private`. Bên ngoài không thể gán tùy tiện `limiter.current_tokens = 9999` để gian lận quota. Mọi tương tác phải qua hàm `public acquire_tokens(int n)` có cơ chế đồng bộ hóa luồng (Thread-safe Lock) và kiểm tra điều kiện nghiêm ngặt.

### 2.2 Tính Trừu tượng (Abstraction)
- **Bản chất**: Trưng ra giao diện tương tác đơn giản, ẩn đi toàn bộ chi tiết cài đặt thuật toán phức tạp và hạ tầng công nghệ bên dưới.
- **Ví dụ Kỹ thuật Thực tế**:
  Một interface `VectorStore`:
  ```python
  class VectorStore(ABC):
      @abstractmethod
      def similarity_search(self, query_vector: list[float], top_k: int) -> list[Document]:
          pass
  ```
  Ứng dụng RAG chỉ cần gọi `vector_store.similarity_search(...)` mà hoàn toàn không cần bận tâm bên dưới đang chạy PostgreSQL pgvector, Milvus cluster hay Pinecone cloud.

### 2.3 Tính Kế thừa (Inheritance)
- **Bản chất**: Cho phép lớp con tái sử dụng cấu trúc và hành vi chung của lớp cha, mở rộng hoặc ghi đè (Override) các hành vi đặc thù.
- **Ví dụ Kỹ thuật Thực tế**:
  Lớp cha `BaseEmbeddingModel` quản lý cơ chế caching, đo lường độ trễ (latency tracking) và batching. Các lớp con `OpenAIEmbedding` và `HuggingFaceBGEEmbedding` chỉ cần kế thừa và cài đặt hàm cụ thể `_encode_text()`.

### 2.4 Tính Đa hình (Polymorphism)
- **Bản chất**: Khả năng các đối tượng khác nhau phản ứng theo các cách khác nhau đối với cùng một thông điệp/lời gọi hàm (Dynamic Dispatch / Late Binding).
- **Ví dụ Kỹ thuật Thực tế**:
  Một danh sách các bộ truy xuất: `retrievers: list[BaseRetriever] = [DenseVectorRetriever(), BM25SparseRetriever(), KnowledgeGraphRetriever()]`. Vòng lặp `for r in retrievers: r.retrieve(query)` thực thi hành vi hoàn toàn khác nhau cho từng đối tượng tại thời điểm chạy mà code điều phối không cần bất kỳ câu lệnh `if/else` nào.

```mermaid
classDiagram
    class BaseLLMClient {
        <<abstract>>
        -api_key: str
        #timeout: int
        +generate(prompt: str)* str
        +stream(prompt: str)* Iterator
        #log_latency(ms: int) void
    }
    
    class OpenAIGPTClient {
        -model_name: str
        +generate(prompt: str) str
        +stream(prompt: str) Iterator
    }
    
    class AnthropicClaudeClient {
        -anthropic_version: str
        +generate(prompt: str) str
        +stream(prompt: str) Iterator
    }
    
    BaseLLMClient <|-- OpenAIGPTClient : Inheritance
    BaseLLMClient <|-- AnthropicClaudeClient : Inheritance
```

---

## 3. Tử Huyệt Phỏng Vấn: "Vì Sao Lại Cần Phải Có Interface?" (From Questtion.txt)

Đây là câu hỏi phân định đẳng cấp giữa một thợ code và một Kỹ sư Thiết kế Hệ thống:
1. **Lập trình hướng Giao diện, không hướng Cài đặt (Program to an Interface, not an Implementation)**:
   - Nếu tầng Service gọi trực tiếp lớp cụ thể `MySQLDatabase db = new MySQLDatabase()`, tầng Service bị trói chặt (Tightly Coupled) với MySQL. Khi công ty muốn chuyển sang PostgreSQL hoặc mock dữ liệu để viết Unit Test, toàn bộ mã nguồn Service bị phá vỡ.
   - Khi có interface `DatabaseConnection`, Service chỉ phụ thuộc vào bản hợp đồng (Contract). Việc hoán đổi sang `PostgreSQLDatabase` hay `MockDatabase` diễn ra trong 0 dòng code sửa đổi ở Service.
2. **Khắc phục Giới hạn Đơn kế thừa (Multiple Inheritance)**:
   - Các ngôn ngữ như Java/C# cấm đa kế thừa class để tránh "Vấn đề Kim cương" (Diamond Problem). Interface cho phép một lớp có thể thực thi nhiều hợp đồng độc lập: một `DocumentProcessor` có thể vừa `implements AutoCloseable`, vừa `implements Searchable`, vừa `implements Serializable`.
3. **Mở khóa Đa hình và Dependency Injection**:
   - Interface là nền tảng tuyệt đối để triển khai chữ **D** trong SOLID ([[solid-principles|Dependency Inversion Principle]]) và các Design Patterns kinh điển (Strategy, Factory, Adapter).

---

## 4. Phân Biệt Thực Thể: Object vs Class; Abstract Class vs Interface

| Khía cạnh | Abstract Class (Lớp trừu tượng) | Interface (Giao diện) |
| :--- | :--- | :--- |
| **Bản chất triết lý** | Quan hệ bản thể: **LÀ MỘT (IS-A)**. Đại diện cho bản sắc của đối tượng. | Quan hệ năng lực: **CÓ THỂ LÀM ĐƯỢC (CAN-DO / LIKE-A)**. Đại diện cho một hợp đồng hành vi. |
| **Trạng thái (State)** | Có thể chứa các thuộc tính thành viên có trạng thái (`protected int counter`), constructor đầy đủ. | Không thể chứa trạng thái thành viên (chỉ có hằng số `public static final`). |
| **Phương thức cài đặt** | Có thể chứa cả phương thức trừu tượng lẫn phương thức đã cài đặt logic mặc định cụ thể. | Chủ yếu là các phương thức trừu tượng (từ Java 8 có thêm `default method`). |
| **Mức độ kế thừa** | Một lớp chỉ có thể kế thừa **1 Abstract Class duy nhất** (Đơn kế thừa). | Một lớp có thể thực thi **nhiều Interface cùng lúc** (Đa giao diện). |

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[solid-principles]] — Sự kế thừa và nâng tầm từ 4 tính chất OOP lên 5 nguyên lý thiết kế bền vững.
- [[tool-use-and-function-calling]] — Thiết kế các Tools của Agent tuân thủ tính đóng gói và trừu tượng.
- [[database-indexing-optimization]] — Thiết kế lớp Repository trừu tượng hóa tương tác cơ sở dữ liệu.
""",

    "solid-principles.md": r"""# 5 Nguyên Lý Thiết Kế SOLID (SOLID Principles in AI & Backend Engineering)

> **Khái niệm chính thống**: Robert C. Martin (Uncle Bob) *"Clean Architecture: A Craftsman's Guide to Software Structure and Design"*; *Questtion.txt*; *JavaOOP-Core.jpg*.
> **Miền kiến thức**: [[software-data-overview|Clean Architecture & System Design]]
> **Tài liệu gốc liên quan**:
> - [Questtion.txt](../../resources/software/Questtion.txt) (Trang 1: Chữ D trong SOLID và ví dụ thực tế)
> - [JavaOOP-Core.jpg](../../resources/software/JavaOOP-Core.jpg) (Sơ đồ phỏng vấn OOP/SOLID)
> - [Backend Engineering (Phần 1) - LeThienHoa.pdf](../../resources/software/Backend%20Engineering%20%28Ph%E1%BA%A7n%201%29%20-%20LeThienHoa.pdf) (Trang 30-55)

---

## 1. Tóm tắt (Executive Summary)
**5 Nguyên lý SOLID** là tập hợp các chỉ dẫn kiến trúc phần mềm cốt lõi do Robert C. Martin đúc kết nhằm xây dựng các hệ thống phần mềm dễ đọc, dễ mở rộng, dễ kiểm thử và có khả năng chống chọi trước sự thay đổi của yêu cầu kinh doanh:
- **S** — Single Responsibility Principle (Đơn trách nhiệm)
- **O** — Open/Closed Principle (Đóng để sửa, Mở để thêm)
- **L** — Liskov Substitution Principle (Thay thế Liskov)
- **I** — Interface Segregation Principle (Phân tách Giao diện)
- **D** — Dependency Inversion Principle (Đảo ngược Phụ thuộc)

---

## 2. Định nghĩa chính thống & Ví Dụ Thực Chiến (Production-Grade Code Examples)

*(Tuyệt đối không dùng ví dụ con chim/con chó — toàn bộ minh họa bằng kiến trúc AI / RAG / Payment Service thực tế theo yêu cầu)*:

### 2.1 S — Single Responsibility Principle (SRP)
> *"A class should have one, and only one, reason to change."* (Một lớp chỉ nên có một lý do duy nhất để thay đổi).

- **Vi phạm SRP**:
  Một class `RAGPipeline` vừa làm nhiệm vụ cào dữ liệu PDF, vừa gọi OpenAI embedding, vừa lưu vào Postgres, vừa sinh mã HTML hiển thị ra web. Khi thư viện PDF thay đổi, hoặc khi đổi DB, class này đều bị sửa đổi $\rightarrow$ Rất dễ sinh lỗi dây chuyền.
- **Tuân thủ SRP**:
  Tách thành 4 class độc lập:
  1. `PDFDocumentParser`: Chỉ chịu trách nhiệm bóc tách text từ file.
  2. `TextEmbedder`: Chỉ chịu trách nhiệm biến đổi text thành vector.
  3. `VectorRepository`: Chỉ chịu trách nhiệm đọc/ghi dữ liệu vào cơ sở dữ liệu.
  4. `RAGOrchestrator`: Chỉ chịu trách nhiệm điều phối luồng dữ liệu giữa các thành phần trên.

### 2.2 O — Open/Closed Principle (OCP)
> *"Software entities should be open for extension, but closed for modification."* (Mở để mở rộng, nhưng Đóng đối với việc sửa đổi mã nguồn sẵn có).

- **Vi phạm OCP**:
  Dùng câu lệnh `if/else` hoặc `switch/case` khổng lồ để tính phí mô hình:
  ```python
  def calculate_cost(model_name: str, tokens: int) -> float:
      if model_name == "gpt-4o": return tokens * 0.005
      elif model_name == "claude-3-5": return tokens * 0.003
      # Mỗi khi có model mới (Gemini, DeepSeek), ta buộc phải vào sửa code cũ!
  ```
- **Tuân thủ OCP**:
  Định nghĩa interface `CostStrategy` và tạo các class riêng biệt. Khi có model mới, chỉ cần tạo thêm class mới mà **không sửa một dòng code nào của hệ thống đang chạy**.

### 2.3 L — Liskov Substitution Principle (LSP)
> *"Subtypes must be substitutable for their base types without altering the correctness of the program."* (Lớp con phải có khả năng thay thế hoàn toàn cho lớp cha mà không làm thay đổi tính đúng đắn của chương trình).

- **Vi phạm LSP**:
  Lớp cha `ReadOnlyVectorStore` có phương thức `search()`. Kỹ sư tạo lớp con `WritableVectorStore` kế thừa từ lớp cha nhưng trong phương thức xóa `delete()` lại ném ra lỗi `NotSupportedException` vì kho không hỗ trợ xóa. Bất kỳ đoạn code nào gọi hàm trên lớp cha sẽ bị crash khi nhận đối tượng lớp con.
- **Tuân thủ LSP**:
  Đảm bảo lớp con không thắt chặt điều kiện tiên quyết (Preconditions) và không nới lỏng điều kiện sau (Postconditions) của lớp cha.

### 2.4 I — Interface Segregation Principle (ISP)
> *"Clients should not be forced to depend upon interfaces that they do not use."* (Không ép buộc client phải phụ thuộc vào các phương thức giao diện mà nó không hề dùng đến).

- **Vi phạm ISP**:
  Tạo một "God Interface" khổng lồ:
  ```java
  public interface AIModelOperations {
      void textGeneration();
      void imageGeneration();
      void speechToText();
      void vectorEmbedding();
  }
  ```
  Khi cài đặt một model chuyên về Text (`ClaudeClient`), ta vẫn bị ép phải override các hàm `imageGeneration()` và `speechToText()` với thân hàm ném lỗi `throw new UnsupportedOperationException()`.
- **Tuân thủ ISP**:
  Phân rã thành các interface hạt mịn (Fine-grained interfaces): `TextGeneratable`, `ImageGeneratable`, `Embeddable`. Một class chỉ `implements` đúng năng lực nó sở hữu.

### 2.5 D — Dependency Inversion Principle (DIP) — Trọng Tâm Phỏng Vấn (From Questtion.txt)
> *"1. High-level modules should not depend on low-level modules. Both should depend on abstractions.  
> 2. Abstractions should not depend on details. Details should depend on abstractions."*

```mermaid
flowchart TD
    subgraph Anti-Pattern: Tightly Coupled
        High1["RAGService (High-Level Business Logic)"] --> Low1["QdrantVectorDB (Low-Level Implementation)"]
    end
    
    subgraph DIP Compliant: Inversion of Control
        High2["RAGService (High-Level)"] --> Interface["<<Interface>> IVectorRepository"]
        Low2["QdrantVectorDB (Low-Level)"] -.->|Implements| Interface
        Low3["PostgresVectorDB (Low-Level)"] -.->|Implements| Interface
    end
```

- **Ví dụ Kỹ thuật Thực tế mà bạn đã làm (Trả lời TechLead)**:
  - *"Trong hệ thống RAG enterprise, module nghiệp vụ cấp cao `RAGChatService` của em không bao giờ trực tiếp `import QdrantClient` hay khởi tạo `qdrant = QdrantClient()`."*
  - *"Thay vào đó, em định nghĩa một Abstraction interface `IVectorRepository`. Module `RAGChatService` chỉ nhận `IVectorRepository` thông qua **Constructor Injection** (sử dụng FastAPI `Depends()` trong Python hoặc `@Autowired` trong Spring Boot)."*
  - *"Tầng hạ tầng cụ thể `QdrantVectorRepository` thực thi interface này. Nhờ đó, khi viết Unit Test, em dễ dàng mock một `FakeVectorRepository` trong RAM mà không cần bật server Qdrant thật; và khi công ty chuyển sang Milvus, em chỉ cần viết một adapter mới mà không phải chạm vào một dòng logic nghiệp vụ nào của `RAGChatService`."*

---

## 3. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[oop-core-principles]] — Nền tảng hướng đối tượng mà SOLID xây dựng dựa trên đó.
- [[database-indexing-optimization]] — Phân tách tầng Repository và Service trong tối ưu hóa cơ sở dữ liệu.
- [[model-serving-api]] — Triển khai Dependency Injection trong FastAPI backend.
""",

    "database-indexing-optimization.md": r"""# Đánh Chỉ Mục Cơ Sở Dữ Liệu và Tối Ưu Hóa Truy Vấn (Database Indexing & Query Optimization)

> **Khái niệm chính thống**: *Fundamentals of Database Systems* (Elmasri & Navathe, Pearson); *Nền tảng Hệ thống Cơ sở dữ liệu cho Data Scientist* (TS. Lê Thiện Hòa); *DatabaseSQL.jpg*.
> **Miền kiến thức**: [[software-data-overview|Relational Databases & Performance Tuning]]
> **Tài liệu gốc liên quan**:
> - [DatabaseSQL.jpg](../../resources/software/DatabaseSQL.jpg) (Sơ đồ phỏng vấn Database / SQL)
> - [Fundamentals of Database System.pdf](../../resources/software/Fundamentals%20of%20Database%20System.pdf) (Trang 1-45)
> - [Nền tảng Hệ thống Cơ sở dữ liệu cho Data Scientist – Bài giảng của Tiến sĩ Lê Thiện Hòa.pdf](../../resources/data-sciense/N%E1%BB%81n%20t%E1%BB%A7ng%20H%E1%BB%87%20th%E1%BB%91ng%20C%C6%A1%20s%E1%BB%9F%20d%E1%BB%AF%20li%E1%BB%87u%20cho%20Data%20Scientist%20%E2%80%93%20B%C3%A0i%20gi%E1%BA%A3ng%20c%E1%BB%A7a%20Ti%E1%BA%BFn%20si%20L%C3%AA%20Thi%E1%BB%87n%20H%C3%B2a.pdf) (Trang 1-40)

---

## 1. Tóm tắt (Executive Summary)
**Đánh Chỉ mục Cơ sở dữ liệu (Database Indexing)** là cấu trúc dữ liệu bổ trợ (thường là **B-Tree / B+Tree**) được xây dựng trên một hoặc nhiều cột của bảng dữ liệu nhằm tăng tốc độ tìm kiếm và trích xuất dữ liệu từ độ phức tạp quét toàn bộ bảng $\mathcal{O}(N)$ (**Full Table Scan**) xuống độ phức tạp logarit $\mathcal{O}(\log N)$. Tuy nhiên, việc lạm dụng chỉ mục sẽ làm chậm các thao tác ghi dữ liệu (INSERT, UPDATE, DELETE) và tiêu tốn bộ nhớ đĩa. Tối ưu hóa truy vấn SQL đòi hỏi kỹ sư phải đọc hiểu kế hoạch thực thi (**EXPLAIN Execution Plan**), xử lý triệt để vấn đề **N+1 Query Problem**, và nắm vững nguyên lý chọn cột đánh chỉ mục.

---

## 2. Định nghĩa chính thống & Cấu trúc Dữ liệu B+Tree Index

```mermaid
flowchart TD
    Root["B+Tree Root Node [100 | 500]"] --> Internal1["Internal Node [20 | 50]"]
    Root --> Internal2["Internal Node [200 | 350]"]
    Root --> Internal3["Internal Node [600 | 800]"]
    
    Internal1 --> Leaf1["Leaf Node: [10, 15, 20] -> Disk Row Pointers"]
    Internal1 --> Leaf2["Leaf Node: [25, 40, 50] -> Disk Row Pointers"]
    
    Leaf1 <-->|"Doubly Linked List (Fast Range Queries)"| Leaf2
```

### 2.1 Đặc tính vượt trội của B+Tree
- Mọi bản ghi dữ liệu thực tế (hoặc con trỏ trỏ tới dòng dữ liệu trên đĩa) **chỉ nằm ở các nút lá (Leaf Nodes)**.
- Các nút lá được liên kết với nhau bằng danh sách liên kết đôi (Doubly Linked List), giúp các truy vấn tìm kiếm theo dải phạm vi (`WHERE age BETWEEN 20 AND 30`) chạy với tốc độ cực đại.
- Cây luôn tự cân bằng hoàn hảo; độ cao của cây $h \approx \log_B(N)$ (với bậc nhánh $B \approx 100 - 500$). Một bảng 100 triệu dòng chỉ có độ cao cây $h \approx 3 - 4$, đồng nghĩa chỉ cần **tối đa 3 đến 4 lần đọc đĩa (Disk I/O)** để tìm thấy bất kỳ bản ghi nào!

### 2.2 Phân biệt Clustered Index vs Non-Clustered Index
- **Clustered Index (Chỉ mục Cụm)**:
  - Bản thân các dòng dữ liệu vật lý trên ổ đĩa được sắp xếp đúng theo thứ tự của chỉ mục cụm (trong MySQL InnoDB, khóa chính `PRIMARY KEY` mặc định là Clustered Index).
  - Mỗi bảng **chỉ có duy nhất 1 Clustered Index**.
- **Non-Clustered / Secondary Index (Chỉ mục Phụ)**:
  - Cấu trúc B+Tree độc lập nằm ở vùng đĩa khác; nút lá chứa giá trị khóa phụ và giá trị khóa chính (Primary Key).
  - Khi tìm kiếm qua Secondary Index, database phải thực hiện thêm một bước tra cứu ngược (**Bookmark Lookup / Table Access by Index RowID**) để lấy toàn bộ dữ liệu dòng, trừ khi đó là một **Covering Index** (chỉ mục bao phủ chứa đủ toàn bộ các cột được `SELECT`).

---

## 3. Câu Hỏi Phỏng Vấn Sát Sườn: Trả Lời Bộ Câu Hỏi DatabaseSQL.jpg

### 3.1 Em đã từng dùng EXPLAIN để tối ưu query chưa? Những chỉ số nào hay xem nhất?
Khi chạy lệnh `EXPLAIN ANALYZE SELECT ...`, các chỉ số sống còn cần phân tích:
1. **`type` (Access Type - Loại truy cập)**: Thể hiện cách database tìm kiếm dữ liệu (thứ tự từ tốt nhất đến tệ nhất):
   $$\text{system} > \text{const} > \text{eq\_ref} > \text{ref} > \text{range} > \text{index} > \text{ALL}$$
   - Nếu `type = ALL`: Báo động đỏ! Đây là **Full Table Scan** (quét toàn bộ bảng).
   - Mục tiêu tối ưu: Đưa về ít nhất `range` hoặc `ref`.
2. **`key`**: Tên của Index thực tế mà bộ tối ưu hóa (Query Optimizer) đã chọn sử dụng. Nếu `key = NULL`, nghĩa là không dùng index.
3. **`rows`**: Số lượng dòng ước tính mà database phải quét qua.
4. **`Extra`**:
   - `Using index`: Rất tốt! Đạt trạng thái **Covering Index** (không cần đọc bảng đĩa).
   - `Using filesort`: Báo động! Database phải tự sắp xếp dữ liệu trong RAM/đĩa ngoài thay vì tận dụng index sẵn có.
   - `Using temporary`: Cực xấu! Phải tạo bảng tạm để xử lý `GROUP BY` hoặc `DISTINCT`.

### 3.2 Index nên tạo ở những cột nào? Dựa vào đâu để quyết định?
- **NÊN TẠO**:
  1. Cột xuất hiện thường xuyên trong mệnh đề `WHERE`, `JOIN ON`, `ORDER BY`, `GROUP BY`.
  2. Cột có **Độ chọn lọc cao (High Cardinality)**: Tỷ lệ các giá trị phân biệt lớn (ví dụ: `email`, `user_id`, `citizen_id`).
  3. Sử dụng **Composite Index (Chỉ mục Hỗn hợp)** tuân thủ quy tắc tiền tố bên trái (**Leftmost Prefix Rule**).
- **KHÔNG NÊN TẠO**:
  1. Cột có độ chọn lọc quá thấp (Low Cardinality: như cột `gender` chỉ có Nam/Nữ, `status` chỉ có 0/1). Đánh index ở đây vô ích vì database thà quét Full Table Scan còn nhanh hơn!
  2. Bảng có tần suất GHI (Insert/Update) liên tục hàng chục ngàn TPS mà ít khi đọc.

### 3.3 Vấn đề N+1 Query Problem là gì? Cách xử lý triệt để?
- **Bản chất**: Xảy ra khi sử dụng các framework ORM (Hibernate, JPA, SQLAlchemy, Django ORM).
  - 1 câu query ban đầu để lấy danh sách $N$ bản ghi: `SELECT * FROM orders LIMIT 100;` (1 query).
  - Sau đó trong vòng lặp duyệt qua từng đơn hàng, ORM lại bắn thêm 1 câu query để lấy thông tin khách hàng tương ứng: `SELECT * FROM customer WHERE id = ?;` ($N$ queries).
  - Tổng cộng hệ thống bắn **$1 + N = 101$ câu queries vào database**, gây nghẽn kết nối và sập server.
- **Cách xử lý**:
  1. Sử dụng kỹ thuật **Eager Loading** qua phép `JOIN` tường minh: trong SQL dùng `LEFT JOIN FETCH`, trong SQLAlchemy dùng `joinedload()` hoặc `selectinload()`.
  2. Gom cụm các ID để truy vấn 1 lần bằng mệnh đề `IN`: `SELECT * FROM customer WHERE id IN (1, 2, ..., N);`.

### 3.4 Khi nào dùng WHERE, khi nào dùng HAVING?
- **`WHERE`**: Lọc dữ liệu **trước khi** thực hiện gom nhóm (`GROUP BY`). Không được dùng các hàm tổng hợp (`SUM`, `COUNT`, `AVG`) trong `WHERE`.
- **`HAVING`**: Lọc dữ liệu **sau khi** đã tính toán gom nhóm và tổng hợp.
- **Quy tắc hiệu năng**: Luôn luôn lọc tối đa bằng `WHERE` trước để giảm số dòng cần nạp vào RAM tính toán, chỉ dùng `HAVING` cho các điều kiện dựa trên kết quả của hàm aggregate.

### 3.5 So sánh TRUNCATE, DELETE và DROP
- **`DELETE`**: Lệnh DML (Data Manipulation Language). Xóa từng dòng một, kích hoạt Triggers, ghi nhận toàn bộ log vào Transaction Log (Undo/Rollback được). Tốc độ chậm nhất.
- **`TRUNCATE`**: Lệnh DDL (Data Definition Language). Xóa trắng toàn bộ bảng bằng cách hủy cấp phát các trang dữ liệu (Deallocate Data Pages), reset lại cột tự tăng (Auto-increment), không kích hoạt trigger, ghi log tối thiểu. Tốc độ cực nhanh.
- **`DROP`**: Lệnh DDL. Xóa bỏ hoàn toàn toàn bộ bảng (cả dữ liệu, cấu trúc schema, index và phân quyền) khỏi cơ sở dữ liệu.

---

## 4. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[acid-and-transactions]] — Quản lý giao dịch và khóa dòng khi tối ưu truy vấn.
- [[sql-vs-nosql-data-architecture]] — So sánh giữa cơ sở dữ liệu quan hệ dòng và cơ sở dữ liệu cột OLAP.
- [[vector-embeddings]] — Chỉ mục ANN (HNSW) là sự tiến hóa của chỉ mục B-Tree lên không gian đa chiều.
""",

    "acid-and-transactions.md": r"""# Giao Dịch và Nguyên Lý ACID (ACID Properties & Transaction Isolation Levels)

> **Khái niệm chính thống**: *Fundamentals of Database Systems* (Elmasri & Navathe), Chapter 20 & 21 (Transaction Processing & Concurrency Control); ANSI SQL-92 Standard; *DatabaseSQL.jpg*.
> **Miền kiến thức**: [[software-data-overview|Database Concurrency & Transaction Management]]
> **Tài liệu gốc liên quan**:
> - [DatabaseSQL.jpg](../../resources/software/DatabaseSQL.jpg) (Trang 1: ACID và xử lý đồng thời)
> - [Fundamentals of Database System.pdf](../../resources/software/Fundamentals%20of%20Database%20System.pdf) (Trang 45-75)
> - [Backend Engineering (Phần 1) - LeThienHoa.pdf](../../resources/software/Backend%20Engineering%20%28Ph%E1%BA%A7n%201%29%20-%20LeThienHoa.pdf) (Trang 60-85)

---

## 1. Tóm tắt (Executive Summary)
**Giao dịch Cơ sở Dữ liệu (Database Transaction)** là một chuỗi tuần tự gồm một hoặc nhiều thao tác đọc/ghi dữ liệu được thực thi như một đơn vị công việc logic duy nhất không thể phân tách. Một hệ thống cơ sở dữ liệu giao dịch chuẩn mực bắt buộc phải bảo đảm 4 thuộc tính **ACID**: **Atomicity (Tính Nguyên tử)**, **Consistency (Tính Nhất quán)**, **Isolation (Tính Cô lập)**, và **Durability (Tính Bền vững)**. Để giải quyết mâu thuẫn giữa tính toàn vẹn dữ liệu và thông lượng xử lý đồng thời (Concurrency Throughput), chuẩn ANSI SQL định nghĩa **4 cấp độ cô lập giao dịch (Transaction Isolation Levels)** kết hợp cơ chế khóa (**Pessimistic vs Optimistic Locking**) và kỹ thuật đa phiên bản (**MVCC**).

---

## 2. Định nghĩa chính thống 4 Thuộc tính ACID

1. **A — Atomicity (Tính Nguyên tử - "All or Nothing")**:
   - Toàn bộ các thao tác bên trong giao dịch phải hoàn thành thành công 100%. Nếu có bất kỳ lỗi nào xảy ra ở bất kỳ bước nào, toàn bộ giao dịch phải được khôi phục trạng thái ban đầu (**Rollback**) như thể chưa từng xảy ra.
   - *Cơ chế kỹ thuật*: Được bảo đảm thông qua nhật ký hoàn tác (**Undo Log / Write-Ahead Logging - WAL**).
2. **C — Consistency (Tính Nhất quán)**:
   - Dữ liệu trước và sau giao dịch đều phải tuân thủ nghiêm ngặt toàn bộ các quy tắc toàn vẹn (Integrity Constraints), khóa ngoại, ràng buộc duy nhất (Unique), và logic nghiệp vụ định sẵn.
   - *Ví dụ*: Tổng số dư tài khoản của bên gửi và bên nhận trước và sau chuyển khoản phải không đổi.
3. **I — Isolation (Tính Cô lập)**:
   - Các giao dịch thực thi đồng thời không được nhìn thấy hoặc can thiệp vào trạng thái trung gian chưa hoàn thành của nhau.
   - *Cơ chế kỹ thuật*: Khóa (Locks) hoặc Đa phiên bản đồng thời (**MVCC - Multi-Version Concurrency Control**).
4. **D — Durability (Tính Bền vững)**:
   - Khi một giao dịch đã được xác nhận thành công (**Commit**), toàn bộ dữ liệu thay đổi sẽ tồn tại vĩnh viễn trên bộ nhớ lưu trữ bền vững (Disk/SSD), không bị mất đi ngay cả khi máy chủ bị mất điện đột ngột hoặc sập hệ điều hành.
   - *Cơ chế kỹ thuật*: Nhật ký ghi trước (**Redo Log / WAL**) được ghi đĩa trước khi trả về kết quả thành công cho client.

```mermaid
flowchart TD
    subgraph 4 Phenomena (Concurrency Bugs)
        P1["1. Dirty Read (Đọc dữ liệu rác chưa commit)"]
        P2["2. Non-Repeatable Read (Cùng 1 query ra 2 kết quả khác nhau do UPDATE)"]
        P3["3. Phantom Read (Cùng 1 query dải phạm vi ra số dòng khác nhau do INSERT)"]
    end
    
    subgraph 4 ANSI Isolation Levels
        L1["Read Uncommitted (Weakest, Fast, All bugs present)"]
        L2["Read Committed (Blocks Dirty Read, Uses MVCC snapshots)"]
        L3["Repeatable Read (Blocks Dirty & Non-Repeatable Read)"]
        L4["Serializable (Strictly Serialized, Zero bugs, Slowest)"]
    end
    
    L1 -.-> P1
    L2 -.-> P2
    L3 -.-> P3
```

---

## 3. Câu Hỏi Phỏng Vấn: "Nếu 2 Người Dùng Cùng Lúc Thay Đổi 1 Giá Trị (VD: Số Dư), Làm Sao Để Đảm Bảo Chính Xác?"

Đây là câu hỏi kinh điển trong *DatabaseSQL.jpg*. Có 2 trường phái giải quyết:

### 3.1 Phương pháp 1: Khóa Bi quan (Pessimistic Locking)
- **Triết lý**: Luôn giả định điều tồi tệ nhất sẽ xảy ra (xác suất đụng độ dữ liệu rất cao).
- **Cơ chế**: Khóa chặt dòng dữ liệu ngay từ thời điểm đọc bằng câu lệnh `SELECT ... FOR UPDATE`:
  ```sql
  BEGIN TRANSACTION;
  SELECT balance FROM accounts WHERE user_id = 101 FOR UPDATE; -- Đặt Exclusive Lock (X-Lock)
  -- Toàn bộ các request khác muốn đọc/ghi dòng này đều phải xếp hàng chờ!
  UPDATE accounts SET balance = balance - 100 WHERE user_id = 101;
  COMMIT; -- Nhả khóa
  ```
- **Đánh giá**: Tuyệt đối an toàn; nhưng làm giảm thông lượng hệ thống (Throughput) và dễ gây nghẽn cổ chai (Contention) nếu thời gian xử lý giao dịch kéo dài.

### 3.2 Phương pháp 2: Khóa Lạc quan (Optimistic Locking)
- **Triết lý**: Giả định phần lớn thời gian không có đụng độ; chỉ kiểm tra xung đột tại thời điểm lưu dữ liệu.
- **Cơ chế**: Thêm cột phiên bản `version` (hoặc `updated_at` timestamp):
  ```sql
  -- Bước 1: Đọc số dư và version hiện tại (không khóa)
  SELECT balance, version FROM accounts WHERE user_id = 101; -- Nhận được version = 5
  
  -- Bước 2: Khi cập nhật, kiểm tra xem version có còn bằng 5 không
  UPDATE accounts 
  SET balance = balance - 100, version = version + 1 
  WHERE user_id = 101 AND version = 5;
  ```
- Nếu lệnh UPDATE trả về `affected_rows == 0`, hệ thống phát hiện đã có người khác cập nhật trước đó $\rightarrow$ Tự động hủy thao tác và kích hoạt kịch bản thử lại (Retry loop) từ đầu.
- **Đánh giá**: Thông lượng cực cao, không làm khóa dòng trong database; phù hợp tuyệt đối cho hệ thống Read-Heavy hoặc Microservices phân tán.

---

## 4. 4 Cấp Độ Cô Lập Giao Dịch (Transaction Isolation Levels)

| Cấp độ Cô lập (Isolation Level) | Ngăn chặn Dirty Read | Ngăn chặn Non-Repeatable Read | Ngăn chặn Phantom Read | Cơ chế ngầm trong Database |
| :--- | :---: | :---: | :---: | :--- |
| **Read Uncommitted** | ❌ | ❌ | ❌ | Cho phép đọc bừa bãi dữ liệu đang sửa chưa commit. |
| **Read Committed** | ✅ | ❌ | ❌ | **Mặc định trong PostgreSQL, Oracle, SQL Server**. Mỗi câu lệnh `SELECT` tạo một snapshot MVCC mới. |
| **Repeatable Read** | ✅ | ✅ | ❌ (Trong ANSI SQL) | **Mặc định trong MySQL InnoDB**. Toàn bộ transaction chỉ dùng duy nhất 1 snapshot MVCC được tạo ở câu `SELECT` đầu tiên. (MySQL InnoDB dùng Next-Key Lock để ngăn cả Phantom Read!). |
| **Serializable** | ✅ | ✅ | ✅ | Các giao dịch được xếp hàng tuần tự tuyệt đối (Strict Two-Phase Locking - 2PL). Tỷ lệ abort/deadlock cao nhất. |

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[database-indexing-optimization]] — Indexing hỗ trợ khóa theo dải (Gap Lock/Next-Key Lock) trong transaction.
- [[sql-vs-nosql-data-architecture]] — So sánh giữa tính nhất quán ACID của SQL và tính khả dụng BASE của NoSQL.
- [[oop-core-principles]] — Áp dụng `@Transactional` decorator/annotation trong kiến trúc Service-Repository.
""",

    "sql-vs-nosql-data-architecture.md": r"""# Kiến Trúc Dữ Liệu SQL vs NoSQL (SQL, NoSQL, Columnar OLAP & Lakehouse)

> **Khái niệm chính thống**: *Fundamentals of Database Systems for Data Scientist* (TS. Lê Thiện Hòa, 2025); Brewer (2000) *"CAP Theorem"*; *Fundamentals of Database System.pdf*.
> **Miền kiến thức**: [[software-data-overview|Data Systems Architecture & Big Data]]
> **Tài liệu gốc liên quan**:
> - [Fundamentals of Database System.pdf](../../resources/software/Fundamentals%20of%20Database%20System.pdf) (Trang 1-25)
> - [Nền tảng Hệ thống Cơ sở dữ liệu cho Data Scientist – Bài giảng của Tiến sĩ Lê Thiện Hòa.pdf](../../resources/data-sciense/N%E1%BB%81n%20t%E1%BB%A7ng%20H%E1%BB%87%20th%E1%BB%91ng%20C%C6%A1%20s%E1%BB%9F%20d%E1%BB%AF%20li%E1%BB%87u%20cho%20Data%20Scientist%20%E2%80%93%20B%C3%A0i%20gi%E1%BA%A3ng%20c%E1%BB%A7a%20Ti%E1%BA%BFn%20si%20L%C3%AA%20Thi%E1%BB%87n%20H%C3%B2a.pdf) (Trang 1-35)
> - [AIO2026_[Slide_v4]-Data-Pipeline-and-Orchestration.pdf](../../resources/data-sciense/AIO2026_%5BSlide_v4%5D-Data-Pipeline-and-Orchestration.pdf) (Trang 1-67)

---

## 1. Tóm tắt (Executive Summary)
**Kiến trúc Dữ liệu Hiện đại (Modern Data Systems)** được phân hóa sâu sắc để phục vụ hai loại tải công việc (Workloads) hoàn toàn đối nghịch nhau: **OLTP (Online Transaction Processing)** — tối ưu hóa cho các giao dịch kinh doanh nhỏ lẻ, đọc/ghi tức thì trên từng dòng bản ghi; và **OLAP (Online Analytical Processing)** — tối ưu hóa cho các truy vấn phân tích tổng hợp (Aggregation), phân tích chuỗi thời gian trên hàng tỷ bản ghi. Để đáp ứng các nhu cầu này, kỹ sư dữ liệu và AI Engineer phải điều phối sự kết hợp giữa **Cơ sở dữ liệu Quan hệ dòng (Row-oriented SQL)**, **Hệ thống NoSQL phân tán (Document, Key-Value, Graph)**, **Cơ sở dữ liệu Cột phân tích (Columnar DB)**, và kiến trúc thế hệ mới **Data Lakehouse**.

---

## 2. So sánh Kiến trúc Chuyên sâu: Row-wise vs Column-wise Databases

```mermaid
flowchart TD
    subgraph Row-wise Storage (OLTP - PostgreSQL / MySQL)
        R1["Disk Block 1: [ID: 1, Name: Alice, Age: 25, Country: VN]"]
        R2["Disk Block 2: [ID: 2, Name: Bob,   Age: 30, Country: US]"]
    end
    
    subgraph Column-wise Storage (OLAP - ClickHouse / Parquet / Snowflake)
        C1["Disk Block A (Ages): [25, 30, 45, 22, 38, ...] -> Heavy Compression"]
        C2["Disk Block B (Countries): [VN, US, VN, UK, US, ...] -> Dictionary Encoded"]
    end
    
    QueryOLAP["SELECT AVG(Age) FROM Users;"] --> C1
    NoteOLAP["Column-wise only reads Disk Block A! (90% Disk I/O Saved)"]
```

### 2.1 Bản chất lưu trữ vật lý
- **Row-wise (Lưu trữ theo Dòng)**:
  - Toàn bộ các trường của một bản ghi được lưu nằm liền kề nhau trên cùng một khối đĩa (Disk Block).
  - *Lợi thế tuyệt đối*: Thao tác ghi một đơn hàng mới (`INSERT`) hoặc cập nhật thông tin một người dùng (`UPDATE`) diễn ra tức thì chỉ trong một lần ghi đĩa duy nhất. Phù hợp tuyệt đối cho **OLTP**.
- **Column-wise (Lưu trữ theo Cột)**:
  - Toàn bộ giá trị của cùng một cột trên toàn bộ hàng triệu bản ghi được lưu gom lại nằm liền kề nhau trên đĩa.
  - *Lợi thế tuyệt đối*: Khi cần tính `AVG(salary)` hay `SUM(revenue)`, hệ thống chỉ cần đọc đúng cột dữ liệu đó từ đĩa, **hoàn toàn bỏ qua các cột còn lại**, giảm 80-95% lưu lượng Disk I/O!
  - *Khả năng nén siêu việt*: Vì các phần tử trong cùng một cột có chung kiểu dữ liệu và giá trị thường lặp lại, các thuật toán nén (Run-Length Encoding, Dictionary Encoding) có thể nén dữ liệu giảm dung lượng tới 10 lần. Phù hợp tuyệt đối cho **OLAP**.

---

## 3. Hệ Thống Phân Tán và Định Lý CAP (Brewer's CAP Theorem)

Theo bài giảng của TS. Lê Thiện Hòa (*Fundamentals of Database Systems for Data Scientist*):
Trong một hệ thống dữ liệu phân tán qua mạng, khi xảy ra hiện tượng **Đứt gãy mạng (Network Partition - P)** — điều chắc chắn sẽ xảy ra trong thế giới thực — hệ thống **chỉ có thể chọn 1 trong 2 thuộc tính còn lại**:
1. **Consistency (Tính Nhất quán - CP)**:
   - Mọi nút mạng đều trả về cùng một dữ liệu mới nhất giống nhau tại cùng một thời điểm. Nếu một nút mạng bị cô lập không đồng bộ được, hệ thống từ chối phục vụ để bảo vệ tính toàn vẹn (Ví dụ: HBase, MongoDB, Google Spanner).
2. **Availability (Tính Khả dụng - AP)**:
   - Mọi yêu cầu gửi tới hệ thống đều nhận được phản hồi không bị lỗi, nhưng dữ liệu có thể chưa phải là phiên bản mới nhất (**Nhất quán sau cùng - Eventual Consistency** / Nguyên lý **BASE**). (Ví dụ: Apache Cassandra, Amazon DynamoDB, CouchDB).

```mermaid
flowchart TD
    CAP["CAP Theorem in Distributed Systems"] --> CP["CP Systems (Consistency + Partition Tolerance)\ne.g. MongoDB, HBase, Redis Cluster\nSacrifices Availability during Network Split"]
    CAP --> AP["AP Systems (Availability + Partition Tolerance)\ne.g. Apache Cassandra, DynamoDB\nSacrifices Immediate Consistency (Eventual Consistency)"]
    CAP --> CA["CA Systems (Consistency + Availability)\ne.g. Traditional Single-node PostgreSQL / MySQL\nCannot survive Network Partition!"]
```

---

## 4. Sự Tiến Hóa của Hạ Tầng Dữ Liệu Lớn (Evolution to Lakehouse)

1. **Database / Data Warehouse (DWH)**:
   - Dữ liệu có cấu trúc cao (Structured), tuân thủ Star Schema / Snowflake Schema. Dùng cho báo cáo tài chính và BI Dashboard kinh điển. *Hạn chế*: Đắt đỏ, không lưu được video/ảnh/text thô của AI.
2. **Data Lake (Hadoop HDFS / AWS S3)**:
   - Lưu trữ toàn bộ dữ liệu thô phi cấu trúc (Raw unstructured data: JSON, log, audio, image) với chi phí rẻ như cho. *Hạn chế*: Dễ biến thành "Bãi rác dữ liệu" (Data Swamp), thiếu giao dịch ACID, chất lượng dữ liệu kém.
3. **Data Lakehouse (Tiêu chuẩn hiện đại 2025-2026: Apache Iceberg, Delta Lake)**:
   - Dung hợp hoàn hảo: Đặt một tầng siêu dữ liệu (Metadata Layer) hỗ trợ giao dịch **ACID**, phân quyền bảo mật và time-travel query trực tiếp lên trên lớp lưu trữ tệp đối tượng rẻ tiền (S3/GCS) dưới định dạng cột mở **Parquet**.
   - Cung cấp trực tiếp dữ liệu sạch cho cả hai luồng: Dashboard BI và Huấn luyện Mô hình Machine Learning/LLM.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[database-indexing-optimization]] — Tối ưu hóa chỉ mục trong hệ quản trị cơ sở dữ liệu quan hệ.
- [[acid-and-transactions]] — So sánh đối chiếu giữa nguyên lý ACID của SQL và BASE của NoSQL.
- [[mlops-lifecycle]] — Dữ liệu từ Lakehouse là đầu vào nuôi sống các pipeline huấn luyện AI.
"""
}

def generate():
    for filename, content in ENTITIES.items():
        filepath = WIKI_DIR / filename
        filepath.write_text(content.strip(), encoding="utf-8")
        print(f"Created: {filepath.name}")

if __name__ == "__main__":
    generate()
