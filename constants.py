"""Constants relating to MIDI data.

These constants are used by MIDI data operations.

I'm not convinced all of these are useful. It might be nice to tidy 
them up a bit and make it clear what they're all for.

"""
OCTAVE_MAX_VALUE = 12
OCTAVE_VALUES = range( OCTAVE_MAX_VALUE )

NOTE_NAMES = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
"""A set of names for each note in the 12-tet octave."""

WHITE_KEYS = [0, 2, 4, 5, 7, 9, 11]
"""Indices in the octave of the white notes on a piano keyboard."""

BLACK_KEYS = [1, 3, 6, 8, 10]
"""Indices in the octave of the black notes on a piano keyboard."""

NOTE_PER_OCTAVE = len( NOTE_NAMES )
NOTE_VALUES = range( OCTAVE_MAX_VALUE * NOTE_PER_OCTAVE )
NOTE_NAME_MAP_FLAT = {}
NOTE_VALUE_MAP_FLAT = []
NOTE_NAME_MAP_SHARP = {}
NOTE_VALUE_MAP_SHARP = []

for value in range( 128 ):
    noteidx = value % NOTE_PER_OCTAVE
    octidx = value / OCTAVE_MAX_VALUE
    name = NOTE_NAMES[noteidx]
    if len( name ) == 2:
        # sharp note
        flat = NOTE_NAMES[noteidx+1] + 'b'
        NOTE_NAME_MAP_FLAT['%s-%d' % (flat, octidx)] = value
        NOTE_NAME_MAP_SHARP['%s-%d' % (name, octidx)] = value
        NOTE_VALUE_MAP_FLAT.append( '%s-%d' % (flat, octidx) )
        NOTE_VALUE_MAP_SHARP.append( '%s-%d' % (name, octidx) )
        globals()['%s_%d' % (name[0] + 's', octidx)] = value
        globals()['%s_%d' % (flat, octidx)] = value
    else:
        NOTE_NAME_MAP_FLAT['%s-%d' % (name, octidx)] = value
        NOTE_NAME_MAP_SHARP['%s-%d' % (name, octidx)] = value
        NOTE_VALUE_MAP_FLAT.append( '%s-%d' % (name, octidx) )
        NOTE_VALUE_MAP_SHARP.append( '%s-%d' % (name, octidx) )
        globals()['%s_%d' % (name, octidx)] = value

BEATNAMES = ['whole', 'half', 'quarter', 'eighth', 'sixteenth', 'thiry-second', 'sixty-fourth']
BEATVALUES = [4, 2, 1, .5, .25, .125, .0625]
WHOLE = 0
HALF = 1
QUARTER = 2
EIGHTH = 3
SIXTEENTH = 4
THIRTYSECOND = 5
SIXTYFOURTH = 6

DEFAULT_MIDI_HEADER_SIZE = 14


CONTROL_MESSAGE_DICTIONARY = \
{0:'Bank Select, MSB',
 1:'Modulation Wheel',
 2:'Breath Controller',
 4:'Foot Controller',
 5:'Portamento Time',
 6:'Data Entry',
 7:'Channel Volume',
 8:'Balance',
 10:'Pan',
 11:'Expression Controller',
 12:'Effect Control 1',
 13:'Effect Control 2',
 16:'Gen Purpose Controller 1',
 17:'Gen Purpose Controller 2',
 18:'Gen Purpose Controller 3',
 19:'Gen Purpose Controller 4',
 32:'Bank Select, LSB',
 33:'Modulation Wheel',
 34:'Breath Controller',
 36:'Foot Controller',
 37:'Portamento Time',
 38:'Data Entry',
 39:'Channel Volume',
 40:'Balance',
 42:'Pan',
 43:'Expression Controller',
 44:'Effect Control 1',
 45:'Effect Control 2',
 48:'General Purpose Controller 1',
 49:'General Purpose Controller 2',
 50:'General Purpose Controller 3',
 51:'General Purpose Controller 4',
 64:'Sustain On/Off',
 65:'Portamento On/Off',
 66:'Sostenuto On/Off',
 67:'Soft Pedal On/Off',
 68:'Legato On/Off',
 69:'Hold 2 On/Off',
 70:'Sound Controller 1  (TG: Sound Variation;   FX: Exciter On/Off)',
 71:'Sound Controller 2   (TG: Harmonic Content;   FX: Compressor On/Off)',
 72:'Sound Controller 3   (TG: Release Time;   FX: Distortion On/Off)',
 73:'Sound Controller 4   (TG: Attack Time;   FX: EQ On/Off)',
 74:'Sound Controller 5   (TG: Brightness;   FX: Expander On/Off)',
 75:'Sound Controller 6   (TG: Decay Time;   FX: Reverb On/Off)',
 76:'Sound Controller 7   (TG: Vibrato Rate;   FX: Delay On/Off)',
 77:'Sound Controller 8   (TG: Vibrato Depth;   FX: Pitch Transpose On/Off)',
 78:'Sound Controller 9   (TG: Vibrato Delay;   FX: Flange/Chorus On/Off)',
 79:'Sound Controller 10   (TG: Undefined;   FX: Special Effects On/Off)',
 80:'General Purpose Controller 5',
 81:'General Purpose Controller 6',
 82:'General Purpose Controller 7',
 83:'General Purpose Controller 8',
 84:'Portamento Control (PTC)   (0vvvvvvv is the source Note number)   (Detail)',
 91:'Effects 1 (Reverb Send Level)',
 92:'Effects 2 (Tremelo Depth)',
 93:'Effects 3 (Chorus Send Level)',
 94:'Effects 4 (Celeste Depth)',
 95:'Effects 5 (Phaser Depth)',
 96:'Data Increment',
 97:'Data Decrement',
 98:'Non Registered Parameter Number (LSB)',
 99:'Non Registered Parameter Number (MSB)',
 100:'Registered Parameter Number (LSB)',
 101:'Registered Parameter Number (MSB)',
 120:'All Sound Off',
 121:'Reset All Controllers',
 122:'Local Control On/Off',
 123:'All Notes Off',
 124:'Omni Mode Off (also causes ANO)',
 125:'Omni Mode On (also causes ANO)',
 126:'Mono Mode On (Poly Off; also causes ANO)',
 127:'Poly Mode On (Mono Off; also causes ANO)'}

