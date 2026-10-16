'use client';

import React, { useState } from 'react';
import { ChevronDown } from 'lucide-react';
import { QAItem } from '../../types/lecture';

interface QAAccordionProps {
  items: QAItem[];
}

export function QAAccordion({ items }: QAAccordionProps) {
  const [openIndices, setOpenIndices] = useState<number[]>([0]); // Mở câu đầu tiên mặc định

  if (!items || items.length === 0) return null;

  const toggle = (idx: number) => {
    setOpenIndices(prev =>
      prev.includes(idx) ? prev.filter(i => i !== idx) : [...prev, idx]
    );
  };

  return (
    <div className="space-y-3 my-6">
      <div className="flex items-center gap-2 mb-3">
        <span className="text-[18px]">🎯</span>
        <h3 className="text-[15px] font-semibold text-[#0B0B0F] uppercase tracking-wider">
          Góc Phỏng Vấn Kỹ Sư & Phản Biện Chuyên Sâu
        </h3>
      </div>

      {items.map((item, idx) => {
        const isOpen = openIndices.includes(idx);
        return (
          <div
            key={idx}
            className="rounded-[16px] bg-white border border-[#E9E9EE] overflow-hidden shadow-[0_1px_2px_rgba(16,16,24,0.04)] transition-all"
          >
            <button
              onClick={() => toggle(idx)}
              className="w-full px-5 py-4 flex items-center justify-between text-left hover:bg-[#F4F4F6]/50 transition-colors"
            >
              <div className="flex items-center gap-3 pr-4">
                <span className="w-6 h-6 rounded-full bg-[#111114] text-white flex items-center justify-center text-[11px] font-bold shrink-0">
                  Q{idx + 1}
                </span>
                <span className="text-[14px] font-semibold text-[#0B0B0F]">
                  {item.question}
                </span>
              </div>
              <ChevronDown
                className={`w-4 h-4 text-[#6B6B76] shrink-0 transition-transform duration-200 ${
                  isOpen ? 'rotate-180' : ''
                }`}
              />
            </button>

            {isOpen && (
              <div className="px-5 pb-5 pt-2 text-[14px] text-[#333338] border-t border-[#EFEFF2] bg-[#FBFBFC] leading-relaxed">
                <div
                  className="prose prose-sm max-w-none"
                  dangerouslySetInnerHTML={{ __html: item.answer }}
                />
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}
