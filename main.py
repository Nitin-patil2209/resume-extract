# importing PyPDF2 Module
import PyPDF2
#creating text that contain file data
with open('Nitin Patil.pdf', 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    text = pageObj.extractText()
# write to new data.txt file
with open('data.txt','w') as textt:
    textt.writelines(text)

let = False
with open("data.txt", "r") as datatext:
    info = datatext.read()
    if 'Education' in info:
        f = info.find('Education')
        goods = info[f:]
        l = goods.find("\n \n \n \n")

        goods = goods[:l]

        with open("nn.txt", "a") as nnfile:
            nnfile.write(goods)
    if 'Experience' in info:
        f = info.find('Experience')
        goods = info[f:]
        l = goods.find(".")
        goods = goods[:l]
        with open("nn.txt", "a") as nnfile:
            nnfile.write(goods)
    if 'Skill' in info:
        f = info.find('Skill')
        goods = info[f:]
        l = goods.find(".")
        goods = goods[:l]
        with open("nn.txt", "a") as nnfile:
            nnfile.write(goods)
