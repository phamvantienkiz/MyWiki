import React from 'react';
import { clsx, type ClassValue } from 'clsx';
import { twMerge } from 'tailwind-merge';

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

interface CardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
  className?: string;
}

export function Card({ children, className, ...props }: CardProps) {
  return (
    <div
      className={cn(
        "bg-white rounded-[28px] border border-[#E9E9EE] p-6 shadow-[0_1px_2px_rgba(16,16,24,0.04),0_8px_24px_rgba(16,16,24,0.06)] flex flex-col gap-5 transition-shadow hover:shadow-[0_2px_4px_rgba(16,16,24,0.06),0_12px_32px_rgba(16,16,24,0.08)]",
        className
      )}
      {...props}
    >
      {children}
    </div>
  );
}
