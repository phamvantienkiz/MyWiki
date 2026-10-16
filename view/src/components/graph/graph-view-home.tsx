'use client';

import React, { useState, useCallback } from 'react';
import { GraphData, GraphNode } from '../../types/graph';
import { EntityMetadata, DomainId } from '../../types/wiki';
import { KnowledgeGraph } from './knowledge-graph';
import { NodeQuickDrawer } from './node-quick-drawer';
import { GraphControls } from './graph-controls';
import { DocumentsListModal } from './documents-list-modal';

interface GraphViewHomeProps {
  initialGraphData: GraphData;
  entities: EntityMetadata[];
}

export function GraphViewHome({ initialGraphData, entities }: GraphViewHomeProps) {
  const [selectedNode, setSelectedNode] = useState<GraphNode | null>(null);
  const [activeDomainId, setActiveDomainId] = useState<DomainId | null>(null);
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [isListViewOpen, setIsListViewOpen] = useState<boolean>(false);

  const handleSelectNode = useCallback((node: GraphNode) => {
    setSelectedNode(node);
  }, []);

  const handleCloseDrawer = useCallback(() => {
    setSelectedNode(null);
  }, []);

  const handleSelectRelatedNode = useCallback((slug: string) => {
    const target = initialGraphData.nodes.find(n => n.id.toLowerCase() === slug.toLowerCase());
    if (target) {
      setSelectedNode(target);
    }
  }, [initialGraphData.nodes]);

  const handleResetView = useCallback(() => {
    setActiveDomainId(null);
    setSearchQuery('');
    setSelectedNode(null);
  }, []);

  return (
    <main className="w-screen h-screen relative overflow-hidden bg-[#F5F5F7]">
      {/* Floating Controls Toolbar */}
      <GraphControls
        searchQuery={searchQuery}
        onSearchChange={setSearchQuery}
        activeDomainId={activeDomainId}
        onDomainToggle={setActiveDomainId}
        onResetView={handleResetView}
        onToggleListView={() => setIsListViewOpen(prev => !prev)}
        isListViewOpen={isListViewOpen}
      />

      {/* Main Graph Viewport */}
      <KnowledgeGraph
        data={initialGraphData}
        onSelectNode={handleSelectNode}
        selectedNodeId={selectedNode?.id}
        activeDomainId={activeDomainId}
        searchQuery={searchQuery}
      />

      {/* Quick View Drawer */}
      <NodeQuickDrawer
        node={selectedNode}
        onClose={handleCloseDrawer}
        onSelectRelatedNode={handleSelectRelatedNode}
      />

      {/* Traditional Document List Modal */}
      <DocumentsListModal
        isOpen={isListViewOpen}
        onClose={() => setIsListViewOpen(false)}
        entities={entities}
        onSelectEntity={slug => {
          handleSelectRelatedNode(slug);
        }}
      />
    </main>
  );
}
