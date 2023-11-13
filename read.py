# def readdocx(filename):
#     # Initialize an empty string to store the text
#     import docx2txt

#     # Extract text from a Word document
#     Docx_file_path = "C:\\Users\\Dell\\Desktop\\shabir\\fresume_files" + f"\\{filename}"
#     text = docx2txt.process(Docx_file_path)

#     # 'text' now contains the extracted text
#     p=str(text)
#     return p

import docx2txt

def readdocx(filename):
    # Construct the full file path
    file_path = "C:\\Users\\Dell\\Desktop\\HR\\uploads" + "\\" + filename
    print(file_path)

    try:
        # Extract text from the Word document
        text = docx2txt.process(file_path)
        return text
    except Exception as e:
        print(f"Error reading the .docx file {filename}: {e}")
        return None

# print(readdocx("Shubham Tate CV.docx"))



import PyPDF2

# Open and read a PDF file

  # Replace with the path to your PDF file
def pdfread(file):
        file_path = "C:\\Users\\Dell\\Desktop\\HR\\uploads" + "\\" + file
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)

            # Initialize an empty string to store the text
            pdf_text = ""

            # Iterate through the pages and concatenate their text
            for page in range(len(pdf_reader.pages)):
                page_obj = pdf_reader.pages[page]
                pdf_text += page_obj.extract_text()

            # Print or use the extracted text
            return pdf_text


# pdfread("Data science interview pdf.pdf")