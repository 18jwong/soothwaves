# soothwaves

soothwaves was my CruzHacks hackathon project that would generate music based on the major pentatonic scale with the intent of providing some relaxing music that people could easily generate. I ended up not submitting this project upon discovering [Magenta](https://magenta.tensorflow.org/), a research project that uses machine learning to generate music and art. In the end, I was glad to have been able to participate in this hackathon since I was able to be exposed to so many technologies, such as machine learning and AWS.

## Getting Started

My project makes use of midiutil and can be installed using the following command.

pip install midiutil

## Usage

python soothwaves.py <output_file_name> <number_of_notes>

ex: soothwaves.py myMidiFile.mid 30

Be sure to include .mid at the end of your file name.
