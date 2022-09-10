# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class GetListLength(iograft.Node):
    """
    Return the length of a list.
    """
    list_in = iograft.InputDefinition("list", iopythontypes.AnyList())
    length = iograft.OutputDefinition("length", iobasictypes.UnsignedInt())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_list_length")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddOutput(cls.length)
        return node

    @staticmethod
    def Create():
        return GetListLength()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)

        # Get the length of the list.
        length = len(list_in)
        iograft.SetOutput(self.length, data, length)


def LoadPlugin(plugin):
    node = GetListLength.GetDefinition()
    plugin.RegisterNode(node, GetListLength.Create)
