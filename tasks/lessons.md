# Lessons Learned: Xây dựng AI Engineer Wiki Web App (Next.js + Soft Clean Cards + Lecture Visualizer)

Tài liệu này tổng kết các bài học kinh nghiệm thu được từ quá trình xây dựng giao diện ứng dụng web Next.js (App Router) cho Personal Knowledge Wiki.

---

## 1. Tích Hợp Đồ Thị Động Lực Học (Force-Directed Graph) trong Next.js App Router

### Vấn đề Lỗi SSR (`window is not defined` / `HTMLCanvasElement`)
- `react-force-graph-2d` sử dụng trực tiếp các API của trình duyệt (HTML5 Canvas, RequestAnimationFrame, MouseEvent).
- Khi Next.js chạy Static Site Generation (SSG) hoặc Server-Side Rendering (SSR) trên Node.js, `window` không tồn tại, dẫn đến lỗi build.
- **Giải pháp**:
  - Tách phần component đồ thị thành Client Component (`'use client';`).
  - Sử dụng `dynamic(() => import('react-force-graph-2d'), { ssr: false })` để Next.js chỉ nạp canvas trên trình duyệt.
  - Cung cấp một placeholder loading trang nhã với spinner mờ theo chuẩn Soft Clean để tránh Layout Shift.

### Kỹ thuật Highlight Ego-Network (Mạng Lân Cận Trực Tiếp)
- Thay vì để tất cả các node sáng đều gây rối mắt, khi người dùng hover vào một node:
  - Chỉ giữ 100% opacity cho node đó và các node kết nối trực tiếp (Neighbors bậc 1).
  - Làm mờ các node còn lại về màu xám trung tính (`#D1D1D6`).
  - Tăng độ dày và độ sáng cho các cạnh kết nối (`rgba(31, 95, 255, 0.6)`), giúp người đọc nhận biết ngay cụm khái niệm phụ thuộc.

---

## 2. Kỹ Thuật Parse Markdown Sang Cấu Trúc Sư Phạm `lecture-visualizer`

### Render Công thức Toán Học KaTeX
- Cần render công thức toán học **trước khi** parse các cú pháp Markdown thông thường (như `*`, `_`, `^`), vì cú pháp Markdown có thể vô tình làm hỏng các ký hiệu toán học (ví dụ: `W_Q` có thể bị hiểu nhầm là italic).
- Dùng regex phân biệt:
  - Khối toán học `$$...$$` -> `katex.renderToString(math, { displayMode: true, throwOnError: false })` bọc trong thẻ nền `bg-[#F4F4F6] rounded-[12px]`.
  - Toán học nội dòng `$x$` -> `katex.renderToString(math, { displayMode: false, throwOnError: false })`.

### Bảng Từ Điển Ký Hiệu 4 Cột (Pedagogical Symbol Dictionary)
- Một rào cản lớn nhất của người tự nhận "học chậm" là choáng ngợp trước các ký hiệu toán học.
- Bảng từ điển 4 cột quy chuẩn hóa:
  - Cột 1: Ký hiệu LaTeX ($\mathcal{M}, \theta, \mathcal{L}$).
  - Cột 2: Tên tiếng Anh.
  - Cột 3: Tên tiếng Việt.
  - Cột 4: Nghĩa đời thường trực giác (Ví dụ: "Chiếc kính lọc để xác định xem token đang tìm kiếm loại thông tin gì").

---

## 3. Quy Chuẩn Thiết Kế "Soft Clean Cards" Trong Thực Tế

### Quy tắc Thẻ Mềm (Soft Card Standard)
- Nền trắng tinh khiết trên nền trang xám nhẹ `#F5F5F7` chuyển mờ sang `#EDEDF0`.
- Bo góc cực lớn `rounded-[28px]` tạo cảm giác thân thiện, mềm mại.
- Viền mảnh mờ 1px `border-[#E9E9EE]` kết hợp bóng mờ rộng `shadow-[0_1px_2px_rgba(16,16,24,0.04),0_8px_24px_rgba(16,16,24,0.06)]`.
- **Màu sắc chỉ dùng cho dữ liệu**: 7 màu pastel đại diện cho 7 miền tri thức, màu xanh mầm `#22C55E` cho hộp trực giác 🌱, màu đỏ `#EF4444` cho hộp mâu thuẫn ⚖️.

---

## 4. Xử Lý TypeScript & Next.js Build Flags

