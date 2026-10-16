'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { ArrowLeft, BookOpen, Compass } from 'lucide-react';
import { LectureSection } from '../../types/lecture';

interface LectureSidebarProps {
  title: string;
  domainName: string;
  sections: LectureSection[];
}

export function LectureSidebar({ title, domainName, sections }: LectureSidebarProps) {
  const [activeId, setActiveId] = useState<string>('sec-intuition');
  const [scrollProgress, setScrollProgress] = useState<number>(0);

  useEffect(() => {
    const handleScroll = () => {
      // Calculate reading progress percentage
      const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
      if (totalHeight > 0) {
        const current = window.scrollY;
        setScrollProgress(Math.min(100, Math.max(0, Math.round((current / totalHeight) * 100))));
      }

      // ScrollSpy detection
      const sectionElements = sections
        .map(sec => document.getElementById(sec.id))
        .filter((el): el is HTMLElement => el !== null);

      const scrollPosition = window.scrollY + 160;

      for (let i = sectionElements.length - 1; i >= 0; i--) {
        const el = sectionElements[i];
        if (el.offsetTop <= scrollPosition) {
          setActiveId(el.id);
          break;
        }
      }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();
    return () => window.removeEventListener('scroll', handleScroll);
  }, [sections]);

  const scrollTo = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      const top = el.getBoundingClientRect().top + window.scrollY - 100;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  };

  return (
    <aside className="w-72 shrink-0 hidden lg:block">
      <div className="sticky top-8 flex flex-col gap-5">
        {/* Back to Graph Navigation */}
        <Link
          href="/"
          className="inline-flex items-center gap-2 px-4 py-2.5 rounded-[16px] bg-white border border-[#E9E9EE] shadow-sm text-[13px] font-semibold text-[#0B0B0F] hover:bg-[#F4F4F6] transition-all group"
        >
          <ArrowLeft className="w-4 h-4 text-[#6B6B76] group-hover:-translate-x-1 transition-transform" />
          <span>Về Đồ Thị Tri Thức</span>
        </Link>

        {/* Reading Progress Card */}
        <div className="bg-white rounded-[24px] border border-[#E9E9EE] p-5 shadow-[0_1px_2px_rgba(16,16,24,0.04)]">
          <div className="flex items-center justify-between text-[12px] font-medium text-[#6B6B76] mb-2">
            <span className="flex items-center gap-1.5">
              <BookOpen className="w-3.5 h-3.5 text-[#1F5FFF]" />
              Tiến độ bài học
            </span>
            <span className="font-mono text-[#0B0B0F] font-bold">{scrollProgress}%</span>
          </div>
          <div className="w-full h-1.5 bg-[#F4F4F6] rounded-full overflow-hidden">
            <div
              className="h-full bg-[#1F5FFF] rounded-full transition-all duration-150"
              style={{ width: `${scrollProgress}%` }}
            />
          </div>
        </div>

        {/* Outline / ScrollSpy Table of Contents */}
        <div className="bg-white rounded-[24px] border border-[#E9E9EE] p-5 shadow-[0_1px_2px_rgba(16,16,24,0.04)]">
          <div className="flex items-center gap-2 mb-4 pb-2 border-b border-[#EFEFF2]">
            <Compass className="w-4 h-4 text-[#6B6B76]" />
            <h4 className="text-[12px] font-bold text-[#6B6B76] uppercase tracking-wider">
              Mục Lục Sư Phạm
            </h4>
          </div>

          <nav className="flex flex-col gap-1.5">
            {sections.map(sec => {
              const isActive = activeId === sec.id;
              return (
                <button
                  key={sec.id}
                  onClick={() => scrollTo(sec.id)}
                  className={`text-left px-3 py-2 rounded-[10px] text-[13px] transition-all flex items-center justify-between ${
                    isActive
                      ? 'bg-[#1F5FFF]/10 text-[#1F5FFF] font-semibold translate-x-1'
                      : 'text-[#6B6B76] hover:text-[#0B0B0F] hover:bg-[#F4F4F6]'
                  }`}
                >
                  <span className="truncate">{sec.title}</span>
                  {isActive && (
                    <span className="w-1.5 h-1.5 rounded-full bg-[#1F5FFF] shrink-0" />
                  )}
                </button>
              );
            })}
          </nav>
        </div>
      </div>
    </aside>
  );
}
