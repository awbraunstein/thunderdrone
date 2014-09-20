import itertools
import tranny
import midi


def get_note_pitch_generator():
    note_gen = tranny.note_tranny.get_generator()
    pitch_gen = tranny.pitch_tranny.get_generator()
    return itertools.izip(note_gen, pitch_gen)

def main():
    g = get_note_pitch_generator()
    track = midi.TrackConfig('Sample Track')
    m = midi.Midi([track])
    time = 0
    while time < 1000:
        note, pitch = g.next()
        time = m.append_note(note, pitch)
    m.write_file('out.mid')
    return 0

if __name__ == '__main__':
    main()

