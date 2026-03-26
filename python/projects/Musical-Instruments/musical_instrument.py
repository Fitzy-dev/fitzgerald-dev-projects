# Jordan Fitzgerald
# 3/26/2026
# Musical Instrument

# This module defines a MusicalInstrument class with attributes for the instrument's name and type, as well as methods to play the instrument and get a fact about it. The class is then used to create instances of musical instruments and demonstrate their functionality.

class MusicalInstrument:
    def __init__(self, name, instrument_type):
        self.name = name
        self.instrument_type = instrument_type

    def play(self):
        print(f'The {self.name} is fun to play!')

    def get_fact(self):
        return f'The {self.name} is part of the {self.instrument_type} family of instruments.'


instrument_1 = MusicalInstrument('Oboe', 'woodwind')
instrument_2 = MusicalInstrument('Trumpet', 'brass')

instrument_1.play()
print(instrument_1.get_fact())

instrument_2.play()
print(instrument_2.get_fact())
