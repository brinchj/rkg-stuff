#!/bin/sh
firefox -print `pwd`/html/$1.html -printmode pdf -printfile `pwd`/compiled/$1.pdf
