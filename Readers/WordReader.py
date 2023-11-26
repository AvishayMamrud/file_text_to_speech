import win32com.client
import os


def read_word(file_path):
    full_path = os.path.abspath(file_path)
    word = win32com.client.Dispatch("Word.Application")
    word.visible = False
    wb = word.Documents.Open(full_path)
    doc = word.ActiveDocument
    file_contents = doc.Range().Text
    doc.Close(False)
    word.Quit()
    return file_contents

