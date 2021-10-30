from fpdf import FPDF
import os

EXPORT_PATH = 'data/export'


def dir_creation(file_format):
    if os.path.exists(os.path.join(EXPORT_PATH, file_format)):
        pass
    else:
        os.makedirs(os.path.join(EXPORT_PATH, file_format))


def pdf_converter(source, title, news):
    file_format = 'pdf'
    pdf = FPDF(orientation="P", unit="mm", format="A5")
    pdf.add_page()
    pdf.set_font('times', size=12)
    pdf.cell(txt="hello world")
    pdf.output(os.path.join(EXPORT_PATH, "hello_world.pdf"))
