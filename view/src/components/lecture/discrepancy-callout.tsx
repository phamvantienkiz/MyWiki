import React from 'react';

interface DiscrepancyCalloutProps {
  title?: string;
  children: React.ReactNode;
}

export function DiscrepancyCallout({
  title = 'MÂU THUẪN & SẮC THÁI GIỮA GIÁO TRÌNH HÀN LÂM VÀ THỰC TIỄN CÔNG NGHIỆP',
  children,
}: DiscrepancyCalloutProps) {
  return (
    <div className="my-6 rounded-[20px] bg-[#FEF2F2] border-l-[4px] border-[#EF4444] border border-[#FEE2E2] p-5 shadow-sm">
      <div className="flex items-center gap-2 mb-2">
        <span className="text-[18px]">⚖️</span>
        <h4 className="text-[12px] font-bold text-[#991B1B] uppercase tracking-wider">
          {title}
        </h4>
      </div>
      <div className="text-[14px] text-[#991B1B] leading-relaxed space-y-2">
        {children}
      </div>
    </div>
  );
}
