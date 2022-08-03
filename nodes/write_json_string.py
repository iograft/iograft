# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes
import json


class WriteJSONString(iograft.Node):
    """
    Serialize a dictionary object to a JSON string. This node can only
    serialize basic types, lists, and dictionaries.
    """
    contents = iograft.InputDefinition("contents", iopythontypes.Dict())
    json_string = iograft.OutputDefinition("json_string", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("write_json_string")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.contents)
        node.AddOutput(cls.json_string)
        return node

    @staticmethod
    def Create():
        return WriteJSONString()

    def Process(self, data):
        contents = iograft.GetInput(self.contents, data)

        # Serialize the contents to a string.
        json_string = json.dumps(contents)

        # Set the output filename.
        iograft.SetOutput(self.json_string, data, json_string)


def LoadPlugin(plugin):
    node = WriteJSONString.GetDefinition()
    plugin.RegisterNode(node, WriteJSONString.Create)
