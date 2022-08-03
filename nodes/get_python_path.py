# Copyright 2022 Fabrica Software, LLC

import sys

import iograft
import iobasictypes


class GetPythonPath(iograft.Node):
    """
    Return the Python Path defined in sys.path.
    """
    output = iograft.OutputDefinition("python_path", iobasictypes.StringList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_python_path")
        node.SetMenuPath("General/Environment")
        node.AddOutput(cls.output)
        return node

    @staticmethod
    def Create():
        return GetPythonPath()

    def Process(self, data):
        # Set the output value.
        result = sys.path
        iograft.SetOutput(self.output, data, result)


def LoadPlugin(plugin):
    node = GetPythonPath.GetDefinition()
    plugin.RegisterNode(node, GetPythonPath.Create)
