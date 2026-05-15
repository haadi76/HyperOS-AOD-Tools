import tarfile
import os
import io

def create_final_validated_backup(source_folder, output_filename):
    # 1. EXACT HEADER FROM ORIGINAL HEX
    # [span_4](start_span)This block matches the signature and alignment MIUI expects[span_4](end_span)
    header_text = (
        "MIUI BACKUP\n2\ncom.miui.aod Always-on display\n-1\n0\n"
        "ANDROID BACKUP\n5\n0\nnone\n"
    ).encode('utf-8')

    # 2. PREPARE THE TAR PAYLOAD
    tar_stream = io.BytesIO()
    
    # [span_5](start_span)We use USTAR format and manual UID/GID setting to match the original[span_5](end_span)
    with tarfile.open(fileobj=tar_stream, mode='w', format=tarfile.USTAR_FORMAT) as tar:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                full_path = os.path.join(root, file)
                
                # [span_6](start_span)Create internal paths (e.g. apps/com.miui.aod/miui_bak/custom_theme_01/...)[span_6](end_span)
                arcname = os.path.relpath(full_path, start=os.path.dirname(source_folder))
                
                # [span_7](start_span)Set metadata to match system-level signatures (UID/GID 1000)[span_7](end_span)
                info = tar.gettarinfo(full_path, arcname=arcname)
                info.uid = 1000
                info.gid = 1000
                info.uname = "" 
                info.gname = ""
                
                with open(full_path, 'rb') as f:
                    tar.addfile(info, f)

    # 3. ASSEMBLE FINAL BINARY
    with open(output_filename, 'wb') as out_file:
        out_file.write(header_text)
        out_file.write(tar_stream.getvalue())

    print(f"Validated backup created: {output_filename}")

if __name__ == "__main__":
    # Ensure the 'apps' folder is in your current directory
    if os.path.exists("apps"):
        create_final_validated_backup("apps", "custom_aod_backup.bak")
    else:
        print("Error: Required 'apps' directory not found.")
        