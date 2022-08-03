# Copyright 2022 Fabrica Software, LLC

import os

import iograft
import iobasictypes


class SplitPath(iograft.Node):
    """
    Split a path into the directory and basename components. Wrapper
    around os.path.split().
    """
    path = iograft.InputDefinition("path", iobasictypes.Path())
    dirname = iograft.OutputDefinition("dirname", iobasictypes.Path())
    basename = iograft.OutputDefinition("basename", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("split_path")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.path)
        node.AddOutput(cls.dirname)
        node.AddOutput(cls.basename)
        return node

    @staticmethod
    def Create():
        return SplitPath()

    def Process(self, data):
        # Get the input path.
        path = iograft.GetInput(self.path, data)

        # Split the path and get the directory name and the basename.
        dirname, basename = os.path.split(path)

        # Set the output components.
        iograft.SetOutput(self.dirname, data, dirname)
        iograft.SetOutput(self.basename, data, basename)


def LoadPlugin(plugin):
    node = SplitPath.GetDefinition()
    plugin.RegisterNode(node, SplitPath.Create)
