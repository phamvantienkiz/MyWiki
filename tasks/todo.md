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

---

## Phần 3: Chuyên Đề Ôn Tập Phỏng Vấn AI Intern - BAHA Homes (`interview/`)

- [x] Phân tích JD và Khảo sát thông tin chính thống về BAHA Homes & BAHA Group <!-- id: 13.1 -->
- [x] Bóc tách nhu cầu tuyển dụng thực chất & triết lý: "Process → Data → Integration → Automation → AI" <!-- id: 13.2 -->
- [x] Liên kết mạng lưới tri thức AI/ML/DL từ `wiki/` (Agentic AI, ReAct, Prompt, RAG, Tool Use) <!-- id: 13.3 -->
- [x] Tích hợp tiêu chuẩn Kỹ nghệ Phần mềm (FastAPI, Clean Code, SOLID, REST API, Docker, n8n) <!-- id: 13.4 -->
- [x] Nghiên cứu chuyên sâu bộ công cụ Antigravity (Desktop/CLI/IDE) và Google AI (AI Studio, Flow) <!-- id: 13.5 -->
- [x] Xây dựng Single-File HTML `interview/index.html` chuẩn `lecture-visualizer` <!-- id: 13.6 -->
  - [x] Bố cục Full-Width, Soft Clean Cards, Sticky Sidebar ScrollSpy, Progress Bar, KaTeX <!-- id: 13.6.1 -->
  - [x] Canvas 3D Three.js mô phỏng căn hộ Vinhomes Grand Park tương tác 360 độ <!-- id: 13.6.2 -->
  - [x] Bộ mô phỏng ReAct chu trình Antigravity step-by-step <!-- id: 13.6.3 -->
  - [x] Nâng cấp Bảng trắc nghiệm 25 tiêu chí tự đánh giá độ sẵn sàng (Readiness Scorecard) <!-- id: 13.6.4 -->
  - [x] Tuyển tập 30 kịch bản phỏng vấn thực tế & câu trả lời chuẩn Senior/Staff (20 câu GenAI + 5 câu Software Engineering + 5 câu Database & SQL) <!-- id: 13.6.5 -->
  - [x] Tích hợp đầy đủ các Module nền tảng AI: Transformer (Self-Attention, RoPE, KV Cache, PagedAttention), LLMs (Pretrain/SFT/RLHF, LoRA, QLoRA, System 2 Reasoning o1/R1), Prompt Engineering (RICE, Injection defense), RAG (HNSW, Hybrid Search, Rerank, Ragas), Agent Harness (9 thành phần cốt lõi, Self-Healing) <!-- id: 13.6.6 -->
  - [x] Mở rộng Module 08 toàn diện Kỹ nghệ Phần mềm (10 chuyên đề): Python Async/GIL/OOP, Design Patterns, Clean Code, Clean Architecture, SOLID, React & Next.js App Router, TypeScript, TailwindCSS, FastAPI, REST vs GraphQL, Realtime (SSE vs WebSocket vs Polling), JWT/OAuth2/RBAC, System Design & Microservices (Saga, Outbox, CAP), Nginx Reverse Proxy & Cloudflare CDN, Git/Docker/K8s/Cloud, và Bộ ba vận hành AI (MLOps, LLMOps, AIOps) <!-- id: 13.6.7 -->
  - [x] Xây dựng Module 09 Cẩm Nang Cơ Sở Dữ Liệu Sư Phạm Từ Đầu: DB vs DBMS, DDL/DML/DQL & Thứ tự thực thi SQL Engine, Toàn tập phép JOIN (Inner/Left/Right/Full/Cross/Self), Subquery/CTE/Window Functions, Chuẩn hóa 1NF-3NF vs Phi chuẩn hóa, Giao dịch ACID & 4 Cấp độ cô lập (MVCC), B+Tree Index & EXPLAIN ANALYZE, Toàn cảnh NoSQL (Mongo, Redis, Cassandra, Neo4j) & BASE, CSDL Vector & pgvector cho AI Engineer, Bảng quyết định chọn DB <!-- id: 13.6.8 -->
