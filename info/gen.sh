#!/bin/bash
xelatex info.tex && \
convert -density 400 info.pdf -background white -alpha remove info.png

xelatex behold.tex && \
convert -density 400 behold.pdf -background white -alpha remove behold.png
