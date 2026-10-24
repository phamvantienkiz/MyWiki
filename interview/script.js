/* ==========================================================================
   BAHA HOMES - AI INTERN LECTURE VISUALIZER
   Interactive Engine & ScrollSpy Controller (Unified Sidebar Architecture)
   ========================================================================== */

// 0. Dark Mode / Light Mode Theme Controller
function initTheme() {
    const savedTheme = localStorage.getItem('baha_interview_theme');
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
        applyTheme('dark');
    } else {
        applyTheme('light');
    }

    // Listen for system preference changes if user hasn't explicitly set a preference
    if (window.matchMedia) {
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            if (!localStorage.getItem('baha_interview_theme')) {
                applyTheme(e.matches ? 'dark' : 'light');
            }
        });
    }
}

function applyTheme(theme) {
    const isDark = theme === 'dark';
    document.documentElement.classList.toggle('dark', isDark);
    if (document.body) {
        document.body.classList.toggle('dark', isDark);
    }
    document.documentElement.setAttribute('data-theme', theme);

    // Update toggle button icons and titles
    const toggleBtns = document.querySelectorAll('.theme-toggle-btn');
    toggleBtns.forEach(btn => {
        btn.innerHTML = isDark ? '☀️' : '🌙';
        btn.setAttribute('title', isDark ? 'Chuyển sang giao diện Sáng' : 'Chuyển sang giao diện Tối');
        btn.setAttribute('aria-label', isDark ? 'Chuyển sang giao diện Sáng' : 'Chuyển sang giao diện Tối');
    });

    const footerToggle = document.getElementById('theme-toggle-footer');
    if (footerToggle) {
        footerToggle.innerHTML = isDark ? '☀️ Giao Diện: Tối (Bấm để sang Sáng)' : '🌙 Giao Diện: Sáng (Bấm để sang Tối)';
    }
}

function toggleTheme() {
    const isDark = document.documentElement.classList.contains('dark');
    const newTheme = isDark ? 'light' : 'dark';
    localStorage.setItem('baha_interview_theme', newTheme);
    applyTheme(newTheme);
}

// Make toggleTheme accessible globally
window.toggleTheme = toggleTheme;

document.addEventListener("DOMContentLoaded", () => {
    // 0. Theme System Initialization
    initTheme();

    // 1. Safe KaTeX Auto-Render
    initKaTeXSafe();

    // 2. Navigation & Live ScrollSpy (Unified Left Sidebar)
    initScrollSpy();

    // 3. ReAct Simulator
    initSim();

    // 4. Three.js 3D Scene
    init3DScene();

    // 5. Automation ROI Calculator
    updateROICalc();

    // 6. Mobile Drawer Toggle
    initMobileDrawer();
});

/* --------------------------------------------------------------------------
   1. Safe KaTeX Initialization
   -------------------------------------------------------------------------- */
function initKaTeXSafe() {
    try {
        if (typeof renderMathInElement === "function") {
            renderMathInElement(document.body, {
                delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false },
                    { left: '\\[', right: '\\]', display: true },
                    { left: '\\(', right: '\\)', display: false }
                ],
                throwOnError: false
            });
            console.log("KaTeX auto-render initialized successfully.");
        } else {
            console.warn("KaTeX library not detected on CDN. Formulas will display in plain LaTeX notation.");
        }
    } catch (err) {
        console.warn("KaTeX render error caught gracefully:", err);
    }
}

/* --------------------------------------------------------------------------
   2. Reading Progress Bar & ScrollSpy (Unified Sidebar Navigation)
   -------------------------------------------------------------------------- */
