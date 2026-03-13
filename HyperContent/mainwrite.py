import os
import shutil

def setup_hfs_environment():
    # Detect Termux environment
    termux_bin = "/data/data/com.termux/files/usr/bin"
    local_bin = os.path.expanduser("~/bin")
    target_dir = termux_bin if os.path.exists(termux_bin) else local_bin
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # EXACT mapping based on your GitHub screenshot
    file_map = {
        "execute$1.py": "nutch-algr",  # This creates your main command
        "con$afterdo.py": "con$afterdo",
        "con$blanklet.py": "con$blanklet",
        "con$editor.py": "con$editor",
        "con$listener.py": "con$listener",
        "debug.py": "debug",
        "gen$hfc.py": "gen$hfc",
        "gen.py": "gen"
    }

    print(f"[*] Mapping HFS commands to {target_dir}...")

    for src, cmd in file_map.items():
        if os.path.exists(src):
            target_path = os.path.join(target_dir, cmd)
            shutil.copy(src, target_path)
            os.chmod(target_path, 0o755)
            print(f"[+] Energized: {cmd}")
        else:
            print(f"[!] Skip: {src} not found in directory.")

    # Self-install hfs-init
    shutil.copy(__file__, os.path.join(target_dir, "hfs-init"))
    os.chmod(os.path.join(target_dir, "hfs-init"), 0o755)
    print("[✔] Environment live. Type 'nutch-algr' to start.")

if __name__ == "__main__":
    setup_hfs_environment()
