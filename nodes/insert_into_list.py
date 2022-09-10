# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class InsertIntoList(iograft.Node):
    """
    Insert an item into a list at the given index and output
    the updated list.
    """
    list_in = iograft.MutableInputDefinition("list")
    item = iograft.MutableInputDefinition("item")
    index = iograft.InputDefinition("index", iobasictypes.Int())
    list_out = iograft.MutableOutputDefinition("list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("insert_into_list")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddInput(cls.item)
        node.AddInput(cls.index)
        node.AddOutput(cls.list_out)
        return node

    @staticmethod
    def Create():
        return InsertIntoList()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)
        item = iograft.GetInput(self.item, data)
        index = iograft.GetInput(self.index, data)

        # Insert the item and output the list.
        list_in.insert(index, item)
        iograft.SetOutput(self.list_out, data, list_in)


def LoadPlugin(plugin):
    node = InsertIntoList.GetDefinition()
    plugin.RegisterNode(node, InsertIntoList.Create)
