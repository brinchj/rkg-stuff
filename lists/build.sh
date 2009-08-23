#!/bin/sh

echo "Compiling '$1' with data from '$2'.."
./compile.py $* > html/$1.html &&
./compile-pdf.sh $1 && wait &&
echo "done."

