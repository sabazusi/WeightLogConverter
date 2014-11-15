#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.apps import WeightData

class RecStyleLogParser:
    def parse(self, file, postfix):
        result = []
        for line in file:
            data = self._get_data_from_line(line, postfix)
            if data.isValid:
                result.append(data)
        return result

    def _get_data_from_line(self, line, postfix):
        colums = line.split(postfix)

        if not len(colums) == 11:
            return WeightData()
        if "Date" in colums[0]:
            return WeightData()

        date = "/".join(list(map(lambda x:x.zfill(2), colums[0][1:-1].split("/"))))
        weight = colums[1]
        fat = colums[4] 

        if "\"-\"" in [date, weight, fat]:
            return WeightData()
        
        return WeightData(date, weight, fat)
