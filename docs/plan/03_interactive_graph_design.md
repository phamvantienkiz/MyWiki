# Interactive Knowledge Graph Design: Simple, Intuitive & Connected

> **Tiêu chí chỉ đạo**: *"Thông thường chỉ cần view graph là được, đơn giản thôi không cần phức tạp. Có các chỗ để ví dụ như muốn xem một tài liệu thì có thể click vào và view lên, nội dung chính là các file trong wiki."*

---

## 1. Triết lý Thiết kế Đồ thị: Tinh gọn & Trực giác (Minimalist Graph Explorer)

Đồ thị không phải là một công cụ phức tạp, mà là **Bản đồ Tri thức Tự nhiên** đặt ngay tại Trang Chủ:
- **Tập trung vào Mối quan hệ**: Khi truy cập web, người dùng thấy ngay mạng lưới 48 khái niệm liên kết với nhau bằng các đường dây thanh mảnh.
- **Thao tác 1-Click để Xem Tài liệu**: Click vào bất kỳ node nào sẽ mở ngay ngăn xem nhanh (Quick View Drawer) bên cạnh mà không làm mất góc nhìn đồ thị, hoặc có thể mở toàn màn hình để học chuyên sâu.
- **Phân loại Màu sắc Rõ ràng**: 7 màu pastel/data đại diện cho 7 miền tri thức, dễ dàng nhận diện đâu là cụm GenAI, RAG, Deep Learning hay MLOps.

---

## 2. Bố cục Giao diện Graph Trang Chủ (`/`)

```
┌────────────────────────────────────────────────────────────────────────┐
│  ✦ AI Engineer Knowledge Graph       [ Search Concept ]  [ 7 Domains ] │
├──────────────────────────────────────────┬─────────────────────────────┤
│                                          │  QUICK VIEW DRAWER (Slide)  │
│                                          │  ┌───────────────────────┐  │
│          ( Transformer )                 │  │ Large Language Models │  │
│            /         \                   │  │ [GenAI & Foundation]  │  │
│     ( LLMs )-------( Attention )         │  │                       │  │
│       /   \         /                    │  │ 📖 Tóm Tắt Bản Chất:  │  │
│  ( LoRA ) ( RAG )-( Vector Embeddings )  │  │ LLM là các mô hình... │  │
│                                          │  │                       │  │
│                                          │  │ 🔗 Liên kết:          │  │
│   CANVAS VIEWPORT MƯỢT MÀ                │  │ • Transformer         │  │
│   • Kéo thả chuột để xoay / dời vị trí   │  │ • Prompt Engineering  │  │
│   • Cuộn chuột để phóng to / thu nhỏ     │  │                       │  │
│   • Hover node để sáng lân cận           │  │ [ 📖 Đọc Bài Giảng ➔] │  │
│                                          │  └───────────────────────┘  │
└──────────────────────────────────────────┴─────────────────────────────┘
```

---

## 3. Đặc tả Tương tác Đồ thị

### 3.1 Trực quan hóa Node & Cạnh (Visual Attributes)
- **Node (Khái niệm)**:
  - Hình tròn phẳng hoặc cầu ngọc mờ 3D đơn giản.
  - Màu sắc lấy theo bảng màu 7 miền (xanh dương, tím, cam, xanh lá, xanh ngọc, hồng, xám thép).
  - Bán kính tỷ lệ theo mức độ quan trọng (tổng số liên kết in + out).
  - Nhãn văn bản (Label): Tên khái niệm hiển thị rõ ràng, font Inter, màu xám đậm dễ đọc.
- **Cạnh (Liên kết giữa các khái niệm)**:
  - Đường kẻ thanh mảnh 1px, màu xám nhạt trong suốt `rgba(16, 16, 24, 0.12)`.
  - Có mũi tên nhỏ tinh tế biểu thị chiều dẫn truyền tri thức.

### 3.2 Tương tác Chuột (Mouse Interaction)
1. **Hover vào Node**:
   - Node đang rê chuột và toàn bộ các node kết nối trực tiếp (1st-degree neighbors) cùng các cạnh liên kết giữ độ sáng 100%.
   - Tất cả các node khác tự động mờ đi nhẹ nhàng (30% opacity).
   - Xuất hiện tooltip nhỏ hiển thị tên và miền kiến thức.
2. **Click vào Node**:
   - Tự động mở **Quick View Drawer** trượt ra từ cạnh phải màn hình.
   - Camera đồ thị tự động chuyển động mượt mà để căn node đó vào trung tâm góc nhìn.
3. **Double Click vào Node**:
   - Chuyển hướng trực tiếp đến trang bài giảng chi tiết `/wiki/[slug]`.

---

## 4. Ngăn Xem Nhanh Tài liệu (`<NodeQuickDrawer />`)

Là chiếc "cầu nối" giúp người dùng xem nhanh tài liệu wiki mà không bị gián đoạn trải nghiệm đồ thị:
- **Tiêu đề & Badge**: Tên khái niệm H1 + Badge miền kiến thức.
- **Tóm tắt Sư phạm**: Đoạn tóm tắt trực giác từ file markdown gốc, font 14px dễ đọc, khoảng cách dòng thoáng.
- **Định nghĩa Học thuật Rút gọn**: Trích đoạn công thức toán học KaTeX nếu có.
- **Mạng lưới Liên kết Nhanh**:
  - *Kết nối tới (Connects To)*: Danh sách các khái niệm liên quan, click vào sẽ nhảy tâm đồ thị sang node đó ngay lập tức.
  - *Được trích dẫn bởi (Referenced By)*: Danh sách các bài khác tham chiếu tới bài này.
- **Nút Hành động Chính**: Nút đen `--ink` bo góc 12px *"Đọc Bài Giảng Đầy Đủ $\rightarrow$"* dẫn đến trang `lecture-visualizer` toàn màn hình.

---

## 5. Thanh Điều khiển Tối giản (`<GraphControls />`)

- **Ô Tìm kiếm Nhanh (Instant Filter)**: Gõ chữ để tìm khái niệm (ví dụ: `rag`, `yolo`, `transformer`), đồ thị sẽ tự động lọc và phóng to vào node đó.
- **Bộ lọc 7 Miền Kiến thức (Domain Filter Chips)**: 7 nút bấm tròn nhỏ tương ứng 7 màu. Bấm vào nút nào thì chỉ hiển thị các node thuộc miền đó, giúp người dùng tập trung nghiên cứu riêng lẻ từng mảng.
- **Nút Đặt lại Góc nhìn (Reset Center)**: Đưa đồ thị về vị trí căn giữa tối ưu.
