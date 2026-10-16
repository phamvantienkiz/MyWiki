'use client';

import React from 'react';
import Link from 'next/link';
import { X, ArrowRight, ExternalLink } from 'lucide-react';
import { EntityMetadata, DomainId } from '../../types/wiki';
import { DOMAINS } from '../../lib/constants';
import { Badge } from '../ui/badge';
import { IconButton } from '../ui/icon-button';

interface DocumentsListModalProps {
  isOpen: boolean;
  onClose: () => void;
  entities: EntityMetadata[];
  onSelectEntity: (slug: string) => void;
}

export function DocumentsListModal({
  isOpen,
  onClose,
  entities,
  onSelectEntity,
}: DocumentsListModalProps) {
  if (!isOpen) return null;

  // Group by domain
  const domainGroups: Record<DomainId, EntityMetadata[]> = {
    genai: [],
    rag: [],
    agentic: [],
    deeplearning: [],
    mlmath: [],
    mlops: [],
    software: [],
  };

  entities.forEach(e => {
    if (domainGroups[e.domainId]) {
      domainGroups[e.domainId].push(e);
    }
  });

  const domainKeys = Object.keys(domainGroups) as DomainId[];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/30 backdrop-blur-sm animate-in fade-in duration-200">
      <div className="w-full max-w-4xl max-h-[85vh] bg-white rounded-[28px] border border-[#E9E9EE] shadow-[0_16px_48px_rgba(16,16,24,0.16)] flex flex-col overflow-hidden">
        {/* Header */}
        <div className="px-6 py-5 border-b border-[#EFEFF2] flex items-center justify-between">
          <div>
            <h2 className="text-[18px] font-bold text-[#0B0B0F]">
              Danh Mục Toàn Bộ 48 Khái Niệm AI Engineer Wiki
            </h2>
            <p className="text-[13px] text-[#6B6B76]">
              Chọn bài viết để mở bài giảng chi tiết hoặc định vị trên đồ thị.
            </p>
          </div>
          <IconButton ariaLabel="Đóng danh mục" onClick={onClose}>
            <X className="w-4 h-4 text-[#6B6B76]" />
          </IconButton>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          {domainKeys.map(key => {
            const dom = DOMAINS[key];
            const list = domainGroups[key];
            if (list.length === 0) return null;

            return (
              <div key={key} className="space-y-3">
                <div className="flex items-center gap-2">
                  <Badge domainId={key} />
                  <span className="text-[12px] text-[#9A9AA5]">({list.length} bài)</span>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {list.map(item => (
                    <div
                      key={item.slug}
                      className="p-4 rounded-[16px] bg-[#F9F9FB] border border-[#EFEFF2] hover:border-[#1F5FFF]/30 hover:bg-white transition-all flex items-start justify-between gap-3 group"
                    >
                      <div className="flex-1 min-w-0">
                        <Link
                          href={`/wiki/${item.slug}`}
                          className="text-[14px] font-semibold text-[#0B0B0F] group-hover:text-[#1F5FFF] transition-colors block truncate"
                        >
                          {item.title}
                        </Link>
                        <p className="text-[12px] text-[#6B6B76] line-clamp-1 mt-0.5">
                          {item.summary}
                        </p>
                      </div>

                      <div className="flex items-center gap-1 shrink-0">
                        <button
                          onClick={() => {
                            onClose();
                            onSelectEntity(item.slug);
                          }}
                          title="Định vị trên đồ thị"
                          className="p-1.5 rounded-full hover:bg-[#EFEFF2] text-[#6B6B76] text-[11px]"
                        >
                          📍
                        </button>
                        <Link
                          href={`/wiki/${item.slug}`}
                          className="p-1.5 rounded-full hover:bg-[#111114] hover:text-white text-[#6B6B76] transition-colors"
                        >
                          <ExternalLink className="w-3.5 h-3.5" />
                        </Link>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}
