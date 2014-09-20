class Pitch:
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'
    G = 'g'

class Note:
    WHOLE = 'whole'
    HALF = 'half'
    QUARTER = 'quarter'
    EIGHTH = 'eighth'


PITCH_MAP = {
    Pitch.C: 60,
    Pitch.D: 62,
    Pitch.E: 64,
    Pitch.F: 65,
    Pitch.G: 67,
    Pitch.A: 69,
    Pitch.B: 71
    }

NOTE_MAP = {
    Note.WHOLE: 4,
    Note.HALF: 2,
    Note.QUARTER: 1,
    Note.EIGHTH: .5
    }
