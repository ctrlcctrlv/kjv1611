#!/bin/bash
fontforge -lang=py -script script.txt
rm *.ttx
# We use TTX to clean up the font after building it…
ttx KJV1611.otf
rm KJV1611.otf
ttx KJV1611.ttx
# …and also generate a WOFF, if posssible
hash sfnt2woff 2>/dev/null && sfnt2woff KJV1611.otf
# Prompt to install / overwrite
#read -e -p "Install? [y/N] " -i "N" INSTALL
INSTALLDIR=$HOME/.fonts/k
if [[ "$INSTALL" =~ ^[Yy]$ ]]; then
    mkdir -p $INSTALLDIR
    cp KJV1611.otf $INSTALLDIR
    >&2 echo "Installed"
fi
