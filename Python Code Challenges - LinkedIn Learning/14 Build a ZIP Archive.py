# Challenge: Write a Python function to build a ZIP archive.
# Input: input directory path, list of file extensions, output file path;   Output: ZIP file

import os
from zipfile import ZipFile

def zipFiles(inputPath, extensions, outputPath):
    with ZipFile(outputPath, 'w') as zippedFile:
        for path, names, files in os.walk(inputPath):
            rel_path = os.path.relpath(path, inputPath)
            for file in files:
                name, ext = os.path.splitext(file)
                if ext.lower() in extensions:
                    zippedFile.write(os.path.join(path, file), arcname=os.path.join(rel_path, file))

# zipFiles("C:\\Users\\User\\Desktop\\input_folder", [".jpg", ".png"], "C:\\Users\\User\\Desktop")

# Relied on provided solution
