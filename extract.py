import tarfile
import os
import glob

def extract_xiaomi_bak():
    # 1. Find all .bak files in the current directory
    bak_files = glob.glob("*.bak")
    
    if not bak_files:
        print("No .bak files found in the current folder.")
        return

    for bak_path in bak_files:
        print(f"Processing: {bak_path}")
        output_dir = bak_path.replace(".bak", "_extracted")
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(bak_path, 'rb') as f:
            data = f.read()
            
            # 2. Identify the TAR container within the Xiaomi backup
            # The 'ustar' magic bytes are at offset 257 of a TAR header block
            tar_magic_offset = data.find(b'ustar')
            if tar_magic_offset == -1:
                print(f"Skipping {bak_path}: No valid TAR structure found.")
                continue
                
            # Calculate the actual start of the TAR block (257 bytes before 'ustar')
            tar_start = max(0, tar_magic_offset - 257)
            
            # 3. Save the payload to a temporary file for extraction
            temp_tar = "temp_payload.tar"
            with open(temp_tar, 'wb') as tmp:
                tmp.write(data[tar_start:])

        # 4. Extract the TAR contents
        try:
            with tarfile.open(temp_tar, "r:") as tar:
                tar.extractall(path=output_dir)
                print(f"Successfully extracted to: {output_dir}")
                # List a few extracted files for verification
                for member in tar.getnames()[:5]:
                    print(f" - {member}")
        except Exception as e:
            print(f"Error extracting {bak_path}: {e}")
        finally:
            if os.path.exists(temp_tar):
                os.remove(temp_tar)

if __name__ == "__main__":
    extract_xiaomi_bak()
    