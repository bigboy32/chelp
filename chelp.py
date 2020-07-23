import webbrowser
import sys

full_str = ""
for item in sys.argv:
    if sys.argv.index(item) != 0:
        full_str += sys.argv[sys.argv.index(item)] + "+"
webbrowser.open("https://stackoverflow.com/search?q=" + full_str)
