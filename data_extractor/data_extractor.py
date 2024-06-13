import os
from docx import Document
import re

def extract_text_around_keyword(text, keyword, window=50): # change 50 to another number to signify how many characters to return
    match = re.search(rf'({keyword}|{keyword.lower()}|{keyword.upper()})\W*(\d+(\.\d+)?\s*\w*)?', text)
    if match:
        start = max(0, match.start() - window)
        end = min(len(text), match.end() + window)
        return text[start:end]
    return None
def search_word_documents_for_keyword(folder_path, keyword):
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(folder_path, filename)
            doc = Document(file_path)
            text = '\n'.join([para.text for para in doc.paragraphs])
            extracted_text = extract_text_around_keyword(text, keyword)
            if extracted_text:
                print(f"File: {filename}")
                print(extracted_text)
                print("----")
folder_path = "your/path/here"
keyword = 'your keyword here'
search_word_documents_for_keyword(folder_path, keyword)
