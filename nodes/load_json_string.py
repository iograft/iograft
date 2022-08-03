# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes
import json


class LoadJSONString(iograft.Node):
    """
    Load a JSON object from a string.
    """
    json_string = iograft.InputDefinition("json_string", iobasictypes.String())

    # Allow comments in the JSON file being read. Requires the commentjson
    # module to be installed and available in the environment.
    allow_comments = iograft.InputDefinition("allow_comments",
                                             iobasictypes.Bool(),
                                             default_value=False)
    contents = iograft.OutputDefinition("contents", iopythontypes.Dict())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("load_json_string")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.json_string)
        node.AddInput(cls.allow_comments)
        node.AddOutput(cls.contents)
        return node

    @staticmethod
    def Create():
        return LoadJSONString()

    def Process(self, data):
        json_string = iograft.GetInput(self.json_string, data)
        allow_comments = iograft.GetInput(self.allow_comments, data)

        # If comments are allowed, use the commentjson library to read
        # the JSON file.
        if allow_comments:
            import commentjson
            contents = commentjson.loads(json_string)
        else:
            contents = json.loads(json_string)

        # Set the output data.
        iograft.SetOutput(self.contents, data, contents)


def LoadPlugin(plugin):
    node = LoadJSONString.GetDefinition()
    plugin.RegisterNode(node, LoadJSONString.Create)
