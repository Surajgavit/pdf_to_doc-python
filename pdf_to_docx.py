from tkinter import Tk
from tkinter.filedialog import askopenfilename
import PyPDF2

Tk().withdraw()
filename = askopenfilename()
FILE_PATH = filename
with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(0)
    print(page.extractText())
