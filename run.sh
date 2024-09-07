#!/bin/bash
python3 bsky.py bcache
python3 bsky.py ffollowers
python3 bsky.py fallmypostlikes

# Usage: 
# create a urlwatch.txt
# add links (one per line) to posts you want
# to track and follow who liked them
URL_FILE="urlwatch.txt"
COMMAND="python3 bsky.py fpostlikes -e"

while IFS= read -r url; do
    echo "Running for $url"
    $COMMAND $url
done < "$URL_FILE"

