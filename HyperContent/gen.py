import os
import binascii

def suppress_to_bytes(input_file, extension):
    if not os.path.exists(input_file):
        return
    
    with open(input_file, "r") as f:
        data = f.read()
    
    # Convert text to hex-encoded bytes for "unreadable" effect
    # You can later add hardware-specific salting here
    byte_data = binascii.hexlify(data.encode('utf-8'))
    
    output_file = input_file.replace("temp_", "").replace(".raw", f".{extension}")
    with open(output_file, "wb") as f:
        f.write(byte_data)
    
    print(f"[+] Suppressed: {output_file}")
    os.remove(input_file)

if __name__ == "__main__":
    print("[*] Gen: Suppressing HFS components...")
    suppress_to_bytes("temp_fen.raw", "fen")
    suppress_to_bytes("temp_ccs.raw", "ccs")
    suppress_to_bytes("temp_vtc.raw", "vtc") 
