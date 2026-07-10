import os
import re
import unicodedata

VAULT_ROOT = "/Users/suyoo/Library/Mobile Documents/iCloud~md~obsidian/Documents/KM"
WIKI_DIR = os.path.join(VAULT_ROOT, "wiki")

def normalize(s):
    return unicodedata.normalize('NFC', s)

# 1. Build current wiki map: filename -> current relative path from VAULT_ROOT
wiki_map = {}
for root, dirs, files in os.walk(WIKI_DIR):
    for file in files:
        if file.endswith(".md"):
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, VAULT_ROOT)
            
            norm_name = normalize(file)
            norm_name_no_ext = normalize(os.path.splitext(file)[0])
            
            # Map both with and without extension using raw rel_path to preserve actual disk encoding
            wiki_map[norm_name] = rel_path
            wiki_map[norm_name_no_ext] = os.path.splitext(rel_path)[0]

def get_new_path(link_content):
    # Remove alias if exists: [[path|alias]] -> path
    path_part = link_content.split('|')[0].strip()
    filename = os.path.basename(path_part)
    norm_filename = normalize(filename)
    
    if norm_filename in wiki_map:
        return wiki_map[norm_filename]
    
    # Try removing .md if it was there
    name_no_ext = os.path.splitext(norm_filename)[0]
    if name_no_ext in wiki_map:
        return wiki_map[name_no_ext]
        
    return None

def update_links(content):
    def replace_link(match):
        full_link = match.group(1) # e.g., "wiki/AI/file|Alias"
        parts = full_link.split('|')
        link_path = parts[0]
        alias = "|" + parts[1] if len(parts) > 1 else ""
        
        new_path = get_new_path(link_path)
        if new_path:
            # Check if it needs extension (Obsidian usually doesn't, but we'll follow current style)
            # If original had .md, keep it or follow vault preference. 
            # Here we just provide the mapped path.
            return f"[[{new_path}{alias}]]"
        return match.group(0)

    # Regex for [[link]]
    return re.sub(r'\[\[(.*?)\]\]', replace_link, content)

# 2. Process all files
modified_count = 0
for root, dirs, files in os.walk(WIKI_DIR):
    for file in files:
        if not file.endswith(".md"):
            continue
        
        file_path = os.path.join(root, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = update_links(content)
            
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_count += 1
                print(f"Updated: {file}")
        except Exception as e:
            print(f"Error in {file}: {e}")

print(f"\nTotal files updated: {modified_count}")
