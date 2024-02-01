import asyncio
from Function.remove_file import *
from Function.make_voice import *

VOICE = "en-AU-WilliamNeural"
BUFFER_SIZE = 1024

def speak(TEXT, output_file=None):
    if output_file is None:
        output_file = os.path.join(os.getcwd(), "speak.mp3")
        print(TEXT)
    asyncio.run(amain(TEXT, output_file))


