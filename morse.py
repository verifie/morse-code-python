# morse.py

# Dependencies: numpy, pygame
# pip install pygame

# Morse code is a method used in telecommunication to encode text characters as sequences of two different signal durations, called dots and dashes or dits and dahs.
# Morse code is named after Samuel Morse, an inventor of the telegraph.
# The International Morse Code encodes the 26 basic Latin letters A to Z, some non-Latin letters, the Arabic numerals and a small set of punctuation and procedural signals (prosigns) as standardized sequences of short and long signals called "dots" and "dashes", or "dits" and "dahs".
# Morse code is usually transmitted by on-off keying of an information-carrying medium such as sound waves, visible light, electric current, or radio waves.
# The duration of a dash is three times the duration of a dot.
# Each dot or dash is followed by a short silence, equal to the dot duration.
# The letters of a word are separated by a space equal to three dots (one dash), and the words are separated by a space equal to seven dots.
# Source: https://en.wikipedia.org/wiki/Morse_code


# ========================================================================================
# String to convert to morse code
text = "This is a morse code program that I coded in 2024 in Python as a bit of fun and a learning tool"

# Define the duration of a dot in milliseconds 
# The dashes and pauses are multiples of this value and are calculated automatically.
dot_time = 42

# This adjusts the silence time between the beeps, letters and words.
# It sounds about right, but would be best measured with an oscilloscope for accuracy.
sleep_divide_time = 300 

# Frequency of the beep sound in Hz (typically 1000)
pitch_frequency = 2000  


# Import modules
import time
import pygame
import numpy as np

# ========================================================================================
# Announce
print("\n\n")
print("Morse Code Generator")
print("====================\n\n")

# ========================================================================================
# Code to play beep sound

# Initialize the mixer module
pygame.mixer.init()

# Create a sound buffer with a given frequency and duration
# Function to generate a beep sound
def generate_beep(frequency, duration):
    sample_rate = 44100  # Sample rate in Hz
    n_samples = int(sample_rate * duration / 1000.0)  # Convert duration from milliseconds to samples

    # Generate a waveform array
    t = np.linspace(0, duration / 1000.0, n_samples, endpoint=False)
    waveform = np.sin(2 * np.pi * frequency * t)

    # Convert waveform to 16-bit signed integers
    waveform = np.int16(waveform * 32767)

    # Repeat the waveform in 2 columns for stereo (left and right channels)
    stereo_waveform = np.column_stack((waveform, waveform))

    # Create the sound object from the stereo waveform
    sound = pygame.mixer.Sound(buffer=stereo_waveform)
    return sound



# ========================================================================================
# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': ' '
}

# ========================================================================================
# Morse code timing dictionary
morse_timing = {
    '.': 1, '-': 3, ' ': 1
}


# ========================================================================================
# Convert text to morse code
def text_to_morse(text):
    morse = ' '
    for char in text:
        morse += morse_code[char.upper()] + '|'
    return morse

# ========================================================================================
# Convert text to morse code
def text_to_morse_and_letter(text):
    morse = ''
    for char in text:
        morse += " | " + str(char) + " " + str(morse_code[char.upper()])
    return morse

# ========================================================================================
# Convert text to morse code
def convert_to_morse(text):

    # Convert text to morse code
    morse = text_to_morse(text)


    print(" ", end='', flush=True)

    # Play out the morse code
    for char in morse:

        if char == '.':
            print(".", end='', flush=True) # Print the character, but stay on the same line for the next character
            
            beep = generate_beep(pitch_frequency, dot_time)  # frequency, ms duration
            beep.play()
            # Keep the script running long enough for the sound to play
            time.sleep(dot_time/sleep_divide_time)

        elif char == '-':
            print("-", end='', flush=True) # Print the character, but stay on the same line for the next character
            
            beep = generate_beep(pitch_frequency, (dot_time*3))  # frequency, ms duration
            beep.play()
            time.sleep(dot_time/sleep_divide_time)

        elif char == '|':
            print("|", end='', flush=True) # Print the character, but stay on the same line for the next character
            time.sleep((dot_time*2)/sleep_divide_time) 
            # Note we already add one pause after the letter, so we simply add 2 
            # more pauses to make it 3 pauses, compliant with a letter separation.

        elif char == ' ':
            time.sleep((dot_time*6)/sleep_divide_time)
            print(" ", end='', flush=True) # Print the character, but stay on the same line for the next character
            # Note we already add one pause after the letter, so we simply add 6 
            # more pauses to make it 7 pauses, compliant with a word separation.

    print("\n\n")


# ========================================================================================
# Run the morse code Program

print("================================================================================")
print("Morse Code Dictionary: ")
for key, value in morse_code.items():
    print("  ", key, ":", value, end='', flush=True)  


print("================================================================================")
print("Text to convert to morse code: ", text, "\n")
print("Conversion: \n\n  ", text_to_morse_and_letter(text), "\n")
print("\n", text_to_morse(text), "\n\n")

print("================================================================================\n")
print("Morse play out: \n")
convert_to_morse(text)
