# MBTA Metadata Generation

To regenerate the metadata, tags, etc. for all MBTA stuff for `data.py`, go to the website http://www.mbtainfo.com/ and copy HTML source of the *station list* of each of the Green, Red, Blue, and Orange lines into `green.txt`, `red.txt`, `blue.txt`, and `orange.txt` respectively. Then run

    python3 generate.py

and copy the output (stdout) to necessary place in `data.py`.
