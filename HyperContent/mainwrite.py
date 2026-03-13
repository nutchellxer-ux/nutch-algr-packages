import os
import shutil

def setup_hfs_environment():
    # Detect Termux environment
    termux_bin = "/data/data/com.termux/files/usr/bin"
    local_bin = os.path.expanduser("~/bin")
    target_dir = termux_bin if os.path.exists(termux_bin) else local_bin
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Actual filenames currently in your GitHub HyperContent folder
    file_map = {
        "command_1.py": "nutch-algr",
        "execute_1.py": "execute_1",
        "con_editor.py": "con_editor",
        "con_blanklet.py": "con_blanklet",
        "con_afterdo.py": "con_afterdo",
        "con_listener.py": "con_listener",
        "gen.py": "gen",
        "gen_hfc.py": "gen_hfc",
        "debug.py": "debug"
    }

    print(f"[*] Mapping HFS commands to {target_dir}...")

    for src, cmd in file_map.items():
        if os.path.exists(src):
            target_path = os.path.join(target_dir, cmd)
            shutil.copy(src, target_path)
            os.chmod(target_path, 0o755)
            print(f"[+] Energized: {cmd}")
        else:
            print(f"[!] Skip: {src} not found in download.")

    # Create the 'hfs-init' command to re-run this setup
    shutil.copy(__file__, os.path.join(target_dir, "hfs-init"))
    os.chmod(os.path.join(target_dir, "hfs-init"), 0o755)

if __name__ == "__main__":
    setup_hfs_environment()
