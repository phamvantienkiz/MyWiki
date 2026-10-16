# Tasks: Xây dựng LLM Knowledge Wiki cho AI Engineer

- [x] Phân tích toàn diện kho tài liệu `resources/` (114 files, 8 danh mục) <!-- id: 1 -->
  - [x] Viết script phân tích cấu trúc thư mục, mục lục sách và từ khóa trong `docs/ai/` <!-- id: 1.1 -->
  - [x] Trích xuất các chủ đề / khái niệm cốt lõi theo từng miền (GenAI/LLM, Deep Learning, Machine Learning, MLOps, Data Science, Software Eng) <!-- id: 1.2 -->
  - [x] Xác định các sách kinh điển làm nguồn chân lý (Ground Truth) vs các bài giảng/slide/tutorial <!-- id: 1.3 -->
- [x] Thiết kế kiến trúc Entity Page chuẩn phong cách Karpathy LLM Wiki <!-- id: 2 -->
  - [x] Định dạng entity markdown: Summary, Canonical Definition, Mechanism & Architecture, Discrepancies/Nuances across Sources, Practical Engineering Considerations, Wiki-links `[[concept]]`, Direct Source Links `[Document](../resources/...)` <!-- id: 2.1 -->
  - [x] Danh mục phân loại 47 thực thể cốt lõi trên 7 miền kiến thức <!-- id: 2.2 -->
- [x] Biên dịch & Tạo các trang thực thể (Entity Pages) trong `wiki/` <!-- id: 3 -->
  - [x] Miền 1: GenAI, Foundation Models & Reasoning (8 entities) <!-- id: 3.1 -->
  - [x] Miền 2: RAG & Retrieval Systems (7 entities) <!-- id: 3.2 -->
  - [x] Miền 3: Agentic AI & Design Patterns (8 entities) <!-- id: 3.3 -->
  - [x] Miền 4: Deep Learning & Computer Vision / NLP (6 entities) <!-- id: 4.1 -->
  - [x] Miền 5: Machine Learning & Math Foundations (7 entities) <!-- id: 4.2 -->
  - [x] Miền 6: MLOps & Production Engineering (6 entities) <!-- id: 4.3 -->
  - [x] Miền 7: Software Engineering & Data Systems (5 entities) <!-- id: 4.4 -->
- [x] Xây dựng `wiki/index.md` (Tổng quan, mục lục phân tầng, chỉ mục chữ cái A-Z, bản đồ tri thức) <!-- id: 5 -->
- [x] Rà soát, kiểm tra mâu thuẫn giữa các tài liệu và xác nhận tính toàn vẹn liên kết <!-- id: 6 -->
  - [x] Xác minh cú pháp `[[wiki-links]]` và markdown link hoạt động tốt <!-- id: 6.1 -->
  - [x] Kiểm tra liên kết trỏ chính xác về file trong `resources/` <!-- id: 6.2 -->
  - [x] Cập nhật `tasks/lessons.md` <!-- id: 6.3 -->

---

## Phần 2: Xây dựng Giao diện Next.js Web App (`view/`)

- [x] Giai đoạn 1: Khởi tạo Nền tảng & Cấu hình Tokens (`view/`) <!-- id: 7 -->
  - [x] Khởi tạo dự án Next.js (TypeScript, Tailwind CSS) trong `view/` <!-- id: 7.1 -->
  - [x] Cài đặt dependencies: lucide-react, katex, clsx, tailwind-merge, react-force-graph-2d, minisearch <!-- id: 7.2 -->
  - [x] Cấu hình Tailwind Tokens (Soft Clean Cards, 7 Domains, Sư phạm Intuition 🌱 / Discrepancy) & KaTeX CSS <!-- id: 7.3 -->
- [x] Giai đoạn 2: Tầng Dữ liệu, Graph Engine & Bộ Bóc Tách Sư Phạm <!-- id: 8 -->
  - [x] Types định nghĩa: EntityMetadata, GraphNode, GraphLink, LectureModule <!-- id: 8.1 -->
  - [x] Module `src/lib/wiki.ts` đọc và phân tích 48 file markdown trong `../wiki/` <!-- id: 8.2 -->
  - [x] Module `src/lib/graph.ts` tính toán cấu trúc đồ thị, Degree, Domain color <!-- id: 8.3 -->
  - [x] Module `src/lib/lecture-parser.ts` chuyển đổi cấu trúc markdown sang chuẩn `lecture-visualizer` <!-- id: 8.4 -->
- [x] Giai đoạn 3: Bộ Thư viện Thành phần UI & Sư phạm <!-- id: 9 -->
  - [x] Thư viện UI Soft Clean Cards: Card, Badge, IconButton, GhostButton <!-- id: 9.1 -->
  - [x] Thư viện Sư phạm: SymbolDictionary (4 cột), IntuitionCallout 🌱, DiscrepancyCallout, QAAccordion <!-- id: 9.2 -->
  - [x] Thư viện Điều hướng: LectureSidebar với ScrollSpy & Reading Progress Bar <!-- id: 9.3 -->
- [x] Giai đoạn 4: Trang Chủ Graph-First & Quick View Drawer <!-- id: 10 -->
  - [x] Component `KnowledgeGraph`: Canvas Force-Directed 2D, hover highlight ego-network, zoom/pan <!-- id: 10.1 -->
  - [x] Thanh điều khiển: Tìm kiếm nhanh, lọc 7 miền kiến thức, nút chuyển danh sách tài liệu <!-- id: 10.2 -->
  - [x] Component `NodeQuickDrawer`: Ngăn kéo trượt ra xem nhanh tài liệu khi click node <!-- id: 10.3 -->
  - [x] Trang chủ `app/page.tsx` hoàn thiện <!-- id: 10.4 -->
- [x] Giai đoạn 5: Trang Bài Giảng Chi Tiết & Khung Mở Rộng Bài Học <!-- id: 11 -->
  - [x] Trang bài giảng `app/wiki/[slug]/page.tsx` chuẩn `lecture-visualizer` <!-- id: 11.1 -->
  - [x] Khung mở rộng `app/learn/[topic]/page.tsx` cho các chuyên đề học tập sau này <!-- id: 11.2 -->
- [x] Giai đoạn 6: Kiểm Thử Toàn Diện & Nghiệm Thu <!-- id: 12 -->
  - [x] Chạy type-check TypeScript: `npx tsc --noEmit` đạt 0 lỗi <!-- id: 12.1 -->
  - [x] Chạy Production Build: `npm run build` thành công 100% (51/51 static pages) <!-- id: 12.2 -->
  - [x] Cập nhật `tasks/lessons.md` <!-- id: 12.3 -->
