import constants
import tranny

class Generator(object):

    def __init__(self, tranny):
        self.tranny = tranny

    def generate_list(self, size=10):
        seq = []
        if size == 0:
            return seq
        seq.append(self.tranny.get_next(None))
        for _ in range(size - 1):
            seq.append(self.tranny.get_next(seq[-1]))
        return seq


g = Generator(tranny.note_tranny)
print str(g.generate_list(20))
            
