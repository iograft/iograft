# Copyright 2022 Fabrica Software, LLC

import iograft


class CreateEmptyList(iograft.Node):
    """
    Create a new empty list.
    """
    list_out = iograft.MutableOutputDefinition("list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("create_empty_list")
        node.SetMenuPath("General/Lists")
        node.AddOutput(cls.list_out)
        return node

    @staticmethod
    def Create():
        return CreateEmptyList()

    def Process(self, data):
        # Set the output list.
        iograft.SetOutput(self.list_out, data, [])


def LoadPlugin(plugin):
    node = CreateEmptyList.GetDefinition()
    plugin.RegisterNode(node, CreateEmptyList.Create)
