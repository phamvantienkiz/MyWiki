# Design System Specification: "Soft Clean Cards" & "Lecture Visualizer"

> Tài liệu này hợp nhất tinh hoa của hai nguồn chuẩn mực:
> 1. [soft-clean-cards.md](../../docs/references/soft-clean-cards.md): Phong cách thẻ mềm bo góc 28px, đổ bóng mờ nhẹ, nền trang xám sáng thoáng, màu sắc chỉ dùng cho dữ liệu.
> 2. [lecture-visualizer SKILL](../../.agents/skills/lecture-visualizer/SKILL.md): Phương pháp sư phạm trực quan cho người học chậm, bảng từ điển ký hiệu 4 cột, hộp thoại `.callout.intuition` 🌱, thanh tiến trình đọc và sidebar ScrollSpy.

---

## 1. Triết lý Thiết kế Tích hợp

1. **Giao diện Phục vụ Nhận thức (Cognitive-First Design)**:
   - Đồ thị tri thức đóng vai trò là "Bản đồ tư duy toàn cảnh" giúp người học thấy ngay mối liên hệ giữa các khái niệm.
   - Khi đọc bài giảng, giao diện chuyển sang trạng thái tĩnh lặng, tập trung cao độ (Deep Focus Reading): không pop-up gây xao nhãng, khoảng trắng hào phóng, chữ sắc nét.
2. **Một Thẻ = Một Nhiệm vụ (One Card, One Intent)**:
   - Mỗi đơn vị kiến thức (Từ điển ký hiệu, Khối toán học, Hộp thoại trực giác, Phân tích mâu thuẫn) được đóng gói trong một thẻ Soft Card riêng biệt hoặc một vùng phụ rõ ràng.
3. **Màu Sắc là Tín hiệu Sư phạm (Color as Pedagogical Signal)**:
   - **Xanh Ngọc Bảo (`#0E6320` trên nền `#D8F3E4`)**: Hộp thoại Trực giác "Góc Dành Cho Người Học Chậm" 🌱.
   - **Đỏ Tín hiệu (`#9E221B` trên nền `#FDECEB`)**: Cảnh báo mâu thuẫn, lỗi thường gặp (Failure modes), điểm vênh nhau giữa lý thuyết và thực tiễn.
   - **Xanh Dương Điện (`#0D3EA3` trên nền `#D9E8FF`)**: Công thức toán học và định lý kinh điển.
   - **Tím Bão hòa (`#6A1AA3` trên nền `#E6DDFB`)**: Thuật toán và cơ chế kiến trúc.

---

## 2. Hệ thống Tokens Hoàn chỉnh

### 2.1 Bảng Màu Trung tính & Sư phạm

```css
:root {
  /* Neutral Palette (soft-clean-cards) */
  --bg-page: #F5F5F7;
  --bg-card: #FFFFFF;
  --bg-subtle: #F4F4F6;
  --bg-subtle-hover: #ECECEF;
  --border-hairline: #EFEFF2;
  --border-card: #E9E9EE;
  --text-primary: #0B0B0F;
  --text-secondary: #6B6B76;
  --text-tertiary: #9A9AA5;
  --ink: #111114;

  /* Pedagogical & Data Tokens (lecture-visualizer) */
  --color-intuition-bg: #F0FDF4;        /* Nền hộp trực giác xanh mầm */
  --color-intuition-border: #86EFAC;    /* Viền hộp trực giác */
  --color-intuition-text: #166534;      /* Chữ hộp trực giác */
  
  --color-discrepancy-bg: #FEF2F2;      /* Nền hộp mâu thuẫn đỏ nhạt */
  --color-discrepancy-border: #FCA5A5;  /* Viền hộp mâu thuẫn */
  --color-discrepancy-text: #991B1B;    /* Chữ hộp mâu thuẫn */

  /* 7 Domain Palette */
  --domain-genai: #1F5FFF;
  --domain-rag: #B13BF0;
  --domain-agentic: #FF8A1F;
  --domain-deeplearning: #1FA63A;
  --domain-ml-math: #0EA5E9;
  --domain-mlops: #EC4899;
  --domain-software: #64748B;

  /* Radius Tokens */
  --radius-xs: 4px;
  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-lg: 16px;
  --radius-xl: 28px;                  /* Chuẩn Soft Card */
  --radius-full: 999px;

  /* Shadows */
  --shadow-card: 0 1px 2px rgba(16, 16, 24, 0.04), 0 8px 24px rgba(16, 16, 24, 0.06);
  --shadow-control: 0 1px 2px rgba(16, 16, 24, 0.08), 0 0 0 1px rgba(16, 16, 24, 0.04);
}
```

