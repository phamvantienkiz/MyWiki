import React from 'react';
import { DomainId } from '../../types/wiki';
import { DOMAINS } from '../../lib/constants';

interface BadgeProps {
  domainId: DomainId;
  label?: string;
  className?: string;
}

export function Badge({ domainId, label, className = '' }: BadgeProps) {
  const domain = DOMAINS[domainId] || DOMAINS.genai;
  const text = label || domain.shortName;

  return (
    <span
      className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-[12px] font-medium transition-transform hover:scale-105 select-none ${className}`}
      style={{
        backgroundColor: domain.pastelBg,
        color: domain.textColor,
      }}
    >
      <span
        className="w-1.5 h-1.5 rounded-full"
        style={{ backgroundColor: domain.color }}
      />
      {text}
    </span>
  );
}
