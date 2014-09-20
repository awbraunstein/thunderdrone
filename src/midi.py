import constants
from midiutil.MidiFile import MIDIFile

class TrackConfig(object):

    def __init__(self, name, time=0, tempo=120):
        self.name = name
        self.time = time
        self.tempo = tempo


class Midi(object):

    def __init__(self, track_configs):
        self.midi_file = MIDIFile(len(track_configs))
        self.track_time = []
        for i, config in enumerate(track_configs):
            self.track_time.append(0)
            self.midi_file.addTrackName(i, config.time, config.name)
            self.midi_file.addTempo(i, config.time, config.tempo)

    def append_note(self, note, pitch, volume=100, track=0, channel=0):
        duration = constants.NOTE_MAP[note]
        midi_pitch = constants.PITCH_MAP[pitch]
        time = self.track_time[track]
        self.midi_file.addNote(track, channel, midi_pitch, time, duration, volume)
        self.track_time[track] += duration
        return time

    def write_file(self, filename):
        binfile = open(filename, 'wb')
        self.midi_file.writeFile(binfile)
        binfile.close()
