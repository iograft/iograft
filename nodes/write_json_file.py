# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes
import json


class WriteJSONFile(iograft.Node):
    """
    Write a dictionary object to a JSON file. This node can only serialize
    basic types, lists, and dictionaries.
    """
    json_file = iograft.InputDefinition("json_file", iobasictypes.Path())
    contents = iograft.InputDefinition("contents", iopythontypes.Dict())
    out_json_file = iograft.OutputDefinition("json_file", iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("write_json_file")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.json_file)
        node.AddInput(cls.contents)
        node.AddOutput(cls.out_json_file)
        return node

    @staticmethod
    def Create():
        return WriteJSONFile()

    def Process(self, data):
        json_file = iograft.GetInput(self.json_file, data)
        contents = iograft.GetInput(self.contents, data)

        # Open the file and write the contents.
        with open(json_file, "w") as f:
            json.dump(contents, f)

        # Set the output filename.
        iograft.SetOutput(self.out_json_file, data, json_file)


def LoadPlugin(plugin):
    node = WriteJSONFile.GetDefinition()
    plugin.RegisterNode(node, WriteJSONFile.Create)
