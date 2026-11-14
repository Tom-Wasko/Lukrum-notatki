#!/bin/sh
# Zrzut podglądu 4: zrzut.sh <nazwa> <szer,wys> "<parametry po #>"
C="/c/Program Files/Google/Chrome/Application/chrome.exe"
W="C:/Users/PC/Pulpit/Levas/lukrum/_robocze/wyglad"
MSYS_NO_PATHCONV=1 "$C" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=4000 "--screenshot=$W/zrzuty4/$1.png" --window-size=$2 "file:///$W/podglad4.html#$3" 2>&1 | grep -c "bytes written"
