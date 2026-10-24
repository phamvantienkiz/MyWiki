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

## 2. Hệ thống Tokens Hoàn chỉnh (3-Layer Architecture)

Hệ thống token được tổ chức theo chuẩn mực 3 tầng: **Primitive** (Giá trị nguyên bản) $\rightarrow$ **Semantic** (Ý nghĩa sử dụng & Chuyển đổi giao diện) $\rightarrow$ **Component** (Tùy biến từng thành phần).

```
┌────────────────────────────────────────────────────────┐
│  Component Tokens: --btn-active-bg, --pill-reading-bg  │
├────────────────────────────────────────────────────────┤
│  Semantic Tokens: --bg-card, --text-primary, --primary │ (Đổi giá trị khi sang Dark Mode)
├────────────────────────────────────────────────────────┤
│  Primitive Tokens: --slate-900, --blue-600, --space-4   │ (Cố định, không đổi)
└────────────────────────────────────────────────────────┘
```

### 2.1 Bảng Tokens Chuẩn Light Mode (`:root`)

```css
:root {
  /* Primitive Colors - Slate & Accents */
  --slate-50: #F8FAFC;
  --slate-100: #F1F5F9;
  --slate-200: #E2E8F0;
  --slate-300: #CBD5E1;
  --slate-400: #94A3B8;
  --slate-600: #475569;
  --slate-700: #334155;
  --slate-900: #0F172A;
  --slate-950: #0B0F19;

  /* Semantic Brand & Accents */
  --primary: #2563EB;
  --primary-light: #EFF6FF;
  --primary-dark: #1D4ED8;
  --primary-glow: rgba(37, 99, 235, 0.2);

  /* Semantic Surfaces (Light) */
  --bg-page: #F6F7F9;
  --bg-sidebar: #FFFFFF;
  --bg-card: #FFFFFF;
  --bg-subtle: #F1F3F5;
  --bg-subtle-hover: #E9ECEF;
  --bg-elevated: #FFFFFF;

  /* Semantic Hairlines & Borders */
  --border-hairline: #EEF0F2;
  --border-card: #E2E6EA;
  --border-highlight: #BFDBFE;

  /* Semantic Typography */
  --text-primary: #0F172A;
  --text-body: #334155;
  --text-secondary: #475569;
  --text-tertiary: #94A3B8;
  --ink: #0B0F19;

  /* Pedagogical Callout Tokens (Light) */
  --callout-intuition-bg: #ECFDF5;
  --callout-intuition-border: #059669;
  --callout-intuition-text: #064E3B;
  --callout-intuition-header: #065F46;

  --callout-def-bg: #EFF6FF;
  --callout-def-border: #2563EB;
  --callout-def-text: #1E3A8A;
  --callout-def-header: #1D4ED8;

  --callout-tip-bg: #F5F3FF;
  --callout-tip-border: #7C3AED;
  --callout-tip-text: #4C1D95;
  --callout-tip-header: #6D28D9;

  --callout-warn-bg: #FEF2F2;
  --callout-warn-border: #DC2626;
  --callout-warn-text: #991B1B;
  --callout-warn-header: #B91C1C;

  /* 7 Domain Palette */
  --domain-genai: #1F5FFF;
  --domain-rag: #B13BF0;
  --domain-agentic: #FF8A1F;
  --domain-deeplearning: #1FA63A;
  --domain-ml-math: #0EA5E9;
  --domain-mlops: #EC4899;
  --domain-software: #64748B;

  /* Code & Syntax Tokens */
  --code-inline-bg: #E2E8F0;
  --code-inline-text: #0F172A;
  --code-inline-border: transparent;
  --code-block-bg: #0F172A;
  --code-block-text: #F8FAFC;
  --code-block-border: #1E293B;

  /* Shadows (Light Soft Shadow) */
  --shadow-sm: 0 1px 2px rgba(15, 23, 42, 0.04);
  --shadow-card: 0 1px 3px rgba(15, 23, 42, 0.05), 0 10px 25px -5px rgba(15, 23, 42, 0.04);
  --shadow-card-hover: 0 4px 12px rgba(15, 23, 42, 0.06), 0 12px 28px -4px rgba(15, 23, 42, 0.05);

  /* Radius Tokens */
  --radius-xs: 4px;
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --radius-xl: 26px;
  --radius-full: 9999px;
}
```

### 2.2 Bảng Tokens Chuẩn Dark Mode (`html.dark, body.dark`)

