import { notFound } from 'next/navigation';
import Link from 'next/link';
import { getAllEntities, getEntityBySlug } from '../../../lib/wiki';
import { parseLecture } from '../../../lib/lecture-parser';
import { DOMAINS } from '../../../lib/constants';
import { Badge } from '../../../components/ui/badge';
import { Card } from '../../../components/ui/card';
import { SymbolDictionary } from '../../../components/lecture/symbol-dictionary';
import { IntuitionCallout } from '../../../components/lecture/intuition-callout';
import { DiscrepancyCallout } from '../../../components/lecture/discrepancy-callout';
import { QAAccordion } from '../../../components/lecture/qa-accordion';
import { LectureSidebar } from '../../../components/lecture/lecture-sidebar';
import { FileText, ExternalLink, Link2, ArrowLeft } from 'lucide-react';

interface WikiPageProps {
  params: {
    slug: string;
  };
}

export async function generateStaticParams() {
  const entities = await getAllEntities();
  return entities.map(e => ({ slug: e.slug }));
}

export async function generateMetadata({ params }: WikiPageProps) {
  const entity = await getEntityBySlug(params.slug);
  if (!entity) return { title: 'Not Found' };
  return {
    title: `${entity.title} — AI Engineer Wiki`,
    description: entity.summary,
  };
}

