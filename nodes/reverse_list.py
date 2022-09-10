# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class ReverseList(iograft.Node):
    """
    Reverse the items of a list and output the reversed list.
    """
    list_in = iograft.MutableInputDefinition("list")
    list_out = iograft.MutableOutputDefinition("list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("reverse_list")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddOutput(cls.list_out)
        return node

    @staticmethod
    def Create():
        return ReverseList()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)

        # Output a new reversed list.
        list_in.reverse()
        iograft.SetOutput(self.list_out, data, list_in)


def LoadPlugin(plugin):
    node = ReverseList.GetDefinition()
    plugin.RegisterNode(node, ReverseList.Create)
