#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.apps import WeightData

class SimpleDietLogParser:
    def parse(self, file, postfix):
        result = []
        for line in file:
            data = self._get_data_from_line(line, postfix)
            if data.isValid:
                result.append(data)
        return result

    def _get_data_from_line(self, line, postfix):
        colums = line.split(postfix)

        if not len(colums) == 9:
            return WeightData()

        date = colums[0].split(" ")[0]
        weight = colums[1]
        fat = colums[2] 

        if "" in [date, weight, fat]:
            return WeightData()
        
        return WeightData(date, weight, fat)
