#!/usr/bin/env python
### Test all bib files
### Requires installation of github.com/personalrobotics/prl-website

from personalrobotics.main.publications import RenderableEntry
import os
import sys

import pybtex.database

if __name__ == "__main__":
  bibdir = os.path.dirname(os.path.realpath(__file__))
  for filename in os.listdir(bibdir):
    if not filename.endswith('.bib'):
      continue
    print("Checking Bib File: " + filename)

    with open(os.path.join(bibdir, filename), 'r') as file:
      try:
        database = pybtex.database.parse_string(file.read(), "bibtex")
        entries = [RenderableEntry("Publication", e) for e in database.entries.values()]
        for entry in entries:
          entry.__str__()
      except Exception as e:
        print(type(e))
        print(e.args)
        print(e)
        sys.exit(-1)