- [x] Kiểm thử cú pháp HTML, kiểm thử cú pháp JavaScript bằng Node.js đạt 0 lỗi, 100% 49 anchor links & tag balance hợp lệ (240KB HTML) <!-- id: 13.7 -->
- [x] Tái cấu trúc Design System 3 Tầng & Thiết lập Chế độ Dark Mode Chuẩn Mực (`interview/`) <!-- id: 13.8 -->
  - [x] Phân tích hiện trạng design system, loại bỏ 100% hardcoded hex trong inline styles <!-- id: 13.8.1 -->
  - [x] Thiết lập bảng màu Dark Mode chuẩn Surface Elevation (0dp - 4dp) & WCAG AA Contrast <!-- id: 13.8.2 -->
  - [x] Bảo tồn trọn vẹn 4 nhóm tín hiệu sư phạm (Callout Intuition 🌱, Def 📘, Tip 💡, Warn ⚠️) <!-- id: 13.8.3 -->
  - [x] Tích hợp Theme Controller Engine: Lưu localStorage, lắng nghe prefers-color-scheme, toggle smooth transition 250ms <!-- id: 13.8.4 -->
  - [x] Cập nhật tài liệu quy hoạch `docs/plan/01_design_system_spec.md`, `docs/plan/00_master_plan.md` & tạo chuyên đề `docs/plan/06_dark_mode_design_system.md` <!-- id: 13.8.5 -->
- [x] Bổ sung cẩm nang sử dụng chi tiết Google Antigravity Desktop (App 2.0) từ tài liệu chính thức `https://antigravity.google/docs/getting-started/` (Hệ thống Slash Commands `/plan`, `/goal`, `/schedule`, `/grill-me`, cơ chế cô lập Git Worktree Mode, bảng phím tắt điều hướng, phân quyền bảo tầng và kịch bản thực chiến BAHA Homes) <!-- id: 13.9 -->
- [x] Tích hợp cẩm nang chuyên sâu Antigravity Python SDK (`google-antigravity`) & Ma trận hiệp đồng 4 bề mặt từ `https://antigravity.google/docs/sdk/overview/` (Async context manager, streaming đa kênh, custom tools & subagents, declarative policies, session persistence và ví dụ microservice FastAPI) <!-- id: 13.10 -->

---

## Phần 4: Nâng Cấp Toàn Diện Kiến Thức Machine Learning & Deep Learning Computer Vision (`interview/`)

- [x] Module 02: Tích hợp trọn bộ Thuật toán Machine Learning Cổ điển & Tối ưu hóa <!-- id: 14.1 -->
  - [x] Linear Regression, Logistic Regression, Perceptron, SVM, Decision Tree, Random Forest, XGBoost, PCA <!-- id: 14.1.1 -->
  - [x] Bias - Underfitting - Variance - Overfitting Tradeoff & Learning Curves <!-- id: 14.1.2 -->
  - [x] Thuật toán tối ưu hóa (Optimizers): SGD, Momentum, NAG, AdaGrad, RMSprop, Adam, AdamW <!-- id: 14.1.3 -->
  - [x] Mạng nơ-ron đa tầng MLP: Fully Connected / Dense Layer, Forward Prop, Loss Functions, Backprop, Chain Rule & Parameter Update ($\mathbf{W} \leftarrow \mathbf{W} - \eta \nabla_{\mathbf{W}}\mathcal{L}$) kèm vết dò số học Toy Network 2 tầng <!-- id: 14.1.4 -->
