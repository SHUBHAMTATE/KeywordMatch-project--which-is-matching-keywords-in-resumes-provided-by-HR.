# import PyPDF2
# file="Data science interview pdf"
# pdf_file_path = "C:\\Users\\Dell\\Desktop\\shabir\\fresume_files" + f"\\{file}"
# print(pdf_file_path)
# with open(pdf_file_path, 'rb') as file:
#             pdf_reader = PyPDF2.PdfReader(file)

#             # Initialize an empty string to store the text
#             pdf_text = ""

#             # Iterate through the pages and concatenate their text
#             for page in range(len(pdf_reader.pages)):
#                 page_obj = pdf_reader.pages[page]
#                 pdf_text += page_obj.extract_text()

#             # Print or use the extracted text
#             print(pdf_text)

def find_keywords_in_string(big_string, keywords):
    found_keywords = []
    for keyword in keywords:
        if keyword in big_string:
            found_keywords.append(keyword)
    return found_keywords

# def main():
#     big_string = input("Enter the big string: ")
#     keywords = input("Enter keywords (comma-separated): ").split(',')

#     found_keywords = find_keywords_in_string(big_string, keywords)

#     if found_keywords:
#         print("Found keywords in the big string:")
#         for keyword in found_keywords:
#             print(keyword)
#     else:
#         print("No keywords found in the big string.")


