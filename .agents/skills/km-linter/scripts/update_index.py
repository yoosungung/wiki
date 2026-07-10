import os
import unicodedata
import datetime

VAULT_ROOT = "/Users/suyoo/Library/Mobile Documents/iCloud~md~obsidian/Documents/KM"
WIKI_DIR = os.path.join(VAULT_ROOT, "wiki")

def normalize(s):
    return unicodedata.normalize('NFC', s)

def count_files(dir_path):
    count = 0
    for root, dirs, files in os.walk(dir_path):
        count += len([f for f in files if f.endswith(".md") and not f.startswith("000_")])
    return count

def get_moc(dir_path):
    dir_name = os.path.basename(dir_path)
    moc_name = f"000_{dir_name}-MOC.md"
    moc_path = os.path.join(dir_path, moc_name)
    if os.path.exists(moc_path):
        return f"[[{os.path.relpath(moc_path, VAULT_ROOT)}]]"
    return None

def run():
    categories = {
        "AGENTS": "wiki/Agents",
        "MODELS": "wiki/Models",
        "RAG": "wiki/RAG",
        "ENGINEERING": "wiki/Engineering",
        "BUSINESS": "wiki/Business"
    }
    
    today = datetime.date.today().strftime("%Y-%m-%d")
    content = "# KM_INDEX_AGENT_v1\n"
    content += f"[META] Updated: {today} | Root: wiki/\n\n"
    
    content += "## 📂 CATEGORIES_MOC\n"
    for cat, path in categories.items():
        moc = get_moc(os.path.join(VAULT_ROOT, path))
        if moc:
            content += f"- {cat}: {moc}\n"
    
    # Add special ones or planning
    content += "- PLANNING: [[projects/Rebellions-EXAONE/planning.md]], [[projects/Browser-Inference/planning.md]]\n\n"
    
    content += "## 🌲 DIRECTORY_MAPPING\n"
    for cat, path in categories.items():
        abs_path = os.path.join(VAULT_ROOT, path)
        subdirs = [d for d in os.listdir(abs_path) if os.path.isdir(os.path.join(abs_path, d)) and not d.startswith(".")]
        content += f"### {path}/\n"
        content += f"- Sub: [{', '.join(subdirs)}]\n"
        for sd in subdirs:
            sd_path = os.path.join(abs_path, sd)
            sd_moc = get_moc(sd_path)
            if sd_moc:
                content += f"    - {sd}: {sd_moc}\n"
        content += "\n"

    content += "## 📌 KEY_FILE_LIST\n"
    for cat, path in categories.items():
        abs_path = os.path.join(VAULT_ROOT, path)
        total = count_files(abs_path)
        content += f"- {path}/ ({total} files)\n"
        subdirs = [d for d in os.listdir(abs_path) if os.path.isdir(os.path.join(abs_path, d)) and not d.startswith(".")]
        for sd in subdirs:
            sd_path = os.path.join(abs_path, sd)
            sd_total = count_files(sd_path)
            if sd_total > 0:
                content += f"    - {sd}: {sd_total} files\n"

    with open(os.path.join(VAULT_ROOT, "index.md"), 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    run()
