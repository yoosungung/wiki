import os
import re
import unicodedata

VAULT_ROOT = "/Users/suyoo/Library/Mobile Documents/iCloud~md~obsidian/Documents/KM"
WIKI_DIR = os.path.join(VAULT_ROOT, "wiki")

def normalize(s):
    return unicodedata.normalize('NFC', s)

def get_moc_name(dir_path):
    dir_name = os.path.basename(dir_path)
    return f"000_{dir_name}-MOC.md"

def update_moc(dir_path):
    moc_name = get_moc_name(dir_path)
    moc_path = os.path.join(dir_path, moc_name)
    
    # Files in this directory
    files = [f for f in os.listdir(dir_path) if f.endswith(".md") and f != moc_name and not f.startswith("000_")]
    files.sort()
    
    # Subdirectories that have MOCs
    subdirs = [d for d in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, d)) and not d.startswith(".")]
    subdirs.sort()
    
    rel_dir = os.path.relpath(dir_path, VAULT_ROOT)
    
    content = f"# {os.path.basename(dir_path)} MOC\n\n"
    
    if subdirs:
        content += "## 📂 Categories\n"
        for sd in subdirs:
            sd_path = os.path.join(dir_path, sd)
            sd_moc_name = get_moc_name(sd_path)
            sd_moc_path = os.path.join(sd_path, sd_moc_name)
            if os.path.exists(sd_moc_path):
                content += f"- [[{os.path.relpath(sd_moc_path, VAULT_ROOT)}|{sd}]]\n"
        content += "\n"
        
    content += "## 📄 Documents\n"
    for f in files:
        content += f"- [[{os.path.join(rel_dir, f)}]]\n"
    
    with open(moc_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return os.path.relpath(moc_path, VAULT_ROOT)

def run():
    mocs = []
    # Use top-down to ensure parents can link to children (though order doesn't strictly matter for link creation)
    # Actually, bottom-up is better so children exist when parent links to them
    for root, dirs, files in os.walk(WIKI_DIR, topdown=False):
        if ".obsidian" in root: continue
        
        has_md = any(f.endswith(".md") for f in files)
        has_sub_moc = False
        for d in dirs:
            sd_path = os.path.join(root, d)
            if os.path.exists(os.path.join(sd_path, get_moc_name(sd_path))):
                has_sub_moc = True
                break
                
        if has_md or has_sub_moc:
            moc_rel_path = update_moc(root)
            mocs.append(moc_rel_path)
            print(f"Updated MOC: {moc_rel_path}")
    
    return mocs

if __name__ == "__main__":
    run()
