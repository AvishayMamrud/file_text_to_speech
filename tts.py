import sys

import pyttsx3
import os
from Readers import PdfReader, TextReader, WordReader


def get_reader_func(ext):
    return {
        '.pdf': PdfReader.readPDF,
        '.doc': WordReader.read_word,
        '.docx': WordReader.read_word,
        '.txt': TextReader.read_textfile,
        '.py': TextReader.read_textfile
    }[ext]


def read_text(file_path, ext):
    reader_func = get_reader_func(ext)
    return reader_func(file_path)


def tts(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    speaker = pyttsx3.init()
    text = read_text(file_path, file_extension)
    speech_rate = speaker.getProperty('rate')
    speaker.setProperty('rate', speech_rate - 50)
    speaker.save_to_file(text, f'{file_name}_{file_extension[1:]}.mp3')
    speaker.runAndWait()
    speaker.stop()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('started converting text to speech...')
        for file_path in sys.argv[1:]:
            tts(file_path)
            print(f'generated an mp3 file for - \'{file_path}\'')
        print('finished')
    else:
        file_path = input('enter a file path (relative or absolute: ')
        tts(file_path)
        print(f'generated an mp3 file for - \'{file_path}\'')