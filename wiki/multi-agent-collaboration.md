# Hợp Tác Đa Tác Nhân (Multi-Agent Collaboration)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 14.5; *Master All 20 Agentic AI Design Patterns*, Pattern 7; Wu et al. (2023) *"AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"*; Hong et al. (2023) *"MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"*.
> **Miền kiến thức**: [[index|Distributed Agentic Systems & Swarm Intelligence]]
> **Tài liệu gốc liên quan**:
> - [Master All 20 Agentic AI Design Patterns.pdf](../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 18-22)
> - [Agentic AI Design Patterns(2026 Edition).pdf](../resources/genai/Agentic%20AI%20Design%20Patterns%282026%20Edition%29.pdf) (Trang 16-20)
> - [A Vision for Auto Research with LLM Agents.pdf](../resources/genai/A%20Vision%20for%20Auto%20Research%20with%20LLM%20Agents.pdf) (Trang 10-18)

---

## 1. Tóm tắt (Executive Summary)
**Hợp tác Đa tác nhân (Multi-Agent Collaboration)** là mô thức kiến trúc phân tán trong đó một bài toán quy mô lớn được giải quyết thông qua sự tương tác, phối hợp và giao tiếp của nhiều tác nhân AI chuyên môn hóa độc lập. Thay vì bắt một Agent duy nhất (Single monolithic agent) phải gánh vác mọi vai trò và nhồi nhét hàng tá công cụ vào context window gây nhiễu loạn chú ý, Multi-Agent áp dụng nguyên lý công nghệ phần mềm: **Phân chia trách nhiệm (Separation of Concerns)**. Mỗi Agent hoạt động như một chuyên viên trong một tổ chức (ví dụ: Product Owner, Software Architect, Coder, Code Reviewer) tương tác với nhau qua các quy trình chuẩn (SOPs).

---

## 2. Định nghĩa chính thống & Các hình thái Tổ chức (Collaboration Topologies)

```mermaid
flowchart TD
    subgraph 1. Supervisor-Worker Hierarchy
        Super["Supervisor / Router Agent"] --> W1["Researcher Agent"]
        Super --> W2["Coder Agent"]
        Super --> W3["Tester Agent"]
    end
    
    subgraph 2. Peer-to-Peer Debate
        AgentA["Bull Analyst (Positive)"] <-->|"Debate / Critique"| AgentB["Bear Analyst (Negative)"]
        AgentA --> Judge["Consensus Judge"]
        AgentB --> Judge
    end
    
    subgraph 3. Assembly Line (Sequential SOP)
        P1["Product Analyst (PRD)"] --> P2["System Architect (Design)"]
        P2 --> P3["Engineer (Code)"]
        P3 --> P4["QA (Unit Test)"]
    end
```

### 2.1 4 Hình thái tổ chức Multi-Agent chủ đạo
1. **Supervisor-Worker (Cấu trúc Thứ bậc)**:
   - Một Agent trung tâm (Supervisor/Orchestrator) nhận nhiệm vụ từ người dùng, phân tích và giao việc cho các Worker Agents chuyên trách. Kết quả của các Worker được Supervisor tổng hợp, kiểm tra và gửi lại cho người dùng.
2. **Sequential Assembly Line (Dây chuyền sản xuất SOP)**:
   - Áp dụng trong MetaGPT: Mỗi Agent nhận đầu ra của Agent phía trước làm đầu vào, tuân thủ nghiêm ngặt Quy trình Vận hành Tiêu chuẩn (Standard Operating Procedures). Đầu ra là các tài liệu kỹ thuật có cấu trúc (PRD $\rightarrow$ Architecture Document $\rightarrow$ Code $\rightarrow$ Test).
3. **Debate & Consensus (Tranh luận và Đồng thuận)**:
   - Hai hoặc nhiều Agent được cấp các quan điểm/định kiến trái ngược nhau (ví dụ: một bên tìm kiếm luận điểm ủng hộ, một bên tìm rủi ro phản đối). Cuộc tranh luận giúp loại bỏ các "ảo giác tự tin" của LLM và nâng cao chất lượng quyết định cuối cùng.
