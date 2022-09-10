# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class RemoveListItem(iograft.Node):
    """
    Remove the given item from a list and output the updated list with the
    item removed.
    """
    list_in = iograft.MutableInputDefinition("list")
    item = iograft.MutableInputDefinition("item")
    list_out = iograft.MutableOutputDefinition("list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("remove_list_item")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddInput(cls.item)
        node.AddOutput(cls.list_out)
        return node

    @staticmethod
    def Create():
        return RemoveListItem()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)
        item = iograft.GetInput(self.item, data)

        # Remove the first instance of the item in the list.
        list_in.remove(item)
        iograft.SetOutput(self.list_out, data, list_in)


def LoadPlugin(plugin):
    node = RemoveListItem.GetDefinition()
    plugin.RegisterNode(node, RemoveListItem.Create)
