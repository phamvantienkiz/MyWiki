import React from 'react';
import { ChevronRight } from 'lucide-react';

interface GhostButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  label: string;
  icon?: React.ReactNode;
}

export function GhostButton({ label, icon, className = '', ...props }: GhostButtonProps) {
  return (
    <button
      className={`w-full h-11 px-4 rounded-[12px] bg-[#F4F4F6] hover:bg-[#ECECEF] text-[#0B0B0F] flex items-center justify-between text-[13px] font-medium transition-colors group focus:outline-none focus:ring-2 focus:ring-[#1F5FFF] focus:ring-offset-2 ${className}`}
      {...props}
    >
      <span className="flex items-center gap-2 truncate">
        {icon}
        <span className="truncate">{label}</span>
      </span>
      <ChevronRight className="w-4 h-4 text-[#6B6B76] group-hover:translate-x-0.5 transition-transform shrink-0" />
    </button>
  );
}
