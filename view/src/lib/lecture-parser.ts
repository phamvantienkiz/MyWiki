import katex from 'katex';
import { ParsedLecture, SymbolItem, QAItem, LectureSection } from '../types/lecture';
import { EntityMetadata } from '../types/wiki';
import { DOMAINS } from './constants';

function renderMath(text: string): string {
  // Replace block math $$...$$
  let processed = text.replace(/\$\$([\s\S]+?)\$\$/g, (_, math) => {
    try {
      return `<div class="katex-display my-4 p-3 bg-[#F4F4F6] rounded-[12px] overflow-x-auto text-center">${katex.renderToString(math.trim(), { displayMode: true, throwOnError: false })}</div>`;
    } catch {
      return `<div class="p-2 bg-red-50 text-red-700 font-mono text-sm">${math}</div>`;
    }
  });

  // Replace inline math $...$
  processed = processed.replace(/\$([^\$\n]+?)\$/g, (_, math) => {
    try {
      return katex.renderToString(math.trim(), { displayMode: false, throwOnError: false });
    } catch {
      return `$${math}$`;
    }
  });

  return processed;
}

function renderWikiLinks(text: string): string {
  return text.replace(/\[\[([a-zA-Z0-9_-]+)(?:\|([^\]]+))?\]\]/g, (_, slug, label) => {
    const displayText = label || slug.replace(/-/g, ' ');
    return `<a href="/wiki/${slug.toLowerCase()}" class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full bg-[#EFEFF2] hover:bg-[#E0E7FF] text-[#0B0B0F] hover:text-[#1F5FFF] font-medium text-[13px] border border-[#E9E9EE] transition-all">✦ ${displayText}</a>`;
  });
}

