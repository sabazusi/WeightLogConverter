#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class SimpleDietLogBuilder:
    def __init__(self):
        nowstr = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
        self.output_filename = nowstr + ".csv"

    def build(self, convertables_logs):
        seq_dict = {}
        for convertable in convertables_logs:
            seq_dict[convertable.date] = ",".join([convertable.weight, convertable.fat, "", "", "", "", "", ""])

        result = []
        for date, value in seq_dict.items():
            result.append(date + " 0:00:00," + value)

        result.sort()
        return result
