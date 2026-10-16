# Data Pipeline & Pedagogical Architecture

> Tài liệu này mô tả luồng bóc tách dữ liệu từ các file Markdown trong `../wiki/*.md`, bộ chuyển đổi cấu trúc sư phạm `lecture-visualizer`, và cơ chế mở rộng cho các bài học tương lai.

---

## 1. Luồng Bóc Tách Cấu Trúc Sư Phạm (`lib/lecture-parser.ts`)

Mỗi tệp Markdown trong `wiki/` đã được biên dịch theo cấu trúc Karpathy nghiêm ngặt. Khi hiển thị lên giao diện web, bộ chuyển đổi `lecture-parser` sẽ nhận diện các đề mục để đóng gói thành các khối sư phạm tương tác:

```
File Markdown thô (wiki/*.md)
       │
       ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. # Title & Summary                                        │
│    ──► Render: Hero Card + Đoạn Trực giác Bản chất          │
├─────────────────────────────────────────────────────────────┤
│ 2. ## 1. Canonical Definition                               │
│    ──► Render: Khối Định nghĩa Học thuật + KaTeX Math       │
│    ──► Tự động tạo: Bảng Từ điển Ký hiệu 4 Cột              │
├─────────────────────────────────────────────────────────────┤
│ 3. ## 2. Mechanism & Architecture                           │
│    ──► Render: Sơ đồ luồng Mermaid + Phân tích thuật toán   │
├─────────────────────────────────────────────────────────────┤
│ 4. ## 3. Discrepancies & Nuances across Sources             │
│    ──► Render: Hộp thoại .callout-discrepancy (Màu đỏ nhạt) │
├─────────────────────────────────────────────────────────────┤
│ 5. ## 4. Practical Considerations & Interview Angle         │
│    ──► Render: .callout-intuition (Màu xanh mầm 🌱)         │
│    ──► Render: Bộ câu hỏi Phỏng vấn QAAccordion             │
├─────────────────────────────────────────────────────────────┤
│ 6. ## 5. Related Concepts & Original Sources                │
│    ──► Render: Chip liên kết [[wiki-links]] có Hover Popup  │
│    ──► Render: Backlinks Panel & Original Sources Panel     │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Mô hình Bài học Mở rộng Tương lai (`src/types/lecture.ts`)

Khi người dùng sau này yêu cầu: *"Hãy tạo một bài học chi tiết về [Chủ đề X] theo phong cách lecture-visualizer"*, cấu trúc bài học sẽ tuân theo Schema chuẩn:

```typescript
export interface LectureModule {
  slug: string;                 // Mã định danh bài giảng, ví dụ: 'fp-growth-algorithm'
  title: string;                // Tiêu đề bài học
  domainId: string;             // Miền kiến thức liên kết
  readingTimeMinutes: number;   // Thời gian đọc ước tính
  sections: {
    id: string;                 // Phục vụ ScrollSpy anchor
    title: string;              // Tên đề mục (H2)
    type: 'intuition' | 'dictionary' | 'math' | 'mechanism' | 'discrepancy' | 'practice' | 'qa';
    contentHtml: string;        // Nội dung đã parse an toàn
  }[];
  symbolDictionary?: {
    symbol: string;             // Ký hiệu LaTeX
    enName: string;             // Tên tiếng Anh
    viName: string;             // Tên tiếng Việt
    intuition: string;          // Ý nghĩa đời thường
  }[];
  qaList?: {
    question: string;
    answer: string;
    difficulty: 'Senior' | 'Staff' | 'Lead';
  }[];
  outgoingLinks: string[];
  backlinks: string[];
  resourceLinks: { label: string; url: string }[];
}
```

---

## 3. Cơ chế Khám phá Động (Dynamic Discovery & Auto-Indexing)

1. **Quét tự động**:
   - Tầng Server (`lib/wiki.ts`) quét toàn bộ các file `.md` trong thư mục `wiki/` (và bất kỳ thư mục bài học mới nào được chỉ định sau này).
   - Tự động phát hiện liên kết hai chiều: Nếu bài học mới chứa liên kết `[[large-language-models]]`, hệ thống tự động cập nhật `backlinks` của trang `large-language-models` ngay tại thời điểm build/request.
2. **Tự động Cập nhật Đồ thị Tri thức**:
   - Mỗi bài học mới tự động trở thành một node mới trong đồ thị Graph.
   - Các `[[wiki-links]]` trong bài học tự động trở thành các cạnh (links) nối bài học mới vào cụm tri thức tương ứng mà **không cần cấu hình bằng tay**.
3. **Hiệu năng Caching**:
   - Sử dụng In-Memory Cache tại runtime. Quá trình nạp và phân giải toàn bộ 48 bài học và mạng lưới đồ thị chỉ mất dưới 20ms.
