# This file starts a new screen, and keeps the program running
# even when the ssh session has closed. This allows the program
# to keep running 24/7 and requires no human input
screen -dr ha -X quit
screen -dmS ha ./main.py
screen -r ha
