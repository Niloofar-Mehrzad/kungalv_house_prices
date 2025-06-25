from bs4 import BeautifulSoup
import tarfile

# Path to your tar.gz file
tar_path = "C:/Users/mmehr/OneDrive/Desktop/CHALMERS/3_ThirdYear/3_StudyPeriod2/Introduction to data science and AI - DAT565/Assignments/Assignment_2/directory_kungalv_slutpriser/kungalv_slutpriser.tar"
extract_path = "C:/Users/mmehr/OneDrive/Desktop/CHALMERS/3_ThirdYear/3_StudyPeriod2/Introduction to data science and AI - DAT565/Assignments/Assignment_2"

with tarfile.open(tar_path, "r") as tar:
    tar.extractall(path=extract_path)

print("Files extracted successfully!")
