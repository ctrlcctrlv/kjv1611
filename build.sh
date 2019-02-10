#!/bin/bash
# We use TTX to clean up the font after building it…
# Why `-x GPOS`? See https://github.com/fontforge/fontforge/issues/3415
fontforge -lang=py -script script.txt
rm *.ttx
ttx -x GPOS KJV1611.otf
rm KJV1611.otf
ttx KJV1611.ttx
# …and also generate a WOFF, if posssible
hash sfnt2woff 2>/dev/null && sfnt2woff KJV1611.otf
