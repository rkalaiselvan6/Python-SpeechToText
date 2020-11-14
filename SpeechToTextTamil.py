  
#!/usr/bin/env python3

import speech_recognition as sr
from datetime import datetime
from os import path,makedirs

# use the audio file as the audio source
r = sr.Recognizer()

# can be used to load audio from file
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "tamil_sample.wav")
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file

# get audio from microphone
with sr.Microphone() as source:
    print("Vanakkam! Talk without long pause...")
    audio = r.listen(source)
    print("Time over, thanks")

# recognize speech using Google Speech Recognition
try:
    now = datetime.now()
    file_path = path.join(path.curdir, 'Conversions')
    #check if path exists else create one
    if not path.exists(file_path):
        makedirs(file_path)
    #adding timestamps to differentiate multiple files
    file_name = path.join(file_path,f'converted_tamil_text_{now.strftime("%d_%M_%Y_%H_%M_%S")}.txt')

    with open(path.abspath(file_name), mode='w', encoding="utf-8") as f:
        #uncomment this below line in order to get more translation related details from googletranslate api
        # converted_str = r.recognize_google(audio, language = 'ta-IN',show_all=True)
        converted_str = r.recognize_google(audio, language = 'ta-IN')
        f.write(converted_str)
        # print(f"Google Speech Recognition thinks you said {converted_str}")
except sr.UnknownValueError:
    print("Could not understand audio, Please try to speak clearly!")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
