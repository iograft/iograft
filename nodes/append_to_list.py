# Copyright 2022 Fabrica Software, LLC

import iograft


class AppendToList(iograft.Node):
    """
    Append an item to a list and output the updated list.
    """
    list_in = iograft.MutableInputDefinition("list")
    item = iograft.MutableInputDefinition("item")
    list_out = iograft.MutableOutputDefinition("list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("append_to_list")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list_in)
        node.AddInput(cls.item)
        node.AddOutput(cls.list_out)
        return node

    @staticmethod
    def Create():
        return AppendToList()

    def Process(self, data):
        list_in = iograft.GetInput(self.list_in, data)
        item = iograft.GetInput(self.item, data)

        # Append the item to the list and return the result.
        # Note: While this modifies the list *in-place* in Python,
        # the input list will not be modified within iograft. Only
        # the list set as the output of this node will have the added
        # value.
        list_in.append(item)
        iograft.SetOutput(self.list_out, data, list_in)


def LoadPlugin(plugin):
    node = AppendToList.GetDefinition()
    plugin.RegisterNode(node, AppendToList.Create)
