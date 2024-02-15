import os
from docx import Document

def get_word_count(filename):
    doc = Document(filename)
    word_count = 0
    for paragraph in doc.paragraphs:
        word_count += len(paragraph.text.split())
    return word_count

def main():
    folder_path = 'path/to/folder'
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(folder_path, filename)
            word_count = get_word_count(file_path)
            print(f"File: {filename}, Word Count: {word_count}")

if __name__ == "__main__":
    main()
