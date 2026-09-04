import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(__file__))
from vault_paths import find_vault_root

VAULT_ROOT = find_vault_root(__file__)
WIKI_DIR = os.path.join(VAULT_ROOT, "wiki")
INDEX_FILE = os.path.join(VAULT_ROOT, "INDEX.md")

def normalize(s):
    return unicodedata.normalize('NFC', s)

def get_all_wiki_files():
    wiki_files = {}
    for root, dirs, files in os.walk(VAULT_ROOT):
        if ".obsidian" in root or ".gemini" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                rel_path = normalize(os.path.relpath(os.path.join(root, file), VAULT_ROOT))
                wiki_files[rel_path] = {
                    "inbound_links": [],
                    "outbound_links": []
                }
    return wiki_files

def extract_links(content):
    # Regex for [[link]] or [[link|alias]]
    links = re.findall(r'\[\[(.*?)\]\]', content)
    clean_links = []
    for link in links:
        path = link.split('|')[0].strip()
        clean_links.append(normalize(path))
    return clean_links

def resolve_link(link_path, current_file_path, all_files):
    link_path = normalize(link_path)
    current_file_path = normalize(current_file_path)
    # Obsidian links can be:
    # 1. Full path from vault root: wiki/Category/File.md
    # 2. Relative to current file: ../Other/File.md
    # 3. Just filename: File.md (if unique)
    
    # Try direct match
    if link_path in all_files:
        return link_path
    if link_path + ".md" in all_files:
        return link_path + ".md"
    
    # Try just filename
    filename = os.path.basename(link_path)
    if not filename.endswith(".md"):
        filename += ".md"
        
    potential_matches = [f for f in all_files if os.path.basename(f) == filename]
    if len(potential_matches) == 1:
        return potential_matches[0]
    
    # Try relative path
    dir_of_current = os.path.dirname(current_file_path)
    rel_resolved = os.path.normpath(os.path.join(dir_of_current, link_path))
    if rel_resolved in all_files:
        return rel_resolved
    if rel_resolved + ".md" in all_files:
        return rel_resolved + ".md"

    return None

def analyze():
    all_files = get_all_wiki_files()
    dead_links = []
    
    for file_path in all_files:
        abs_path = os.path.join(VAULT_ROOT, file_path)
        try:
            with open(abs_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            links = extract_links(content)
            for link in links:
                resolved = resolve_link(link, file_path, all_files)
                if resolved:
                    if resolved != file_path: # Ignore self-links
                        all_files[resolved]["inbound_links"].append(file_path)
                        all_files[file_path]["outbound_links"].append(resolved)
                else:
                    dead_links.append({"from": file_path, "target": link})
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    orphans = [f for f in all_files if len(all_files[f]["inbound_links"]) == 0 and "wiki/" in f]
    
    # Filter orphans: MOCs and index are expected to be linked from somewhere or are entry points
    # But usually MOCs should be linked from index.md
    
    print(f"--- DEAD LINKS ({len(dead_links)}) ---")
    for dl in dead_links[:20]:
        print(f"From: {dl['from']} -> Target: {dl['target']}")
    if len(dead_links) > 20:
        print(f"... and {len(dead_links) - 20} more")

    print(f"\n--- ORPHANED NOTES ({len(orphans)}) ---")
    for o in orphans[:20]:
        print(o)
    if len(orphans) > 20:
        print(f"... and {len(orphans) - 20} more")
        
    return all_files, dead_links, orphans

if __name__ == "__main__":
    analyze()
