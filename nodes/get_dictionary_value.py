# Copyright 2022 Fabrica Software, LLC

import iograft
import iopythontypes


class NoDefault(object):
    """
    The NoDefault object serves as a "sentinel" value to let the node know
    that no explicit default value was provided by the user to be returned
    in the case of the desired key being missing.
    """
    def __init__(self):
        pass

    def __str__(self):
        return "<no default>"
_nodefault = NoDefault()


class GetDictionaryValue(iograft.Node):
    """
    Extract the value from a dictionary with the given key. Optionally
    can provide a 'default' to return if the key is not in the dictionary.
    """
    dictionary = iograft.InputDefinition("dictionary", iopythontypes.Dict())

    # The key can be any hashable object.
    key = iograft.MutableInputDefinition("key")

    # An optional default if the key is not found.
    # This would be better if it was a mutable type, but no way to specify
    # a default value for mutable types currently.
    default = iograft.InputDefinition("default", iopythontypes.Any(),
                                      default_value=_nodefault)

    value = iograft.MutableOutputDefinition("value")

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_dictionary_value")
        node.SetMenuPath("General")
        node.AddInput(cls.dictionary)
        node.AddInput(cls.key)
        node.AddInput(cls.default)
        node.AddOutput(cls.value)
        return node

    @staticmethod
    def Create():
        return GetDictionaryValue()

    def Process(self, data):
        dictionary = iograft.GetInput(self.dictionary, data)
        key = iograft.GetInput(self.key, data)
        default = iograft.GetInput(self.default, data)

        if default != _nodefault:
            value = dictionary.get(key, default)
        else:
            value = dictionary[key]

        iograft.SetOutput(self.value, data, value)


def LoadPlugin(plugin):
    node = GetDictionaryValue.GetDefinition()
    plugin.RegisterNode(node, GetDictionaryValue.Create)
