import os

def getfiles():
    pdf_list = []
    outer_list = [x[2] for x in os.walk(os.getcwd())] #walk all the files through all of the subfolders
    for l in outer_list:
        pdf_list = pdf_list + l #stretch the nested list
    return [p for p in pdf_list if p.endswith('.pdf')]
        
print(getfiles())