export default async function WikiDetailPage({ params }: WikiPageProps) {
  const entity = await getEntityBySlug(params.slug);
  if (!entity) {
    notFound();
  }

  const lecture = parseLecture(entity);
  const domain = DOMAINS[entity.domainId];

  return (
    <div className="min-h-screen bg-[#F5F5F7] text-[#0B0B0F] py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto flex gap-8 items-start justify-center">
        {/* Sticky Sidebar Navigation with ScrollSpy */}
        <LectureSidebar
          title={lecture.title}
          domainName={domain.name}
          sections={lecture.sections}
        />

        {/* Main Lecture Content Container */}
        <main className="flex-1 max-w-4xl min-w-0 space-y-6">
          {/* Mobile Back Button */}
          <div className="lg:hidden">
            <Link
              href="/"
              className="inline-flex items-center gap-2 px-3.5 py-2 rounded-full bg-white border border-[#E9E9EE] shadow-sm text-[13px] font-semibold text-[#0B0B0F]"
            >
              <ArrowLeft className="w-4 h-4" />
              <span>Về Đồ Thị Tri Thức</span>
            </Link>
          </div>

          {/* Section 1: Hero & Trực Giác Bản Chất */}
          <Card id="sec-intuition" className="p-8">
            <div className="flex flex-wrap items-center gap-3 mb-4">
              <Badge domainId={entity.domainId} />
              <span className="text-[12px] text-[#6B6B76]">
                Độ dài: ~{entity.wordCount} từ · Thời gian đọc: ~{Math.ceil(entity.wordCount / 200)} phút
              </span>
            </div>

            <h1 className="text-[32px] sm:text-[36px] font-extrabold text-[#0B0B0F] tracking-tight leading-tight mb-4">
              {lecture.title}
            </h1>

            {/* Trực Giác Đời Thường (Intuition Before Notation) */}
            <div className="p-5 rounded-[20px] bg-[#F4F4F6] border border-[#EFEFF2]">
              <span className="text-[11px] font-bold text-[#6B6B76] uppercase tracking-wider block mb-2">
                💡 Trực Giác Bản Chất (Intuition Before Notation)
              </span>
              <p className="text-[16px] text-[#0B0B0F] leading-relaxed font-normal">
                {lecture.summary}
              </p>
            </div>
          </Card>

          {/* Section 2: Bảng Từ Điển Ký Hiệu 4 Cột */}
          <div id="sec-dictionary">
            <SymbolDictionary symbols={lecture.symbols} />
          </div>

          {/* Section 3: Định Nghĩa Chính Thống & Công Thức Toán Học */}
          <Card id="sec-definition" className="p-8">
            <div className="flex items-center gap-2 pb-3 border-b border-[#EFEFF2]">
              <span className="text-[20px]">📐</span>
              <h2 className="text-[20px] font-bold text-[#0B0B0F]">
                1. Định Nghĩa Chính Thống & Cơ Sở Toán Học
              </h2>
            </div>
            <div
              className="prose prose-slate max-w-none text-[15px] leading-relaxed text-[#333338]"
              dangerouslySetInnerHTML={{ __html: lecture.canonicalDefHtml }}
            />
          </Card>

          {/* Section 4: Cơ Chế Hoạt Động & Kiến Trúc */}
          <Card id="sec-mechanism" className="p-8">
            <div className="flex items-center gap-2 pb-3 border-b border-[#EFEFF2]">
              <span className="text-[20px]">⚙️</span>
              <h2 className="text-[20px] font-bold text-[#0B0B0F]">
                2. Cơ Chế Hoạt Động & Kiến Trúc Kỹ Nghệ
              </h2>
            </div>
            <div
              className="prose prose-slate max-w-none text-[15px] leading-relaxed text-[#333338]"
              dangerouslySetInnerHTML={{ __html: lecture.mechanismHtml }}
            />
          </Card>

          {/* Section 5: Hộp Thoại Góc Dành Cho Người Học Chậm */}
          <div id="sec-intuition-slow">
            <IntuitionCallout>
              <p className="font-medium">
                <strong>Bí quyết ghi nhớ bản chất của {lecture.title}:</strong> Đừng cố gắng ghi nhớ từng biến số phức tạp. Hãy hình dung cơ chế này như một quy trình chuyển dịch thông tin từ không gian dữ liệu thô sang một biểu diễn ngữ nghĩa cô đặc, nơi các đặc trưng quan trọng nhất được giữ lại và nhiễu loạn được triệt tiêu.
              </p>
            </IntuitionCallout>
          </div>

          {/* Section 6: Hộp Thoại Mâu Thuẫn & Sắc Thái Thực Chiến */}
          <div id="sec-discrepancies">
            <DiscrepancyCallout>
              <div
                className="prose prose-sm max-w-none text-[#991B1B]"
                dangerouslySetInnerHTML={{ __html: lecture.discrepanciesHtml }}
              />
            </DiscrepancyCallout>
          </div>

          {/* Section 7: Bộ Câu Hỏi Phỏng Vấn & Phản Biện Accordion */}
          <div id="sec-qa">
            <QAAccordion items={lecture.qaList} />
          </div>

          {/* Section 8: Mạng Lưới Tri Thức Hai Chiều & Nguồn Tài Liệu Gốc */}
          <div id="sec-network" className="grid grid-cols-1 md:grid-cols-2 gap-5 pt-2">
            {/* Outgoing & Backlinks Card */}
            <Card className="p-6">
              <div className="flex items-center gap-2 pb-2 border-b border-[#EFEFF2]">
                <Link2 className="w-4 h-4 text-[#1F5FFF]" />
                <h3 className="text-[14px] font-bold text-[#0B0B0F] uppercase tracking-wider">
                  Mạng Lưới Tri Thức Hai Chiều
                </h3>
              </div>

              <div className="space-y-4 pt-2">
                <div>
                  <span className="text-[12px] font-semibold text-[#6B6B76] block mb-2">
                    Khái niệm liên quan trỏ tới ({lecture.outgoingLinks.length}):
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {lecture.outgoingLinks.map(slug => (
                      <Link
                        key={slug}
                        href={`/wiki/${slug}`}
                        className="px-2.5 py-1 rounded-full bg-[#F4F4F6] hover:bg-[#E0E7FF] hover:text-[#1F5FFF] text-[#0B0B0F] text-[12px] font-medium border border-[#E9E9EE] transition-colors"
                      >
                        ✦ {slug.replace(/-/g, ' ')}
                      </Link>
                    ))}
                  </div>
                </div>

                <div>
                  <span className="text-[12px] font-semibold text-[#6B6B76] block mb-2">
                    Bài viết khác trích dẫn bài này ({lecture.backlinks.length}):
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {lecture.backlinks.length > 0 ? (
                      lecture.backlinks.map(slug => (
                        <Link
                          key={slug}
                          href={`/wiki/${slug}`}
                          className="px-2.5 py-1 rounded-full bg-emerald-50 hover:bg-emerald-100 text-emerald-800 text-[12px] font-medium border border-emerald-200 transition-colors"
                        >
                          ⮑ {slug.replace(/-/g, ' ')}
                        </Link>
                      ))
                    ) : (
                      <span className="text-[12px] text-[#9A9AA5] italic">Chưa có bài viết phụ thuộc.</span>
                    )}
                  </div>
                </div>
              </div>
            </Card>

            {/* Original Resources Card */}
            <Card className="p-6">
              <div className="flex items-center gap-2 pb-2 border-b border-[#EFEFF2]">
                <FileText className="w-4 h-4 text-[#FF8A1F]" />
                <h3 className="text-[14px] font-bold text-[#0B0B0F] uppercase tracking-wider">
                  Tài Liệu Gốc (Ground Truth)
                </h3>
              </div>

              <div className="space-y-2 pt-2">
                {lecture.resourceLinks.length > 0 ? (
                  lecture.resourceLinks.map((res, i) => (
                    <div
                      key={i}
                      className="p-3 rounded-[14px] bg-[#F9F9FB] border border-[#EFEFF2] flex items-center justify-between gap-3 text-[13px]"
                    >
                      <div className="flex items-center gap-2 truncate">
                        <span className="text-[14px]">
                          {res.sourceType === 'book' ? '📚' : res.sourceType === 'slide' ? '📑' : '🖼️'}
                        </span>
                        <span className="font-medium text-[#0B0B0F] truncate">{res.label}</span>
                      </div>
                      <span className="text-[11px] font-mono text-[#9A9AA5] shrink-0 uppercase px-2 py-0.5 bg-[#EFEFF2] rounded-md">
                        {res.sourceType}
                      </span>
                    </div>
                  ))
                ) : (
                  <span className="text-[12px] text-[#9A9AA5] italic">Tổng hợp từ các giáo trình nền tảng.</span>
                )}
              </div>
            </Card>
          </div>
        </main>
      </div>
    </div>
  );
}
