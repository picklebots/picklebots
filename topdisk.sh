#!/bin/bash

DIR=$1
[ "$DIR" ] || DIR="/"

du -hx $DIR | sort -k1rh | head -10

