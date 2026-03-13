import os
import subprocess

def open_editor(target_file="sample_hfs.ccs"):
    print(f"[*] HFS Editor: Opening {target_file}...")
    
    # Attempt to use nano or vi (standard in Termux/Linux)
    # If those aren't found, it falls back to a simple input-based rewrite
    try:
        editor = os.environ.get('EDITOR', 'nano')
        subprocess.call([editor, target_file])
    except FileNotFoundError:
        print("[!] Terminal editor not found. Use 'input' mode?")
        new_code = input("Paste your updated CCS code here (Finish with enter):\n")
        with open(target_file, "w") as f:
            f.write(new_code)

    print(f"\n[✔] Edit complete. File '{target_file}' is saved and ready.")

if __name__ == "__main__":
    open_editor()
