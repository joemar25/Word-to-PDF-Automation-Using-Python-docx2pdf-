import os
from shutil import copytree
from docx2pdf import convert

def word_to_pdf(input_folder, output_folder):
    # If the output folder doesn't exist, create it
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Walk through all directories and files in the input folder
    for dirpath, dirnames, filenames in os.walk(input_folder):
        # Create corresponding directories in the output folder
        structure = os.path.join(output_folder, os.path.relpath(dirpath, input_folder))
        if not os.path.isdir(structure):
            os.makedirs(structure)

        # Convert each file to PDF
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            output_path = os.path.join(structure, os.path.splitext(filename)[0] + '.pdf')
            convert(file_path, output_path)
            
if __name__ == "__main__":
    input_folder = "folder/"
    output_folder = "output/"
    word_to_pdf(input_folder, output_folder)

