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
    text = reader_func(file_path)
    text = text.replace('\n',' ' )
    # text = text.replace('\r', '')

    return text


def tts(file_path, speaker):
    file_name, file_extension = os.path.splitext(file_path)
    text = read_text(file_path, file_extension)
    speech_rate = speaker.getProperty('rate')
    speaker.setProperty('rate', speech_rate - 50)
    speaker.save_to_file(text, f'{file_name}_{file_extension[1:]}.mp3')
    speaker.runAndWait()
    speaker.stop()


def select_language(speaker):
    voices = speaker.getProperty('voices')
    lang_ind = -1
    while lang_ind <= 0 or lang_ind > len(voices):
        i = 1
        for voice in voices:
            print(f'{i}. {voice.name}')
            i += 1
        lang_ind = int(input(f'select voice from the options above (1-{len(voices)}): '))
    speaker.setProperty('voice', voices[lang_ind - 1].id)


if __name__ == '__main__':
    engine = pyttsx3.init()
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        index = 0
        if args[0] == '-L':
            select_language(engine)
            index += 1
        print('started converting text to speech...')
        for file_path in args[index:]:
            tts(file_path, engine)
            print(f'generated an mp3 file for - \'{file_path}\'')
        print('finished')
    else:
        file_path = input('enter a file path (relative or absolute: ')
        tts(file_path, engine)
        print(f'generated an mp3 file for - \'{file_path}\'')