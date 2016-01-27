#!/bin/bash

echo "Google TTS Engine Testing ..."
echo

echo "Text : "
read text

./urltts.sh $text