4. **Swarm / Decentralized Collaboration**:
   - Các Agent tự do trao đổi thông điệp không qua trung gian tập trung, thực hiện chuyển giao tác vụ (handoff) linh hoạt dựa trên sự kiện kích hoạt (Event-driven architecture).

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Mô hình | Chi phí Token & Độ trễ | Khả năng giải quyết bài toán phức tạp | Điểm nghẽn rủi ro chính |
| :--- | :--- | :--- | :--- | :--- |
| **Single Monolithic Agent** | Thấp nhất; chạy trong 1 luồng prompt. | Kém khi tác vụ vượt quá 5-10 bước hoặc đòi hỏi nhiều góc nhìn đối lập. | Context window bị quá tải (Context clutter); dễ quên chỉ thị ban đầu. |
| **Hierarchical Multi-Agent** | Trung bình đến cao. | Rất tốt; kiểm soát luồng chặt chẽ qua Supervisor. | Supervisor trở thành điểm nghẽn cổ chai (Single Point of Failure). |
| **Decentralized Swarm / Chat Group** | Rất cao; chi phí token tăng theo cấp số nhân. | Giải quyết các bài toán sáng tạo, khám phá tri thức. | Dễ rơi vào hiện tượng "nói chuyện phiếm" (chatter loops), các Agent tự khen ngợi nhau mà không tạo ra giá trị cụ thể. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Khi nào NÊN và KHÔNG NÊN dùng Multi-Agent?
- **KHÔNG NÊN DÙNG (Cạm bẫy over-engineering)**:
  - Nếu bài toán có thể giải quyết được bằng một luồng **Prompt Chaining** tuyến tính hoặc 1 Agent với 3-5 tools đơn giản. Việc đưa Multi-Agent vào sẽ làm tăng chi phí token lên gấp 5-10 lần và độ trễ tăng từ vài giây lên vài phút một cách vô ích.
- **NÊN DÙNG KHI**:
  - Tác vụ đòi hỏi **các góc nhìn phê bình đối lập thực sự** (e.g., Đội đỏ Red-Teaming tấn công bảo mật vs Đội xanh Blue-Teaming phòng thủ).
  - Tác vụ đòi hỏi **bối cảnh công cụ quá lớn**: Chia tách Agent tra cứu cơ sở dữ liệu nội bộ riêng và Agent tương tác web bên ngoài để tránh rủi ro bảo mật rò rỉ dữ liệu.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Làm thế nào để đo lường và cắt giảm lãng phí chi phí token trong một hệ thống Multi-Agent phức tạp?*
  - **A**: Áp dụng 3 nguyên tắc tối ưu hóa:
    1. **Context Isolation**: Không chia sẻ toàn bộ lịch sử trò chuyện của Agent A cho Agent B. Chỉ truyền các bản tóm tắt có cấu trúc (Structured Hand-off Data: ví dụ JSON kết quả) qua lại giữa các Agent.
    2. **Model Tiering (Phân tầng mô hình)**: Sử dụng các mô hình nhỏ, rẻ (như GPT-4o-mini, Claude 3.5 Haiku) cho các Worker thực thi tác vụ đơn giản; chỉ gọi Frontier Model (Claude 3.5 Sonnet, GPT-4o) cho vai trò Supervisor và Reviewer.
    3. **Hard Stop Timeout**: Cài đặt giới hạn số lượng tin nhắn trao đổi tối đa giữa các Agent (ví dụ tối đa 6 lượt trao đổi) trước khi buộc phải chốt kết quả.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & `wiki-links`)
- [[agentic-ai-core]] — Khung kiến trúc nền tảng của từng tác nhân thành phần.
- [[planning-and-decomposition]] — Cơ chế phân bổ công việc từ Supervisor xuống Worker.
- [[reflection-and-self-correction]] — Mô hình Actor-Critic là dạng tối giản của 2-Agent collaboration.
- [[agent-memory-systems]] — Quản lý bộ nhớ chia sẻ và bộ nhớ riêng tư cho từng tác nhân.