- [x] Module 03: Tích hợp trọn bộ Kiến trúc Deep Learning Thị Giác Máy Tính (Computer Vision) chuẩn `lecture-visualizer` <!-- id: 14.2 -->
  - [x] 3.3 Mạng Tích Chập (CNNs): Kernels, Filter size, Stride, Padding (Valid vs Same), Channels ($C_{in}, C_{out}$), Convolution on Volume, Output size formula, Local Connectivity & Parameter Sharing, Vết dò số học $4 \times 4$ với kernel $3 \times 3$ <!-- id: 14.2.1 -->
  - [x] 3.4 Pooling Layer & Receptive Field vs ERF: Max Pooling, Avg Pooling, Global Avg Pooling (GAP), công thức Receptive Field lý thuyết, bản chất phân phối chuẩn Gauss 2D của Effective Receptive Field (ERF) <!-- id: 14.2.2 -->
  - [x] 3.5 Internal Covariate Shift & Batch Normalization: Tại sao Normalization làm mịn Loss Landscape, BN Training phase vs BN Inference phase, kỹ thuật gập trọng số (Folding BN into Conv) cho deploy biên; Bảng đối chiếu Bộ Tứ Chuẩn Hóa qua tensor $(N, C, H, W)$ giữa BN, LN, IN, GN <!-- id: 14.2.3 -->
  - [x] 3.6 Inverted Dropout & Triệt Tiêu Gradient: Chuẩn công nghiệp Inverted Dropout (chia bù $1-p$ trong training, zero overhead khi inference); Phân tích tích chuỗi đạo hàm Triệt tiêu / Bùng nổ Gradient và 4 giải pháp phòng thủ (ReLU, He Init, Normalization, Gradient Clipping) <!-- id: 14.2.4 -->
  - [x] 3.7 Kiến Trúc Đột Phá ResNet & U-Net: Suy thoái (Degradation), Residual Block $F(x)+x$, chứng minh toán học đạo hàm số hạng $+1$ mở đường cao tốc gradient không bao giờ tắt; Kiến trúc chữ U U-Net (Encoder-Decoder), khác biệt mấu chốt giữa Skip-Connection của ResNet (phép cộng) và U-Net (ghép nối kênh Concat), hàm mất mát kết hợp Combo Loss (BCE + Dice) <!-- id: 14.2.5 -->
  - [x] 3.8 Transfer Learning, Fine-Tuning & Data Augmentation: 3 cấp độ (Feature Extraction, Partial Fine-Tuning, Full Fine-Tuning + Warmup LR); Tăng cường hình học, quang học, và kỹ thuật nâng cao SOTA (Cutout, Mixup, CutMix, Mosaic YOLO) <!-- id: 14.2.6 -->
  - [x] 3.9 MobileNet Edge & Vision Transformers: Depthwise Separable Conv ($DW + PW$) giảm ~9 lần FLOPs; ViT Patch extraction $16 \times 16$ vs Swin Transformer Shifted Windows ($O(M^2 N)$); Bảng so sánh 1-1 CNNs vs ViT vs Swin Transformer <!-- id: 14.2.7 -->
- [x] Hoàn thiện kế hoạch & báo cáo tổng kết trong `docs/ai/deep_learning_cv_plan.md` và `docs/ai/deep_learning_cv_walkthrough.md` <!-- id: 14.3 -->
- [x] Đóng gói toàn bộ các Sơ Đồ Kiến Trúc theo tiêu chuẩn `diagram-design` (Container Frames, Eyebrow Tags on Mask, Orthogonal Connectors, No Markdown/ASCII): ResNet Residual Block, U-Net, MobileNet Separable Conv, ViT vs Swin, Đại Pipeline 1 (Traffic), Đại Pipeline 2 (Smart Port), Đại Pipeline 3 (Face Access), C2AE Multi-label, Agent Harness 9 Thành phần, và Clean Architecture Củ hành <!-- id: 14.4 -->

---

## Phần 5: Rà Soát & Chuẩn Hóa Hệ Thống Màu Sắc Light / Dark Mode (`interview/`)

