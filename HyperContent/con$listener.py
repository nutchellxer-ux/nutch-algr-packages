import os

def hfs_listener():
    source_file = "sample_hfs.ccs"
    prefix = "# How this section works"
    
    if not os.path.exists(source_file):
        print(f"[!] Error: {source_file} not found.")
        return

    print("[*] Listener: Parsing HFS sections...")
    
    with open(source_file, "r") as f:
        content = f.read()

    # Splitting the code into its components based on your custom prefix
    sections = content.split(prefix)
    
    # Logic to identify which section belongs to which file
    parsed_data = {
        "fen": "",
        "ccs": "",
        "vtc": ""
    }

    for sect in sections:
        if "Section: FEN_IDENTITY" in sect:
            parsed_data["fen"] = sect.strip()
        elif "Section: CCS_LOGIC" in sect:
            parsed_data["ccs"] = sect.strip()
        elif "Section: VTC_TRANSPILE" in sect:
            parsed_data["vtc"] = sect.strip()

    print("[✔] Sections identified. Triggering Byte Generation...")
    
    # We pass the parsed data to Gen.py (which we will build next)
    # For now, we simulate the handoff
    import subprocess
    # Saving temp data for Gen.py to pick up
    for key, value in parsed_data.items():
        with open(f"temp_{key}.raw", "w") as tmp:
            tmp.write(value)
            
    os.system("python3 Gen.py")

if __name__ == "__main__":
    hfs_listener() 
