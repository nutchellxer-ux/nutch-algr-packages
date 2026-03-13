import os
import shutil
import subprocess

def setup_hfs_environment():
    # Detect if running in Termux or standard Linux
    termux_bin = "/data/data/com.termux/files/usr/bin"
    local_bin = os.path.expanduser("~/bin")
    
    target_dir = termux_bin if os.path.exists(termux_bin) else local_bin
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # List of files to move and make executable
    core_files = [
        "command$1.py", "execute$1.py", "con$editor.py", 
        "con$blanklet.py", "con$afterdo.py", "con$listener.py",
        "Gen.py", "Gen$hfc.py", "debug.py"
    ]

    print(f"[*] Initializing HFS Environment in {target_dir}...")

    try:
        for file in core_files:
            if os.path.exists(file):
                target_path = os.path.join(target_dir, file.replace('.py', ''))
                shutil.copy(file, target_path)
                
                # Apply chmod +x so it runs as a command
                os.chmod(target_path, 0o755)
                print(f"[+] {file} mapped and energized.")
            else:
                print(f"[!] Warning: {file} not found in local directory.")

        # Self-move logic for debugging access
        script_name = os.path.basename(__file__)
        shutil.copy(__file__, os.path.join(target_dir, "hfs-init"))
        os.chmod(os.path.join(target_dir, "hfs-init"), 0o755)

        print("\n[✔] HFS Environment is live. Use 'hfs-init' to re-sync.")
        
    except Exception as e:
        print(f"[✘] Critical Error during HFS write: {e}")

if __name__ == "__main__":
    setup_hfs_environment()
