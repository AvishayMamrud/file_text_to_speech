import PyPDF2


def readPDF(file_path):
    pdf_reader = PyPDF2.PdfReader(open(file_path, 'rb'))
    clean_text = ''
    for page in pdf_reader.pages:
        text = page.extract_text()
        clean_text += text.strip().replace('\n', ' ')
    return clean_text
