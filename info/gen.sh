#!/bin/bash
xelatex info.tex && \
convert -density 400 info.pdf -background white -alpha remove info.png
