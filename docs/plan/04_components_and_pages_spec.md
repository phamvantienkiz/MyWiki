# Components & Pages Specification: Graph Explorer & Lecture Visualizer

> Tài liệu này mô tả chi tiết giao diện trang web, cách bố trí các thành phần và tương tác người dùng theo phương châm: **"Mặc định xem Graph đơn giản, click là xem được tài liệu, trình bày chuẩn lecture-visualizer"**.

---

## 1. Bản Đồ Các Trang (Pages Map)

| Đường dẫn (Route) | Vai trò & Mục đích | Trải nghiệm Chính |
| :--- | :--- | :--- |
| **`/` (Trang Chủ)** | **Graph-First Knowledge Explorer** | Hiển thị đồ thị liên kết toàn cảnh các khái niệm, thanh tìm kiếm nhanh, lọc 7 miền, và Quick View Drawer xem nhanh tài liệu. |
| **`/wiki/[slug]`** | **Trang Bài Giảng Chuyên Sâu** | Trình bày nội dung tài liệu wiki theo phương pháp sư phạm `lecture-visualizer` (Sidebar ScrollSpy, Từ điển ký hiệu, KaTeX, Callout trực giác 🌱, Q&A). |
| **`/learn/[topic]`** | **Khung Mở Rộng Bài Học Sau Này** | Dành cho các chuyên đề học tập mới do người dùng yêu cầu tạo thêm, tự động kế thừa toàn bộ engine sư phạm và tự động nối vào đồ thị. |

---

## 2. Trang Chủ: Graph-First Explorer (`app/page.tsx`)

### 2.1 Thành phần Giao diện
1. **Header Tối giản Nổi (Floating Minimal Bar)**:
   - Logo: `✦ AI Wiki`.
   - Ô tìm kiếm nhanh: Gõ để highlight và zoom tới node tương ứng.
   - 7 chip lọc màu đại diện cho 7 miền tri thức.
   - Nút chuyển nhanh sang dạng xem Danh mục tài liệu (`Danh Sách 48 Bài`).
2. **Khu vực Đồ thị Trung tâm (Interactive Canvas)**:
   - Chiếm toàn bộ khung nhìn chính (full viewport).
   - Nền xám dịu `#F5F5F7`.
   - Các quả cầu khái niệm nổi bật với màu sắc của miền kiến thức.
   - Các đường liên kết nối mờ giữa các khái niệm có liên quan (`[[wiki-links]]`).
3. **Ngăn Kéo Xem Nhanh (`<NodeQuickDrawer />`)**:
   - Khi người dùng click vào bất kỳ node nào trên đồ thị, ngăn kéo này trượt ra từ bên phải màn hình (rộng ~420px):
     - Tiêu đề khái niệm + Badge miền tri thức.
     - Tóm tắt trực giác từ file wiki gốc.
     - Định nghĩa chính và công thức toán học nếu có.
     - Danh sách các khái niệm liên quan (Outgoing / Backlinks).
     - Nút đen `--ink` bo góc 12px *"Xem Toàn Bộ Bài Giảng $\rightarrow$"* chuyển sang `/wiki/[slug]`.

---

## 3. Trang Bài Giảng Chuyên Sâu: Chuẩn `lecture-visualizer` (`app/wiki/[slug]/page.tsx`)

Bố cục 2 phần: Sidebar điều hướng cố định + Khung bài giảng Full-Width thoáng đãng:

