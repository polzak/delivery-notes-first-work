import os

def getfiles():
    pdf_list = []
    folder_list = [(x[0], x[2]) for x in os.walk(os.getcwd())] #x[0] is a subfolder, and x[2] is a list of files in it
    for ft in folder_list:
        pdf_list = pdf_list + [os.path.join(ft[0], f) for f in ft[1] if f.endswith('.pdf')]
    return pdf_list


print(getfiles())