function markdownToHtml(md: string): string {
  let html = md;

  // Math first to protect symbols
  html = renderMath(html);
  // Wiki-links
  html = renderWikiLinks(html);

  // Headers
  html = html.replace(/^### (.*$)/gim, '<h3 class="text-[17px] font-semibold text-[#0B0B0F] mt-5 mb-2">$1</h3>');
  html = html.replace(/^## (.*$)/gim, '<h2 class="text-[20px] font-semibold text-[#0B0B0F] mt-6 mb-3 pb-2 border-b border-[#EFEFF2]">$1</h2>');

  // Bold & Italic
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong class="font-semibold text-[#0B0B0F]">$1</strong>');
  html = html.replace(/\*(.*?)\*/g, '<em class="italic text-[#6B6B76]">$1</em>');

  // Code blocks ```lang ... ```
  html = html.replace(/```([a-z]*)\n([\s\S]*?)```/gim, (_, lang, code) => {
    return `<div class="my-4 rounded-[16px] bg-[#111114] text-[#F5F5F7] p-4 text-[13px] font-mono overflow-x-auto shadow-sm">
      <div class="text-[11px] text-[#9A9AA5] mb-2 uppercase tracking-wider font-semibold border-b border-white/10 pb-1">${lang || 'code'}</div>
      <pre><code>${code.trim()}</code></pre>
    </div>`;
  });

  // Inline code `code`
  html = html.replace(/`([^`]+)`/g, '<code class="px-1.5 py-0.5 rounded-[6px] bg-[#F4F4F6] text-[#0B0B0F] font-mono text-[13px] border border-[#EFEFF2]">$1</code>');

  // Blockquotes / Callouts
  html = html.replace(/^\> (.*$)/gim, '<blockquote class="border-l-2 border-[#1F5FFF] pl-4 py-1 my-3 text-[#6B6B76] bg-[#F4F4F6]/50 rounded-r-[8px] italic">$1</blockquote>');

  // Unordered lists
  html = html.replace(/^\- (.*$)/gim, '<li class="ml-4 list-disc text-[#6B6B76] text-[15px] leading-relaxed my-1">$1</li>');

  // Ordered lists
  html = html.replace(/^\d+\. (.*$)/gim, '<li class="ml-4 list-decimal text-[#6B6B76] text-[15px] leading-relaxed my-1">$1</li>');

  // Paragraphs
  html = html.split('\n\n').map(para => {
    if (para.startsWith('<h') || para.startsWith('<div') || para.startsWith('<li') || para.startsWith('<blockquote') || para.startsWith('<table')) {
      return para;
    }
    return `<p class="text-[15px] text-[#333338] leading-relaxed mb-4">${para.trim()}</p>`;
  }).join('\n');

  return html;
}

export function parseLecture(entity: EntityMetadata): ParsedLecture {
  const content = entity.contentRaw;
  const domain = DOMAINS[entity.domainId];

  // 1. Extract Sections for ScrollSpy
  const sections: LectureSection[] = [
    { id: 'sec-intuition', title: 'Trực Giác Bản Chất', level: 2 },
    { id: 'sec-dictionary', title: 'Từ Điển Ký Hiệu & Khái Niệm', level: 2 },
    { id: 'sec-definition', title: 'Định Nghĩa Chính Thống & Toán Học', level: 2 },
    { id: 'sec-mechanism', title: 'Cơ Chế Kiến Trúc & Sơ Đồ', level: 2 },
    { id: 'sec-intuition-slow', title: 'Góc Dành Cho Người Học Chậm', level: 2 },
    { id: 'sec-discrepancies', title: 'Mâu Thuẫn & Sắc Thái Thực Chiến', level: 2 },
    { id: 'sec-qa', title: 'Câu Hỏi Phỏng Vấn & Phản Biện', level: 2 },
    { id: 'sec-network', title: 'Mạng Lưới Tri Thức & Tài Liệu Gốc', level: 2 },
  ];

  // 2. Extract Canonical Definition
  let canonicalDefHtml = '';
  const canonMatch = content.match(/##\s+1\.\s+Định nghĩa Chính thống\s+([\s\S]*?)(?=##|\n#|$)/i);
  if (canonMatch) {
    canonicalDefHtml = markdownToHtml(canonMatch[1].trim());
  }

  // 3. Extract Mechanism
  let mechanismHtml = '';
  const mechMatch = content.match(/##\s+2\.\s+Cơ chế Hoạt động & Kiến trúc\s+([\s\S]*?)(?=##|\n#|$)/i);
  if (mechMatch) {
    mechanismHtml = markdownToHtml(mechMatch[1].trim());
  }

  // 4. Extract Discrepancies
  let discrepanciesHtml = '';
  const discMatch = content.match(/##\s+3\.\s+So sánh, Mâu thuẫn & Sắc thái\s+([\s\S]*?)(?=##|\n#|$)/i);
  if (discMatch) {
    discrepanciesHtml = markdownToHtml(discMatch[1].trim());
  }

  // 5. Extract Practical & Questions
  let practicalHtml = '';
  const qaList: QAItem[] = [];
  const pracMatch = content.match(/##\s+4\.\s+Góc nhìn Thực chiến & Phỏng vấn\s+([\s\S]*?)(?=##|\n#|$)/i);
  if (pracMatch) {
    const rawPrac = pracMatch[1].trim();
    practicalHtml = markdownToHtml(rawPrac);

    // Extract questions starting with "Câu hỏi phỏng vấn" or "Q:" or bold questions
    const qMatches = rawPrac.match(/(?:Câu hỏi phỏng vấn|Q:|Hỏi:)\s*([^\n\?]+\?)([\s\S]*?)(?=(?:Câu hỏi|Q:|Hỏi:)|$)/gi);
    if (qMatches) {
      for (const qBlock of qMatches) {
        const parts = qBlock.split('\n');
        const question = parts[0].replace(/^(?:Câu hỏi phỏng vấn\s*\d*:?|Q:|Hỏi:)\s*/i, '').trim();
        const answer = parts.slice(1).join('\n').trim();
        if (question) {
          qaList.push({
            question,
            answer: markdownToHtml(answer || 'Xem chi tiết trong mục phân tích thực chiến.'),
          });
        }
      }
    }
  }

  // Fallback QA if not extracted specifically
  if (qaList.length === 0) {
    qaList.push({
      question: `Trọng tâm phỏng vấn Senior AI về ${entity.title} là gì?`,
      answer: markdownToHtml(`Khi phỏng vấn về ${entity.title}, các câu hỏi sẽ xoay quanh: (1) Bản chất toán học/kiến trúc nền tảng; (2) Các đánh đổi (Trade-offs) trong triển khai thực tế; (3) Cách phát hiện và khắc phục các Failure Modes điển hình.`),
    });
  }

  // 6. Generate Pedagogical Symbol Dictionary (Bảng từ điển ký hiệu 4 cột)
  const symbols: SymbolItem[] = [
    {
      symbol: '\\mathcal{M}',
      enName: 'Model Architecture',
      viName: 'Kiến trúc mô hình',
      intuition: 'Bộ khung thuật toán và các tham số biến đổi dòng thông tin.'
    },
    {
      symbol: '\\theta, \\mathbf{W}',
      enName: 'Weights & Parameters',
      viName: 'Trọng số học tập',
      intuition: 'Độ nhạy và tri thức tích lũy sau quá trình huấn luyện dữ liệu.'
    },
    {
      symbol: '\\mathcal{L}(\\theta)',
      enName: 'Loss Function',
      viName: 'Hàm mất mát',
      intuition: 'Thước đo mức độ sai lệch giữa dự đoán và thực tế cần tối thiểu hóa.'
    },
    {
      symbol: '\\nabla_\\theta \\mathcal{L}',
      enName: 'Gradient Vector',
      viName: 'Vectơ độ dốc Gradient',
      intuition: 'Kim chỉ nam chỉ hướng đi để điều chỉnh trọng số tốt hơn qua từng bước.'
    }
  ];

  return {
    slug: entity.slug,
    title: entity.title,
    domainId: entity.domainId,
    domainName: domain.name,
    summary: entity.summary,
    canonicalDefHtml,
    mechanismHtml,
    discrepanciesHtml,
    practicalHtml,
    symbols,
    qaList,
    sections,
    outgoingLinks: entity.outgoingLinks,
    backlinks: entity.backlinks,
    resourceLinks: entity.resourceLinks,
  };
}
