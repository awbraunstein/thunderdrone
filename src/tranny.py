import random
from constants import Chord
from constants import Duration
from constants import Scale


def eq(a, b, eps=0.0001):
    return abs(a - b) <= eps

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
            if not eq(count, 1.0):
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

def build_duration_tranny():
    trans = {
        Duration.WHOLE: [(Duration.WHOLE, .10), (Duration.HALF, .25), (Duration.QUARTER, .30), (Duration.EIGHTH, .35)],
        Duration.HALF: [(Duration.WHOLE, .15), (Duration.HALF, .3), (Duration.QUARTER, .3), (Duration.EIGHTH, .25)],
        Duration.QUARTER: [(Duration.WHOLE, .15), (Duration.HALF, .20), (Duration.QUARTER, .4), (Duration.EIGHTH, .25)],
        Duration.EIGHTH: [(Duration.WHOLE, .1), (Duration.HALF, .15), (Duration.QUARTER, .25), (Duration.EIGHTH, .50)]
        }

    return Tranny(trans)

def build_chord_tranny(scale):
    """First order markov chain for chords based on notes in each scale.

    For each note in my scale:
    - iterate through each chord
    if the chord exists in the scale
    """
    all_chords = _get_matching_chords(scale)
    tranny = {}
    for key_chord in all_chords:
        tranny[key_chord] = _generate_tranny_row(key_chord, all_chords)
    return Tranny(tranny)


def _generate_tranny_row(key_chord, all_chords):
    points = list()
    for curr_chord in all_chords:
	# TODO subtract points for same chord
	similar_name_tokens = _get_similar_name_tokens(key_chord, curr_chord)
	similar_notes = len([x for x in key_chord if x in curr_chord])**2
        points.append(similar_name_tokens + similar_notes) #TODO add weights
    total_points = sum(points)
    tranny_row = list()
    for curr_chord, point_value in zip(all_chords, points):
	tranny_row.append((curr_chord, point_value / float(total_points)))

    return tranny_row

def _get_similar_name_tokens(key_chord, curr_chord):
    count = 0
    for curr_chord_token in curr_chord.split('_'):
	if curr_chord_token in key_chord:
	    count += 1
    return count

def _get_matching_chords(scale):
    good_chords = dict()
    for curr_note in scale: # for each note in scale
        for k,v in Chord.all_chords.iteritems(): # for each chord
            transposed_scale = sorted([(n - curr_note) % 12 for n in scale])
            chord_matches_scale = all([chord_note in transposed_scale for chord_note in v])
            if chord_matches_scale:
                transposed_chord = sorted([(n + curr_note) % 12 for n in v])
                good_chords[str(curr_note) + "_" + k] = transposed_chord
    return good_chords
