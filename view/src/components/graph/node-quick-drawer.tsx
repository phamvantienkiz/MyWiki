'use client';

import React from 'react';
import Link from 'next/link';
import { X, ArrowRight, Link2, BookOpen } from 'lucide-react';
import { GraphNode } from '../../types/graph';
import { Badge } from '../ui/badge';
import { IconButton } from '../ui/icon-button';

interface NodeQuickDrawerProps {
  node: GraphNode | null;
  onClose: () => void;
  onSelectRelatedNode: (slug: string) => void;
}

export function NodeQuickDrawer({ node, onClose, onSelectRelatedNode }: NodeQuickDrawerProps) {
  if (!node) return null;

  return (
    <div className="absolute top-4 right-4 bottom-4 w-96 max-w-[calc(100vw-32px)] bg-white/95 backdrop-blur-md rounded-[28px] border border-[#E9E9EE] shadow-[0_8px_32px_rgba(16,16,24,0.12)] p-6 z-20 flex flex-col justify-between transition-all animate-in slide-in-from-right-8 duration-200">
      <div className="space-y-5 overflow-y-auto pr-1">
        {/* Top Header */}
        <div className="flex items-start justify-between gap-3">
          <Badge domainId={node.domainId} />
          <IconButton ariaLabel="Đóng ngăn xem nhanh" onClick={onClose}>
            <X className="w-4 h-4 text-[#6B6B76]" />
          </IconButton>
        </div>

        {/* Title & Domain */}
        <div>
          <h2 className="text-[22px] font-bold text-[#0B0B0F] tracking-tight leading-snug">
            {node.name}
          </h2>
          <span className="text-[12px] text-[#6B6B76]">
            Miền: {node.domainName}
          </span>
        </div>

        {/* Connections Metric Row */}
        <div className="grid grid-cols-2 gap-3 p-3.5 rounded-[16px] bg-[#F4F4F6] border border-[#EFEFF2]">
          <div>
            <span className="text-[11px] text-[#6B6B76] block mb-0.5">Trích dẫn (In)</span>
            <span className="text-[20px] font-bold text-[#0B0B0F] font-mono">
              {node.inDegree}
            </span>
            <span className="text-[11px] text-[#9A9AA5] ml-1">bài viết</span>
          </div>
          <div>
            <span className="text-[11px] text-[#6B6B76] block mb-0.5">Liên kết (Out)</span>
            <span className="text-[20px] font-bold text-[#0B0B0F] font-mono">
              {node.outDegree}
            </span>
            <span className="text-[11px] text-[#9A9AA5] ml-1">khái niệm</span>
          </div>
        </div>

        {/* Summary Block */}
        <div>
          <div className="flex items-center gap-1.5 text-[12px] font-bold text-[#6B6B76] uppercase tracking-wider mb-2">
            <BookOpen className="w-3.5 h-3.5 text-[#1F5FFF]" />
            Tóm Tắt Trực Giác
          </div>
          <div className="p-4 rounded-[16px] bg-[#F9F9FB] border border-[#EFEFF2] text-[13.5px] text-[#333338] leading-relaxed">
            {node.summary || 'Khái niệm nền tảng trong hệ sinh thái kỹ thuật AI.'}
          </div>
        </div>
      </div>

      {/* Footer CTA Button */}
      <div className="pt-4 border-t border-[#EFEFF2] mt-4">
        <Link
          href={`/wiki/${node.id}`}
          className="w-full h-12 rounded-[14px] bg-[#111114] hover:bg-[#232328] active:scale-[0.98] text-white flex items-center justify-center gap-2 text-[14px] font-medium shadow-[0_4px_16px_rgba(16,16,24,0.2)] transition-all group"
        >
          <span>Đọc Toàn Bộ Bài Giảng</span>
          <ArrowRight className="w-4 h-4 text-white group-hover:translate-x-1 transition-transform" />
        </Link>
      </div>
    </div>
  );
}
