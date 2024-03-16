import zipfile
import os

# Check if the file exists
file_zip = "student.dat"
ex_folder = "extract"

if os.path.exists(file_zip):
    # Create a directory for extracted files if it doesn't exist
    if not os.path.exists(ex_folder):
        os.makedirs(ex_folder)
    
    # Extract the zip file
    with zipfile.ZipFile(file_zip, 'r') as zf:
        zf.extractall(ex_folder)

    # List files in the extract folder
    extracted_files = os.listdir(ex_folder)
    for extracted_file in extracted_files:
        file_path = os.path.join(ex_folder, extracted_file)
        # Check if the extracted file is a regular file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                print("Contents of", extracted_file, ": ")
                print(f.read())
else:
    print("The file does not exist.")
