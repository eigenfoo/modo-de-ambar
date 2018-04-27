# helper script to kill play.py

pgrep -f 'python play.py' | xargs kill -9
