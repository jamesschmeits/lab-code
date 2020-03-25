"""Directory monitor to watch for new files"""

import os
import time

path_to_watch = "."
before = dict([(f, None) for f in os.listdir(path_to_watch)])
while 1:
    time.sleep(5)
    after = dict([(f, None) for f in os.listdir(path_to_watch)])
    added = [f for f in after if f not in before]
    removed = [f for f in before if f not in after]
    if added:
        print("Added: {}".format(added))
    if removed:
        print("Removed: {}".format(removed))
    before = after
