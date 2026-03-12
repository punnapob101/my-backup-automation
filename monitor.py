import os
import glob

files = glob.glob("*.tar.gz")

if not files:
    print("❌ Backup file not found!")

else:
   
    latest_file = max(files, key=os.path.getctime)
    
    file_size = os.path.getsize(latest_file) / 1024

    print(f"✅ Detected file: {latest_file}")
    print(f"📊 File size: {file_size:.2f} KB")

    if file_size < 1:
        print("⚠️ Warning: File size is unusually small!")
    else:
        print("🚀 Everything looks good!")
