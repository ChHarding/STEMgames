import  
ngss = open(r"C:\Users\UTEC\Desktop\hci584\HCI584 - STEM games\NGSS.pdf", mode = "rb")
pdf_document = PyPDF2.PdfFileReader(ngss)
pdf_document.numPages