
def readfile(key):
    import os
    # folder_path = r"C:\Users\Dell\Desktop\HR\uploads"  # Replace with the path to your folder
    key = str(key).split(',')
    key.extend(list(map(lambda x: x.title() ,key)))
    key.extend([x.upper() for x in key])
    keywords=set(key)
    keywords=list(keywords)
    print(keywords)
    dictt=dict()
    # dictt.update({1:"one"})
    # print(dictt)
    # Check if the folder path exists
    folder_path = r"C:\Users\Dell\Desktop\HR\uploads" 
    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        # List all files in the folder
        for filename in os.listdir(folder_path):
            # Check if the item is a file (not a directory)
            if os.path.isfile(os.path.join(folder_path, filename)):
                # print(os.path.splitext(filename)[1])
                extention=os.path.splitext(filename)[1]
                # print(extention)
                file=os.path.splitext(filename)[0]+extention
                print(file)
                if extention==".pdf":
                    from read import pdfread
                    from pr1 import find_keywords_in_string
                    # print(type(pdfread(file)))
                    # print(find_keywords_in_string(str(pdfread(file)),keywords))
                    dictt.update({os.path.splitext(filename)[0]:find_keywords_in_string(str(pdfread(file)),keywords)})
                elif extention==".docx":
                    from read import readdocx
                    from pr1 import find_keywords_in_string
                    # print(find_keywords_in_string(str(readdocx(file)),keywords))
                    dictt.update({os.path.splitext(filename)[0]:find_keywords_in_string(str(readdocx(file)),keywords)})
                    # print(readdocx(file))
                else:
                    print("No Files")
                # Extract the file extension
                # file_extension = os.path.splitext(filename)[-1]
                # file_extensions.add(file_extension)
        print("="*100)
        return dictt
    # for (key, values) in enumerate(dictt.items()):
    #         print(key, "=", values, " > ", (len(values)))
# readfile("re,python,ml")
    # print(file_extensions)
# file="Data science interview pdf.pdf"
# pdf_file_path = "C:\\Users\\Dell\\Desktop\\shabir\\fresume_files" + f"\\{file}"
# print(pdf_file_path)