```
┌─────────────────┬────────────────────────────────────────────────────────┐
│  STICKY SIDEBAR │  KHUNG BÀI GIẢNG FULL-WIDTH CHUẨN LECTURE-VISUALIZER   │
│  (ScrollSpy)    │                                                        │
│                 │  ┌──────────────────────────────────────────────────┐  │
│  • Tiến trình   │  │ 1. Hero Card: Tiêu đề & Trực giác đời thường     │  │
│    đọc (0-100%) │  └──────────────────────────────────────────────────┘  │
│                 │                                                        │
│  • 1. Trực giác │  ┌──────────────────────────────────────────────────┐  │
│  • 2. Từ điển   │  │ 2. Bảng Từ Điển Ký Hiệu 4 Cột                    │  │
│  • 3. Định nghĩa│  └──────────────────────────────────────────────────┘  │
│  • 4. Kiến trúc │                                                        │
│  • 5. Góc chậm  │  ┌──────────────────────────────────────────────────┐  │
│  • 6. Mâu thuẫn │  │ 3. Định Nghĩa Chính Thống & Công Thức Toán KaTeX │  │
│  • 7. Q&A       │  └──────────────────────────────────────────────────┘  │
│  • 8. Liên kết  │                                                        │
│                 │  ┌──────────────────────────────────────────────────┐  │
│  [⬅ Về Graph]   │  │ 4. Hộp Thoại "Góc Dành Cho Người Học Chậm" 🌱     │  │
│                 │  └──────────────────────────────────────────────────┘  │
│                 │                                                        │
│                 │  ┌──────────────────────────────────────────────────┐  │
│                 │  │ 5. Hộp Thoại Phân Tích Mâu Thuẫn & Sắc Thái      │  │
│                 │  └──────────────────────────────────────────────────┘  │
│                 │                                                        │
│                 │  ┌──────────────────────────────────────────────────┐  │
│                 │  │ 6. Bộ Câu Hỏi Phỏng Vấn & Phản Biện (Accordion)  │  │
│                 │  └──────────────────────────────────────────────────┘  │
└─────────────────┴────────────────────────────────────────────────────────┘
```

### Chi tiết các khối sư phạm trên trang bài giảng:
1. **Hero Card**: Tên khái niệm H1 lớn, Badge pastel miền tri thức, thời gian đọc ước tính, và lời giải thích bản chất bằng văn phong đời thường.
2. **Bảng Từ Điển Ký Hiệu 4 Cột (`<SymbolDictionary />`)**:
   - Liệt kê các ký hiệu toán học / biến số xuất hiện trong bài kèm tên tiếng Anh, tên tiếng Việt, và nghĩa đời thường trực giác.
3. **Khối Toán Học & Định Nghĩa Chuẩn Mực (`<MathBlock />`)**:
   - Trích xuất từ sách giáo khoa kinh điển, công thức LaTeX render qua KaTeX sắc nét, căn giữa, nền xám phụ dịu mắt.
4. **Hộp Thoại "Góc Dành Cho Người Học Chậm" (`<IntuitionCallout />`)**:
   - Khối màu xanh lá mầm 🌱 (`bg-[#F0FDF4] border-l-[3px] border-[#22C55E]`) giải thích cặn kẽ các cơ chế trừu tượng (như Self-Attention, Receptive Field, Gradient Vanishing, K-Fold, LoRA).
5. **Hộp Thoại Phân Tích Mâu Thuẫn (`<DiscrepancyCallout />`)**:
   - Khối màu đỏ nhạt (`bg-[#FEF2F2] border-l-[3px] border-[#EF4444]`) chỉ ra sự khác biệt giữa lý thuyết hàn lâm và triển khai thực chiến.
6. **Bộ Câu Hỏi Phỏng Vấn & Phản Biện Accordion (`<QAAccordion />`)**:
   - Các câu hỏi phỏng vấn Senior AI Engineer có nút bấm mở rộng xem đáp án và phân tích sâu.
7. **Mạng Lưới Hai Chiều & Tài Liệu Gốc**:
   - Các khái niệm liên quan hiển thị dưới dạng thẻ Soft Clean Card, click vào để chuyển sang bài giảng tương ứng.
   - Nút mở trực tiếp file tài liệu PDF/Slide gốc trong thư mục `resources/`.

---

## 4. Khung Mở Rộng Bài Học Tương Lai (`app/learn/[topic]/page.tsx`)

- Khi người dùng muốn học bất kỳ chuyên đề mới nào (ví dụ: *"Tạo bài học về Contrastive Learning"*, *"Tạo bài học về State Space Models & Mamba"*):
- Hệ thống sử dụng chung template `LectureLayout`:
  - Đọc file bài giảng mới.
  - Tự động áp dụng toàn bộ giao diện sư phạm `lecture-visualizer`.
  - Tự động nối vào Đồ thị Tri thức trên Trang Chủ.
