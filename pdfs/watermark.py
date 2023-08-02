import PyPDF2
import sys

# content_pdf = sys.argv[1]
# watermark_pdf = sys.argv[2]


def watermark(content_pdf: str, watermark_pdf: str):
    reader_content = PyPDF2.PdfFileReader(content_pdf)
    reader_watermark = PyPDF2.PdfFileReader(watermark_pdf)
    watermark = reader_watermark.pages[0]
    output = PyPDF2.PdfFileWriter()
    for page in reader_content.pages:
        page.mergePage(watermark)
        output.addPage(page)
    with open(content_pdf, "wb") as file:
        output.write(file)


watermark('tilt.pdf', 'wtr.pdf')
