# Word to PDF Converter

This Python script automates the conversion of Word documents to PDFs in a specified folder using the `docx2pdf` library.

## Installation

1. Clone this repository or download the script.

2. (Optional) Please use a Virtual Environment in Python:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Activate the virtual environment (Windows)
   ```

3. Install the required Python library using pip:

   ```bash
   pip install docx2pdf
   ```

4. Ensure you have Microsoft Word installed on your system. This script relies on the `docx2pdf` library for document conversion, which in turn uses Microsoft Word.

## Usage

1. Open the command prompt or terminal.

2. Navigate to the directory where the script is located.

3. Run the script using the following command:

   ```bash
   python word_to_pdf.py
   ```

4. The script will prompt you for the input folder containing Word documents and the output folder where the PDFs will be saved. Provide the paths as instructed.

5. The script will convert all Word documents (`.docx` and `.doc`) in the input folder to PDFs and save them in the output folder.

6. The converted PDFs will be named the same as the original Word documents.

7. You can now find the converted PDFs in the specified output folder.

## Example

Suppose you have the following directory structure:

```
project_folder/
    word_to_pdf.py
    input_documents/
        document1.docx
        document2.doc
    output_pdfs/
```

1. Run the script and provide the following paths when prompted:

   - Input Folder: `input_documents`
   - Output Folder: `output_pdfs`

2. The script will convert `document1.docx` and `document2.doc` to PDFs and save them in the `output_pdfs` folder.

3. You will find the converted PDFs (`document1.pdf` and `document2.pdf`) in the `output_pdfs` folder.

## Notes

- Ensure you have the appropriate permissions to access and write to the input and output folders.

- Make sure Microsoft Word is installed on your system before running the script.

- This script uses the `docx2pdf` library and works on Windows, macOS, and Linux.

- Feel free to modify the script to suit your specific needs or integrate it into other automation workflows. (MAR)

Contact me if there where problems or submit an issue to be addressed.
