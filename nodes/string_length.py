# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes


class StringLength(iograft.Node):
    """
    Return the length of the string passed in.
    """
    string = iograft.InputDefinition("string", iobasictypes.String())
    length = iograft.OutputDefinition("length", iobasictypes.Int())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("string_length")
        node.SetMenuPath("General/String")
        node.AddInput(cls.string)
        node.AddOutput(cls.length)
        return node

    @staticmethod
    def Create():
        return StringLength()

    def Process(self, data):
        input_str = iograft.GetInput(self.string, data)
        iograft.SetOutput(self.length, data, len(input_str))


def LoadPlugin(plugin):
    node = StringLength.GetDefinition()
    plugin.RegisterNode(node, StringLength.Create)
