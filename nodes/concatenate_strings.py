# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes


class ConcatenateStrings(iograft.Node):
    """
    Concatenate two strings.
    """
    string = iograft.InputDefinition("string", iobasictypes.String())
    string2 = iograft.InputDefinition("string2", iobasictypes.String())
    output = iograft.OutputDefinition("output", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("concatenate_strings")
        node.SetMenuPath("General/String")
        node.AddInput(cls.string)
        node.AddInput(cls.string2)
        node.AddOutput(cls.output)
        return node

    @staticmethod
    def Create():
        return ConcatenateStrings()

    def Process(self, data):
        string = iograft.GetInput(self.string, data)
        string2 = iograft.GetInput(self.string2, data)

        result = string + string2

        # Set the output value.
        iograft.SetOutput(self.output, data, result)


def LoadPlugin(plugin):
    node = ConcatenateStrings.GetDefinition()
    plugin.RegisterNode(node, ConcatenateStrings.Create)
