import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showinfo
from docx2pdf import convert

win = tk.Tk()
win.title("Word To PDF Converter Tool")

def openfile():
    file = askopenfile(filetypes=[('Word Files', '*.docx')])
    convert(file.name,

    r'C:\Users\prajw\OneDrive\Desktop\doc2pdf\doc2pdfconverted.pdf')  
    )
    showinfo("Done", "File Converted Successfully")