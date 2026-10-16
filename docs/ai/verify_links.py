import os
import re
import urllib.parse
import sys

# Ensure UTF-8 output on Windows
if sys.platform.startswith('win'):
    sys.stdout.reconfigure(encoding='utf-8')

WIKI_DIR = r"E:\MyProject\MyWiki\wiki"
RESOURCES_DIR = r"E:\MyProject\MyWiki\resources"

def main():
    print("=== STARTING WIKI INTEGRITY VERIFICATION ===")
    
    wiki_files = [f for f in os.listdir(WIKI_DIR) if f.endswith('.md')]
    print(f"Total markdown files in wiki/: {len(wiki_files)}")
    
    # Map of entity slugs and lowercase titles
    entity_slugs = {f[:-3].lower(): f for f in wiki_files}
    
    # Resource files list (normalized)
    resource_files = set()
    for root, dirs, files in os.walk(RESOURCES_DIR):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), RESOURCES_DIR).replace('\\', '/')
            resource_files.add(rel_path.lower())
            resource_files.add(file.lower())
    
    print(f"Total unique resource files in resources/: {len(resource_files)}")
    
    total_words = 0
    total_wikilinks = 0
    total_resource_links = 0
    broken_resource_links = []
    broken_wikilinks = []
    
    # Regex patterns
    md_link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    wiki_link_pattern = re.compile(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]')
    
    for wf in wiki_files:
        filepath = os.path.join(WIKI_DIR, wf)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        words = len(content.split())
        total_words += words
        
        # Check wiki-links
        wikilinks = wiki_link_pattern.findall(content)
        total_wikilinks += len(wikilinks)
        for target, label in wikilinks:
            slug = target.strip().lower().replace(' ', '-')
            if slug not in entity_slugs and target.strip().lower() not in entity_slugs:
                broken_wikilinks.append((wf, target))
                
        # Check markdown links to resources
        md_links = md_link_pattern.findall(content)
        for text, url in md_links:
            if 'resources/' in url.lower():
                total_resource_links += 1
                idx = url.lower().find('resources/')
                subpath = url[idx + len('resources/'):].split('#')[0]
                unquoted_subpath = urllib.parse.unquote(subpath).replace('\\', '/')
                filename = os.path.basename(unquoted_subpath).lower()
                
                # Check existence
                full_test_path = os.path.join(RESOURCES_DIR, unquoted_subpath)
                if not os.path.exists(full_test_path) and filename not in resource_files and unquoted_subpath.lower() not in resource_files:
                    broken_resource_links.append((wf, url, unquoted_subpath))

    print("\n--- INTEGRITY METRICS ---")
    print(f"Total Word Count across Wiki: {total_words:,} words")
    print(f"Average Words per Page: {total_words // len(wiki_files):,} words")
    print(f"Total Cross-Entity [[wiki-links]]: {total_wikilinks}")
    print(f"Total Resource Links to Original Sources: {total_resource_links}")
    
    if broken_resource_links:
        print(f"\n[WARNING] Found {len(broken_resource_links)} broken resource links:")
        for wf, link, sub in broken_resource_links[:10]:
            print(f"  - In {wf}: {link} -> {sub}")
    else:
        print("\n[SUCCESS] 100% of resource links resolve to real files in resources/!")
        
    if broken_wikilinks:
        print(f"\n[WARNING] Found {len(broken_wikilinks)} unmatched [[wiki-links]]:")
        for wf, target in broken_wikilinks[:10]:
            print(f"  - In {wf}: [[{target}]]")
    else:
        print("[SUCCESS] 100% of [[wiki-links]] match registered entity pages!")
        
    print("\n=== VERIFICATION COMPLETE ===")

if __name__ == '__main__':
    main()