function initScrollSpy() {
    const progressBar = document.getElementById('progress-bar');
    const readingPct = document.getElementById('reading-pct');
    const sections = document.querySelectorAll('section[id], header[id], div[id].scroll-target');
    const navLinks = document.querySelectorAll('nav.nav-tree a.nav-link');

    window.addEventListener('scroll', () => {
        // Progress Calculation
        const scrollTop = window.scrollY || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const progress = scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
        
        if (progressBar) progressBar.style.width = `${progress}%`;
        if (readingPct) readingPct.innerText = `${Math.min(100, Math.round(progress))}%`;

        // Active Section Detection
        let currentSectionId = '';
        const offset = scrollTop + 160;

        sections.forEach(sec => {
            const top = sec.offsetTop;
            const height = sec.offsetHeight;
            if (offset >= top && offset < top + height) {
                currentSectionId = sec.getAttribute('id');
            }
        });

        // Update Active Link in Unified Sidebar
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (currentSectionId && link.getAttribute('href') === `#${currentSectionId}`) {
                link.classList.add('active');
            }
        });
    });
}

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function expandAllQA() {
    document.querySelectorAll('details.qa-card').forEach(d => d.open = true);
}

function collapseAllQA() {
    document.querySelectorAll('details.qa-card').forEach(d => d.open = false);
}

function initMobileDrawer() {
    const btn = document.getElementById('mobile-menu-btn');
    const sidebar = document.getElementById('sidebar');
    if (btn && sidebar) {
        btn.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });
    }
}

/* --------------------------------------------------------------------------
   3. ReAct Simulator (Google Antigravity Lifecycle)
   -------------------------------------------------------------------------- */
const simSteps = [
    {
        title: "Bước 1: Tiếp Nhận Yêu Cầu Của Kỹ Sư",
        badge: "USER_INPUT",
        code: `[User Request]:\n"Hãy viết module đọc file bảng bóc tách vật tư căn 2PN Vinhomes Grand Park (BOM_vinhomes_2pn.xlsx), trích xuất mã gỗ An Cường và độ dày, tính tổng chi phí theo bảng giá kho xưởng hiện tại."`,
        note: "Tác nhân nhận prompt có ngữ cảnh rõ ràng về loại căn hộ, tên file và mục tiêu kinh doanh."
    },
    {
        title: "Bước 2: Phân Tích & Lập Kế Hoạch (System 2 CoT)",
        badge: "THOUGHT_DAG",
        code: `[Agent Thought (System 2 CoT)]:\n1. Phân tích: Cần dùng thư viện pandas hoặc openpyxl để parse file Excel.\n2. Công cụ: Kiểm tra workspace xem file BOM có tồn tại không bằng tool list_directory.\n3. Rủi ro: Có thể thiếu thư viện pandas trong .venv -> Cần kiểm tra trước khi import.`,
        note: "Tác nhân chia nhỏ bài toán thành DAG (Directed Acyclic Graph), lường trước rủi ro thiếu thư viện."
    },
    {
        title: "Bước 3: Thực Thi Công Cụ (Tool Execution)",
        badge: "TOOL_CALL",
        code: `[Agent Action -> run_command]:\n$ uv run python -c "import pandas, openpyxl; print('Dependencies ready')"\n\n[Tool Result (STDERR)]:\nModuleNotFoundError: No module named 'openpyxl'`,
        note: "Tác nhân kiểm tra môi trường trong .venv cục bộ, bắt được lỗi thiếu dependency thay vì hoảng loạn."
    },
    {
        title: "Bước 4: Tự Phản Biện & Sửa Lỗi Tức Thì (Self-Correction)",
        badge: "OBSERVATION & FIX",
        code: `[Agent Observation & Self-Correction]:\n-> Phát hiện thiếu openpyxl. Tiến hành cài đặt cô lập:\n$ uv add openpyxl pandas\n-> Dependencies installed successfully.\n\n[Agent Code Generation]:\nTạo file 'app/services/bom_calculator.py' với async function và Pydantic V2 validation.`,
        note: "Tác nhân tự khắc phục lỗi môi trường theo quy tắc AGENTS.md, sinh code phân tầng Service rõ ràng."
    },
    {
        title: "Bước 5: Kiểm Thử & Nghiệm Thu Sản Phẩm (Final Delivery)",
        badge: "DELIVERABLE",
        code: `[Agent Final Output]:\n✅ Đã trích xuất thành công 18 hạng mục gỗ An Cường MDF lõi xanh chống ẩm.\n💰 Tổng dự toán chi phí xưởng: 142.500.000 VNĐ.\n🛡️ Kiểm thử: 100% test case pass, không có dữ liệu null, xuất JSON chuẩn Schema cho n8n trigger.`,
        note: "Hoàn thiện sản phẩm có kiểm thử (pytest pass 100%), bàn giao dữ liệu JSON có cấu trúc cho n8n webhook."
    }
];

