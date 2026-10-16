import { DomainId, ResourceLink } from './wiki';

export interface SymbolItem {
  symbol: string;       // LaTeX symbol, e.g. "W_Q, W_K, W_V"
  enName: string;       // e.g. "Query, Key, Value Projections"
  viName: string;       // e.g. "Các ma trận biến đổi không gian"
  intuition: string;    // e.g. "Các bộ lọc trích xuất góc nhìn tìm kiếm, đặc điểm và thông điệp"
}

export interface QAItem {
  question: string;
  answer: string;
}

export interface LectureSection {
  id: string;
  title: string;
  level: number;
}

export interface ParsedLecture {
  slug: string;
  title: string;
  domainId: DomainId;
  domainName: string;
  summary: string;
  canonicalDefHtml: string;
  mechanismHtml: string;
  discrepanciesHtml: string;
  practicalHtml: string;
  symbols: SymbolItem[];
  qaList: QAItem[];
  sections: LectureSection[];
  outgoingLinks: string[];
  backlinks: string[];
  resourceLinks: ResourceLink[];
}
