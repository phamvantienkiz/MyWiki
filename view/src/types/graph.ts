import { DomainId } from './wiki';

export interface GraphNode {
  id: string;               // slug, e.g. 'large-language-models'
  name: string;             // Display name, e.g. 'Large Language Models'
  domainId: DomainId;
  domainName: string;
  color: string;            // Domain color
  summary: string;
  val: number;              // Node size proportional to total connections
  inDegree: number;
  outDegree: number;
  x?: number;
  y?: number;
  vx?: number;
  vy?: number;
}

export interface GraphLink {
  source: string | GraphNode;
  target: string | GraphNode;
}

export interface GraphData {
  nodes: GraphNode[];
  links: GraphLink[];
}
