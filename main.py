from docx2pdf import convert
import os


def word_to_pdf(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert all .docx files in the input folder to PDF and save them in the output folder
    convert(input_folder, output_folder)


if __name__ == "__main__":
    input_folder = r"C:/Users/{USER_NAME}/{FOLDER IF ANY}/{FOLDER WHERE IS INPUT}"
    output_folder = (r"C:/Users/{USER_NAME}/{FOLDER IF ANY}/{FOLDER WHERE YOU WANT TO SAVE PDF}")
    word_to_pdf(input_folder, output_folder)
