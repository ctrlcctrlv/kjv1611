import fontforge

font = fontforge.activeFont()

def get_em_size(font):
    return font[ord('M')].width

def get_period_size(font):
    return font[ord('.')].width

M = get_em_size(font)

Spaces = dict()

# Em space
uni2003 = M
uni2001 = uni2003
Spaces[0x2003] = uni2003
Spaces[0x2001] = uni2001

# en space
uni2002 = M // 2
uni2000 = uni2002
Spaces[0x2002] = uni2002
Spaces[0x2000] = uni2000

# thick space
uni2004 = M // 3
Spaces[0x2004] = uni2004

# middling space
uni2005 = M // 4
Spaces[0x2005] = uni2005

# thin space
uni2009 = M // 5
uni202f = uni2009
Spaces[0x2009] = uni2009
Spaces[0x202f] = uni202f

# hair space
uni200a = M // 10
Spaces[0x200a] = uni200a

# six per em space
uni2006 = M // 6
Spaces[0x2006] = uni2006

# punctuation space
Period = get_period_size(font)
uni2008 = Period
Spaces[0x2008] = uni2008

# zero width space
uni200b = 0
Spaces[0x200b] = uni200b

# medium mathematical space
uni205f = int(M * (4/18))
Spaces[0x205f] = uni205f

