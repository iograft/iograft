import os

import iograft
import iobasictypes


class GetCurrentDirectory(iograft.Node):
    """
    Get the current working directory. Wrapper around the os.getcwd()
    function.
    """
    directory = iograft.OutputDefinition("directory", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_current_directory")
        node.AddOutput(cls.directory)
        return node

    @staticmethod
    def Create():
        return GetCurrentDirectory()

    def Process(self, data):
        directory = os.getcwd()
        iograft.SetOutput(self.directory, data, directory)


def LoadPlugin(plugin):
    node = GetCurrentDirectory.GetDefinition()
    plugin.RegisterNode(node, GetCurrentDirectory.Create)
