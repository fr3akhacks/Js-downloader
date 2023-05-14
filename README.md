# JS Downloader

The JS Downloader is a Python script that reads a file line by line and downloads all the JavaScript (JS) files mentioned in the file. It creates a folder with a specified name and saves the downloaded files in that folder.

## Usage
python js-downloader.py file_path folder_name [max_workers]

- `file_path`: Path to the file containing the list of JS file URLs (one per line).
- `folder_name`: Name of the folder to create for downloaded files.
- `max_workers` (optional): Maximum number of parallel workers (default: 10).

The program downloads the JS files mentioned in the file using parallel processing and threads. It improves the download speed by utilizing multiple workers to download files simultaneously.

## Examples

To download JS files mentioned in `file.txt` and save them in the `downloaded_js` folder with a maximum of 5 parallel workers:

python js-downloader.py file.txt downloaded_js 5

To use the default maximum number of workers (10):

python js-downloader.py file.txt downloaded_js


## Notes

- Make sure you have the `requests` library installed (`pip install requests`) before running the program.
- Disabling SSL certificate verification (`verify=False`) is included in the program for convenience. However, it's recommended to verify the SSL certificates in a production environment for secure communication.

## License

This project is licensed under the [MIT License](LICENSE).

