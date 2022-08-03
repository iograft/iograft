# Copyright 2022 Fabrica Software, LLC

import os

import iograft
import iobasictypes


class SetCurrentDirectory(iograft.Node):
    """
    Set the current working directory to the path specified.
    """
    directory = iograft.InputDefinition("directory", iobasictypes.Path())
    new_directory = iograft.OutputDefinition("directory", iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("set_current_directory")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.directory)
        node.AddOutput(cls.new_directory)
        return node

    @staticmethod
    def Create():
        return SetCurrentDirectory()

    def Process(self, data):
        # Get the input directory path.
        directory = iograft.GetInput(self.directory, data)

        # Change the directory.
        os.chdir(directory)
        iograft.SetOutput(self.new_directory, data, directory)


def LoadPlugin(plugin):
    node = SetCurrentDirectory.GetDefinition()
    plugin.RegisterNode(node, SetCurrentDirectory.Create)
