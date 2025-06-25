from bs4 import BeautifulSoup
import tarfile

# Path to your tar.gz file
tar_path = "C:/Users/directory_kungalv_slutpriser/kungalv_slutpriser.tar"
extract_path = "C:/Users/extract"

with tarfile.open(tar_path, "r") as tar:
    tar.extractall(path=extract_path)

print("Files extracted successfully!")
