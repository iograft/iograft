# Copyright 2021 Fabrica Software, LLC

import os

import iograft
import iobasictypes


class ListDirectory(iograft.Node):
    """
    Wrapper around the python os.listdir() function to list the
    contents of a directory.
    """
    directory = iograft.InputDefinition("directory", iobasictypes.String())
    full_paths = iograft.InputDefinition("full_paths",
                                         iobasictypes.Bool(),
                                         default_value=False)

    paths = iograft.OutputDefinition("files", iobasictypes.StringList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("list_directory")
        node.AddInput(cls.directory)
        node.AddInput(cls.full_paths)
        node.AddOutput(cls.paths)
        return node

    @staticmethod
    def Create():
        return ListDirectory()

    def Process(self, data):
        # Pull out the input data provided to the node.
        directory = iograft.GetInput(self.directory, data)
        full_paths = iograft.GetInput(self.full_paths, data)

        # List the directory.
        paths = os.listdir(directory)

        # If requested full paths, update the paths to include the diectory.
        if full_paths:
            paths = [os.path.join(directory, path) for path in paths]

        # Sort the paths.
        paths = sorted(paths)

        # Set the output data to be sent back to iograft.
        iograft.SetOutput(self.paths, data, paths)


def LoadPlugin(plugin):
    node = ListDirectory.GetDefinition()
    plugin.RegisterNode(node, ListDirectory.Create)