GM_INSTRUMENT_DICTIONARY =\
{0:"Acoustic Grand Piano",
 1:"Bright Acoustic Piano",
 2:"Electric Grand Piano",
 3:"Honky-tonk Piano",
 4:"Electric Piano 1",
 5:"Electric Piano 2",
 6:"Harpsichord",
 7:"Clavinet",
 8:"Celesta",
 9:"Glockenspiel",
 10:"Music Box",
 11:"Vibraphone",
 12:"Marimba",
 13:"Xylophone",
 14:"Tubular Bells",
 15:"Dulcimer",
 16:"Drawbar Organ",
 17:"Percussive Organ",
 18:"Rock Organ",
 19:"Church Organ",
 20:"Reed Organ",
 21:"Accordion",
 22:"Harmonica",
 23:"Tango Accordion",
 24:"Acoustic Guitar (nylon)",
 25:"Acoustic Guitar (steel)",
 26:"Electric Guitar (jazz)",
 27:"Electric Guitar (clean)",
 28:"Electric Guitar (mute)",
 29:"Overdriven Guitar",
 30:"Distortion Guitar",
 31:"Guitar Harmonics",
 32:"Acoustic Bass",
 33:"Electric Bass (finger)",
 34:"Electric Bass (pick)",
 35:"Fretless Bass",
 36:"Slap Bass 1",
 37:"Slap Bass 2",
 38:"Synth Bass 1",
 39:"Synth Bass 2",
 40:"Violin",
 41:"Viola",
 42:"Cello",
 43:"Contrabass",
 44:"Tremolo Strings",
 45:"Pizzicato Strings",
 46:"Orchestral Harp",
 47:"Timpani",
 48:"String Ensemble 1",
 49:"String Ensemble 2",
 50:"SynthStrings 1",
 51:"SynthStrings 2",
 52:"Choir Aahs",
 53:"Voice Oohs",
 54:"Synth Voice",
 55:"Orchestra Hit",
 56:"Trumpet",
 57:"Trombone",
 58:"Tuba",
 59:"Muted Trumpet",
 60:"French Horn",
 61:"Brass Section",
 62:"SynthBrass 1",
 63:"SynthBrass 2",
 64:"Soprano Sax",
 65:"Alto Sax",
 66:"Tenor Sax",
 67:"Baritone Sax",
 68:"Oboe",
 69:"English Horn",
 70:"Bassoon",
 71:"Clarinet",
 72:"Piccolo",
 73:"Flute",
 74:"Recorder",
 75:"Pan Flute",
 76:"Blown Bottle",
 77:"Shakuhachi",
 78:"Whistle",
 79:"Ocarina",
 80:"Lead 1 (square)",
 81:"Lead 2 (sawtooth)",
 82:"Lead 3 (calliope)",
 83:"Lead 4 (chiff)",
 84:"Lead 5 (charang)",
 85:"Lead 6 (voice)",
 86:"Lead 7 (fifths)",
 87:"Lead 8 (bass+lead)",
 88:"Pad 1 (new age)",
 89:"Pad 2 (warm)",
 90:"Pad 3 (polysynth)",
 91:"Pad 4 (choir)",
 92:"Pad 5 (bowed)",
 93:"Pad 6 (metallic)",
 94:"Pad 7 (halo)",
 95:"Pad 8 (sweep)",
 96:"FX 1 (rain)",
 97:"FX 2 (soundtrack)",
 98:"FX 3 (crystal)",
 99:"FX 4 (atmosphere)",
 100:"FX 5 (brightness)",
 101:"FX 6 (goblins)",
 102:"FX 7 (echoes)",
 103:"FX 8 (sci-fi)",
 104:"Sitar",
 105:"Banjo",
 106:"Shamisen",
 107:"Koto",
 108:"Kalimba",
 109:"Bag pipe",
 110:"Fiddle",
 111:"Shanai",
 112:"Tinkle Bell",
 113:"Agogo",
 114:"Steel Drums",
 115:"Woodblock",
 116:"Taiko Drum",
 117:"Melodic Tom",
 118:"Synth Drum",
 119:"Reverse Cymbal",
 120:"Guitar Fret Noise",
 121:"Breath Noise",
 122:"Seashore",
 123:"Bird Tweet",
 124:"Telephone Ring",
 125:"Helicopter",
 126:"Applause",
 127:"Gunshot"}
