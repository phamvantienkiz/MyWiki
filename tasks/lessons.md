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
