import random

from constants import Pitch
from constants import Note

class Tranny(object):
    def __init__(self, trans):
        is_valid = self.verify_trans(trans)
        if not is_valid:
            raise Exception('transformation is not valid')
        self.trans = trans


    def verify_trans(self, trans):
        for key in trans:
            probablity_tuples = trans[key]
            count = 0
            for (item, prob) in probablity_tuples:
                count += prob
            if count != 1:
                return False
        return True

    def get_generator(self):
        last = None
        last = self.get_next(last)
        yield last
        while True:
            last = self.get_next(last)
            yield last


    def get_next(self, prev):
        if prev is None:
            prev = random.choice(self.trans.keys())
        probablity_tuples = self.trans[prev]
        rand = random.random()
        count = 0
        for (item, prob) in probablity_tuples:
            count += prob
            if rand < count:
                return item

def build_pitch_tranny():
    trans = {
        Pitch.A: [(Pitch.A, .1), (Pitch.B, .1), (Pitch.C, .2), (Pitch.D, .2),
                  (Pitch.E, .2), (Pitch.F, .1), (Pitch.G, .1)],
        Pitch.B: [(Pitch.A, .1), (Pitch.B, .1), (Pitch.C, .2), (Pitch.D, .2),
                  (Pitch.E, .2), (Pitch.F, .1), (Pitch.G, .1)],
        Pitch.C: [(Pitch.A, .1), (Pitch.B, .1), (Pitch.C, .2), (Pitch.D, .2),
                  (Pitch.E, .2), (Pitch.F, .1), (Pitch.G, .1)],
        Pitch.D: [(Pitch.A, .1), (Pitch.B, .1), (Pitch.C, .2), (Pitch.D, .2),
                  (Pitch.E, .2), (Pitch.F, .1), (Pitch.G, .1)],
        Pitch.E: [(Pitch.A, .1), (Pitch.B, .1), (Pitch.C, .2), (Pitch.D, .2),
                  (Pitch.E, .2), (Pitch.F, .1), (Pitch.G, .1)],
        Pitch.F: [(Pitch.A, .1), (Pitch.B, .1), (Pitch.C, .2), (Pitch.D, .2),
                  (Pitch.E, .2), (Pitch.F, .1), (Pitch.G, .1)],
        Pitch.G: [(Pitch.A, .1), (Pitch.B, .1), (Pitch.C, .2), (Pitch.D, .2),
                  (Pitch.E, .2), (Pitch.F, .1), (Pitch.G, .1)]
        }

    return Tranny(trans)

def build_note_tranny():
    trans = {
        Note.WHOLE: [(Note.WHOLE, .25), (Note.HALF, .25), (Note.QUARTER, .25), (Note.EIGHTH, .25)],
        Note.HALF: [(Note.WHOLE, .25), (Note.HALF, .25), (Note.QUARTER, .25), (Note.EIGHTH, .25)],
        Note.QUARTER: [(Note.WHOLE, .25), (Note.HALF, .25), (Note.QUARTER, .25), (Note.EIGHTH, .25)],
        Note.EIGHTH: [(Note.WHOLE, .25), (Note.HALF, .25), (Note.QUARTER, .25), (Note.EIGHTH, .25)]
        }

    return Tranny(trans)

pitch_tranny = build_pitch_tranny()

note_tranny = build_note_tranny()
