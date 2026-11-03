import fs from 'fs/promises';
import path from 'path';
import { EntityMetadata, ResourceLink, DomainId } from '../types/wiki';
import { DOMAINS, DOMAIN_SLUG_MAP } from './constants';

const WIKI_DIR = path.resolve(process.cwd(), '../wiki');

let cachedEntities: EntityMetadata[] | null = null;

export async function getAllEntities(): Promise<EntityMetadata[]> {
  if (cachedEntities) {
    return cachedEntities;
  }

  try {
    const files = await fs.readdir(WIKI_DIR);
    const mdFiles = files.filter(f => f.endsWith('.md') && f !== 'index.md');

    const entityMap = new Map<string, { raw: string; outgoing: string[]; resLinks: ResourceLink[] }>();

    // Pass 1: Read all files and extract raw data & outgoing links
    for (const file of mdFiles) {
      const slug = file.replace(/\.md$/, '');
      const filePath = path.join(WIKI_DIR, file);
      const content = await fs.readFile(filePath, 'utf-8');

      // Extract outgoing wiki-links: [[slug]] or [[slug|Label]]
      const outgoing: string[] = [];
      const wikiLinkRegex = /\[\[([a-zA-Z0-9_-]+)(?:\|([^\]]+))?\]\]/g;
      let match;
      while ((match = wikiLinkRegex.exec(content)) !== null) {
        const targetSlug = match[1].toLowerCase();
        if (targetSlug !== slug && !outgoing.includes(targetSlug)) {
          outgoing.push(targetSlug);
        }
      }

      // Extract original resources: [Text](../resources/...)
      const resLinks: ResourceLink[] = [];
      const resLinkRegex = /\[([^\]]+)\]\((\.\.\/resources\/[^)]+)\)/g;
      while ((match = resLinkRegex.exec(content)) !== null) {
        const label = match[1];
        const url = match[2];
        const fileName = decodeURIComponent(url.split('/').pop() || '');
        let sourceType: ResourceLink['sourceType'] = 'book';
        if (fileName.endsWith('.pdf')) {
          if (fileName.includes('Slide') || fileName.includes('Session') || fileName.includes('Bai giang')) {
            sourceType = 'slide';
          } else {
            sourceType = 'book';
          }
        } else if (fileName.match(/\.(jpg|jpeg|png)$/i)) {
          sourceType = 'infographic';
        } else if (fileName.endsWith('.txt')) {
          sourceType = 'interview';
        }

        resLinks.push({ label, url, fileName, sourceType });
      }

      entityMap.set(slug, { raw: content, outgoing, resLinks });
    }

    // Pass 2: Compute backlinks
    const backlinksMap = new Map<string, string[]>();
    Array.from(entityMap.entries()).forEach(([sourceSlug, data]) => {
      for (const targetSlug of data.outgoing) {
        if (!backlinksMap.has(targetSlug)) {
          backlinksMap.set(targetSlug, []);
        }
        backlinksMap.get(targetSlug)!.push(sourceSlug);
      }
    });

    // Pass 3: Assemble EntityMetadata
    const entities: EntityMetadata[] = [];
    Array.from(entityMap.entries()).forEach(([slug, data]) => {
      const content = data.raw;
      
      // Extract title from first H1
      const titleMatch = content.match(/^#\s+(.+)$/m);
      const title = titleMatch ? titleMatch[1].trim() : slug;

      // Extract summary from "## Tóm tắt", blockquote "Tóm tắt điều hành", or first paragraph
      let summary = '';
      const summaryMatch = content.match(/##\s+(?:\d+\.\s+)?Tóm tắt[^\n]*\n([\s\S]*?)(?=##|\n#|$)/i);
      if (summaryMatch) {
        summary = summaryMatch[1].replace(/^\s*>\s*/gm, '').trim();
      } else {
        const execMatch = content.match(/>\s*\*\*Tóm tắt điều hành\*\*:\s*([\s\S]*?)(?=\n\n|$)/i);
        if (execMatch) {
          summary = execMatch[1].replace(/\n>\s*/g, ' ').trim();
        } else {
          // Find first paragraph that is not a heading or metadata blockquote
          const paras = content.split('\n\n');
          for (const p of paras) {
            const trimmed = p.trim();
            if (trimmed && !trimmed.startsWith('#') && !trimmed.startsWith('>') && !trimmed.startsWith('---')) {
              summary = trimmed;
              break;
            }
          }
        }
      }

      // Extract canonical definition snippet
      let canonicalDef = '';
      const canonMatch = content.match(/##\s+(?:\d+\.\s+)?(?:Định nghĩa [^\n]+|Nền Tảng[^\n]+|Bối Cảnh[^\n]+)\n([\s\S]*?)(?=##|\n#|$)/i);
      if (canonMatch) {
        canonicalDef = canonMatch[1].trim().substring(0, 300) + '...';
      }

      const domainId = DOMAIN_SLUG_MAP[slug] || 'genai';
      const domain = DOMAINS[domainId];

      entities.push({
        slug,
        title,
        domainId,
        domainName: domain.name,
        summary,
        canonicalDef,
        wordCount: content.split(/\s+/).length,
        outgoingLinks: data.outgoing,
        backlinks: backlinksMap.get(slug) || [],
        resourceLinks: data.resLinks,
        contentRaw: content,
      });
    });

    cachedEntities = entities;
    return entities;
  } catch (err) {
    console.error('Error reading wiki files:', err);
    return [];
  }
}

export async function getEntityBySlug(slug: string): Promise<EntityMetadata | null> {
  const all = await getAllEntities();
  return all.find(e => e.slug.toLowerCase() === slug.toLowerCase()) || null;
}
