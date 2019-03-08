from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("CERN.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)