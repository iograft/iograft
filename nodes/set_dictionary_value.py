# Copyright 2022 Fabrica Software, LLC

import iograft
import iopythontypes


class SetDictionaryValue(iograft.Node):
    """
    Set the value of the given key in a dictionary. This modifies the
    dictionary in place and does NOT generate a new dictionary.
    """
    dictionary = iograft.InputDefinition("dictionary", iopythontypes.Dict())

    # The key can be any hashable object.
    key = iograft.MutableInputDefinition("key")

    # The value to set in the dictionary.
    value = iograft.MutableInputDefinition("value")

    # The dictionary that was updated. This is the SAME dictionary object
    # that was passed in. It is not a copy.
    out_dictionary = iograft.OutputDefinition("dictionary",
                                              iopythontypes.Dict())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("set_dictionary_value")
        node.SetMenuPath("General")
        node.AddInput(cls.dictionary)
        node.AddInput(cls.key)
        node.AddInput(cls.value)
        node.AddOutput(cls.out_dictionary)
        return node

    @staticmethod
    def Create():
        return SetDictionaryValue()

    def Process(self, data):
        dictionary = iograft.GetInput(self.dictionary, data)
        key = iograft.GetInput(self.key, data)
        value = iograft.GetInput(self.value, data)

        # Set the value in the dictionary.
        dictionary[key] = value

        # Passthrough the dictionary for convenience.
        iograft.SetOutput(self.out_dictionary, data, dictionary)


def LoadPlugin(plugin):
    node = SetDictionaryValue.GetDefinition()
    plugin.RegisterNode(node, SetDictionaryValue.Create)
