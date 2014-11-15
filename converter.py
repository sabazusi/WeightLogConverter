#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converter

Usage:
converter.py [-h] (-m <mode>) (<files>...)

Options: 
<files>...  Choose Application WeightLog File.
-m <mode>   Choose Output File Application Type.
-h          Show Help Message.

"""

from docopt import docopt
from modules.logreader import ApplicationWeightLogReader
from modules.logbuilder import ApplicationWeightLogBuilder

if __name__ == '__main__':
    args = docopt(__doc__)
    mode = args["-m"]
    files = args["<files>"]

    reader = ApplicationWeightLogReader()
    builder = ApplicationWeightLogBuilder(mode)

    convartables = []
    for file in files:
        convartables.append(reader.read_as_convertable(file))

    output = builder.build(convartables)
    print(output)
