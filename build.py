import fontforge
import psMat
import unicodedata
font = fontforge.open("KJV1611.sfd")

font.encoding = "UnicodeBMP"

import spaces
for k in spaces.Spaces.keys():
    font.createChar(k)
for k, v in spaces.Spaces.items():
    font[k].width = v

scPUA = 0xE500
smallcaps = list()

def createSC(font, glyph, scPUA):
    font.selection.select(glyph)
    font.copyReference()
    font.createChar(scPUA)
    font.selection.select(scPUA)
    font.paste()
    font[scPUA].transform(psMat.scale(0.78))
    font[scPUA].glyphname = glyph.glyphname + '.sc'

for glyph in font.glyphs():
    enc = chr(glyph.encoding)
    if unicodedata.category(enc) == "Lu":
        print(enc, hex(ord(enc)))
        createSC(font, glyph, scPUA)
        smallcaps.append((enc, glyph.glyphname))
        scPUA+=1

scfea = open("smallcaps.fea", "w+")
scfea.write("languagesystem DFLT dflt; languagesystem latn dflt; languagesystem grek dflt; languagesystem cyrl dflt;")
scfea.write("feature c2sc {\n\tlookup c2sc1 {\n")
for sc in smallcaps:
    scfea.write("\t\tsub {0} by {0}.sc;\n".format(sc[1]))
scfea.write("\t} c2sc1;\n} c2sc;")
scfea.close()

font.selection.select(("unicode","ranges"),0xE000,0xE0FF)
font.clear()
font.selection.all()
font.unlinkReferences()
font.removeOverlap()
font.mergeFeature("features.fea")
font.mergeFeature("smallcaps.fea")
font.generate("KJV1611.otf", flags=("opentype", "no-hints", "no-flex"))
