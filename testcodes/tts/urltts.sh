#!/bin/bash

say(){

mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en-us&q=$*";

}

say $*
