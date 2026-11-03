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

function parseTables(text: string): string {
  // Replace Markdown tables with styled HTML tables
  return text.replace(
    /(?:^|\n)(\|.+?\|\n\|[-: |]+\|\n(?:\|.+?\|\n?)+)/g,
    (match) => {
      const lines = match.trim().split('\n');
      if (lines.length < 2) return match;

      const headerCells = lines[0]
        .split('|')
        .slice(1, -1)
        .map(c => c.trim());

      const bodyRows = lines.slice(2);

      let tableHtml = '<div class="my-5 overflow-x-auto rounded-[14px] border border-[#E9E9EE] bg-white shadow-sm">';
      tableHtml += '<table class="w-full text-left text-[14px] border-collapse">';
      tableHtml += '<thead class="bg-[#F4F4F6] text-[#0B0B0F] border-b border-[#E9E9EE] font-semibold"><tr>';
      for (const h of headerCells) {
        tableHtml += `<th class="py-3 px-4 whitespace-nowrap">${h}</th>`;
      }
      tableHtml += '</tr></thead>';

      tableHtml += '<tbody class="divide-y divide-[#EFEFF2] text-[#333338]">';
      for (const row of bodyRows) {
        if (!row.includes('|')) continue;
        const cells = row.split('|').slice(1, -1).map(c => c.trim());
        tableHtml += '<tr class="hover:bg-[#F9F9FB] transition-colors">';
        for (const cell of cells) {
          tableHtml += `<td class="py-2.5 px-4">${cell}</td>`;
        }
        tableHtml += '</tr>';
      }
      tableHtml += '</tbody></table></div>';
      return '\n\n' + tableHtml + '\n\n';
    }
  );
}

function markdownToHtml(md: string): string {
  let html = md;

  // Math first to protect symbols
  html = renderMath(html);
  // Wiki-links
  html = renderWikiLinks(html);
  // Markdown Tables
  html = parseTables(html);

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

  // GitHub Alert callouts: > [!NOTE], > [!TIP], > [!IMPORTANT], > [!WARNING], > [!CRITICAL]
  html = html.replace(/^\>\s*\[\!(NOTE|TIP|IMPORTANT|WARNING|CRITICAL|CAUTION)\]\s*(.*$)/gim, (_, type, rest) => {
    const t = type.toUpperCase();
    const borderCol = t === 'CRITICAL' || t === 'WARNING' || t === 'CAUTION' ? 'border-amber-500 bg-amber-50/60 text-amber-900' : 'border-[#1F5FFF] bg-[#F4F4F6] text-[#0B0B0F]';
    return `<div class="my-3 border-l-4 ${borderCol} p-3 rounded-r-[10px] text-[14px] font-medium"><span class="font-bold uppercase text-[11px] block tracking-wider mb-1">${t}</span>${rest}`;
  });

  // Generic Blockquotes
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

  // 1. Dynamic extraction of all body sections
  const rawSections = content.split(/\n(?=##\s+)/);
  const contentSections: { id: string; title: string; level: number; html: string }[] = [];

  for (let idx = 0; idx < rawSections.length; idx++) {
    const sec = rawSections[idx];
    const match = sec.match(/^##\s+(.+)$/m);
    if (!match) continue;
    const rawHeading = match[1].trim();

    // Exclude summary (rendered in Hero) and Wiki links (rendered in Section 8)
    if (/tóm tắt/i.test(rawHeading) || /mạng lưới liên kết|wiki links/i.test(rawHeading)) {
      continue;
    }

    const secBody = sec.replace(/^##\s+.+$/m, '').trim();
    // Generate clean URL/DOM safe ID
    const cleanId = 'sec-body-' + idx + '-' + rawHeading.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    
    contentSections.push({
      id: cleanId,
      title: rawHeading,
      level: 2,
      html: markdownToHtml(secBody),
    });
  }

  // 2. Build Sidebar Sections for ScrollSpy
  const sections: LectureSection[] = [
    { id: 'sec-intuition', title: 'Trực Giác Bản Chất', level: 2 },
    { id: 'sec-dictionary', title: 'Từ Điển Ký Hiệu & Khái Niệm', level: 2 },
    ...contentSections.map(cs => ({ id: cs.id, title: cs.title, level: cs.level })),
    { id: 'sec-intuition-slow', title: 'Góc Cho Người Học Chậm', level: 2 },
    { id: 'sec-qa', title: 'Câu Hỏi Phỏng Vấn & Phản Biện', level: 2 },
    { id: 'sec-network', title: 'Mạng Lưới Tri Thức & Tài Liệu Gốc', level: 2 },
  ];

  // 3. Fallback extraction for compatibility
  let canonicalDefHtml = contentSections[0]?.html || '';
  let mechanismHtml = contentSections[1]?.html || '';
  let discrepanciesHtml = '';
  const discMatch = content.match(/##\s+(?:\d+\.\s+)?(?:So sánh|Mâu thuẫn)[^\n]*\n([\s\S]*?)(?=##|\n#|$)/i);
  if (discMatch) {
    discrepanciesHtml = markdownToHtml(discMatch[1].trim());
  }

  // 4. Extract Questions for QAAccordion
  const qaList: QAItem[] = [];
  const qMatches = content.match(/(?:Câu hỏi phỏng vấn|Q:|Hỏi:)\s*([^\n\?]+\?)([\s\S]*?)(?=(?:Câu hỏi|Q:|Hỏi:)|##|$)/gi);
  if (qMatches) {
    for (const qBlock of qMatches) {
      const parts = qBlock.split('\n');
      const question = parts[0].replace(/^(?:Câu hỏi phỏng vấn\s*\d*:?|Q:|Hỏi:)\s*/i, '').replace(/^\*+|\*+$/g, '').trim();
      const answer = parts.slice(1).join('\n').trim();
      if (question) {
        qaList.push({
          question,
          answer: markdownToHtml(answer || 'Xem chi tiết trong mục phân tích thực chiến.'),
        });
      }
    }
  }

  // Fallback QA if not extracted specifically
  if (qaList.length === 0) {
    qaList.push({
      question: `Trọng tâm phỏng vấn Senior AI về ${entity.title} là gì?`,
      answer: markdownToHtml(`Khi phỏng vấn về ${entity.title}, các câu hỏi trọng tâm bao gồm: (1) Bản chất toán học và kiến trúc hệ thống nền tảng; (2) Các đánh đổi kỹ thuật (Trade-offs) trong triển khai thực tế; (3) Cách thiết kế bộ rào chắn an toàn (Guardrails) và xử lý lỗi hệ thống khi vận hành production.`),
    });
  }

  // 5. Pedagogical Symbol Dictionary
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
    practicalHtml: '',
    contentSections,
    symbols,
    qaList,
    sections,
    outgoingLinks: entity.outgoingLinks,
    backlinks: entity.backlinks,
    resourceLinks: entity.resourceLinks,
  };
}
