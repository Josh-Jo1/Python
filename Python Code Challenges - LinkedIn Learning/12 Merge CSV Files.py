# Challenge: Write a Python function to merge multiple CSV files.
# Input: list of input files, output file path;   Output: new merged CSV file

import csv

def mergeCSV(files, outFile):
    
    # Determine headers for merged CSV file
    
    allHeaders = list()

    for file in files:
        with open(file) as input_file:
            fileHeaders = csv.DictReader(input_file).fieldnames

            for header in fileHeaders:
                if header not in allHeaders:
                    allHeaders.append(header)

    # Create merged CSV file

    with open(outFile, 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=allHeaders)
        writer.writeheader()

        for file in files:
            with open(file) as input_file:
                reader = csv.DictReader(input_file)
                
                for row in reader:
                    writer.writerow(row)

mergeCSV(["12 file 1.csv", "12 file 2.csv"], "merged.csv")


# Relied on provided solution for writing rows
