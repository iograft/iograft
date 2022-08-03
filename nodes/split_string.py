# Copyright 2022 Fabrica Software, LLC

from operator import delitem
import os

import iograft
import iobasictypes


class SplitString(iograft.Node):
    """
    Split a a string with the given delimeter. Optionally can provide a
    maximum number of times to split.
    """
    string = iograft.InputDefinition("string", iobasictypes.String())

    # Delimiter to use to split the string. By default, this is any
    # whitespace.
    delimiter = iograft.InputDefinition("delimiter", iobasictypes.String(),
                                        default_value="")

    # Maximum number of times to split the string. Defaults to -1 meaning
    # that there is no limit.
    max_splits = iograft.InputDefinition("max_splits", iobasictypes.Int(),
                                         default_value=-1)

    substrings = iograft.OutputDefinition("substrings",
                                          iobasictypes.StringList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("split_string")
        node.SetMenuPath("General/String")
        node.AddInput(cls.string)
        node.AddInput(cls.delimiter)
        node.AddInput(cls.max_splits)
        node.AddOutput(cls.substrings)
        return node

    @staticmethod
    def Create():
        return SplitString()

    def Process(self, data):
        # Get the inputs.
        string = iograft.GetInput(self.string, data)
        delimiter = iograft.GetInput(self.delimiter, data)
        max_splits = iograft.GetInput(self.max_splits, data)

        # Split the string.
        if delimiter:
            substrings = string.split(delimiter, max_splits)
        else:
            substrings = string.split(maxsplit=max_splits)

        # Set the output value.
        iograft.SetOutput(self.substrings, data, substrings)


def LoadPlugin(plugin):
    node = SplitString.GetDefinition()
    plugin.RegisterNode(node, SplitString.Create)
