import constants
import itertools
import tranny
import midi


def get_note_pitch_generator():
    chord_tranny = tranny.build_chord_tranny(constants.Scale.BLUES)
    duration_tranny = tranny.build_duration_tranny()    
    duration_gen = duration_tranny.get_generator()
    chord_gen = chord_tranny.get_generator()
    return itertools.izip(duration_gen, chord_gen)

def get_chord(chord_desc):
    split_chord = chord_desc.split('_', 1)
    if len(split_chord) != 2:
        raise Exception('Oh fuck!')
    transpose_factor = int(split_chord[0])
    note_list = constants.Chord.all_chords[split_chord[1]]
    return [n + transpose_factor for n in note_list]

def main():
    g = get_note_pitch_generator()
    track = midi.TrackConfig('Sample Track')
    m = midi.Midi([track])
    time = 0
    while time < 1000:
        duration, chord_desc = g.next()
        pitches = get_chord(chord_desc)
        time = m.append_note(duration/2.0, pitches)
    m.write_file('out.mid')
    return 0

if __name__ == '__main__':
    main()



