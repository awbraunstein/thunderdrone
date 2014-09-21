C3 = 60
    
class Duration:
    WHOLE = 4
    HALF = 2
    QUARTER = 1
    EIGHTH = .5

class Scale:
    MAJOR = [0,2,4,5,7,9,11]
    MINOR = [0,2,3,5,7,9,10]
    BLUES = [0,3,5,6,7,10]
    LYDIAN_B7 = [0,2,4,6,7,9,10,12]

"""
Scale /Hungarian_Gypsy 0 2 3 6 7 8 10");
Scale Hungarian_Minor 0 2 3 6 7 8 11");
Scale Hungarian_Major 0 3 4 6 7 9 10");
Scale Whole_Tone 0 2 4 6 8 10");
Scale Blues 0 3 5 6 7 10");
Scale Pentatonic 0 2 4 7 9");
Scale Harmonic_Minor 0 2 3 5 7 8 11");
Scale Ascending_Melodic_Minor 0 2 3 5 7 9 11");
Scale Lydian-Augmented 0 2 4 6 8 9 11");
Scale Lydian_b7 0 2 4 6 7 9 10 12");
Scale Locrian_#2 0 2 3 5 6 8 10");
Scale Super_Locrian 0 1 3 4 6 8 10");
Scale Bop 0 2 4 5 7 8 9 11");
Scale Egyptian 0 2 5 7 10");
Scale Phrygian_Dominant 0 1 4 5 7 8 10");
"""

class Chord:
    all_chords = {
	'MAJOR_TRIAD': [0,4,7],
        'MINOR_TRIAD': [0,3,7],
        'AUG_TRIAD': [0,4,8],
        'DIM_TRIAD': [0,3,6],
	'DIM_7TH': [0,3,6,9],
	'HALF_DIMINISHED_7TH': [0,3,6,10],
        'MINOR_7TH': [0,3,7,10],
        'MINOR_MAJOR_7TH': [0,3,7,11],
        'DOM_7TH': [0,4,7,10],
        'MAJOR_7TH': [0,4,7,11],
	'AUG_7TH': [0,4,8,10],
	'AUG_MAJ_7TH': [0,4,8,11]
        }
