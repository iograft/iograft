# Copyright 2022 Fabrica Software, LLC

import iograft


class ThrowException(iograft.Node):
    """
    Throw an exception.
    """
    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("throw_exception")
        node.SetMenuPath("General")
        return node

    @staticmethod
    def Create():
        return ThrowException()

    def Process(self, data):
        raise RuntimeError


def LoadPlugin(plugin):
    node = ThrowException.GetDefinition()
    plugin.RegisterNode(node, ThrowException.Create)
