from docx import Document
import os

def convert_rtf_to_docx(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(".rtf"):
            rtf_file = os.path.join(input_folder, filename)
            docx_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".docx")
            try:
                doc = Document()
                with open(rtf_file, "r", encoding="utf-8") as rtf:
                    # read RTF file
                    rtf_content = rtf.read()
                # add content to the DOCX
                doc.add_paragraph(rtf_content)
                # save as DOCX
                doc.save(docx_file)
                print(f"Converted {filename} to DOCX")
            except Exception as e:
                print(f"Error converting {filename}: {e}")

# replace 'input_folder' with the path to the folder containing RTF files
input_folder = 'input/path/here'

# replace 'output_folder' with the path to the folder where DOCX files will be saved
output_folder = 'output/path/here'

convert_rtf_to_docx(input_folder, output_folder)