### Lỗi TS2802: MapIterator Downlevel Iteration
- Khi lặp qua `entityMap.entries()` trong môi trường TypeScript với target thấp hơn ES2015, trình biên dịch sẽ cảnh báo lỗi TS2802.
- **Giải pháp Clean Code**:
  - Thêm `"target": "es2020"` và `"downlevelIteration": true` trong `tsconfig.json`.
  - Dùng `Array.from(entityMap.entries()).forEach(([k, v]) => ...)` để đảm bảo tương thích 100% với mọi môi trường runtime.

---

## 5. Kinh Nghiệm Biên Soạn Bài Giảng Phỏng Vấn AI Intern (BAHA Homes)

### Chiến Lược Đọc Vị Tuyển Dụng Thực Chất (Subtext Decoding)
- Doanh nghiệp SME/Startup trong ngành nội thất (như BAHA Homes) khi tuyển AI Intern không tìm kiếm nghiên cứu sinh lý thuyết, mà cần một **"Builder/Doer"** có khả năng:
  - Vận hành thành thạo bộ công cụ lập trình AI thế hệ mới (**Google Antigravity** Desktop/CLI/IDE).
  - Tự động hóa các nút thắt quy trình (báo giá, tư vấn, bóc tách vật tư CAD/Excel, đồng bộ CRM) theo triết lý `Process → Data → Integration → Automation → AI`.
  - Giữ vững tư duy phản biện, kiểm soát và phát hiện khi AI sinh mã lỗi (không phụ thuộc mù quáng).

### Phối Hợp Sức Mạnh Công Cụ (The Power Stack)
- **Google Flow (`flow.google`)**: Phục vụ giai đoạn sáng tạo ý tưởng thị giác (Visual Concept), tạo video walk-through căn hộ từ ảnh tĩnh nhờ khả năng điều khiển góc máy camera và phong cách ánh sáng kiến trúc.
- **Google AI Studio (`aistudio.google`)**: Web Prototyping cho logic suy luận, khóa chặt định dạng đầu ra bằng `Structured Outputs (JSON Schema)` và kết nối hệ thống bằng `Function Calling` trước khi bấm *Get Code* sang Python.
- **Antigravity (IDE & Desktop 2.0)**: Môi trường ghép nối hoàn chỉnh, phân chia task DAG cho subagents, kiểm thử tự động trong sandbox và viết backend FastAPI chuẩn Clean Code/SOLID.
- **Three.js / WebGL Canvas**: Giúp trực quan hóa không gian nội thất căn hộ 32m² mẫu tại Vinhomes Grand Park, minh chứng cho sự giao thoa giữa Spatial Computing và AI Engineering.

---

## 6. Kiến Thức Kỹ Nghệ Phần Mềm Cốt Lõi Cho AI Engineer (Full-Stack & Operations)

### Mối Quan Hệ Giữa AI Engineering và Software Engineering
- Mô hình AI / Agent chỉ là hạt nhân tính toán (Compute Core); để tạo ra giá trị kinh tế thực tế, AI phải được bao bọc bởi một hệ thống phần mềm công nghiệp hoàn chỉnh:
  - **Clean Code & SOLID**: Bảo vệ hệ thống khỏi nợ kỹ thuật (Technical Debt), giúp mã nguồn dễ đọc, dễ viết test và dễ bảo trì khi nghiệp vụ mở rộng.
  - **Clean Architecture**: Phân tách rạch ròi 4 tầng (Domain Entities $\to$ Use Cases $\to$ Interface Adapters $\to$ Frameworks). Lõi nghiệp vụ hoàn toàn độc lập với database hay thư viện bên ngoài.
  - **Giao Thức Realtime**: Phân biệt dứt khoát giữa **Server-Sent Events (SSE)** (1 chiều, lý tưởng cho Streaming Token của LLM) và **WebSocket** (2 chiều song công, lý tưởng cho Multiplayer Canvas 3D và Chat).
  - **Bảo Mật Web & JWT**: Tuyệt đối không lưu Access/Refresh Token trong LocalStorage (chống XSS); sử dụng `HttpOnly, Secure, SameSite=Strict` Cookie kết hợp Refresh Token Rotation.
  - **Bộ Ba Vận Hành AI**:
    - **MLOps**: Quản lý vòng đời mô hình học máy truyền thống, Feature Store, phát hiện Data Drift / Concept Drift.
    - **LLMOps**: Quản lý phiên bản Prompt, RAG observability (LangSmith/Phoenix), Semantic Caching (GPTCache/Redis), Serving hiệu năng cao (vLLM PagedAttention).
    - **AIOps**: Sử dụng telemetry (Metrics, Logs, Traces) và học máy để tự động phát hiện bất thường và kích hoạt self-healing hạ tầng.

---

## 7. Cẩm Nang CSDL & SQL Sư Phạm Dành Cho AI Engineer

