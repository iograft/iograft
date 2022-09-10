# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class SortList(iograft.Node):
    """
    Sort the items of a list and output the updated list.
    """
    list_in = iograft.MutableInputDefinition("list")
    list_out = iograft.MutableOutputDefinition("list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("sort_list")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddOutput(cls.list_out)
        return node

    @staticmethod
    def Create():
        return SortList()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)

        # Sort and output the new list.
        list_out = sorted(list_in)
        iograft.SetOutput(self.list_out, data, list_out)


def LoadPlugin(plugin):
    node = SortList.GetDefinition()
    plugin.RegisterNode(node, SortList.Create)
