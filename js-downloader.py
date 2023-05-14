import os
import requests
import sys
from concurrent.futures import ThreadPoolExecutor
import urllib3

# Disable warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

DEFAULT_MAX_WORKERS = 10  # Default maximum number of parallel workers


def download_file(url, folder_name):
    try:
        # Extract the filename from the URL
        file_name = os.path.basename(url)

        # Download the file
        response = requests.get(url, stream=True, verify=False)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        file_path = os.path.join(folder_name, file_name)

        # Save the file
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        return f"Downloaded: {file_name}"
    except requests.exceptions.RequestException as e:
        return f"Failed to download: {file_name}. Error: {str(e)}"


def download_js_files(file_path, folder_name, max_workers=DEFAULT_MAX_WORKERS):
    try:
        # Create a folder for downloaded files
        os.makedirs(folder_name, exist_ok=True)

        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file if line.strip().endswith('.js')]

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = [executor.submit(download_file, url, folder_name) for url in urls]

            for future in results:
                print(future.result())
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except OSError as e:
        print(f"Failed to create folder: {folder_name}. Error: {str(e)}")


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) < 3 or sys.argv[1] == '--help':
        print("Usage: python program_name.py file_path folder_name [max_workers]")
        print("Downloads all the JS files mentioned in the file using parallel processing and threads.")
        print("Arguments:")
        print("  file_path    : Path to the file containing the list of JS file URLs (one per line)")
        print("  folder_name  : Name of the folder to create for downloaded files")
        print("  max_workers  : (Optional) Maximum number of parallel workers (default: 10)")
        sys.exit(1)

    # Get the file path and folder name from command-line arguments
    file_path = sys.argv[1]
    folder_name = sys.argv[2]

    # Get the maximum number of workers from user input (if provided)
    max_workers = int(sys.argv[3]) if len(sys.argv) >= 4 else DEFAULT_MAX_WORKERS

    download_js_files(file_path, folder_name, max_workers)
