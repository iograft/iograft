# Copyright 2022 Fabrica Software, LLC

import iograft
import iopythontypes


class CreateEmptyDictionary(iograft.Node):
    """
    Create an empty dictionary. This node is provided as an alternative
    to specifying an empty dictionary in a user input value since that
    value could be modified and persist through graph reset operations
    much like setting a dictionary as a default value to a Python function.
    """
    dictionary = iograft.OutputDefinition("dictionary", iopythontypes.Dict())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("create_empty_dictionary")
        node.SetMenuPath("General")
        node.AddOutput(cls.dictionary)
        return node

    @staticmethod
    def Create():
        return CreateEmptyDictionary()

    def Process(self, data):
        iograft.SetOutput(self.dictionary, data, {})


def LoadPlugin(plugin):
    node = CreateEmptyDictionary.GetDefinition()
    plugin.RegisterNode(node, CreateEmptyDictionary.Create)
