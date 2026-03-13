import os
import sys

def clear_screen():
    # Clears terminal for a clean UI feel
    os.system('cls' if os.name == 'nt' else 'clear')

def run_hfc_interface():
    clear_screen()
    
    # Custom ASCII Art for HFC Converter
    hfc_logo = """
    ██╗  ██╗███████╗ ██████╗     ██████╗ ██████╗ ███╗   ██╗██╗   ██╗
    ██║  ██║██╔════╝██╔════╝    ██╔════╝██╔═══██╗████╗  ██║██║   ██║
    ███████║█████╗  ██║         ██║     ██║   ██║██╔██╗ ██║██║   ██║
    ██╔══██║██╔══╝  ██║         ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝
    ██║  ██║██║     ╚██████╗    ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ 
    ╚═╝  ╚═╝╚═╝      ╚═════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  
                    [ H F S  S Y S T E M S ]
    """
    print(hfc_logo)
    print("-" * 60)
    print(" >>> HFS V.1 | INITIALIZING VIRTUAL TEXT COMPILATION <<<")
    print("-" * 60)

    # Step 1: File Extension Name (FEN)
    fen_name = input("\n[?] Enter your environment data name (FEN): ").strip()
    if not fen_name:
        print("[!] Error: FEN cannot be empty.")
        return

    # Step 2: Cryptic Data Structure (CCS)
    print("\n[*] Prepare Cryptic Data Structure (The Compiler/Structure)")
    print("    (Type your structure and press Enter)")
    ccs_data = input(" >>> ")

    # Step 3: Confirmation
    print(f"\n[!] DATA LOGGED:")
    print(f"    - IDENTITY: {fen_name}")
    print(f"    - STRUCTURE: {ccs_data[:20]}...") 
    
    confirm = input("\nConfirm to proceed to HFS mapping? (y/n): ").lower()

    if confirm == 'y':
        print("\n[*] Handing off to con$listener.py...")
        # Here we would trigger the listener to start the generation
        # os.system(f"python3 con$listener.py {fen_name}")
    else:
        print("[*] Aborted.")

if __name__ == "__main__":
    run_hfc_interface()
