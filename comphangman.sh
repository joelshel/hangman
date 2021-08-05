#!/usr/bin/bash

pyinstaller --onefile \
 --upx-dir="/bin" \
 --distpath="./comphangman/dist" \
 --workpath="./comphangman/build" \
 --specpath="./comphangman" \
 --hidden-import="PIL" \
 --collect-submodules="PIL" \
 --add-data="../src/words.txt:src" \
 --add-data="../img/hangman.png:img" \
 --add-data="../img/hangman_?.png:img" \
 --name="hangman" frontend.py
