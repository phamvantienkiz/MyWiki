import { getGraphData } from '../lib/graph';
import { getAllEntities } from '../lib/wiki';
import { GraphViewHome } from '../components/graph/graph-view-home';

export const revalidate = 60; // ISR cache

export default async function HomePage() {
  const graphData = await getGraphData();
  const entities = await getAllEntities();

  return <GraphViewHome initialGraphData={graphData} entities={entities} />;
}