---

## 3. Quy chuẩn Thành phần Sư phạm (`lecture-visualizer`)

### 3.1 Hộp Thoại Trực Giác (`.callout-intuition`)
- **Mục đích**: Giải thích bản chất khái niệm bằng lời văn mộc mạc, ví dụ đời thường (siêu thị, giỏ hàng, thí sinh thi cử).
- **Kiểu dáng**: Nền xanh lá dịu `bg-[#F0FDF4]`, viền trái dày 3px `border-l-[3px] border-[#22C55E]`, bo góc `rounded-[16px]`, padding `20px`.
- **Header**: Icon mầm cây 🌱 kết hợp nhãn: *"GÓC DÀNH CHO NGƯỜI HỌC CHẬM — HIỂU BẢN CHẤT"* (`text-[12px] font-semibold text-[#15803D] uppercase tracking-wider`).

### 3.2 Bảng Từ Điển Ký Hiệu 4 Cột (`<SymbolDictionary />`)
- **Mục đích**: Xóa bỏ rào cản ký hiệu toán học gây hoang mang cho người học.
- **Cấu trúc Bảng**:
  - `Ký hiệu (LaTeX)`: Hiển thị qua KaTeX (ví dụ: $\mathcal{L}, \sigma, \mathbf{W}_Q, \mathbf{W}_K$).
  - `Tên tiếng Anh chuẩn`: (ví dụ: *Query Weight Matrix*).
  - `Tên tiếng Việt`: (ví dụ: *Ma trận trọng số truy vấn*).
  - `Nghĩa đời thường`: (ví dụ: *Chiếc kính lọc để xác định xem token đang tìm kiếm loại thông tin gì*).
- **Kiểu dáng**: Nền card phụ `bg-[#F4F4F6] rounded-[20px] p-4`, không dùng viền lưới dày đặc. Dùng xen kẽ nền nhẹ để phân biệt các dòng.

### 3.3 Hộp Phân Tích Mâu Thuẫn & Sắc Thái (`.callout-discrepancy`)
- **Mục đích**: Chỉ ra các mâu thuẫn giữa lý thuyết giáo trình kinh điển và thực tiễn triển khai (Discrepancies & Nuances across Sources).
- **Kiểu dáng**: Nền đỏ nhạt `bg-[#FEF2F2]`, viền trái `border-l-[3px] border-[#EF4444]`, bo góc `rounded-[16px]`, padding `20px`.
- **Header**: Icon cân nhắc ⚖️ hoặc cảnh báo ⚠️ kèm nhãn *"MÂU THUẪN & SẮC THÁI CẦN LƯU Ý"*.

### 3.4 Bộ Câu Hỏi Phản Biện & Phỏng Vấn Accordion (`<QAAccordion />`)
- **Mục đích**: Giúp người học tự kiểm tra kiến thức và chuẩn bị cho các buổi phỏng vấn Senior AI hoặc bảo vệ đề tài.
- **Kiểu dáng**: Từng câu hỏi là một thẻ mini dạng thanh trượt:
  - Trạng thái đóng: Tiêu đề câu hỏi in đậm vừa, icon chevron bên phải.
  - Trạng thái mở: Mở rộng mượt mà (240ms cubic-bezier), hiển thị câu trả lời chi tiết kèm các luận điểm phản biện cốt lõi.

### 3.5 Sticky Sidebar với ScrollSpy & Reading Progress Bar
- **Bố cục**: Cố định bên trái hoặc bên phải bài giảng (chiều rộng ~280px).
- **Thanh tiến trình (Progress Bar)**: Thanh mảnh 3px chạy dọc theo danh sách đề mục bài học, đổi màu tương ứng với tỷ lệ phần trăm đã cuộn.
- **ScrollSpy**: Tự động sáng đèn mục đang đọc trên màn hình, click vào đề mục nào sẽ cuộn mượt đến đúng vị trí đó.
