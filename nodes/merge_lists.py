# Copyright 2022 Fabrica Software, LLC

import iograft


class MergeLists(iograft.Node):
    """
    Merge two lists forming a new list containing the elements
    of both.
    """
    list1 = iograft.MutableInputDefinition("list1")
    list2 = iograft.MutableInputDefinition("list2")
    merged_list = iograft.MutableOutputDefinition("merged_list")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("merge_lists")
        node.SetMenuPath("General/Lists")
        node.AddInput(cls.list1)
        node.AddInput(cls.list2)
        node.AddOutput(cls.merged_list)
        return node

    @staticmethod
    def Create():
        return MergeLists()

    def Process(self, data):
        # Get the input lists.
        list1 = iograft.GetInput(self.list1, data)
        list2 = iograft.GetInput(self.list2, data)

        # Ensure that the inputs are lists.
        if not isinstance(list1, list):
            raise ValueError("The input for: 'list1' is not a list."
                             " Type was: {}".format(type(list1)))

        if not isinstance(list2, list):
            raise ValueError("The input for: 'list2' is not a list."
                             " Type was: {}".format(type(list2)))

        # Create and return the merged list.
        merged_list = list1 + list2
        iograft.SetOutput(self.merged_list, data, merged_list)


def LoadPlugin(plugin):
    node = MergeLists.GetDefinition()
    plugin.RegisterNode(node, MergeLists.Create)