### Bản Chất Thứ Tự Thực Thi SQL vs Thứ Tự Viết
- Lập trình viên thường viết: `SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ... LIMIT`.
- Database Engine thực thi theo thứ tự logic: `FROM & JOIN` $\to$ `WHERE` $\to$ `GROUP BY` $\to$ `HAVING` $\to$ `SELECT` $\to$ `DISTINCT` $\to$ `ORDER BY` $\to$ `LIMIT`.
- **Hệ quả sư phạm**: Mệnh đề `WHERE` lọc từng dòng trước khi gom nhóm, nên không bao giờ dùng được hàm tổng hợp `SUM()` hay `AVG()` trong `WHERE`; phải dùng `HAVING`. Bí danh (Alias) đặt ở `SELECT` chỉ có thể dùng được ở `ORDER BY`, không dùng được trong `WHERE` hay `GROUP BY`.

### Cấu Trúc B+Tree & Tại Sao RDBMS Không Dùng Hash Hay B-Tree
- **B+Tree**: Chỉ lưu trữ con trỏ định hướng tại các nút nội vi, dồn toàn bộ dữ liệu xuống nút lá $\to$ Fan-out cực lớn, chiều cao cây chỉ 3-4 tầng cho hàng triệu dòng (tiết kiệm số lần I/O đọc đĩa). Các nút lá liên kết với nhau bằng danh sách liên kết kép (Doubly Linked List), cho phép duyệt dải dữ liệu tuần tự (`BETWEEN`, `>`, `<`) siêu tốc mà không cần leo ngược lên cây như B-Tree truyền thống hay Hash Index.

### Giao Thoa Giữa CSDL Truyền Thống & AI: `pgvector`
- Các mô hình Generative AI sinh ra vector embeddings nhiều chiều ($d = 1536$ hoặc $3072$).
- Extension `pgvector` trên PostgreSQL mang lại giải pháp hoàn hảo cho SME/Enterprise: Lưu trữ hợp đồng kinh doanh và vector tài liệu trong cùng một database, bảo toàn tính toàn vẹn ACID, cho phép truy vấn kết hợp (Hybrid Filtering) lọc thuộc tính nghiệp vụ và tìm kiếm láng giềng gần nhất ANN (HNSW) trong một câu lệnh SQL duy nhất mà không cần tốn chi phí dựng cụm Dedicated Vector DB riêng biệt.

---

## 8. Kỹ Nghệ Chế Độ Tối (Dark Mode Design System & Cognitive Ergonomics)

### Cấm Kỵ Đảo Màu Âm Bản (Naive Color Inversion)
- Việc đảo màu âm bản (Invert) trực tiếp biến nền đen `#000000` và chữ trắng tinh `#FFFFFF` sẽ gây ra tán sắc chói lóa (halo effect / eye strain) cực kỳ nhức mắt cho các tài liệu đọc dài dạng bài giảng.
- **Giải pháp**:
  - Dùng Deep Slate `#0B0F17` cho Canvas nền trang (0dp).
  - Phân tầng Surface Elevation bằng độ sáng: Thẻ Card `#131B2E` (2dp) sáng hơn nền trang, Bảng con `#1C263B` (3dp), Hover `#26334D` (4dp).
  - Thang chữ công thái học WCAG AA: `--text-primary: #F1F5F9` (không dùng `#FFFFFF`), `--text-body: #CBD5E1`.

### Bảo Tồn Tín Hiệu Sư Phạm Trong Chế Độ Tối
- Màu sắc trong cẩm nang đóng vai trò là "tín hiệu nhận thức" (Pedagogical Signals: Xanh mầm = Trực giác 🌱, Xanh dương = Định nghĩa toán học 📘, Tím = Mẹo kiến trúc 💡, Đỏ = Cảnh báo lỗi ⚠️).
- Để không làm mất tín hiệu nhận thức trong Dark Mode:
  - Nền hộp thoại chuyển sang dạng bán trong suốt bão hòa thấp (`rgba(..., 0.14)`).
  - Chữ nội dung chuyển sang dải phát quang pastel (Luminescent pastel) độ sáng cao (~80-90% luminance) để tạo độ tương phản cao, sắc nét mà vẫn êm dịu.
  - Viền trái giữ nguyên màu bão hòa đậm để dẫn hướng ánh nhìn của mắt.

### Kiến Trúc 3 Tầng Token Làm Nền Tảng Chuyển Đổi
- Primitive Layer (`--slate-900`, `--blue-600`): Cố định không đổi.
- Semantic Layer (`--bg-card`, `--text-primary`, `--callout-*-bg`): Tự động đổi giá trị khi kích hoạt `html.dark` hoặc `body.dark`.
- Component Layer (`.theme-toggle-btn`, `.score-label`): Kế thừa Semantic Layer, loại bỏ 100% hardcoded hex inline styles giúp bảo trì tuyệt đối an toàn.

