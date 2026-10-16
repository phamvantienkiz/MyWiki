'use client';

import React from 'react';
import { Search, RotateCcw, ListFilter, Sparkles } from 'lucide-react';
import { DOMAINS } from '../../lib/constants';
import { DomainId } from '../../types/wiki';
import { IconButton } from '../ui/icon-button';

interface GraphControlsProps {
  searchQuery: string;
  onSearchChange: (query: string) => void;
  activeDomainId: DomainId | null;
  onDomainToggle: (id: DomainId | null) => void;
  onResetView: () => void;
  onToggleListView: () => void;
  isListViewOpen: boolean;
}

export function GraphControls({
  searchQuery,
  onSearchChange,
  activeDomainId,
  onDomainToggle,
  onResetView,
  onToggleListView,
  isListViewOpen,
}: GraphControlsProps) {
  const domainKeys = Object.keys(DOMAINS) as DomainId[];

  return (
    <div className="absolute top-4 left-4 right-4 z-10 flex flex-col sm:flex-row items-center justify-between gap-3 pointer-events-none">
      {/* Left: Brand Pill & Search Box */}
      <div className="flex items-center gap-2.5 pointer-events-auto bg-white/90 backdrop-blur-md px-3 py-2 rounded-[20px] border border-[#E9E9EE] shadow-[0_2px_12px_rgba(16,16,24,0.06)] w-full sm:w-auto">
        <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-[#111114] text-white text-[12px] font-bold shrink-0">
          <Sparkles className="w-3.5 h-3.5 text-[#1F5FFF]" />
          <span>AI Wiki Graph</span>
        </div>

        <div className="relative flex-1 sm:w-64">
          <Search className="w-3.5 h-3.5 text-[#9A9AA5] absolute left-2.5 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Tìm 48 khái niệm (e.g. lora, rag, cnn)..."
            value={searchQuery}
            onChange={e => onSearchChange(e.target.value)}
            className="w-full h-8 pl-8 pr-3 text-[13px] bg-transparent text-[#0B0B0F] placeholder-[#9A9AA5] focus:outline-none"
          />
        </div>
      </div>

      {/* Center: Domain Filter Pills */}
      <div className="hidden lg:flex items-center gap-1.5 pointer-events-auto bg-white/90 backdrop-blur-md px-3 py-2 rounded-[20px] border border-[#E9E9EE] shadow-[0_2px_12px_rgba(16,16,24,0.06)] overflow-x-auto max-w-[60vw]">
        <button
          onClick={() => onDomainToggle(null)}
          className={`px-3 py-1 rounded-full text-[12px] font-medium transition-all ${
            activeDomainId === null
              ? 'bg-[#111114] text-white shadow-sm'
              : 'text-[#6B6B76] hover:bg-[#F4F4F6]'
          }`}
        >
          Tất cả (48)
        </button>

        {domainKeys.map(key => {
          const dom = DOMAINS[key];
          const isActive = activeDomainId === key;
          return (
            <button
              key={key}
              onClick={() => onDomainToggle(isActive ? null : key)}
              className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[12px] font-medium transition-all select-none"
              style={{
                backgroundColor: isActive ? dom.color : dom.pastelBg,
                color: isActive ? '#FFFFFF' : dom.textColor,
                boxShadow: isActive ? '0 2px 8px rgba(0,0,0,0.15)' : 'none',
              }}
            >
              <span
                className="w-1.5 h-1.5 rounded-full"
                style={{ backgroundColor: isActive ? '#FFFFFF' : dom.color }}
              />
              {dom.shortName}
            </button>
          );
        })}
      </div>

      {/* Right: Reset & List View Toggle */}
      <div className="flex items-center gap-2 pointer-events-auto">
        <IconButton ariaLabel="Căn giữa lại đồ thị" onClick={onResetView}>
          <RotateCcw className="w-4 h-4 text-[#6B6B76]" />
        </IconButton>

        <button
          onClick={onToggleListView}
          className={`h-8 px-3.5 rounded-full text-[12px] font-semibold flex items-center gap-1.5 transition-all shadow-sm ${
            isListViewOpen
              ? 'bg-[#111114] text-white'
              : 'bg-white text-[#0B0B0F] border border-[#E9E9EE] hover:bg-[#F4F4F6]'
          }`}
        >
          <ListFilter className="w-3.5 h-3.5" />
          <span>Danh Sách Bài</span>
        </button>
      </div>
    </div>
  );
}
