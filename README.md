# Python-SpeechToText
Google Translate based python speech recognition CLI application that takes inputs as microphone recording and saves them in conversions folder.

It uses Python's SpeechRecognition module to read and generate texts. To install this module, run command pip install SpeechRecognition. Please download PyAudio from wheel file if required. 

Currently this program records and converts audio to Tamil words. This can be changed at line 35 on file SpeechToTextTamil.py where language parameter you could pass your desired language key which can be found at https://cloud.google.com/speech-to-text/docs/languages

run SpeechToTextTamil.py file to get converted files. Google Speech recognition API converts given Tamil Audio input into text file. Since it uses Google's API Internet is required.

you can create a new python exe bundle with this command "pyinstaller --onefile SpeechToTextTamil.py" from the current working directory of python file. After executing this command a bundled exe will be available in the dist folder which can be used or distributed to other windows users if needed.

Added PyInstaller in order to make it as an exe so that the users like schools or government offices don't need to bother about installing specific packages and python environments.