function setSimStep(idx) {
    const buttons = document.querySelectorAll('#react-sim-buttons .interactive-btn');
    buttons.forEach((b, i) => {
        if (i === idx) b.classList.add('active');
        else b.classList.remove('active');
    });

    const step = simSteps[idx];
    const displayBox = document.getElementById('sim-code-display');
    const titleBox = document.getElementById('sim-title-display');
    const badgeBox = document.getElementById('sim-badge-display');
    const noteBox = document.getElementById('sim-note-display');

    if (titleBox) titleBox.innerText = step.title;
    if (badgeBox) badgeBox.innerText = step.badge;
    if (displayBox) displayBox.innerText = step.code;
    if (noteBox) noteBox.innerText = step.note;
}

function initSim() {
    setSimStep(0);
}

/* --------------------------------------------------------------------------
   4. Three.js 3D Spatial Interior Studio
   -------------------------------------------------------------------------- */
let scene3D, camera3D, renderer3D, controls3D, roomMeshGroup;
let isAutoRotating = false;
let currentPaletteMode = 0; // 0: Japandi Wood, 1: Modern Luxury Dark

function init3DScene() {
    const container = document.getElementById('threejs-canvas-container');
    if (!container) return;

    // Fallback if Three.js is not loaded
    if (typeof THREE === "undefined") {
        container.innerHTML = `
            <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; height:100%; color:#94a3b8; text-align:center; padding:20px;">
                <div style="font-size:2.2rem; margin-bottom:8px;">📐</div>
                <strong style="color:#f8fafc; font-size:1.15rem;">Bản Vẽ Kiến Trúc Mặt Bằng Căn Hộ Vinhomes Grand Park</strong>
                <p style="max-width:520px; margin-top:8px; font-size:0.9rem; line-height:1.6;">Phòng khách Studio 32m²: Sàn gỗ MDF An Cường lõi xanh 12mm • Sofa văng bọc nỉ 1.8m • Bàn trà thông minh tròn • Cửa sổ kính Low-E view công viên 36ha.</p>
                <div style="margin-top:14px; font-family:var(--font-mono); font-size:0.82rem; background:rgba(255,255,255,0.08); padding:8px 16px; border-radius:6px;">
                    Spatial AI Nodes: [Sofa: (0, 0.3, 0.5)] • [Table: (0, 0.2, 2.2)] • [Window: (0, 2.3, -3.9)]
                </div>
            </div>
        `;
        return;
    }

    try {
        scene3D = new THREE.Scene();
        scene3D.background = new THREE.Color(0x0f172a);

        const w = container.clientWidth || 900;
        const h = container.clientHeight || 500;

        camera3D = new THREE.PerspectiveCamera(45, w / h, 0.1, 1000);
        camera3D.position.set(9, 7, 10);

        renderer3D = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer3D.setSize(w, h);
        renderer3D.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer3D.shadowMap.enabled = true;
        container.appendChild(renderer3D.domElement);

        if (typeof THREE.OrbitControls !== "undefined") {
            controls3D = new THREE.OrbitControls(camera3D, renderer3D.domElement);
            controls3D.enableDamping = true;
            controls3D.dampingFactor = 0.05;
            controls3D.maxPolarAngle = Math.PI / 2 - 0.05;
        }

        // Lighting
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.65);
        scene3D.add(ambientLight);

        const directionalLight = new THREE.DirectionalLight(0xfff7ed, 1.25);
        directionalLight.position.set(6, 12, 8);
        directionalLight.castShadow = true;
        scene3D.add(directionalLight);

        // Build 3D Furniture & Room
        constructRoomMesh();

        // Render Loop
        const animate = () => {
            requestAnimationFrame(animate);
            if (isAutoRotating && roomMeshGroup) {
                roomMeshGroup.rotation.y += 0.005;
            }
            if (controls3D) controls3D.update();
            renderer3D.render(scene3D, camera3D);
        };
        animate();

        // Resize
        window.addEventListener('resize', () => {
            if (!container || !renderer3D || !camera3D) return;
            const newW = container.clientWidth;
            const newH = container.clientHeight;
            camera3D.aspect = newW / newH;
            camera3D.updateProjectionMatrix();
            renderer3D.setSize(newW, newH);
        });

    } catch (e) {
        console.warn("WebGL initialization note:", e);
    }
}

