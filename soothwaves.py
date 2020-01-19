import sys
import random
import math
from midiutil import MIDIFile

midiName = sys.argv[1]
numNotes = int(sys.argv[2])

#			C   D   E   G   A   C
degrees  = [60, 62, 64, 67, 69, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 240   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(2)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i in range(numNotes):
	n = random.randint(0,len(degrees)-1)
	pitch = degrees[n]
	MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

numChords = math.floor(numNotes/4)
degrees  = [48, 50, 52, 55, 57, 60] 
track    = 1
channel  = 0
time     = 0    # In beats
duration = 4    # In beats
for i in range(numChords):
	n = random.randint(0,len(degrees)-1)
	pitch = degrees[n]
	MyMIDI.addNote(track, channel, pitch, time + i*4, duration, volume)

# ex name: "major-scale.mid"
try:
	output_file = open(midiName, "wb")
	MyMIDI.writeFile(output_file)
except:
	print("soothwaves.py error: make sure the midi file isn't open")