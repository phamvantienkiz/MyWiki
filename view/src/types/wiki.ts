export type DomainId = 
  | 'genai' 
  | 'rag' 
  | 'agentic' 
  | 'deeplearning' 
  | 'mlmath' 
  | 'mlops' 
  | 'software';

export interface DomainInfo {
  id: DomainId;
  name: string;
  shortName: string;
  color: string;
  pastelBg: string;
  textColor: string;
  description: string;
}

export interface ResourceLink {
  label: string;
  url: string;
  fileName: string;
  sourceType: 'book' | 'slide' | 'infographic' | 'paper' | 'interview';
}

export interface EntityMetadata {
  slug: string;
  title: string;
  domainId: DomainId;
  domainName: string;
  summary: string;
  canonicalDef: string;
  wordCount: number;
  outgoingLinks: string[];
  backlinks: string[];
  resourceLinks: ResourceLink[];
  contentRaw: string;
}
