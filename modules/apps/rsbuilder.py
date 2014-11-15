#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class RecStyleLogBuilder:
    def __init__(self):
        nowstr = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
        self.output_filename = nowstr + ".csv"

    def build(self, convertables_logs):
        seq_dict = {}
        for convertable in convertables_logs:
            date = "/".join(list(map(lambda x: x if not x.startswith('0') else x[1:], convertable.date.split("/"))))
            seq_dict[convertable.date] = [convertable.weight, "-", "-", convertable.fat, "-", "-", "-", "-", "-", "-"]

        result = []
        for date,value in seq_dict.items():
            value.insert(0, date)
            log = list(map(lambda x:"\""+x+"\"", value))
            result.append(",".join(log))

        result.sort()
        date_formatted_result = []
        for log in result:
            data = log.split(",")
            data[0] = "/".join(list(map(lambda x: x if not x.startswith('0') else x[1:], data[0].split("/"))))
            date_formatted_result.append(",".join(data))
        return date_formatted_result
