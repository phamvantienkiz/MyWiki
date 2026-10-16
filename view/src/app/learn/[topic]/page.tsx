import React from 'react';
import Link from 'next/link';
import { ArrowLeft, Sparkles, BookOpen } from 'lucide-react';
import { Card } from '../../../components/ui/card';
import { SymbolDictionary } from '../../../components/lecture/symbol-dictionary';
import { IntuitionCallout } from '../../../components/lecture/intuition-callout';
import { DiscrepancyCallout } from '../../../components/lecture/discrepancy-callout';
import { QAAccordion } from '../../../components/lecture/qa-accordion';

interface LearnPageProps {
  params: {
    topic: string;
  };
}

export default function CustomLearningPage({ params }: LearnPageProps) {
  const formattedTopic = params.topic.replace(/-/g, ' ').toUpperCase();

  return (
    <div className="min-h-screen bg-[#F5F5F7] text-[#0B0B0F] py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-4xl mx-auto space-y-6">
        {/* Navigation */}
        <div className="flex items-center justify-between">
          <Link
            href="/"
            className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white border border-[#E9E9EE] shadow-sm text-[13px] font-semibold text-[#0B0B0F] hover:bg-[#F4F4F6] transition-all"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Về Đồ Thị Tri Thức</span>
          </Link>

          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-purple-50 text-purple-700 text-[12px] font-semibold border border-purple-200">
            <Sparkles className="w-3.5 h-3.5" />
            Custom Learning Topic
          </span>
        </div>

        {/* Hero Card */}
        <Card className="p-8">
          <div className="text-[12px] font-bold text-[#6B6B76] uppercase tracking-wider mb-2">
            Chuyên Đề Học Tập Mở Rộng
          </div>
          <h1 className="text-[32px] font-extrabold text-[#0B0B0F] tracking-tight mb-4">
            {formattedTopic}
          </h1>
          <div className="p-5 rounded-[20px] bg-[#F4F4F6] border border-[#EFEFF2]">
            <span className="text-[11px] font-bold text-[#6B6B76] uppercase tracking-wider block mb-2">
              💡 Khung Sư Phạm Cho Người Học Chậm (First Principles)
            </span>
            <p className="text-[15px] text-[#333338] leading-relaxed">
              Trang này được thiết kế sẵn sàng để tiếp nhận chuyên đề học tập chuyên sâu theo yêu cầu của bạn. Mọi bài học mới sẽ tự động được định dạng chuẩn <code>lecture-visualizer</code> với Bảng từ điển ký hiệu 4 cột, KaTeX toán học, hộp thoại trực giác 🌱 và bộ câu hỏi phản biện.
            </p>
          </div>
        </Card>

        {/* Template Elements Preview */}
        <SymbolDictionary
          symbols={[
            {
              symbol: 'X \\in \\mathbb{R}^{n \\times d}',
              enName: 'Input Feature Space',
              viName: 'Không gian dữ liệu đầu vào',
              intuition: 'Bảng số liệu thô thu thập từ thế giới thực trước khi đưa vào mô hình.',
            },
            {
              symbol: 'f_\\theta(X)',
              enName: 'Parametric Hypothesis',
              viName: 'Hàm ánh xạ tham số',
              intuition: 'Công thức biến đổi để dự đoán nhãn từ dữ liệu đầu vào.',
            },
          ]}
        />

        <IntuitionCallout title="BÍ QUYẾT TIẾP CẬN CHUYÊN ĐỀ MỚI">
          <p>
            Khi yêu cầu AI Agent tạo bài học cho chuyên đề này, hệ thống sẽ tự động bóc tách tài liệu bài giảng/giáo trình bạn cung cấp thành các bước số học chi tiết, giải thích cặn kẽ từng ký hiệu và liên kết ngay vào Đồ thị Tri thức trung tâm.
          </p>
        </IntuitionCallout>
      </div>
    </div>
  );
}
