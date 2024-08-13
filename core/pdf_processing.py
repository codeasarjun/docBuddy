
import PyPDF2
import base64

def process_pdf(file):
    pdf_content = file.read()
    pdf_base64 = base64.b64encode(pdf_content).decode("utf-8")
    pdf_reader = PyPDF2.PdfReader(file)
    text_content = ""
    for page_num in range(len(pdf_reader.pages)):
        text_content += pdf_reader.pages[page_num].extract_text()
    return pdf_base64, text_content
