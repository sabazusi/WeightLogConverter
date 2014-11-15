#!/usr/bin/env python
# -*- coding: utf-8 -*-

class WeightData:
    def __init__(self, date=-1, weight=-1, fat=-1):
        self.date = date
        self.weight = weight
        self.fat = fat
        self.isValid = (
            date != -1 and
            weight != -1 and
            fat != -1
        )
            
