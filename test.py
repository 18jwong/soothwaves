import sys
import random
from midiutil import MIDIFile

midiName = sys.argv[1]
numNotes = int(sys.argv[2])

#			C   D   E   G   A   C
degrees  = [60, 62, 64, 67, 69, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

for i in range(numNotes):
	n = random.randint(0,len(degrees)-1)
	pitch = degrees[n]
	MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

# ex name: "major-scale.mid"
with open(midiName, "wb") as output_file:
    MyMIDI.writeFile(output_file)