- [x] Rà soát và giải quyết triệt để lỗi xung đột màu ("trùng màu", chữ chìm vào nền) <!-- id: 15.1 -->
  - [x] Bổ sung biến màu ngữ nghĩa cốt lõi `--bg-primary`, `--bg-surface`, `--bg-main`, `--border`, `--data-rose` vào `:root` và `html.dark, body.dark` <!-- id: 15.1.1 -->
  - [x] Thiết lập hệ thống `--tint-*-bg`, `--tint-*-border`, `--tint-*-text` đa tầng (Blue, Emerald, Purple, Amber, Red, Neutral) thích ứng liền mạch cả Light Mode (màu pastel nhã nhặn) và Dark Mode (độ mờ trong suốt alpha 0.16) <!-- id: 15.1.2 -->
  - [x] Khử sạch 100% (72/72) mã màu hex pastel cứng (`#eff6ff`, `#ecfdf5`, `#fdf4ff`, `#fffbeb`, `#fef2f2`, `#f8fafc`) trong tất cả SVG diagrams và thay thế bằng các biến CSS semantic <!-- id: 15.1.3 -->
  - [x] Khử sạch các mã màu chữ tối tương phản kém trên nền tối (`#047857`, `#b45309`, `#dc2626`, `#d97706`) và mã màu trắng trên nền sáng (`#fff` trên nền pastel) <!-- id: 15.1.4 -->
  - [x] Cập nhật bộ mô phỏng JavaScript `updateBVSim(p)` sang sử dụng token màu theme-aware <!-- id: 15.1.5 -->
  - [x] Đảm bảo đạt chuẩn tương phản WCAG AA, giữ phong cách thanh lịch, tối giản, không gây chói mắt <!-- id: 15.1.6 -->

---

## Phần 6: Nghiên Cứu Chuyên Sâu Doanh Nghiệp ATIN & Chuẩn Bị Gặp Gỡ Lead Tech (`interview/`)

- [x] Khai thác & Thu thập dữ liệu toàn diện về ATIN (`https://atin.com.vn/vi/`) <!-- id: 16.1 -->
  - [x] Hồ sơ pháp nhân, lãnh đạo (CEO Lê Anh Tuấn), ngày thành lập (19/06/2019), trụ sở Phùng Khoang, hotline, email <!-- id: 16.1.1 -->
  - [x] 11 Ngành dọc kinh doanh & Danh mục 30+ module Video Analytics AI <!-- id: 16.1.2 -->
  - [x] Danh sách 70+ dự án thực tế tiêu biểu: BSR Lọc hóa dầu Bình Sơn, Công an Yên Bái, Lào Cai, Cố đô Huế, Sunworld, Chùa Tam Chúc, Dewey Schools <!-- id: 16.1.3 -->
  - [x] Đối tác chiến lược Network Optix (Nx Witness VMS) - Tích hợp Nx Meta Plugin, ứng dụng di động Heza & Agent AI <!-- id: 16.1.4 -->
- [x] Xuất báo cáo nghiên cứu tình báo doanh nghiệp & chiến lược vào `docs/ai/atin_company_intelligence_and_techlead_strategy.md` <!-- id: 16.2 -->
- [x] Cập nhật giao diện cẩm nang `interview/index.html` <!-- id: 16.3 -->
  - [x] Cập nhật Sidebar Navigation (mục 1.1 và 1.5) <!-- id: 16.3.1 -->
  - [x] Tối ưu hóa Section 1.1: Bổ sung hồ sơ xác thực và Bản đồ 70+ Dự án thực địa tiêu biểu <!-- id: 16.3.2 -->
  - [x] Bổ sung Section 1.5: Chiến lược gặp gỡ Tech Lead ATIN, Khung tâm thế trao đổi, Tinh thần học hỏi & 5 Ý tưởng đột phá bám sát bài toán kinh doanh <!-- id: 16.3.3 -->
  - [x] Bộ 4 câu hỏi chiến lược đặt ngược lại cho Tech Lead để khẳng định đẳng cấp senior <!-- id: 16.3.4 -->
