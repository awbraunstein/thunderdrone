import constants
import itertools
import tranny
import midi

current_scale = constants.Scale.LYDIAN_B7

def get_note_pitch_generator():
    chord_tranny = tranny.build_chord_tranny(current_scale)
    chord_gen = chord_tranny.get_generator()
    duration_tranny = tranny.build_duration_tranny()
    duration_gen = duration_tranny.get_generator()
    return itertools.izip(duration_gen, chord_gen)

def get_lead_generator(current_chord):
    note_tranny = tranny.build_note_tranny(current_scale, current_chord)
    note_gen = note_tranny.get_generator()
    duration_tranny = tranny.build_duration_tranny()
    duration_gen = duration_tranny.get_generator()
    return itertools.izip(duration_gen, note_gen)


def get_chord(chord_desc):
    split_chord = chord_desc.split('_', 1)
    if len(split_chord) != 2:
        raise Exception('Oh fuck!')
    transpose_factor = int(split_chord[0])
    note_list = constants.Chord.all_chords[split_chord[1]]
    return [n + transpose_factor for n in note_list]

def main():
    g = get_note_pitch_generator()
    track_r = midi.TrackConfig('Rythm Track')
    track_l = midi.TrackConfig('Lead Track')
    m = midi.Midi([track_r, track_l])
    time = 0
    while time < 1000:
        duration, chord_desc = g.next()
        pitches = get_chord(chord_desc)        
        lead_time = 0
        lg = get_lead_generator(pitches)        
        while True:
            lead_duration, lead_note = lg.next()
            lead_duration = lead_duration / 2
            lead_time += lead_duration
            if lead_time > duration:
                break
            m.append_note(lead_duration, [lead_note], track=1)
        time = m.append_note(duration, pitches)
    m.write_file('out.mid')
    return 0

if __name__ == '__main__':
    main()
