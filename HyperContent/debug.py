import os
import binascii

def run_debug_env(package_path):
    print(f"[*] Debugging {package_path}...")
    
    vtc_path = os.path.join(package_path, "vtc.vtc")
    
    if not os.path.exists(vtc_path):
        print("[!] Execution Error: VTC layer missing.")
        return

    # "Unsuppress" for execution in RAM only
    with open(vtc_path, "rb") as f:
        suppressed_code = f.read()
        executable_logic = binascii.unhexlify(suppressed_code).decode('utf-8')

    print("[*] VTC Layer Unlocked. Executing Custom Code Structure...")
    print("-" * 30)
    # This is where your device actually 'runs' the custom transpiled logic
    try:
        exec(executable_logic) # Running the virtual text
    except Exception as e:
        print(f"[!] Runtime Debug Error: {e}")
    print("-" * 30)
    print("[✔] Execution Finished.")

if __name__ == "__main__":
    # Example call
    run_debug_env("project_alpha.hfc") 
