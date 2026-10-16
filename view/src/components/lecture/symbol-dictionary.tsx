'use client';

import React from 'react';
import katex from 'katex';
import { SymbolItem } from '../../types/lecture';

interface SymbolDictionaryProps {
  symbols: SymbolItem[];
}

export function SymbolDictionary({ symbols }: SymbolDictionaryProps) {
  if (!symbols || symbols.length === 0) return null;

  return (
    <div className="rounded-[20px] bg-[#F4F4F6] border border-[#E9E9EE] p-5 my-6">
      <div className="flex items-center gap-2 mb-4">
        <span className="text-[18px]">📖</span>
        <h3 className="text-[15px] font-semibold text-[#0B0B0F] uppercase tracking-wider">
          Bảng Từ Điển Ký Hiệu & Khái Niệm Đối Chiếu (4 Cột)
        </h3>
      </div>
      <p className="text-[13px] text-[#6B6B76] mb-4">
        Giúp người học chậm đối chiếu tức thời giữa ký hiệu toán học hàn lâm, thuật ngữ chuyên ngành và ý nghĩa đời thường.
      </p>

      <div className="overflow-x-auto">
        <table className="w-full text-left border-collapse text-[13px]">
          <thead>
            <tr className="border-b border-[#E0E0E6] text-[#6B6B76] font-medium">
              <th className="py-2.5 px-3">Ký Hiệu Toán Học</th>
              <th className="py-2.5 px-3">Tên Tiếng Anh Chuẩn</th>
              <th className="py-2.5 px-3">Tên Tiếng Việt</th>
              <th className="py-2.5 px-3">Nghĩa Đời Thường Trực Giác</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-[#EAEAEF]">
            {symbols.map((item, idx) => {
              let renderedSymbol = item.symbol;
              try {
                renderedSymbol = katex.renderToString(item.symbol, { displayMode: false, throwOnError: false });
              } catch {
                renderedSymbol = item.symbol;
              }

              return (
                <tr key={idx} className="hover:bg-white/60 transition-colors">
                  <td
                    className="py-3 px-3 font-mono font-medium text-[#0B0B0F]"
                    dangerouslySetInnerHTML={{ __html: renderedSymbol }}
                  />
                  <td className="py-3 px-3 font-semibold text-[#111114]">
                    {item.enName}
                  </td>
                  <td className="py-3 px-3 text-[#333338]">
                    {item.viName}
                  </td>
                  <td className="py-3 px-3 text-[#166534] bg-emerald-50/50 rounded-[8px] font-medium">
                    {item.intuition}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