---

## 9. Bài Học Vận Hành Google Antigravity Desktop (App 2.0) Trong Thực Chiến Doanh Nghiệp

### Tách Bạch 3 Bề Mặt (Surfaces Separation)
- **Desktop App 2.0**: Phù hợp cho vai trò "Nerve Center" — quản lý đa repository, theo dõi subagents chạy song song, điều phối các tác vụ dài hạn không bị phụ thuộc vào cửa sổ soạn thảo code.
- **CLI (`agy`)**: Phù hợp cho việc tích hợp vào shell script, pipeline CI/CD kiểm thử tự động, hoặc chạy headless trên server/sandbox.
- **IDE Extension**: Dành cho pair-programming trực tiếp từng dòng code (Tab autocomplete, inline `Ctrl+I`).

### Đột Phá An Toàn Với Git Worktree Mode (`New worktree mode`)
- Một sai lầm kinh điển khi dùng AI coding agent là để Agent ghi đè trực tiếp lên cây thư mục làm việc cục bộ của lập trình viên, dẫn đến mất code dang dở hoặc xung đột Git merge.
- **Giải pháp tối ưu từ Antigravity Desktop**: Luôn khởi động Agent trong `New worktree mode`. Agent sẽ tự động sinh nhánh riêng từ commit hiện tại, thực hiện toàn bộ quá trình thử nghiệm, viết code, chạy test trên một worktree độc lập ngầm. Kỹ sư chỉ việc dùng `Ctrl+R` duyệt Artifact Review hoặc `git merge` khi Agent hoàn thành pass 100% test suite.

### Chuỗi Phối Hợp Slash Commands Chuẩn Mực Cho Kỹ Sư AI
- **Quy trình 5 bước vàng**:
  1. `/grill-me`: Ép Agent phỏng vấn ngược để lôi ra mọi giả định ngầm, trường hợp biên (edge cases) và ràng buộc schema dữ liệu.
  2. `@AGENTS.md` + `/plan`: Lập kế hoạch kiến trúc phân tầng (Controller - Service - Repository) trước khi viết code, ngăn chặn AI "ảo giác" tự tiện sáng tạo cấu trúc thư mục dị biệt.
  3. `New worktree mode`: Cô lập không gian code an toàn.
  4. `/goal`: Chạy tự trị giải quyết toàn bộ test suite pytest mà không làm phiền người dùng từng bước nhỏ.
  5. `/schedule`: Đặt lịch cron tự động chạy kiểm thử hồi quy hoặc đồng bộ dữ liệu vào ban đêm với độ chính xác đến từng phút (`minute-level precision`).

---

## 10. Bài Học Tích Hợp Antigravity Python SDK & Hiệp Đồng 4 Bề Mặt Trong Doanh Nghiệp

### Tách Bạch Giữa Môi Trường Dev và Môi Trường Production
- **Giai đoạn R&D / Dev**: Sử dụng Antigravity Desktop 2.0 (GUI), IDE extension và CLI để lập trình viên tương tác, code và duyệt diff trực quan.
- **Giai đoạn Production Backend**: Đóng gói toàn bộ logic tác nhân vào microservice (FastAPI) bằng `google.antigravity` SDK. Tác nhân chạy không cần giao diện (headless), nhận payload từ webhook n8n hoặc API gateway, tự động gọi các tool nghiệp vụ đã đăng ký.

### Sức Mạnh Của Session Persistence Xuyên Bề Mặt
- Việc truyền `conversation_id` cố định và `save_dir="./sessions"` trong `LocalAgentConfig` mở ra khả năng thanh tra (auditability) tuyệt vời:
  - Backend chạy tự động tính giá cho khách hàng.
  - Khi có trường hợp sai lệch hoặc khách hàng khiếu nại, kỹ sư mở **Antigravity Desktop App** hoặc **Remote Control**, load lại đúng `conversation_id` đó để xem lại từng bước suy luận (thoughts), các tool call đã gọi và các giá trị trả về tại thời điểm đó.

### Quản Trị Rủi Ro Với Declarative Policy Engine (Zero Trust)
- Không bao giờ cho phép Agent trong production có quyền chạy lệnh shell tự do.
- Áp dụng triết lý `deny("*")` đầu tiên, sau đó chỉ mở các tool nghiệp vụ an toàn bằng `allow("tool_name")`. Đối với các tool nhạy cảm (ghi file, chạy shell), bắt buộc phải gắn handler kiểm duyệt (`ask_user(..., handler=...)`).



