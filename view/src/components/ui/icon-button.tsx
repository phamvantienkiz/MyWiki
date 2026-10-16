import React from 'react';

interface IconButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  ariaLabel: string;
}

export function IconButton({ children, ariaLabel, className = '', ...props }: IconButtonProps) {
  return (
    <button
      aria-label={ariaLabel}
      className={`relative inline-flex items-center justify-center w-8 h-8 rounded-full bg-white text-[#0B0B0F] border border-[#E9E9EE] shadow-[0_1px_2px_rgba(16,16,24,0.08),0_0_0_1px_rgba(16,16,24,0.04)] hover:bg-[#F4F4F6] active:scale-95 transition-all focus:outline-none focus:ring-2 focus:ring-[#1F5FFF] focus:ring-offset-2 ${className}`}
      {...props}
    >
      {/* 44px invisible touch target for mobile a11y */}
      <span className="absolute -inset-1.5" aria-hidden="true" />
      {children}
    </button>
  );
}
