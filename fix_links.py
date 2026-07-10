import os
import re
import unicodedata

# Configuration
VAULT_ROOT = "/Users/suyoo/Library/Mobile Documents/iCloud~md~obsidian/Documents/KM"
WIKI_DIR = os.path.join(VAULT_ROOT, "wiki")
RAW_DIR = os.path.join(VAULT_ROOT, "raw")

def normalize(s):
    return unicodedata.normalize('NFC', s)

# 1. Build wiki files map: filename -> wiki_path (relative to wiki/)
wiki_files_map = {}
for root, dirs, files in os.walk(WIKI_DIR):
    for file in files:
        if file.endswith(".md"):
            rel_path = os.path.relpath(os.path.join(root, file), WIKI_DIR)
            
            # Normalize to NFC
            norm_file = normalize(file)
            norm_name_no_ext = normalize(os.path.splitext(file)[0])
            norm_rel_path = normalize(rel_path)
            norm_rel_path_no_ext = normalize(os.path.splitext(rel_path)[0])
            
            if norm_file not in wiki_files_map:
                wiki_files_map[norm_file] = norm_rel_path
            if norm_name_no_ext not in wiki_files_map:
                wiki_files_map[norm_name_no_ext] = norm_rel_path_no_ext

def get_wiki_link(filename):
    filename = normalize(filename)
    # Try with extension first
    if filename in wiki_files_map:
        return "wiki/" + wiki_files_map[filename]
    
    # Try without extension
    name_no_ext = os.path.splitext(filename)[0]
    if name_no_ext in wiki_files_map:
        return "wiki/" + wiki_files_map[name_no_ext]
    
    return None

# 2. Source standardization
source_labels = [
    "출처", "Source", "Original URL", "URL", "원문 출처", "원문 URL", 
    "관련 URL", "추출된 URL", "추출된 관련 URL", "추출된 외부 URL", 
    "추출된 이미지 URL", "원문", "추출된 관련 외부 URL"
]
source_regex = re.compile(r'^(\*?\*?(?:' + '|'.join(source_labels) + r')\*?\*?:?\s*)(.*)$', re.IGNORECASE | re.MULTILINE)

def standardize_source(match):
    content = match.group(2).strip()
    url_match = re.search(r'(https?://[^\s\)\],<>]+)', content)
    if not url_match:
        return match.group(0)
    url = url_match.group(1)
    title_match = re.search(r'\[(.*?)\]\(' + re.escape(url) + r'\)', content)
    title = title_match.group(1) if title_match else "원본 링크"
    if title == url:
        title = "원본 링크"
    return f"**출처**: [{title}]({url})"

# 3. Internal link regex
# More inclusive regex to catch [[Resources/...]] as well as [[raw/Resources/...]]
internal_link_regex = re.compile(r'\[\[(?:raw/)?Resources/(?:.*?/)?([^\]|/]+)(\.md)?(\|[^\]]*)?\]\]')
internal_link_paren_regex = re.compile(r'\((?:raw/)?Resources/(?:.*?/)?([^\)|/]+)(\.md)?\)')

def fix_internal_link(match):
    filename = match.group(1)
    ext = match.group(2) or ""
    alias = match.group(3) or ""
    
    wiki_path = get_wiki_link(filename + ext)
    if wiki_path:
        return f"[[{wiki_path}{alias}]]"
    return match.group(0)

def fix_internal_link_paren(match):
    filename = match.group(1)
    ext = match.group(2) or ""
    wiki_path = get_wiki_link(filename + ext)
    if wiki_path:
        return f"({wiki_path})"
    return match.group(0)

# 4. Frontmatter fix
def fix_frontmatter(content):
    if not content.startswith("---"):
        return content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    fm_text = parts[1]
    # Remove raw/Resources/ path in related_raw
    fm_text = re.sub(r'\[\[(?:raw/)?Resources/.*?/([^\]|/]+\.md)\]\]', r'[[\1]]', fm_text)
    return f"---{fm_text}---{parts[2]}"

# Main loop
files_modified = 0
for root, dirs, files in os.walk(WIKI_DIR):
    for file in files:
        if not file.endswith(".md"):
            continue
        file_path = os.path.join(root, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            original_content = content
            content = fix_frontmatter(content)
            content = internal_link_regex.sub(fix_internal_link, content)
            content = internal_link_paren_regex.sub(fix_internal_link_paren, content)
            
            # Separate frontmatter for source standardization
            if content.startswith("---"):
                parts = content.split("---", 2)
                if len(parts) >= 3:
                    body = parts[2]
                    body = source_regex.sub(standardize_source, body)
                    content = f"---{parts[1]}---{body}"
                else:
                    content = source_regex.sub(standardize_source, content)
            else:
                content = source_regex.sub(standardize_source, content)
            
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_modified += 1
        except Exception as e:
            print(f"Error processing {file}: {e}")

print(f"SUCCESS: {files_modified} files modified (including normalization fixes).")
