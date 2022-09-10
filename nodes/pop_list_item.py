# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class PopListItem(iograft.Node):
    """
    Remove the item at the given index of a list and output the item. Also
    output the updated list with the item removed.
    """
    list_in = iograft.MutableInputDefinition("list")
    index = iograft.InputDefinition("index", iobasictypes.Int(),
                                    default_value=-1)

    list_out = iograft.MutableOutputDefinition("list")
    item = iograft.MutableOutputDefinition("item")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("pop_list_item")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddInput(cls.index)
        node.AddOutput(cls.list_out)
        node.AddOutput(cls.item)
        return node

    @staticmethod
    def Create():
        return PopListItem()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)
        index = iograft.GetInput(self.index, data)

        # Pop the item from the list.
        item = list_in.pop(index)
        iograft.SetOutput(self.list_out, data, list_in)
        iograft.SetOutput(self.item, data, item)


def LoadPlugin(plugin):
    node = PopListItem.GetDefinition()
    plugin.RegisterNode(node, PopListItem.Create)
