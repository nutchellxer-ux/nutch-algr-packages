import os
import shutil

def compile_hfc():
    package_name = "project_alpha.hfc"
    if not os.path.exists(package_name):
        os.makedirs(package_name)
    
    # Create the index configuration
    with open(os.path.join(package_name, "index.cf"), "w") as f:
        f.write("HFS_TYPE: CUSTOM_BYTE_EXEC\n")
        f.write("VTC_MODE: TRANSPILE_ON_FLY\n")
        f.write("BOOT_TARGET: .vtc\n")

    # Move suppressed files into the package
    for ext in ["fen", "ccs", "vtc"]:
        filename = f"{ext}.{ext}"
        if os.path.exists(filename):
            shutil.move(filename, os.path.join(package_name, filename))

    print(f"\n[✔] HFC Package Created: {package_name}")
    print("Structure: [index.cf, .fen, .ccs, .vtc]")

if __name__ == "__main__":
    compile_hfc()
