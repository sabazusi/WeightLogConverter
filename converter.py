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
    # for filename in files:
        # convertable_logs.append(reader.read_as_convertable(filename)
    output = builder.build( map(reader.read_as_convertable, files) )
    print(output)
