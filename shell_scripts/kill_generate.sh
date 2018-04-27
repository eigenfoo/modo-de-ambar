# helper script to kill generate.py

pgrep -f 'python generate.py' | xargs kill -9
