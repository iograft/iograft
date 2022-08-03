# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes
import json


class LoadJSONFile(iograft.Node):
    """
    Load a JSON object from file.
    """
    json_file = iograft.InputDefinition("json_file", iobasictypes.Path())

    # Allow comments in the JSON file being read. Requires the commentjson
    # module to be installed and available in the environment.
    allow_comments = iograft.InputDefinition("allow_comments",
                                             iobasictypes.Bool(),
                                             default_value=False)
    contents = iograft.OutputDefinition("contents", iopythontypes.Dict())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("load_json_file")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.json_file)
        node.AddInput(cls.allow_comments)
        node.AddOutput(cls.contents)
        return node

    @staticmethod
    def Create():
        return LoadJSONFile()

    def Process(self, data):
        json_file = iograft.GetInput(self.json_file, data)
        allow_comments = iograft.GetInput(self.allow_comments, data)

        # Open the file and read in the JSON contents.
        with open(json_file) as f:
            # If comments are allowed, use the commentjson library to read
            # the JSON file.
            if allow_comments:
                import commentjson
                contents = commentjson.load(f)
            else:
                contents = json.load(f)

        # Set the output data.
        iograft.SetOutput(self.contents, data, contents)


def LoadPlugin(plugin):
    node = LoadJSONFile.GetDefinition()
    plugin.RegisterNode(node, LoadJSONFile.Create)
