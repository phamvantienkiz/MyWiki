import { getAllEntities } from './wiki';
import { GraphData, GraphNode, GraphLink } from '../types/graph';
import { DOMAINS } from './constants';

export async function getGraphData(): Promise<GraphData> {
  const entities = await getAllEntities();
  const slugSet = new Set(entities.map(e => e.slug.toLowerCase()));

  const nodes: GraphNode[] = entities.map(e => {
    const domain = DOMAINS[e.domainId];
    const totalConnections = e.outgoingLinks.length + e.backlinks.length;
    // Logarithmic scale for radius
    const val = Math.max(5, Math.min(22, 5 + Math.log2(1 + totalConnections) * 3));

    return {
      id: e.slug,
      name: e.title,
      domainId: e.domainId,
      domainName: domain.shortName,
      color: domain.color,
      summary: e.summary,
      val,
      inDegree: e.backlinks.length,
      outDegree: e.outgoingLinks.length,
    };
  });

  const links: GraphLink[] = [];
  for (const e of entities) {
    for (const target of e.outgoingLinks) {
      if (slugSet.has(target.toLowerCase())) {
        links.push({
          source: e.slug,
          target: target.toLowerCase(),
        });
      }
    }
  }

  return { nodes, links };
}
