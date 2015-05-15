#!/bin/bash

original_file=error_log
part_size=40000
mkdir -p tmp

echo "getting head of $original_file..."
head -n $part_size $original_file > tmp/$original_file.head

echo "getting tail of $original_file..."
tail -n $part_size $original_file > tmp/$original_file.tail

echo "merging head, tail and preparing with prepare.py..."
cat tmp/$original_file.head tmp/$original_file.tail |\
../prepare.py > $original_file.mixed.prep
echo "$original_file.mixed.prep ready"

echo "cleaning-up..."
rm -rf tmp/
