'use client';

import React, { useRef, useState, useCallback, useEffect } from 'react';
import dynamic from 'next/dynamic';
import { GraphData, GraphNode } from '../../types/graph';

// Dynamically import ForceGraph2D with ssr disabled
const ForceGraph2D = dynamic(() => import('react-force-graph-2d'), {
  ssr: false,
  loading: () => (
    <div className="w-full h-full flex flex-col items-center justify-center gap-3 text-[#6B6B76]">
      <div className="w-8 h-8 rounded-full border-2 border-[#1F5FFF] border-t-transparent animate-spin" />
      <span className="text-[13px] font-medium">Đang khởi tạo mạng lưới tri thức 48 khái niệm...</span>
    </div>
  ),
});

interface KnowledgeGraphProps {
  data: GraphData;
  onSelectNode: (node: GraphNode) => void;
  selectedNodeId?: string;
  activeDomainId?: string | null;
  searchQuery?: string;
}

export function KnowledgeGraph({
  data,
  onSelectNode,
  selectedNodeId,
  activeDomainId,
  searchQuery = '',
}: KnowledgeGraphProps) {
  const fgRef = useRef<any>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const [dimensions, setDimensions] = useState({ width: 800, height: 600 });
  const [hoverNode, setHoverNode] = useState<GraphNode | null>(null);
  const [neighbors, setNeighbors] = useState<Set<string>>(new Set());

  // Update dimensions on resize
  useEffect(() => {
    const updateSize = () => {
      if (containerRef.current) {
        setDimensions({
          width: containerRef.current.clientWidth,
          height: containerRef.current.clientHeight,
        });
      }
    };

    updateSize();
    window.addEventListener('resize', updateSize);
    return () => window.removeEventListener('resize', updateSize);
  }, []);

  // Filter nodes & links based on activeDomainId
  const filteredData = React.useMemo(() => {
    let nodes = data.nodes;
    if (activeDomainId) {
      nodes = nodes.filter(n => n.domainId === activeDomainId);
    }

    const nodeIds = new Set(nodes.map(n => n.id));
    const links = data.links.filter(l => {
      const sourceId = typeof l.source === 'object' ? (l.source as any).id : l.source;
      const targetId = typeof l.target === 'object' ? (l.target as any).id : l.target;
      return nodeIds.has(sourceId) && nodeIds.has(targetId);
    });

    return { nodes, links };
  }, [data, activeDomainId]);

  // Search zoom
  useEffect(() => {
    if (!searchQuery || !fgRef.current) return;
    const found = filteredData.nodes.find(n =>
      n.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      n.id.toLowerCase().includes(searchQuery.toLowerCase())
    );

    if (found && found.x !== undefined && found.y !== undefined) {
      fgRef.current.centerAt(found.x, found.y, 800);
      fgRef.current.zoom(3, 800);
      onSelectNode(found);
    }
  }, [searchQuery, filteredData.nodes, onSelectNode]);

  // Hover neighbor highlight
  const handleNodeHover = useCallback((node: any) => {
    if (node) {
      setHoverNode(node);
      const neighborSet = new Set<string>();
      neighborSet.add(node.id);

      filteredData.links.forEach(l => {
        const sourceId = typeof l.source === 'object' ? (l.source as any).id : l.source;
        const targetId = typeof l.target === 'object' ? (l.target as any).id : l.target;
        if (sourceId === node.id) neighborSet.add(targetId);
        if (targetId === node.id) neighborSet.add(sourceId);
      });

      setNeighbors(neighborSet);
    } else {
      setHoverNode(null);
      setNeighbors(new Set());
    }
  }, [filteredData.links]);

  return (
    <div ref={containerRef} className="w-full h-full relative overflow-hidden bg-[#F5F5F7] select-none">
      <ForceGraph2D
        ref={fgRef}
        width={dimensions.width}
        height={dimensions.height}
        graphData={filteredData}
        nodeId="id"
        nodeLabel={(n: any) => `${n.name} (${n.domainName})`}
        nodeColor={(n: any) => {
          if (hoverNode) {
            return neighbors.has(n.id) ? n.color : '#D1D1D6';
          }
          if (selectedNodeId) {
            return n.id === selectedNodeId ? n.color : '#C4C4CC';
          }
          return n.color;
        }}
        nodeVal={(n: any) => n.val}
        linkColor={(l: any) => {
          if (hoverNode) {
            const s = typeof l.source === 'object' ? l.source.id : l.source;
            const t = typeof l.target === 'object' ? l.target.id : l.target;
            return s === hoverNode.id || t === hoverNode.id
              ? 'rgba(31, 95, 255, 0.6)'
              : 'rgba(16, 16, 24, 0.05)';
          }
          return 'rgba(16, 16, 24, 0.12)';
        }}
        linkWidth={(l: any) => {
          if (hoverNode) {
            const s = typeof l.source === 'object' ? l.source.id : l.source;
            const t = typeof l.target === 'object' ? l.target.id : l.target;
            return s === hoverNode.id || t === hoverNode.id ? 2 : 1;
          }
          return 1;
        }}
        linkDirectionalArrowLength={3.5}
        linkDirectionalArrowRelPos={1}
        linkCurvature={0.1}
        onNodeHover={handleNodeHover}
        onNodeClick={(node: any) => onSelectNode(node as GraphNode)}
        cooldownTicks={120}
        d3AlphaDecay={0.02}
        d3VelocityDecay={0.3}
        nodeCanvasObject={(node: any, ctx: CanvasRenderingContext2D, globalScale: number) => {
          const isHighlighted = hoverNode ? neighbors.has(node.id) : true;
          const isSelected = selectedNodeId === node.id;
          const r = Math.max(3, (node.val || 5) * 0.7);

          // Node Circle
          ctx.beginPath();
          ctx.arc(node.x, node.y, r, 0, 2 * Math.PI, false);
          ctx.fillStyle = isHighlighted ? node.color : '#D1D1D6';
          ctx.fill();

          // Selection / Highlight ring
          if (isSelected || (hoverNode && hoverNode.id === node.id)) {
            ctx.lineWidth = 2.5 / globalScale;
            ctx.strokeStyle = '#111114';
            ctx.stroke();
          }

          // Node Label
          if (globalScale > 0.8 || isSelected || (hoverNode && hoverNode.id === node.id)) {
            const label = node.name;
            const fontSize = Math.max(10 / globalScale, 3);
            ctx.font = `${fontSize}px Inter, sans-serif`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'top';

            // Text background pill for readability
            const textWidth = ctx.measureText(label).width;
            ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
            ctx.fillRect(
              node.x - textWidth / 2 - 2 / globalScale,
              node.y + r + 2 / globalScale,
              textWidth + 4 / globalScale,
              fontSize + 2 / globalScale
            );

            ctx.fillStyle = isHighlighted ? '#0B0B0F' : '#9A9AA5';
            ctx.fillText(label, node.x, node.y + r + 3 / globalScale);
          }
        }}
      />
    </div>
  );
}
