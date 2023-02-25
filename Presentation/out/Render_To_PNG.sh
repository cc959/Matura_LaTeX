#!/bin/sh
rm ./renders/*
convert -gamma 0.45454545454 -density 600 -resize x1440 ./main.pdf ./renders/Slide_%d.png
#for file in ./renders/*.png; do convert "$file" -colorspace sRGB "${file%.*}_srgb.png"; done


