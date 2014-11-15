#!/usr/bin/env python
# -*- coding: utf-8 -*-

from modules.apps.sdbuilder import SimpleDietLogBuilder
from modules.apps.rsbuilder import RecStyleLogBuilder

class ApplicationWeightLogBuilder:
    def __init__(self, mode):
        self.builder = self._get_builder(mode)

    def _get_builder(self, mode):
        if mode == "sd":
            return SimpleDietLogBuilder()
        elif mode == "rs":
            return RecStyleLogBuilder()
        else:
            return None

    def build(self, convartables_logs):
        if not self.builder:
            print("Log Builder has not found.")
            return

        print("Building import file...")

        output_data = self.builder.build(convartables_logs)
        file = open(self.builder.output_filename, "w")
        for data in output_data:
            file.writelines(data + "\n")

        file.close()
        print("Convert Finished! -> " + self.builder.output_filename)
