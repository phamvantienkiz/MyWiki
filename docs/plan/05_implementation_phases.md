# Implementation Phases & Execution Roadmap

> Lộ trình thực hiện chi tiết cho dự án AI Engineer Wiki Web App theo tiêu chí: **Graph-First View & Lecture Visualizer Pedagogical Reader**.

---

## 1. Lộ trình Thực thi 5 Giai đoạn

### Giai đoạn 1: Khởi tạo Nền tảng & Cấu hình Tokens (Foundation)
- [ ] Khởi tạo dự án Next.js (App Router, TypeScript, Tailwind CSS) bên trong thư mục `view/` bằng `npm`.
- [ ] Cài đặt các gói phụ trợ cần thiết:
  - `lucide-react`: Hệ thống icon nét mảnh 1.5px.
  - `katex`: Hiển thị công thức toán học LaTeX.
  - `clsx`, `tailwind-merge`: Xử lý class linh hoạt.
  - `react-force-graph-2d`: Động cơ đồ thị Canvas Force-Directed mượt mà, tải nhanh.
  - `minisearch`: Tìm kiếm toàn văn in-memory tức thì.
- [ ] Cấu hình `tailwind.config.ts` và `globals.css` tích hợp trọn vẹn:
  - Bảng màu trung tính `soft-clean-cards` (`--bg-page: #F5F5F7`, `--bg-card: #FFFFFF`).
  - Bảng màu 7 miền kiến thức và màu cảnh báo/mầm cây sư phạm (`--color-intuition-bg`, `--color-discrepancy-bg`).
  - Bo góc chuẩn `rounded-card: 28px` và đổ bóng mờ `--shadow-card`.
  - Nhúng stylesheet KaTeX CSS.

### Giai đoạn 2: Tầng Dữ liệu, Graph Engine & Bộ Bóc Tách Sư Phạm (Data & Engine)
- [ ] Xây dựng các Interface kiểu dữ liệu TypeScript trong `src/types/wiki.ts`, `src/types/graph.ts`, và `src/types/lecture.ts`.
- [ ] Viết module `src/lib/wiki.ts`:
  - Đọc 48 file markdown từ `../wiki/*.md`.
  - Bóc tách tiêu đề, tóm tắt, nội dung, `[[wiki-links]]` và liên kết file gốc `../resources/...`.
  - Tính toán danh sách `outgoingLinks` và `backlinks` hai chiều.
- [ ] Viết module `src/lib/graph.ts`:
  - Xây dựng danh sách Nodes và Links đồ thị, gán màu theo miền kiến thức, tính kích thước node theo bậc liên kết.
- [ ] Viết module `src/lib/lecture-parser.ts`:
  - Tự động nhận diện cấu trúc bài viết để chuyển hóa thành các khối sư phạm `lecture-visualizer` (Trực giác, Từ điển ký hiệu, Khối toán KaTeX, Callout trực giác 🌱, Callout mâu thuẫn, Q&A Accordion).

### Giai đoạn 3: Thư viện Thành phần UI & Sư phạm (Component Suite)
- [ ] Xây dựng các UI Components chuẩn "Soft Clean Cards":
  - `<Card />`: Thẻ mềm bo góc 28px, viền mờ 1px, shadow-card.
  - `<Badge />`: Pill badge màu pastel nhận diện miền kiến thức.
  - `<IconButton />`: Nút tròn 32×32px, hit-target 44×44px.
  - `<GhostButton />`: Nút phụ xám nhạt có chevron xoay.
- [ ] Xây dựng bộ Component Sư phạm `lecture-visualizer`:
  - `<SymbolDictionary />`: Bảng từ điển ký hiệu 4 cột.
  - `<IntuitionCallout />`: Hộp thoại "Góc Dành Cho Người Học Chậm" 🌱 màu xanh mầm.
  - `<DiscrepancyCallout />`: Hộp thoại phân tích mâu thuẫn & sắc thái màu đỏ nhạt.
  - `<MathBlock />`: Khối công thức toán học KaTeX.
  - `<QAAccordion />`: Bộ câu hỏi phỏng vấn & phản biện có thể mở/đóng.
  - `<LectureSidebar />`: Sidebar bám dính với ScrollSpy và thanh tiến trình đọc.

### Giai đoạn 4: Trang Chủ Graph-First & Quick View Drawer (Graph Home)
- [ ] Xây dựng trang chủ `app/page.tsx`:
  - Đồ thị toàn cảnh mạng lưới liên kết các khái niệm (Canvas Force Graph 2D).
  - Tương tác chuột: Xoay, kéo, zoom mượt mà; hover highlight ego-network.
  - Thanh công cụ phía trên: Ô tìm kiếm nhanh, nút lọc 7 miền kiến thức, nút chuyển danh sách tài liệu.
- [ ] Xây dựng `<NodeQuickDrawer />`:
  - Ngăn kéo trượt ra từ bên phải khi click vào bất kỳ node nào.
  - Hiển thị nhanh tóm tắt trực giác, định nghĩa, số liên kết và nút *"Đọc Bài Giảng Đầy Đủ $\rightarrow$"*.

### Giai đoạn 5: Trang Bài Giảng Chuyên Sâu & Khung Mở Rộng Sau Này (Lecture Pages)
- [ ] Xây dựng trang bài giảng `app/wiki/[slug]/page.tsx`:
  - Hiển thị toàn bộ nội dung file trong `wiki/` theo đúng layout và phương pháp sư phạm `lecture-visualizer`.
  - Hỗ trợ đầy đủ KaTeX công thức toán, Mermaid sơ đồ luồng, Callouts, và Accordion Q&A.
  - Danh sách liên kết hai chiều (Khái niệm liên quan & Bài viết trỏ tới) + Link mở trực tiếp file gốc trong `resources/`.
- [ ] Xây dựng khung mở rộng `app/learn/[topic]/page.tsx`:
  - Sẵn sàng đón nhận các chuyên đề học tập mới do người dùng yêu cầu tạo sau này.

### Giai đoạn 6: Kiểm Thử Toàn Diện & Tối Ưu Hóa (QA & Verification)
- [ ] Kiểm tra type-check TypeScript: `npx tsc --noEmit` đạt 0 lỗi.
- [ ] Kiểm tra Production Build: `npm run build` thành công 100% trang tĩnh (SSG).
- [ ] Kiểm tra thực tế trên trình duyệt: Đồ thị chuyển động mượt mà, click mở drawer xem tài liệu tức thì, trang bài giảng hiển thị chuẩn sư phạm và công thức toán học sắc nét.

---

## 2. Tiêu Chuẩn Nghiệm Thu (Acceptance Criteria)

- [ ] **Mặc định là Graph**: Vào trang chủ web là thấy ngay đồ thị liên kết trực quan giữa các khái niệm, đơn giản, dễ nhìn.
- [ ] **1-Click xem tài liệu**: Click node là xem được ngay tóm tắt và mở được bài giảng đầy đủ của file wiki tương ứng.
- [ ] **Chuẩn `lecture-visualizer`**: Trang bài giảng có đủ từ điển ký hiệu, hộp thoại trực giác 🌱, KaTeX toán học và Q&A phỏng vấn.
- [ ] **Chuẩn `soft-clean-cards`**: Thẻ trắng bo góc 28px, đổ bóng mờ nhẹ, nền trang xám sáng, màu sắc chỉ dùng cho dữ liệu.
- [ ] **Khả năng mở rộng**: Sẵn sàng tạo thêm các trang chuyên đề học tập mới theo yêu cầu của người dùng sau này.
