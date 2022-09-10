# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes


class GetListItem(iograft.Node):
    """
    Return the item at the given index of a list.
    """
    list_in = iograft.MutableInputDefinition("list")
    index = iograft.InputDefinition("index", iobasictypes.Int())
    item = iograft.MutableOutputDefinition("item")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_list_item")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddInput(cls.index)
        node.AddOutput(cls.item)
        return node

    @staticmethod
    def Create():
        return GetListItem()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)
        index = iograft.GetInput(self.index, data)

        # Extract the index from the list.
        item = list_in[index]
        iograft.SetOutput(self.item, data, item)


def LoadPlugin(plugin):
    node = GetListItem.GetDefinition()
    plugin.RegisterNode(node, GetListItem.Create)
