import time
from dropbox_monitor import download_latest_csv, upload_csv_to_dropbox
from csv_processor import process_csv
# from tableau_uploader import upload_to_tableau_cloud

if __name__ == "__main__":
    print("Script started")  # Print that the script has started running
    
    while True:
        print("Checking for new CSV files in Dropbox...")  # Step into checking CSV files

        # Step 1: Check for new CSV files in Dropbox
        csv_file = download_latest_csv()

        if csv_file:
            print(f"Found new CSV file: {csv_file}")
            
            # Step 2: Process the CSV (convert coordinates to cities)
            print(f"Processing CSV file: {csv_file}")
            processed_csv = process_csv(csv_file)
            print(f"CSV processed: {processed_csv}")
            
            # Step 3: Upload the processed CSV back to Dropbox
            processed_csv_name = processed_csv.split('/')[-1]
            print(f"Uploading processed CSV to Dropbox: {processed_csv_name}")
            upload_csv_to_dropbox(processed_csv, processed_csv_name)
            print(f"Processed CSV uploaded: {processed_csv_name}")

            # Optional: Upload to Tableau Cloud
            # print(f"Uploading processed data to Tableau Cloud...")
            # upload_to_tableau_cloud(processed_csv)
            # print(f"Data uploaded to Tableau Cloud.")

        else:
            print("No new CSV files found.")

        print("Sleeping for 60 seconds...")
        # Wait for 60 seconds before checking again
        time.sleep(60)