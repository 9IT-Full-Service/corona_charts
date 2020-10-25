#!/bin/sh

DATUM=$(date +%Y-%m-%d-%H-%M-%S)

curl -s -o /home/rpr/coronacharts/fetchdm/data/${DATUM}.json "https://products.dm.de/store-availability/DE/availability?dans=595420,708997,137425,28171,485698,799358,863567,452740,610544,846857,709006,452753,879536,452744,485695,853483,594080,504606,593761,525943,842480,535981,127048,524535&storeNumbers=2475"

for i in $(cat /home/rpr/coronacharts/fetchdm/data/${DATUM}.json | jq '.storeAvailabilities' | jq 'to_entries[]' | jq '.[] | arrays | .[] ' | jq '.stockLevel');
do
  # let X=$X+$i;
  X=$(expr $X + $i)
done
rm /home/rpr/coronacharts/fetchdm/data/*
curl -s http://localhost:4006/api/v1/klopapier/${DATUM}/${X}

echo "${DATUM}: curl -s http://localhost:4006/api/v1/klopapier/${DATUM}/${X}" >> /home/rpr/coronacharts/fetchdm/logs/fetch.log