function constructRoomMesh() {
    if (roomMeshGroup) scene3D.remove(roomMeshGroup);
    roomMeshGroup = new THREE.Group();

    // Floor
    const floorGeo = new THREE.BoxGeometry(8, 0.2, 8);
    const floorMat = new THREE.MeshStandardMaterial({
        color: currentPaletteMode === 0 ? 0xc2a679 : 0x334155,
        roughness: 0.7
    });
    const floor = new THREE.Mesh(floorGeo, floorMat);
    floor.position.y = -0.1;
    floor.receiveShadow = true;
    roomMeshGroup.add(floor);

    // Walls
    const wallMat = new THREE.MeshStandardMaterial({ color: 0xf1f5f9, roughness: 0.9 });
    
    const wallBackGeo = new THREE.BoxGeometry(8, 4, 0.2);
    const wallBack = new THREE.Mesh(wallBackGeo, wallMat);
    wallBack.position.set(0, 1.9, -3.9);
    roomMeshGroup.add(wallBack);

    const wallLeftGeo = new THREE.BoxGeometry(0.2, 4, 8);
    const wallLeft = new THREE.Mesh(wallLeftGeo, wallMat);
    wallLeft.position.set(-3.9, 1.9, 0);
    roomMeshGroup.add(wallLeft);

    // Window Glass
    const winGeo = new THREE.BoxGeometry(3.2, 2.2, 0.25);
    const winMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, transparent: true, opacity: 0.45 });
    const winMesh = new THREE.Mesh(winGeo, winMat);
    winMesh.position.set(0, 2.3, -3.88);
    roomMeshGroup.add(winMesh);

    // Sofa
    const sofaBaseGeo = new THREE.BoxGeometry(3.6, 0.6, 1.6);
    const sofaMat = new THREE.MeshStandardMaterial({
        color: currentPaletteMode === 0 ? 0x64748b : 0xd97706,
        roughness: 0.6
    });
    const sofaBase = new THREE.Mesh(sofaBaseGeo, sofaMat);
    sofaBase.position.set(0, 0.3, 0.5);
    sofaBase.castShadow = true;
    roomMeshGroup.add(sofaBase);

    const sofaBackGeo = new THREE.BoxGeometry(3.6, 0.9, 0.5);
    const sofaBack = new THREE.Mesh(sofaBackGeo, sofaMat);
    sofaBack.position.set(0, 0.85, -0.1);
    roomMeshGroup.add(sofaBack);

    // Coffee Table
    const tableGeo = new THREE.CylinderGeometry(0.85, 0.85, 0.4, 24);
    const tableMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.3 });
    const table = new THREE.Mesh(tableGeo, tableMat);
    table.position.set(0, 0.2, 2.2);
    table.castShadow = true;
    roomMeshGroup.add(table);

    // Rug
    const rugGeo = new THREE.PlaneGeometry(4.4, 3.2);
    const rugMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, roughness: 0.9 });
    const rug = new THREE.Mesh(rugGeo, rugMat);
    rug.rotation.x = -Math.PI / 2;
    rug.position.set(0, 0.01, 1.4);
    roomMeshGroup.add(rug);

    // Smart Markers
    const markerGeo = new THREE.SphereGeometry(0.12, 16, 16);
    const markerMat = new THREE.MeshBasicMaterial({ color: 0x10b981 });
    
    const nodeSofa = new THREE.Mesh(markerGeo, markerMat);
    nodeSofa.position.set(1.4, 1.2, 0.6);
    roomMeshGroup.add(nodeSofa);

    const nodeTable = new THREE.Mesh(markerGeo, markerMat);
    nodeTable.position.set(0, 0.6, 2.2);
    roomMeshGroup.add(nodeTable);

    scene3D.add(roomMeshGroup);
}

