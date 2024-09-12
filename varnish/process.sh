#!/bin/bash
convert $1 -scale 7% -dither FloydSteinberg -colors 11 -resize 424x424 processed/$2
