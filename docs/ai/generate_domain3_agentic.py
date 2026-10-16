# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = Path("wiki")
WIKI_DIR.mkdir(parents=True, exist_ok=True)

ENTITIES = {
    "agentic-ai-core.md": r"""# Kiến Trúc Cốt Lõi Của Agentic AI (Agentic AI Core Architecture)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Chapter 14 (Section 14.1); *Master All 20 Agentic AI Design Patterns* (2025), Section 1; *Agentic AI Design Patterns (2026 Edition)*; *giao_trinh_agentic.pdf*.
> **Miền kiến thức**: [[agentic-overview|Agentic AI & Cognitive Autonomous Systems]]
> **Tài liệu gốc liên quan**:
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 1-6)
> - [Agentic AI Design Patterns(2026 Edition).pdf](../../resources/genai/Agentic%20AI%20Design%20Patterns%282026%20Edition%29.pdf) (Trang 1-6)
> - [giao_trinh_agentic.pdf](../../resources/genai/giao_trinh_agentic.pdf) (Trang 1-8)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 129-131)
> - [846485886_122320901828195094_432191169857527385_n.jpg](../../resources/images/846485886_122320901828195094_432191169857527385_n.jpg) (Sơ đồ Human-in-the-Loop)

---

## 1. Tóm tắt (Executive Summary)
**Tác nhân Trí tuệ Nhân tạo (Agentic AI)** đại diện cho bước chuyển dịch mô thức kiến trúc từ các mô hình ngôn ngữ phản xạ thụ động (Reactive Generative AI: Prompt $\rightarrow$ Response) sang các hệ thống tự chủ chủ động (Proactive Autonomous Systems). Một Agentic AI hoàn chỉnh là một hệ thống khép kín gồm 4 trụ cột: **Bộ não Suy luận (LLM Reasoning Core)**, **Bộ nhớ Đa tầng (Memory Systems)**, **Công cụ & Giao tiếp Ngoại vi (Tools & Actuators)**, và **Cơ chế Lập kế hoạch & Tự phản biện (Planning & Reflection)** vận hành liên tục qua chu trình lặp: `Perceive -> Plan -> Act -> Observe -> Reflect` để đạt mục tiêu phức tạp mà con người giao phó.

---

## 2. Định nghĩa chính thống & Mô hình Tư duy Kiến trúc sư (Mental Model 2026)

### 2.1 Mental Model chuẩn mực của Senior Architect
Theo *Agentic AI Design Patterns (2026 Edition)*:
> - **LLMs are CPUs** (Bộ vi xử lý tính toán logic thô).
> - **Prompts are Instructions / Memory Registers** (Mã lệnh và thanh ghi tạm thời).
> - **Agents are Processes** (Tiến trình thực thi nhiệm vụ độc lập có trạng thái).
> - **Agentic Frameworks are Operating Systems** (Hệ điều hành quản lý cấp phát tài nguyên, bộ nhớ, IPC và lập lịch).

```mermaid
flowchart TD
    UserGoal["User Goal / Complex Task"] --> IntentRouter["Intent Router & State Initializer"]
    IntentRouter --> AgentCore["Agent Orchestrator (Process Loop)"]
    
    subgraph Agent Loop Architecture
        AgentCore --> Planner["[[planning-and-decomposition|Planner (Decompose)]]"]
        Planner --> Reasoner["[[llm-reasoning|Reasoning Engine (CoT)]]"]
        Reasoner --> ToolCaller["[[tool-use-and-function-calling|Tool Executor (Act)]]"]
        ToolCaller --> Env[("Environment / External APIs / DB")]
        Env --> Observe["Observation Feedback"]
        Observe --> Reflector["[[reflection-and-self-correction|Reflector (Critique & Verify)]]"]
        Reflector -->|"Needs Correction"| Planner
        Reflector --> State["[[agent-memory-systems|State / Memory Store]]"]
        State --> AgentCore
    end
    
    Reflector -->|"Task Accomplished"| HITL["[[human-in-the-loop|Human Validation Gate]]"]
    HITL --> VerifiedOut["Verified Production Output"]
```

### 2.2 So sánh cốt lõi: Chatbot truyền thống vs Agentic AI
Theo giáo trình *giao_trinh_agentic.pdf*:
1. **Chatbot (Passive LLM)**:
   - Không có trạng thái phiên bền vững; vòng đời kết thúc ngay khi sinh xong chuỗi token.
   - Hoàn toàn mù quáng đối với môi trường thực tế (không thể gọi API, không thể đọc file hệ thống, không thể tương tác web).
   - Không có vòng lặp tự sửa lỗi: nếu sinh sai câu lệnh SQL, nó sẽ trả thẳng lỗi cho người dùng.
2. **AI Agent (Autonomous Process)**:
   - Quản lý trạng thái (State Machine): Theo dõi rõ mình đang ở bước nào trong quy trình.
   - Tự chủ thực thi hành động qua Tool Calling.
   - Tự động bắt lỗi ngoại lệ (Exception Handling): Nếu câu lệnh SQL sinh ra bị lỗi cú pháp từ database trả về, Agent tự đọc log lỗi, tự sửa lại câu query và thử lại mà không làm phiền người dùng.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Khía cạnh | Tài liệu giáo trình sơ cấp | Báo cáo kiến trúc công nghiệp 2026 | Phân tích sâu của AI Engineer |
| :--- | :--- | :--- | :--- |
| **Mức độ tự chủ (Autonomy)** | Khuyến khích xây dựng "Fully Autonomous Agents" (như AutoGPT thời kỳ đầu) để máy tự làm từ A đến Z. | Khẳng định AutoGPT tự do không giới hạn là **thất bại kiến trúc lớn nhất 2023-2024**: Gây vòng lặp vô tận (infinite loops), bùng nổ chi phí token và rủi ro phá hủy hệ thống. | **Bắt buộc phải áp dụng Bound Autonomy**: Giới hạn tối đa số lượt lặp (Max Turns), đặt giới hạn ngân sách (Budget Cap) và bắt buộc có chốt phê duyệt con người ([[human-in-the-loop|Human-in-the-Loop]]). |
| **Độ tin cậy trong sản xuất** | Cho rằng Agent giải quyết được mọi tác vụ nếu prompt đủ dài và chi tiết. | Thống kê 90% lỗi của Agent trong sản xuất không phải do LLM kém thông minh, mà do: thiếu kiểm soát trạng thái, không có timeout, thiếu cơ chế retry và không có observability. | Kỹ sư giỏi tập trung 80% thời gian vào phần mềm truyền thống (State Management, Error Recovery, Retries, Logging) bọc xung quanh LLM. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy tắc vàng triển khai Agentic AI trong Doanh nghiệp
1. **Nguyên tắc "LLM as a Judge / Validator"**: Tách rời vai trò giữa Agent thực thi (Worker) và Agent kiểm thử (Auditor/Evaluator). Không bao giờ để một Agent vừa làm vừa tự chấm bài mà không có tiêu chuẩn độc lập.
2. **Idempotency (Tính bất biến của Tool)**: Đảm bảo các công cụ Agent gọi có tính lũy suy; nếu Agent gọi lại công cụ 2 lần do mạng chập chờn, hành động đó không gây trừ tiền hai lần trong tài khoản ngân hàng.
3. **Structured Outputs**: Bắt buộc Agent trả về dữ liệu tuân thủ nghiêm ngặt JSON Schema bằng Pydantic hoặc Zod, loại bỏ hoàn toàn việc parse text tự do bằng regex thô sơ.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao hầu hết các Agent mã nguồn mở chạy thử nghiệm trên Jupyter Notebook thì rất ấn tượng nhưng đưa vào môi trường Production thực tế đều bị sập hoặc mất kiểm soát?*
  - **A**: Vì trong môi trường thực tế, Agent phải đối mặt với các vấn đề phân tán: API bên thứ ba bị timeout hoặc đổi schema, dữ liệu người dùng chứa prompt injection tiềm ẩn, token context bị tràn sau nhiều lượt hội thoại, và việc không có một Finite State Machine (FSM) quản lý phân luồng trạng thái khiến Agent rơi vào các vòng lặp tư duy lặp đi lặp lại vô nghĩa (hallucination loops).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[react-pattern]] — Mô thức vòng lặp suy luận và hành động kinh điển.
- [[planning-and-decomposition]] — Năng lực phân rã mục tiêu lớn thành các bước khả thi.
- [[tool-use-and-function-calling]] — Cầu nối giúp Agent tương tác với thế giới thực.
- [[reflection-and-self-correction]] — Cơ chế tự đánh giá và sửa sai sau mỗi hành động.
- [[multi-agent-collaboration]] — Kết nối nhiều Agent đơn lẻ thành hệ thống phối hợp chuyên môn hóa.
- [[agent-memory-systems]] — Cơ sở hạ tầng lưu trữ ngữ cảnh ngắn hạn và dài hạn cho Agent.
- [[human-in-the-loop]] — Trụ cột quản trị rủi ro, phân định trách nhiệm pháp lý và an toàn cho Agent.
""",

    "react-pattern.md": r"""# Mô Thức ReAct (ReAct: Synergizing Reasoning and Acting)

> **Khái niệm chính thống**: Yao et al. (ICLR 2023) *"ReAct: Synergizing Reasoning and Acting in Language Models"*; *Master All 20 Agentic AI Design Patterns*, Pattern 16.
> **Miền kiến thức**: [[agentic-overview|Agent Reasoning & Execution Patterns]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_[Description]-AI-Agent-LLM-Tool-Calling.pdf](../../resources/genai/AIO2025_%5BDescription%5D-AI-Agent-LLM-Tool-Calling.pdf) (Trang 15-30)
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 6-10)
> - [giao_trinh_agentic.pdf](../../resources/genai/giao_trinh_agentic.pdf) (Trang 8-14)

---

## 1. Tóm tắt (Executive Summary)
**Mô thức ReAct (Reasoning + Acting)** là mô thức kiến trúc nền tảng cho phép LLM phối hợp chặt chẽ giữa **Suy luận (Reasoning)** và **Hành động (Acting)** trong một vòng lặp liên tục. Thay vì chỉ suy luận đơn thuần (như Chain-of-Thought) dẫn đến ảo giác vì thiếu dữ liệu ngoài, hoặc chỉ hành động mù quáng (như Act-only tool calling) không có định hướng logic, ReAct đan xen các bước: sinh lập luận tư duy (**Thought**), quyết định gọi công cụ ngoại vi (**Action**), và đọc kết quả phản hồi từ môi trường (**Observation**). Chu trình này tiếp diễn cho đến khi bài toán được giải quyết trọn vẹn.

---

## 2. Định nghĩa chính thống & Vòng lặp Thuật toán (Algorithmic Loop)

### 2.1 Cấu trúc Không gian Trạng thái ReAct
Tại mỗi bước thời gian $t \in \{1, ..., T\}$:
1. **Thought Step ($c_t$)**: LLM tự độc thoại nội tâm (Internal Monologue) để phân tích tình hình hiện tại:
   $$c_t \sim P_\theta(\cdot \mid x, a_1, o_1, ..., a_{t-1}, o_{t-1})$$
2. **Action Step ($a_t$)**: Dựa trên suy luận $c_t$, mô hình quyết định gọi một công cụ từ tập action space $\mathcal{A}$ với tham số cụ thể:
   $$a_t \sim P_\theta(\cdot \mid x, a_1, o_1, ..., c_t)$$
3. **Observation Step ($o_t$)**: Môi trường thực thi $a_t$ (gọi API, truy vấn DB, search web) và trả về kết quả quan sát:
   $$o_t = \text{Environment}(a_t)$$

```mermaid
sequenceDiagram
    autonumber
    actor User as User Request
    participant Agent as ReAct LLM Brain
    participant Env as Tool / External Environment
    
    User->>Agent: "Doanh thu năm 2024 của công ty X tăng bao nhiêu % so với 2023?"
    Note over Agent: Thought 1: Cần tìm doanh thu năm 2023 của công ty X trước.
    Agent->>Env: Action 1: search_financial_data(company='X', year=2023)
    Env-->>Agent: Observation 1: Doanh thu 2023 là 100 triệu USD.
    Note over Agent: Thought 2: Đã có 2023. Giờ cần tìm doanh thu năm 2024.
    Agent->>Env: Action 2: search_financial_data(company='X', year=2024)
    Env-->>Agent: Observation 2: Doanh thu 2024 là 150 triệu USD.
    Note over Agent: Thought 3: Có cả 2 số liệu. Tính %: (150-100)/100 = 50%.
    Agent->>User: Final Answer: Doanh thu năm 2024 tăng 50% so với 2023.
```

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Phương pháp | Luồng tư duy | Khả năng tự sửa lỗi | Tỷ lệ Ảo giác |
| :--- | :--- | :--- | :--- |
| **Standard Prompting** | Không có bước trung gian. | 0% | Cực cao trên bài toán đa bước. |
| **Chain-of-Thought (CoT)** | Chuỗi suy luận liên tục kín (Internal only). | Thấp; nếu suy luận sai 1 bước ở giữa sẽ tiếp tục ảo giác cho đến cuối. | Trung bình; phụ thuộc hoàn toàn vào kiến thức tĩnh có trong trọng số. |
| **Act-Only (Tool Calling thuần)** | Gọi công cụ liên tục không có bước phân tích logic. | Kém; hành động theo kiểu thử sai mù quáng (brute-force). | Thấp về dữ liệu, nhưng lãng phí tài nguyên gọi API vô ích. |
| **ReAct (Synergy)** | Đan xen Thought $\rightarrow$ Action $\rightarrow$ Observation. | Xuất sắc; tự đọc kết quả Observation để điều chỉnh Thought của bước tiếp theo. | **Thấp nhất**; triệt tiêu ảo giác nhờ neo chặt vào dữ liệu môi trường thực tế. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Bẫy Vòng Lặp Vô Tận (Infinite Loop Traps) & Biện pháp khắc phục
Một vấn đề nan giải khi chạy ReAct trong production:
- *Tình huống*: Tool trả về kết quả rỗng hoặc báo lỗi `"Resource not found"`. Agent tiếp tục suy nghĩ và gọi lại chính xác tool đó với cùng tham số, lặp lại 20 lần cho đến khi cháy sạch quota token.
- **Giải pháp kỹ thuật**:
  1. **Strict Max Iterations**: Giới hạn cứng vòng lặp tối đa (thường đặt `max_turns = 5 - 10`).
  2. **Loop Detection Middleware**: Lưu hash của cặp `(Action, Action_Input)`. Nếu phát hiện action lặp lại 2 lần liên tiếp, tự động chèn cảnh báo hệ thống vào context: `"[SYSTEM]: Công cụ này đã thất bại với tham số trên. Bạn bắt buộc phải thử hướng giải quyết khác hoặc thừa nhận không thể tìm thấy"`.
  3. **Context Truncation**: Cắt ngắn các Observation quá dài (ví dụ HTML của trang web) để tránh tràn bộ nhớ đệm ngữ cảnh.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao bước "Thought" trong ReAct lại làm giảm đáng kể số lần gọi Tool thừa thãi so với mô hình Act-Only?*
  - **A**: Bước "Thought" hoạt động như một bộ đệm lập kế hoạch vi mô (Micro-Planner). Khi mô hình bắt buộc phải viết ra suy nghĩ logic trước khi sinh cú pháp gọi hàm, nó có cơ hội phân tích câu hỏi người dùng thành các điều kiện tiên quyết, từ đó chọn đúng công cụ có độ ưu tiên cao nhất thay vì gọi hú họa hàng loạt công cụ như phương pháp Act-Only.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[agentic-ai-core]] — Khung kiến trúc tổng thể nơi ReAct làm hạt nhân điều hành.
- [[tool-use-and-function-calling]] — Giao thức thực thi bước Action trong ReAct.
- [[reflection-and-self-correction]] — Nâng cấp ReAct với cơ chế tự phản biện sau khi hoàn tất chu trình.
- [[planning-and-decomposition]] — Phân cấp vĩ mô trước khi ReAct phân tích vi mô.
""",

    "reflection-and-self-correction.md": r"""# Phản Biện và Tự Sửa Lỗi (Reflection & Self-Correction)

> **Khái niệm chính thống**: *Master All 20 Agentic AI Design Patterns*, Pattern 4; Shinn et al. (NeurIPS 2023) *"Reflexion: Language Agents with Verbal Reinforcement Learning"*; Madaan et al. (2023) *"Self-Refine"*.
> **Miền kiến thức**: [[agentic-overview|Cognitive Self-Correction & Evaluator Patterns]]
> **Tài liệu gốc liên quan**:
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 10-14)
> - [Agentic AI Design Patterns(2026 Edition).pdf](../../resources/genai/Agentic%20AI%20Design%20Patterns%282026%20Edition%29.pdf) (Trang 12-16)
> - [A Vision for Auto Research with LLM Agents.pdf](../../resources/genai/A%20Vision%20for%20Auto%20Research%20with%20LLM%20Agents.pdf) (Trang 4-10)

---

## 1. Tóm tắt (Executive Summary)
**Phản biện và Tự sửa lỗi (Reflection & Self-Correction)** là mẫu thiết kế tác nhân cho phép mô hình tự đánh giá, phê bình và hoàn thiện các kết quả do chính nó tạo ra trước khi xuất xưởng ra môi trường người dùng cuối. Thay vì chỉ dựa vào một lượt sinh duy nhất (Single-pass generation), Agent phân vai thành hai thực thể: **Tác nhân Thực thi (Actor / Generator)** và **Tác nhân Phê bình (Critic / Evaluator)**. Bằng cách lưu trữ các bài học tự phê bình vào bộ nhớ ngắn hạn hoặc dài hạn (**Reflexion Memory**), Agent đạt được sự cải thiện chất lượng vượt trội tương tự như học tăng cường nhưng hoàn toàn bằng ngôn ngữ tự nhiên (Verbal Reinforcement Learning).

---

## 2. Định nghĩa chính thống & Kiến trúc Reflexion (Shinn et al., 2023)

### 2.1 Ba thành phần cốt lõi của Reflexion
1. **Actor**: Sinh ra quỹ đạo hành động ban đầu dựa trên trạng thái hiện tại.
2. **Evaluator**: Đánh giá chất lượng của quỹ đạo (sử dụng unit test, compiler output, hoặc heuristic rubric của LLM).
3. **Self-Reflection Model**: Đọc log thất bại từ Evaluator và sinh ra bản đúc kết kinh nghiệm bằng lời: *"Tôi đã phạm sai lầm ở biến X vì quên ép kiểu dữ liệu. Lần sau tôi cần kiểm tra kiểu dữ liệu trước khi thực hiện phép cộng"*. Bản đúc kết này được chèn trực tiếp vào prompt của lượt lặp tiếp theo.

```mermaid
flowchart TD
    Task["Complex Task / Coding Prompt"] --> Actor["Actor LLM (Draft Solution)"]
    Actor --> Code["Generated Code / Solution"]
    Code --> Evaluator{"Evaluator / Unit Tests / Rubric"}
    Evaluator -->|"All Tests Pass (Success)"| Deliver["Deliver Final Verified Product"]
    Evaluator -->|"Test Failed / Syntax Error"| Critic["Self-Reflection Engine"]
    Critic --> VerbalMemory[("Episodic Memory: Failure Analysis & Lessons")]
    VerbalMemory --> Actor
```

### 2.2 Thuật toán Self-Refine (Madaan et al., 2023)
Quy trình lặp 3 bước:
$$\text{Generate } y_0 \rightarrow \text{Feedback } f_0 \rightarrow \text{Refine } y_1 \rightarrow ... \rightarrow \text{Refine } y_k$$
Quá trình dừng lại khi:
- Điểm đánh giá của Evaluator vượt ngưỡng mục tiêu ($Score \ge \text{Threshold}$).
- Hoặc đạt số lần phản biện tối đa ($k \ge K_{\max}$).

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Mô hình Phản biện | Nguồn tín hiệu phản hồi (Feedback Signal) | Độ tin cậy thực tế | Rủi ro sụp đổ chất lượng |
| :--- | :--- | :--- | :--- |
| **Self-Correction nội tại (1 Model tự chấm bài của chính mình)** | Hoàn toàn dựa vào prompt tự vấn: *"Hãy kiểm tra xem bài viết của bạn có lỗi gì không"*. | **Rất thấp**. Các nghiên cứu của DeepMind (2023-2024) chỉ ra rằng nếu một mô hình không đủ thông minh để làm đúng từ đầu, nó cũng không đủ thông minh để tự phát hiện ra lỗi sai của chính nó (Confirmation Bias). | Mô hình có xu hướng sửa từ đúng thành sai hoặc tự khen ngợi bản thân. |
| **External Environment Reflection (Code Interpreter, Test Cases)** | Bộ biên dịch mã nguồn (Python/Rust Compiler), kết quả chạy Unit Test thực tế, API response code (200 vs 500). | **Cực kỳ cao (Ground Truth)**. Không phụ thuộc vào cảm tính của LLM. | Không có; máy tính trả về lỗi rõ ràng để LLM đọc và sửa. |
| **Dual-Agent Actor-Critic (2 Model riêng biệt)** | Một mô hình Generator độc lập và một mô hình Evaluator độc lập với system prompt đối lập. | Cao, nếu Evaluator sử dụng mô hình có năng lực lý luận cao hơn (e.g., Generator là LLaMA-8B, Critic là Claude 3.5 Sonnet). | Cần kiểm soát chi phí token gấp đôi. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy tắc triển khai Reflection an toàn trong Production
- **Không bao giờ tin vào Self-Correction "nói suông"**:
  - Chỉ kích hoạt luồng Reflection khi có **Tín hiệu Khách quan (Objective Ground Truth)**: Unit tests, Linter errors, Pydantic validation failures, SQL syntax verification.
  - Thiết kế tiêu chí phản biện (Rubric) cực kỳ định lượng: *"Câu trả lời có vượt quá 500 từ không? Có chứa trích dẫn nguồn không? Có đúng định dạng JSON không?"*.
- **Chống thoái lui (Regression Prevention)**:
  - Nếu sau 3 lần sửa mà kết quả mới có điểm số thấp hơn bản nháp ban đầu, hệ thống phải tự động Rollback về bản nháp tốt nhất trong lịch sử.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Tại sao trong bài toán sinh mã nguồn (Code Generation), mô hình kết hợp Reflection với Compiler lại cho tỷ lệ Pass@1 cao hơn 40% so với sinh đơn lẻ?*
  - **A**: Trình biên dịch cung cấp phản hồi xác định (deterministic feedback) với thông báo lỗi cụ thể (dòng lỗi, tên biến undefined, lỗi type mismatch). Khi đưa log lỗi này vào context, LLM không phải mò mẫm phỏng đoán mà biến bài toán từ "sinh mã mới từ con số 0" thành bài toán "chẩn đoán và sửa lỗi cục bộ" (targeted debugging), vốn là tác vụ mà LLM thực hiện rất xuất sắc.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[agentic-ai-core]] — Nền tảng kiến trúc nơi Reflection hoàn thiện chu trình kiểm soát chất lượng.
- [[react-pattern]] — ReAct kiểm tra từng bước vi mô, Reflection đánh giá toàn cục vĩ mô.
- [[llm-evaluation]] — Cung cấp các chỉ số và rubric để Evaluator chấm điểm.
- [[human-in-the-loop]] — Điểm dừng leo thang khi Reflection thất bại sau nhiều lần thử.
""",

    "planning-and-decomposition.md": r"""# Lập Kế Hoạch và Phân Rã Nhiệm Vụ (Planning & Task Decomposition)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 14.4; *Master All 20 Agentic AI Design Patterns*, Pattern 6; Wang et al. (2023) *"Plan-and-Solve Prompting"*; Kim et al. (2024) *"LLM Compiler"*.
> **Miền kiến thức**: [[agentic-overview|Hierarchical Planning & Task Execution]]
> **Tài liệu gốc liên quan**:
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 14-18)
> - [Agentic AI Design Patterns(2026 Edition).pdf](../../resources/genai/Agentic%20AI%20Design%20Patterns%282026%20Edition%29.pdf) (Trang 10-14)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 132-134)

---

## 1. Tóm tắt (Executive Summary)
**Lập kế hoạch và Phân rã Nhiệm vụ (Planning & Task Decomposition)** là khả năng kiến trúc cho phép AI Agent chia tách một mục tiêu lớn, trừu tượng, dài hạn thành một đồ thị có hướng không chu trình (**DAG - Directed Acyclic Graph**) của các nhiệm vụ con độc lập, có thể thực thi tuần tự hoặc song song. Thay vì nhảy ngay vào hành động theo cảm tính, Agent dành một giai đoạn tiền khả thi để xây dựng lộ trình, xác định các phụ thuộc dữ liệu giữa các bước, từ đó giảm thiểu tối đa rủi ro đi chệch hướng và tối ưu hóa thời gian thực thi thông qua tính toán song song.

---

## 2. Định nghĩa chính thống & Các chiến lược Lập kế hoạch (Planning Strategies)

### 2.1 Phân loại các mô hình Planning
1. **Planning without Feedback (Static Planning)**:
   - Mô hình lập toàn bộ danh sách các bước từ đầu đến cuối trước khi thực hiện (như **Plan-and-Solve Prompting**). Phù hợp cho các bài toán có quy trình chuẩn xác định (Deterministic Workflows).
2. **Planning with Feedback (Dynamic / Adaptive Planning)**:
   - Mô hình lập kế hoạch sơ bộ, sau mỗi bước thực thi sẽ cập nhật lại kế hoạch dựa trên kết quả thực tế thu được từ môi trường (như **Hierarchical Task Networks - HTN** hoặc **ReAct với Dynamic Todo List**).
3. **LLM Compiler (Parallel DAG Execution)**:
   - Lập kế hoạch theo cấu trúc đồ thị luồng dữ liệu (Dataflow Graph). Các tác vụ không phụ thuộc nhau được bắn đồng thời vào thread pool chạy song song trên nhiều workers, giảm thời gian thực thi từ hàng phút xuống vài giây.

```mermaid
graph TD
    Goal["Complex Objective: Viết báo cáo phân tích thị trường chip AI 2026"] --> Planner["Planner LLM (Decomposition)"]
    
    subgraph DAG Plan Execution
        Planner --> T1["Task 1: Thu thập báo cáo tài chính NVIDIA"]
        Planner --> T2["Task 2: Thu thập báo cáo tài chính AMD"]
        Planner --> T3["Task 3: Thu thập số liệu thị phần TSMC"]
        
        T1 --> T4["Task 4: So sánh doanh thu & biên lợi nhuận (Phụ thuộc T1, T2)"]
        T2 --> T4
        
        T3 --> T5["Task 5: Phân tích năng lực chuỗi cung ứng (Phụ thuộc T3)"]
        
        T4 --> T6["Task 6: Tổng hợp bài viết hoàn chỉnh (Phụ thuộc T4, T5)"]
        T5 --> T6
    end
    
    T6 --> FinalReport["Final Market Intelligence Report"]
```

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Phương pháp | Chi phí Token | Độ trễ tổng thể | Khả năng thích ứng với ngoại lệ |
| :--- | :--- | :--- | :--- |
| **ReAct thuần túy (Không có Planner)** | Rất cao (mỗi bước phải nạp lại toàn bộ lịch sử các bước trước). | Chậm (tuần tự từng bước $1, 2, ..., N$). | Thích ứng vi mô tốt, nhưng dễ bị mất tầm nhìn vĩ mô ("lạc trôi" sau bước thứ 5). |
| **Plan-and-Solve (Kế hoạch tĩnh)** | Thấp (lập kế hoạch 1 lần, sau đó chạy lần lượt). | Nhanh hơn ReAct. | Rất kém; nếu bước 2 bị lỗi, các bước 3, 4, 5 phía sau lập tức bị vô hiệu hóa vì dựa trên dữ liệu không tồn tại. |
| **Hierarchical Planning + DAG Compiler** | Tối ưu hóa nhờ cache prompt và chạy song song. | **Nhanh nhất** (các nhánh độc lập chạy đa luồng). | **Xuất sắc nhất**; có thể tái lập kế hoạch (re-plan) cục bộ cho nhánh bị lỗi mà không ảnh hưởng các nhánh khác. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Quy chuẩn cấu trúc dữ liệu của một Task DAG
Một Task Plan chuyên nghiệp bắt buộc phải có schema rõ ràng:
```json
{
  "plan_id": "market_analysis_01",
  "tasks": [
    {
      "task_id": "fetch_nvidia",
      "description": "Crawl Q3 2026 earnings report of Nvidia",
      "tool": "web_search",
      "dependencies": []
    },
    {
      "task_id": "fetch_amd",
      "description": "Crawl Q3 2026 earnings report of AMD",
      "tool": "web_search",
      "dependencies": []
    },
    {
      "task_id": "synthesize_margin",
      "description": "Calculate gross margin gap",
      "tool": "python_calculator",
      "dependencies": ["fetch_nvidia", "fetch_amd"]
    }
  ]
}
```

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Khi một bước trong DAG Plan bị thất bại do API bên ngoài sập, hệ thống nên xử lý thế nào để không phải chạy lại toàn bộ từ đầu?*
  - **A**: Áp dụng kỹ thuật **Checkpointing & State Serialization**: Lưu trạng thái kết quả của từng node đã hoàn thành vào database (như PostgreSQL hoặc Redis). Khi một node thất bại, cơ chế Error Recovery chỉ kích hoạt bộ Planner để tái lập kế hoạch cục bộ cho các node con bị ảnh hưởng trực tiếp (Downstream dependents), bảo toàn nguyên vẹn kết quả của các node độc lập đã chạy thành công trước đó.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[agentic-ai-core]] — Năng lực điều phối cốt lõi của Agent.
- [[multi-agent-collaboration]] — Phân bổ các tác vụ trong kế hoạch cho các chuyên viên agent khác nhau.
- [[tool-use-and-function-calling]] — Công cụ thực thi từng tác vụ cụ thể trong kế hoạch.
- [[reflection-and-self-correction]] — Đánh giá tính khả thi của kế hoạch trước khi chạy.
""",

    "tool-use-and-function-calling.md": r"""# Sử Dụng Công Cụ và Gọi Hàm (Tool Use & Function Calling)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 14.3; Schick et al. (2023) *"Toolformer: Language Models Can Teach Themselves to Use Tools"*; Anthropic *"Model Context Protocol (MCP) Specification"* (2024-2025).
> **Miền kiến thức**: [[agentic-overview|Tool Integration & Systems Interoperability]]
> **Tài liệu gốc liên quan**:
> - [AIO2025_[Description]-AI-Agent-LLM-Tool-Calling.pdf](../../resources/genai/AIO2025_%5BDescription%5D-AI-Agent-LLM-Tool-Calling.pdf) (Trang 1-42)
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 8-12)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 131-133)

---

## 1. Tóm tắt (Executive Summary)
**Sử dụng Công cụ và Gọi Hàm (Tool Use & Function Calling)** là năng lực của Mô hình Ngôn ngữ Lớn trong việc nhận biết khi nào cần bổ sung tài nguyên ngoài, tự động lựa chọn công cụ phù hợp từ một danh mục định sẵn, và sản sinh ra chuỗi tham số có cấu trúc chuẩn mực (JSON Schema) để hệ thống máy chủ thực thi. Đây là cầu nối sinh tử biến LLM từ một "bộ não bị nhốt trong lồng kính" thành một tác nhân có thể điều khiển máy tính: thực thi truy vấn SQL, gọi REST APIs, tính toán đại số chính xác, đọc ghi tệp tin và giao tiếp với thế giới thực.

---

## 2. Định nghĩa chính thống & Giao thức Hoạt động (Protocols & Mechanism)

### 2.1 Vòng đời của một Function Call
1. **Tool Definition**: Định nghĩa danh mục công cụ kèm tên hàm, mô tả ngữ nghĩa và schema tham số theo chuẩn **JSON Schema**:
   ```json
   {
     "name": "get_stock_price",
     "description": "Truy xuất giá cổ phiếu thời gian thực theo mã ticker",
     "parameters": {
       "type": "object",
       "properties": {
         "ticker": {"type": "string", "description": "Mã chứng khoán, ví dụ: AAPL"}
       },
       "required": ["ticker"]
     }
   }
   ```
2. **Model Decision**: Khi người dùng hỏi *"Giá cổ phiếu Apple hôm nay thế nào?"*, LLM nhận diện không thể trả lời bằng kiến thức tham số, liền ngắt chế độ sinh text thông thường và sinh ra một **Tool Call Object**:
   `{"name": "get_stock_price", "arguments": "{\"ticker\": \"AAPL\"}"}`
3. **Client Execution**: Server ứng dụng nhận lệnh, chạy hàm Python thực tế, lấy dữ liệu từ sàn chứng khoán.
4. **Context Injection**: Kết quả trả về (Tool Output) được đóng gói vào vai trò `role: "tool"` gửi ngược lại cho LLM để sinh câu trả lời tự nhiên cuối cùng cho người dùng.

```mermaid
sequenceDiagram
    autonumber
    actor User as User
    participant App as Backend Application
    participant LLM as LLM Engine
    participant API as External Service / DB
    
    User->>App: "Đặt vé xem phim suất 19h tối nay"
    App->>LLM: Prompt + Tools Definition (JSON Schema)
    Note over LLM: Model selects tool 'book_ticket'<br/>Generates JSON Arguments
    LLM-->>App: tool_calls: {name: 'book_ticket', args: {time: '19:00'}}
    App->>API: Execute booking HTTP POST request
    API-->>App: Response: {status: 'success', seat: 'H12'}
    App->>LLM: Role 'tool': {status: 'success', seat: 'H12'}
    LLM-->>App: Final Text: "Vé của bạn đã được đặt thành công, ghế H12!"
    App-->>User: Hiển thị kết quả cho người dùng
```

### 2.2 Cuộc cách mạng Giao thức: Model Context Protocol (MCP)
Vào cuối 2024 - 2026, ngành công nghiệp chuẩn hóa giao thức **MCP (Model Context Protocol)** do Anthropic khởi xướng:
- Thay vì mỗi công ty viết một adapter tool riêng cho Slack, GitHub, Postgres: MCP đóng vai trò như **cổng USB-C cho AI**.
- Bất kỳ dịch vụ nào cung cấp MCP Server đều có thể cắm trực tiếp vào bất kỳ AI Agent / LLM nào hỗ trợ MCP Client một cách an toàn và tức thì.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Phương thức | Cơ chế bắt lỗi cú pháp | Tỷ lệ sinh JSON hợp lệ | Nguy cơ bảo mật |
| :--- | :--- | :--- | :--- |
| **Prompting chay (Text-based Tool Calling)** | Yêu cầu LLM tự in cú pháp ra text, dùng Regex bóc tách. | Kém (~70-80%). Dễ bị lỗi dấu ngoặc, thoát ký tự (unescaped quotes). | Cao; dễ bị parse sai tham số. |
| **Native Function Calling (OpenAI / Claude API)** | Can thiệp ở tầng Logit Bias và Constrained Decoding của Sampling Engine. | Rất cao (> 99.5%). Đảm bảo đầu ra luôn tuân thủ 100% JSON Schema. | Cần cơ chế phân quyền (Authorization) ở phía backend server. |
| **Model Context Protocol (MCP)** | Giao thức chuẩn hóa Client-Server phân tán (JSON-RPC 2.0 qua stdio / SSE). | Tuyệt đối; có tầng kiểm soát kiểu dữ liệu hai chiều. | Tách biệt ranh giới bảo mật: Server quy định quyền truy cập, Client không thể thực thi mã tùy tiện. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Bí kíp thiết kế Tool Descriptions chuẩn xác
Chất lượng chọn tool của LLM phụ thuộc hoàn toàn vào **phần mô tả (Tool Description)**:
- **Nguyên tắc "Mô tả cả điều công cụ KHÔNG LÀM"**: Nếu có 2 công cụ dễ gây nhầm lẫn (ví dụ: `search_orders` và `search_customers`), hãy ghi chú rõ trong description: *"Dùng để tìm kiếm đơn hàng. KHÔNG dùng công cụ này để tra cứu thông tin cá nhân khách hàng, hãy dùng search_customers"*.
- **Giới hạn số lượng Tool**: Không bao giờ nạp quá 20-30 tools vào context cùng một lúc. Khi danh mục tool quá lớn, hãy dùng kỹ thuật **Tool Retrieval**: Lưu các tool definition vào Vector DB và chỉ truy xuất Top 5 tools liên quan nhất tới query hiện tại nạp vào prompt.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Làm thế nào để phòng chống rủi ro khi Agent tự động gọi một công cụ phá hủy dữ liệu (Destructive Tool như DROP TABLE hay DELETE_FILE)?*
  - **A**: Áp dụng mô hình **Dual-Key Authorization & Sandboxing**:
    1. Gắn cờ thuộc tính `is_destructive: true` vào schema công cụ.
    2. Khi LLM phát lệnh gọi công cụ này, hệ sinh thái Agent bắt buộc phải dừng lại và kích hoạt cổng phê duyệt con người ([[human-in-the-loop|Human-in-the-Loop Gate]]).
    3. Mọi thao tác thực thi bắt buộc phải chạy trong môi trường Sandbox cô lập (như Docker container dùng một lần hoặc máy ảo microVM Firecracker) với quyền tài khoản hạn chế thấp nhất (Least Privilege Principle).

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[agentic-ai-core]] — Khung tích hợp công cụ vào vòng lặp của tác nhân.
- [[react-pattern]] — Mô thức điều phối chu trình gọi công cụ và nhận quan sát.
- [[human-in-the-loop]] — Cơ chế kiểm soát an toàn cho các công cụ nhạy cảm.
- [[prompt-engineering]] — Kỹ thuật tối ưu hóa định nghĩa tool và schema.
""",

    "multi-agent-collaboration.md": r"""# Hợp Tác Đa Tác Nhân (Multi-Agent Collaboration)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 14.5; *Master All 20 Agentic AI Design Patterns*, Pattern 7; Wu et al. (2023) *"AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"*; Hong et al. (2023) *"MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"*.
> **Miền kiến thức**: [[agentic-overview|Distributed Agentic Systems & Swarm Intelligence]]
> **Tài liệu gốc liên quan**:
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 18-22)
> - [Agentic AI Design Patterns(2026 Edition).pdf](../../resources/genai/Agentic%20AI%20Design%20Patterns%282026%20Edition%29.pdf) (Trang 16-20)
> - [A Vision for Auto Research with LLM Agents.pdf](../../resources/genai/A%20Vision%20for%20Auto%20Research%20with%20LLM%20Agents.pdf) (Trang 10-18)

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

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[agentic-ai-core]] — Khung kiến trúc nền tảng của từng tác nhân thành phần.
- [[planning-and-decomposition]] — Cơ chế phân bổ công việc từ Supervisor xuống Worker.
- [[reflection-and-self-correction]] — Mô hình Actor-Critic là dạng tối giản của 2-Agent collaboration.
- [[agent-memory-systems]] — Quản lý bộ nhớ chia sẻ và bộ nhớ riêng tư cho từng tác nhân.
""",

    "agent-memory-systems.md": r"""# Hệ Thống Bộ Nhớ Của Tác Nhân (Agent Memory Systems)

> **Khái niệm chính thống**: *Encyclopedia of LLMs*, Section 14.2; *Master All 20 Agentic AI Design Patterns*, Pattern 8; Packer et al. (2023) *"MemGPT: Towards LLMs as Operating Systems"*; Park et al. (2023) *"Generative Agents"*.
> **Miền kiến thức**: [[agentic-overview|Cognitive Memory Architectures & Persistence]]
> **Tài liệu gốc liên quan**:
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 22-26)
> - [Agentic AI Design Patterns(2026 Edition).pdf](../../resources/genai/Agentic%20AI%20Design%20Patterns%282026%20Edition%29.pdf) (Trang 8-12)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 130-131)

---

## 1. Tóm tắt (Executive Summary)
**Hệ thống Bộ nhớ của Tác nhân (Agent Memory Systems)** là cơ sở hạ tầng lưu trữ, tổ chức và truy hồi thông tin cho phép AI Agent duy trì trạng thái ngữ cảnh nhất quán xuyên suốt phiên làm việc hiện tại và tích lũy tri thức kinh nghiệm qua nhiều phiên làm việc dài hạn trong tương lai. Lấy cảm hứng từ cấu trúc phân tầng bộ nhớ máy tính (RAM vs Disk) và tâm lý học nhận thức của con người, kiến trúc bộ nhớ Agent được chia làm 4 tầng riêng biệt: **Bộ nhớ Ngắn hạn (Short-term Working Memory)**, **Bộ nhớ Sự kiện (Episodic Memory)**, **Bộ nhớ Ngữ nghĩa (Semantic Memory)**, và **Bộ nhớ Thủ tục (Procedural Memory)**.

---

## 2. Định nghĩa chính thống & Kiến trúc 4 Tầng Bộ nhớ (Cognitive Memory Taxonomy)

```mermaid
flowchart TD
    subgraph Agent Memory Architecture
        WM["1. Short-Term Working Memory\n(In-Context Window / KV Cache, RAM)"]
        
        subgraph Long-Term Persistent Storage
            EM["2. Episodic Memory\n(Past Action-Observation Trajectories, Vector DB)"]
            SM["3. Semantic Memory\n(Facts, World Knowledge, User Preferences, KG)"]
            PM["4. Procedural Memory\n(System Prompts, Code Functions, SOPs, Rules)"]
        end
    end
    
    Query["Current User Input"] --> MemController["Memory Controller / Retrieval Engine"]
    WM <--> MemController
    EM <--> MemController
    SM <--> MemController
    PM <--> MemController
    MemController --> SynthesizedContext["Optimized Context Prompt for LLM Brain"]
```

### 2.1 Chi tiết 4 tầng bộ nhớ
1. **Short-Term / Working Memory (Bộ nhớ Làm việc Ngắn hạn)**:
   - *Bản chất*: Toàn bộ chuỗi token nằm trực tiếp trong Context Window của LLM tại thời điểm hiện tại.
   - *Đặc điểm*: Truy xuất tức thì, độ trễ 0ms, nhưng bị giới hạn cứng bởi kích thước context window và chi phí token đắt đỏ.
2. **Episodic Memory (Bộ nhớ Sự kiện / Trải nghiệm)**:
   - *Bản chất*: Lưu trữ biên bản nhật ký về những hành động, sai lầm và kết quả mà Agent đã từng trải qua trong quá khứ: *"Lần trước khi gọi API thanh toán với mã giảm giá X, hệ thống đã báo lỗi mã hết hạn"*.
   - *Cơ chế lưu trữ*: Thường được lưu dưới dạng embedding trong Vector DB, được truy xuất qua tìm kiếm tương đồng mỗi khi Agent gặp tình huống tương tự.
3. **Semantic Memory (Bộ nhớ Ngữ nghĩa / Tri thức thế giới)**:
   - *Bản chất*: Lưu trữ các sự thật khách quan, định nghĩa, thông tin hồ sơ người dùng (User Profile, sở thích cá nhân, điều khoản dịch vụ).
   - *Cơ chế lưu trữ*: Cơ sở dữ liệu quan hệ SQL hoặc Knowledge Graph.
4. **Procedural Memory (Bộ nhớ Thủ tục / Kỹ năng)**:
   - *Bản chất*: Tập hợp các quy tắc ứng xử bất biến, hướng dẫn vận hành chuẩn (SOP), code Python và định nghĩa tools mà Agent sở hữu để hoàn thành tác vụ.

### 2.2 Kiến trúc MemGPT (OS-Style Hierarchical Memory)
MemGPT (Packer et al., 2023) đưa ra cơ chế quản lý bộ nhớ như hệ điều hành:
- LLM được trang bị các công cụ đặc biệt để tự quản lý bộ nhớ của chính mình: `core_memory_append`, `core_memory_replace`, `archival_memory_insert`, `archival_memory_search`.
- Khi bộ nhớ ngắn hạn bị đầy, Agent tự động chạy tiến trình ngầm tóm tắt (Memory Consolidation) và đẩy dữ liệu cũ ra bộ nhớ dài hạn bên ngoài (Disk Offloading), tương tự như cơ chế Virtual Memory Paging trong HĐH.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Khía cạnh | Bộ nhớ Chatbot thông thường | Hệ thống Bộ nhớ Agent hoàn chỉnh | Ý nghĩa đối với AI Engineer |
| :--- | :--- | :--- | :--- |
| **Cách quản lý ngữ cảnh** | Cắt cụt đuôi (Sliding Window): Xóa các tin nhắn cũ nhất khi đầy context. | Tóm tắt phân tầng (Hierarchical Summarization) + RAG Retrieval trên lịch sử quá khứ. | Không làm mất các thông tin quan trọng đã trao đổi ở đầu phiên làm việc (như yêu cầu tiên quyết của người dùng). |
| **Khả năng học tập xuyên phiên** | Hoàn toàn bằng 0. Mỗi phiên chat mới là một thực thể mất trí nhớ (Amnesia). | Lưu trữ hồ sơ người dùng và các bài học thất bại vào Episodic Memory. | Agent trở nên thông minh hơn và cá nhân hóa sâu sắc theo thời gian sử dụng. |
| **Chi phí token** | Tăng tuyến tính và phình to cực nhanh sau 10 lượt chat. | Cố định ở mức tối ưu nhờ chỉ truy xuất các mẩu ký ức liên quan nhất vào prompt. | Tiết kiệm 60-80% chi phí vận hành hạ tầng API. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 Cơ chế Tích tụ và Suy giảm Ký ức (Memory Decay & Consolidation)
Lấy cảm hứng từ nghiên cứu *Generative Agents* (Park et al., 2023), điểm số truy hồi ký ức ($Score$) được tính bằng tổng hợp của 3 yếu tố:
$$Score = \alpha \cdot \text{Recency} + \beta \cdot \text{Importance} + \gamma \cdot \text{Relevance}$$
- **Recency (Độ tươi mới)**: Ký ức vừa diễn ra cách đây vài phút có điểm số cao hơn ký ức từ tháng trước theo hàm suy giảm mũ ($e^{-\lambda \Delta t}$).
- **Importance (Tầm quan trọng)**: LLM tự chấm điểm mức độ quan trọng của sự kiện (thang điểm 1-10); sự kiện mua nhà hay đổi mật khẩu có điểm cao hơn câu chào hỏi thời tiết.
- **Relevance (Độ liên quan)**: Điểm Cosine Similarity giữa câu hỏi hiện tại và nội dung ký ức.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Làm thế nào để xử lý mâu thuẫn tri thức trong bộ nhớ dài hạn của Agent (ví dụ: ngày 1 người dùng nói "Tôi ăn chay", ngày 10 người dùng nói "Hôm nay tôi muốn ăn bít tết bò")?*
  - **A**: Áp dụng kỹ thuật **Temporal Memory Updating & Conflict Resolution**: Mọi mẩu thông tin trong Semantic/Episodic Memory bắt buộc phải có trường metadata thời gian (`timestamp`). Khi phát hiện thông tin mới đối nghịch với thông tin cũ, hệ thống cập nhật trạng thái mới nhất đồng thời gắn cờ trạng thái cũ là `is_superseded: true`, hoặc kích hoạt bước đối thoại xác nhận lại với người dùng.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[agentic-ai-core]] — Nền tảng kiến trúc chứa hệ thống bộ nhớ.
- [[vector-embeddings]] — Công cụ đánh chỉ mục cho Episodic Memory.
- [[reflection-and-self-correction]] — Nguồn dữ liệu sinh ra các bài học đúc kết lưu vào bộ nhớ.
- [[human-in-the-loop]] — Quản trị quyền riêng tư và quyền được xóa bỏ dữ liệu (GDPR) trong bộ nhớ.
""",

    "human-in-the-loop.md": r"""# Con Người Trong Vòng Lặp và Quản Trị Tác Nhân (Human-in-the-Loop & Agent Governance)

> **Khái niệm chính thống**: *Master All 20 Agentic AI Design Patterns*, Pattern 12; *Agentic AI Design Patterns (2026 Edition)*, Section 8; *846485886...jpg* ("5. Ai chịu trách nhiệm kết quả? AI Agents With Human In The Loop"); *848044627...jpg* ("3. Khi nào không nên dùng AI?").
> **Miền kiến thức**: [[agentic-overview|AI Safety, Ethics & Production Governance]]
> **Tài liệu gốc liên quan**:
> - [846485886_122320901828195094_432191169857527385_n.jpg](../../resources/images/846485886_122320901828195094_432191169857527385_n.jpg) (Infographic 5: Trách nhiệm kết quả & HITL)
> - [848044627_122320901882195094_403801078837249544_n.jpg](../../resources/images/848044627_122320901882195094_403801078837249544_n.jpg) (Infographic 3: Khi nào không nên dùng AI?)
> - [Master All 20 Agentic AI Design Patterns.pdf](../../resources/genai/Master%20All%2020%20Agentic%20AI%20Design%20Patterns.pdf) (Trang 26-28)
> - [Encyclopedia of LLMs and Foundation Models.pdf](../../resources/genai/Encyclopedia%20of%20LLMs%20and%20Foundation%20Models.pdf) (Trang 136)

---

## 1. Tóm tắt (Executive Summary)
**Con người trong Vòng lặp (Human-in-the-Loop - HITL)** là mô thức kiến trúc và quản trị sống còn đảm bảo sự kiểm soát an toàn, độ tin cậy và tuân thủ pháp lý của các hệ thống Agentic AI trong môi trường doanh nghiệp. Về mặt kỹ thuật, HITL thiết lập các **Chốt chặn Kiểm duyệt (Approval Gates)** và **Cơ chế Leo thang (Escalation Policies)** để tạm dừng tiến trình tự chủ của Agent trước các hành động rủi ro cao hoặc khi độ tin cậy của mô hình xuống thấp. Về mặt triết lý và đạo đức nghề nghiệp, HITL khẳng định nguyên lý tối thượng: **AI chỉ là công cụ hỗ trợ quyết định; trách nhiệm đạo đức, pháp lý và hậu quả cuối cùng luôn thuộc về con người và tổ chức.**

---

## 2. Định nghĩa chính thống & Triết lý Cốt lõi (Core Philosophy & Architecture)

### 2.1 "Ai chịu trách nhiệm kết quả?" (Triết lý Phân biệt Junior vs Senior)
Theo trích đoạn đúc kết kinh nghiệm thực chiến từ chuyên gia (*resources/images/846485886...jpg*):
> - **Người mới (Junior)**: Hay nghĩ trách nhiệm thuộc về mô hình (Model) hoặc dữ liệu (Data). Khi có sự cố, thường đổ lỗi cho thuật toán.
> - **Người có trình độ (Senior / Architect)**: Hiểu sâu sắc rằng **trách nhiệm luôn thuộc về con người và tổ chức vận hành**.
> - AI chỉ là công cụ hỗ trợ ra quyết định (Decision Support Tool). Bắt buộc phải thiết kế quy trình kiểm soát và phê duyệt kết quả. Không thể đổ lỗi cho thuật toán khi có hậu quả xảy ra. Hiểu được câu hỏi này là dấu hiệu bước sang đẳng cấp Senior.

```mermaid
flowchart TD
    Task["High-Stakes Task Triggered"] --> Agent["Agent Workflow (Perceive -> Plan -> Act)"]
    Agent --> EvalRisk{"Risk & Impact Assessment"}
    
    EvalRisk -->|"Low Risk (Read-only / Sandbox)"| AutoExec["Autonomous Execution"]
    EvalRisk -->|"High Risk (Money / Delete / Medical / Legal)"| Gate["HITL Approval Gate (Paused)"]
    
    Gate --> HumanReview{"Human Operator Review"}
    HumanReview -->|"Approved"| Resume["Resume Execution with Audit Trail"]
    HumanReview -->|"Rejected / Feedback"| Replan["Return Feedback to Agent (Re-plan)"]
    HumanReview -->|"Takeover"| Manual["Manual Override (Bypass Agent)"]
    
    Resume --> Log[("Tamper-Proof Audit Log: Who Approved What & When")]
```

### 2.2 Các hình thái tích hợp Human-in-the-Loop
1. **Human-on-the-Loop (Giám sát thụ động)**: Agent chạy tự động, con người theo dõi dashboard thời gian thực và có thể bấm nút "Emergency Kill Switch" khi phát hiện bất thường.
2. **Human-in-the-Loop (Phê duyệt chủ động)**: Luồng công việc bị đóng băng (State Suspended) tại các điểm giao cắt quan trọng, chờ con người click "Approve" hoặc nhập thông tin bổ sung qua giao diện UI/Slack trước khi tiếp tục.
3. **Human-in-Command (Con người chỉ đạo)**: Con người đưa ra quyết định ở từng chặng, Agent chỉ đóng vai trò phân tích dữ liệu, tóm tắt và đưa ra 3 phương án gợi ý.

---

## 3. So sánh & Mâu thuẫn / Sắc thái giữa các tài liệu

| Tiêu chí | Tư duy Thử nghiệm (Dự án nghiên cứu / Demo) | Tư duy Vận hành Doanh nghiệp (Enterprise Production) |
| :--- | :--- | :--- |
| **Mục tiêu tối thượng** | Tìm kiếm sự tự chủ 100% (Zero-human intervention). | **Quản trị rủi ro tối đa (Zero-unauthorized catastrophic action)**. |
| **Quyền hạn của Agent** | Cung cấp toàn bộ API keys có quyền cao nhất (Admin/Root) cho Agent tự do gọi. | **Nguyên tắc Đặc quyền Tối thiểu (Principle of Least Privilege)**: Chỉ cấp quyền đọc (Read-only). Mọi quyền ghi/xóa/giao dịch tài chính bắt buộc phải qua HITL Gate. |
| **Ghi nhận lịch sử (Auditing)** | Chỉ in log ra terminal qua `print()`. | **Lưu vết kiểm toán bất biến (Tamper-proof Audit Trail)**: Ghi lại từng prompt, token, lý do gọi hàm, ID của nhân viên duyệt, và thời điểm phê duyệt phục vụ thanh tra pháp lý. |

---

## 4. Góc nhìn Thực chiến & Thiết kế Hệ thống cho AI Engineer

### 4.1 "Khi nào KHÔNG NÊN dùng AI?" (Nguyên lý loại trừ từ Infographic 848044627)
Một AI Engineer đẳng cấp thể hiện ở việc **biết từ chối đưa AI vào những bài toán không phù hợp**:
- **Người non**: Thường nghĩ bài toán nào cũng nhét AI vào để thể hiện công nghệ.
- **Người có kinh nghiệm**: Biết rất nhiều trường hợp KHÔNG ĐƯỢC dùng AI:
  1. *Dữ liệu quá ít hoặc quá không ổn định*: Rủi ro mô hình sai lệch cực lớn.
  2. *Bài toán cần giải thích rõ ràng 100% logic*: AI hộp đen phức tạp là bất lợi pháp lý (hãy dùng Rule-based, Decision Tree hoặc SQL).
  3. *Chi phí triển khai và vận hành lớn hơn lợi ích kinh doanh mang lại*.
  4. *Có những bài toán tự động hóa xác định (Automation using connectors/triggers)*: Chạy theo lịch trình (Scheduled triggers) hoặc sự kiện (Event-based webhooks) bằng code thuần hiệu quả và ổn định hơn ngàn lần AI.

### 4.2 Câu hỏi phỏng vấn thực tế
- **Q**: *Nếu hệ thống AI Agent hỗ trợ chẩn đoán y tế hoặc duyệt giải ngân khoản vay ngân hàng đưa ra quyết định sai lầm gây thiệt hại nghiêm trọng, ai là người chịu trách nhiệm trước pháp luật?*
  - **A**: Về mặt pháp lý và tổ chức, thuật toán và mô hình AI không phải là thực thể pháp nhân (Legal Entity) nên không thể chịu trách nhiệm pháp lý. Trách nhiệm hoàn toàn thuộc về **ban lãnh đạo tổ chức sở hữu hệ thống và kỹ sư/chuyên viên con người đã ký duyệt quy trình**. Một kiến trúc sư phần mềm AI có đạo đức phải thiết kế hệ thống sao cho AI luôn ở vị thế "khuyến nghị" (Recommendation) và bắt buộc phải có chữ ký số xác nhận của chuyên gia con người trước khi hành động có hiệu lực.

---

## 5. Mạng lưới Liên kết Tri thức (Knowledge Graph & [[wiki-links]])
- [[agentic-ai-core]] — Khung kiến trúc tổng thể nơi HITL đóng vai trò chốt chặn an toàn.
- [[tool-use-and-function-calling]] — Phân loại các công cụ nguy hiểm cần kích hoạt HITL.
- [[reflection-and-self-correction]] — Điểm leo thang lên con người khi cơ chế tự sửa lỗi thất bại.
- [[llm-evaluation]] — Cung cấp các số liệu định lượng về tỷ lệ sai sót của mô hình để thiết lập ngưỡng HITL.
"""
}

def generate():
    for filename, content in ENTITIES.items():
        filepath = WIKI_DIR / filename
        filepath.write_text(content.strip(), encoding="utf-8")
        print(f"Created: {filepath.name}")

if __name__ == "__main__":
    generate()
