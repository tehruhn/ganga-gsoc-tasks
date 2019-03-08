#!usr/bin/env sh

pdftotext $1 - | sed -e 's/ /\n/g' | grep -ci 'the'
