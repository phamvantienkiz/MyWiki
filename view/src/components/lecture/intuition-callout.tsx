import React from 'react';

interface IntuitionCalloutProps {
  title?: string;
  children: React.ReactNode;
}

export function IntuitionCallout({
  title = 'GÓC DÀNH CHO NGƯỜI HỌC CHẬM — HIỂU BẢN CHẤT NGUYÊN LÝ',
  children,
}: IntuitionCalloutProps) {
  return (
    <div className="my-6 rounded-[20px] bg-[#F0FDF4] border-l-[4px] border-[#22C55E] border border-[#DCFCE7] p-5 shadow-sm">
      <div className="flex items-center gap-2 mb-2">
        <span className="text-[18px]">🌱</span>
        <h4 className="text-[12px] font-bold text-[#15803D] uppercase tracking-wider">
          {title}
        </h4>
      </div>
      <div className="text-[14px] text-[#166534] leading-relaxed space-y-2">
        {children}
      </div>
    </div>
  );
}
