# Copyright 2023 Fabrica Software, LLC

import iograft


class WrapItemInList(iograft.Node):
    """
    Wrap the provided input item in a list and return the newly formed list
    containing that single item.
    """
    item = iograft.MutableInputDefinition("item")
    list_out = iograft.MutableOutputDefinition("list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("wrap_item_in_list")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.item)
        node.AddOutput(cls.list_out)
        return node

    @staticmethod
    def Create():
        return WrapItemInList()

    def Process(self, data):
        item = iograft.GetInput(self.item, data)

        # Create the new list and set it as the output.
        list_out = [item]
        iograft.SetOutput(self.list_out, data, list_out)


def LoadPlugin(plugin):
    node = WrapItemInList.GetDefinition()
    plugin.RegisterNode(node, WrapItemInList.Create)