Dark Mode không đơn thuần là đảo màu âm bản, mà tuân thủ chặt chẽ 4 nguyên tắc công thái học nhận thức:
1. **Phân tầng Độ cao Bề mặt (Surface Elevation Hierarchy)**: Nền trang `#0B0F17` (0dp) $\rightarrow$ Sidebar `#0F1626` (1dp) $\rightarrow$ Thẻ Card `#131B2E` (2dp) $\rightarrow$ Khối phụ `#1C263B` (3dp).
2. **Chống lóa mắt & Đạt chuẩn WCAG AA**: Tuyệt đối không dùng chữ `#FFFFFF` 100% trên nền đen; dùng `--text-primary: #F1F5F9` và `--text-body: #CBD5E1`.
3. **Bảo tồn Tín hiệu Sư phạm**: Dùng nền sẫm bão hòa thấp (`rgba(..., 0.14)`) kết hợp chữ sáng pastel và viền phát quang vi tế.
4. **Nút tương tác Active**: Tự động chuyển sang màu nhấn `--primary: #3B82F6` rực rỡ kèm hiệu ứng glow.

```css
html.dark,
body.dark {
  /* Semantic Brand & Accents */
  --primary: #3B82F6;
  --primary-light: rgba(59, 130, 246, 0.16);
  --primary-dark: #60A5FA;
  --primary-glow: rgba(59, 130, 246, 0.35);

  /* Calculated Surface Elevation */
  --bg-page: #0B0F17;              /* Deep Slate base (0dp) */
  --bg-sidebar: #0F1626;           /* Left fixed navigation surface (1dp) */
  --bg-card: #131B2E;              /* Soft card elevated surface (2dp) */
  --bg-subtle: #1C263B;            /* Secondary container / table-head (3dp) */
  --bg-subtle-hover: #26334D;      /* Hover state on subtle surfaces */
  --bg-elevated: #182238;          /* High elevation modal & floating UI */

  /* Luminescent Hairlines & Borders */
  --border-hairline: rgba(255, 255, 255, 0.07);
  --border-card: rgba(255, 255, 255, 0.11);
  --border-highlight: rgba(96, 165, 250, 0.35);

  /* Contrast-Safe Typography (WCAG AA Compliance) */
  --text-primary: #F1F5F9;         /* Slate 100 - Sáng sắc nét, không chói */
  --text-body: #CBD5E1;            /* Slate 300 - Êm dịu cho bài đọc dài */
  --text-secondary: #94A3B8;       /* Slate 400 - Chú thích và metadata */
  --text-tertiary: #64748B;        /* Slate 500 - Nhãn phụ */
  --ink: #FFFFFF;                  /* Nổi bật tuyệt đối */

  /* Pedagogical Callout Tokens (Dark) */
  --callout-intuition-bg: rgba(5, 150, 105, 0.14);
  --callout-intuition-border: #10B981;
  --callout-intuition-text: #A7F3D0;
  --callout-intuition-header: #34D399;

  --callout-def-bg: rgba(37, 99, 235, 0.14);
  --callout-def-border: #3B82F6;
  --callout-def-text: #BFDBFE;
  --callout-def-header: #60A5FA;

  --callout-tip-bg: rgba(124, 58, 237, 0.14);
  --callout-tip-border: #8B5CF6;
  --callout-tip-text: #DDD6FE;
  --callout-tip-header: #A78BFA;

  --callout-warn-bg: rgba(220, 38, 38, 0.14);
  --callout-warn-border: #EF4444;
  --callout-warn-text: #FECACA;
  --callout-warn-header: #F87171;

  /* Code & Syntax Tokens */
  --code-inline-bg: #1A2438;
  --code-inline-text: #38BDF8;
  --code-inline-border: rgba(255, 255, 255, 0.08);
  --code-block-bg: #070A10;
  --code-block-text: #F1F5F9;
  --code-block-border: rgba(255, 255, 255, 0.12);

  /* Shadows with Dark Elevation Glow */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-card: 0 4px 20px rgba(0, 0, 0, 0.35), 0 0 0 1px rgba(255, 255, 255, 0.06);
  --shadow-card-hover: 0 8px 30px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(96, 165, 250, 0.25);

  /* Interactive Elements */
  --btn-interactive-bg: #162033;
  --btn-interactive-text: var(--text-primary);
  --btn-interactive-border: rgba(255, 255, 255, 0.12);
  --btn-active-bg: var(--primary);
  --btn-active-text: #FFFFFF;
  --btn-active-border: var(--primary);
  --btn-active-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
}
```

### 2.3 Cơ Chế Điều Khiển & Đồng Bộ Theme
- **Tự động nhận diện thiết bị**: Sử dụng `window.matchMedia('(prefers-color-scheme: dark)')` khi người dùng chưa chọn thủ công.
- **Lưu trữ bền vững**: Ghi nhận tùy chọn vào `localStorage.getItem('baha_interview_theme')`.
- **Hiệu ứng chuyển đổi (Smooth Motion Transition)**: Sử dụng `transition: background-color 0.25s ease, color 0.25s ease, border-color 0.25s ease` trên toàn bộ cây thành phần để tránh chớp giật thị giác.

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