function reset3DCamera() {
    if (camera3D && controls3D) {
        camera3D.position.set(9, 7, 10);
        controls3D.target.set(0, 1, 0);
        controls3D.update();
    }
    if (roomMeshGroup) roomMeshGroup.rotation.y = 0;
}

function toggle3DRotate() {
    isAutoRotating = !isAutoRotating;
    const btn = document.getElementById('btn-3d-rotate');
    if (btn) btn.innerText = isAutoRotating ? "Dừng Xoay" : "Bật Xoay Tự Động";
}

function toggle3DStyle() {
    currentPaletteMode = currentPaletteMode === 0 ? 1 : 0;
    constructRoomMesh();
}

/* --------------------------------------------------------------------------
   5. Automation ROI Calculator
   -------------------------------------------------------------------------- */
function updateROICalc() {
    const slider = document.getElementById('leads-slider');
    if (!slider) return;
    const leads = parseInt(slider.value, 10);
    
    const leadsVal = document.getElementById('leads-val');
    const hoursSaved = document.getElementById('hours-saved');
    const moneySaved = document.getElementById('money-saved');

    if (leadsVal) leadsVal.innerText = `${leads} leads`;

    // 1 lead tư vấn & bóc tách thủ công mất 2.5 giờ
    // Dùng AI Agent & Automation n8n giảm còn 0.5 giờ => Tiết kiệm 2.0 giờ / lead
    const hours = leads * 2.5;
    // Chi phí định mức nhân sự kỹ sư ~ 120.000 VNĐ/giờ
    const money = Math.round((hours * 120000) / 1000000);

    if (hoursSaved) hoursSaved.innerText = hours.toLocaleString('vi-VN');
    if (moneySaved) moneySaved.innerText = money.toLocaleString('vi-VN');
}

/* --------------------------------------------------------------------------
   6. Readiness Scorecard
   -------------------------------------------------------------------------- */
function updateScore() {
    const checkboxes = document.querySelectorAll('.score-checkbox:checked');
    const total = document.querySelectorAll('.score-checkbox').length || 15;
    const checkedCount = checkboxes.length;
    const pct = Math.round((checkedCount / total) * 100);

    const display = document.getElementById('score-display');
    const feedback = document.getElementById('readiness-feedback');

    if (display) {
        display.innerText = `${pct}% (${checkedCount}/${total})`;
        if (pct < 40) display.style.color = 'var(--data-red)';
        else if (pct < 80) display.style.color = 'var(--data-amber)';
        else display.style.color = 'var(--data-emerald)';
    }

    if (feedback) {
        if (pct < 40) {
            feedback.innerHTML = `⚠️ <strong>Mức độ khởi động (${pct}%):</strong> Bạn mới nắm được phần cơ bản. Cần đọc kỹ lại Module 01, 02 và 04 để củng cố nền tảng Software Engineering và Antigravity.`;
        } else if (pct < 80) {
            feedback.innerHTML = `📈 <strong>Mức độ khá (${pct}%):</strong> Bạn đã sẵn sàng cho 70% các câu hỏi kỹ thuật. Hãy luyện tập thêm 15 kịch bản phỏng vấn bên dưới để tự tin tuyệt đối.`;
        } else {
            feedback.innerHTML = `🔥 <strong>Sẵn sàng chinh phục (${pct}%):</strong> Bạn sở hữu tư duy hoàn hảo của một Builder/Doer thực thụ. Bạn sẵn sàng ghi điểm tuyệt đối trước ban giám đốc BAHA Homes!`;
        }
    }
}
