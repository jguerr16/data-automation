import dropbox
import time
from config import DROPBOX_ACCESS_TOKEN, DROPBOX_FOLDER_PATH

# Initialize Dropbox client
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

# Function to download the latest CSV from Dropbox
def download_latest_csv():
    # List files in Dropbox folder
    entries = dbx.files_list_folder(DROPBOX_FOLDER_PATH).entries
    
    # Find the latest CSV file
    csv_files = [entry for entry in entries if entry.name.endswith('.csv')]
    if not csv_files:
        print("No CSV files found.")
        return None
    
    latest_file = max(csv_files, key=lambda entry: entry.server_modified)
    
    # Download the latest CSV file
    file_path = f"./{latest_file.name}"
    print(f"Downloading {latest_file.name} from Dropbox")
    metadata, res = dbx.files_download(f"{DROPBOX_FOLDER_PATH}/{latest_file.name}")
    
    with open(file_path, "wb") as f:
        f.write(res.content)
    
    return file_path

# Function to upload the reformatted CSV back to Dropbox
def upload_csv_to_dropbox(local_file, new_file_name):
    with open(local_file, "rb") as f:
        dbx.files_upload(f.read(), f"{DROPBOX_FOLDER_PATH}/{new_file_name}", mode=dropbox.files.WriteMode.overwrite)
    print(f"Uploaded {new_file_name} to Dropbox.")
