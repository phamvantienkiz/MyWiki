# Giao Dịch và Nguyên Lý ACID (ACID Properties & Transaction Isolation Levels)

> **Khái niệm chính thống**: *Fundamentals of Database Systems* (Elmasri & Navathe), Chapter 20 & 21 (Transaction Processing & Concurrency Control); ANSI SQL-92 Standard; *DatabaseSQL.jpg*.
> **Miền kiến thức**: [[index|Database Concurrency & Transaction Management]]
> **Tài liệu gốc liên quan**:
> - [DatabaseSQL.jpg](../resources/software/DatabaseSQL.jpg) (Trang 1: ACID và xử lý đồng thời)
> - [Fundamentals of Database System.pdf](../resources/software/Fundamentals%20of%20Database%20System.pdf) (Trang 45-75)
> - [Backend Engineering (Phần 1) - LeThienHoa.pdf](../resources/software/Backend%20Engineering%20%28Ph%E1%BA%A7n%201%29%20-%20LeThienHoa.pdf) (Trang 60-85)

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

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & `wiki-links`)
- [[database-indexing-optimization]] — Indexing hỗ trợ khóa theo dải (Gap Lock/Next-Key Lock) trong transaction.
- [[sql-vs-nosql-data-architecture]] — So sánh giữa tính nhất quán ACID của SQL và tính khả dụng BASE của NoSQL.
- [[oop-core-principles]] — Áp dụng `@Transactional` decorator/annotation trong kiến trúc Service-Repository.