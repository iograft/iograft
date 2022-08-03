# Copyright 2022 Fabrica Software, LLC

import os

import iograft
import iobasictypes


class SplitFileExtension(iograft.Node):
    """
    Split a given filename into two components: the root filename and the
    extension.
    """
    filename = iograft.InputDefinition("filename", iobasictypes.Path())

    root_filename = iograft.OutputDefinition("root_filename",
                                             iobasictypes.Path())
    extenstion = iograft.OutputDefinition("extension", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("split_file_extension")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.filename)
        node.AddOutput(cls.root_filename)
        node.AddOutput(cls.extenstion)
        return node

    @staticmethod
    def Create():
        return SplitFileExtension()

    def Process(self, data):
        # Get the input filename
        filename = iograft.GetInput(self.filename, data)

        # Split the filename.
        root_filename, extension = os.path.splitext(filename)

        # Set the output values.
        iograft.SetOutput(self.root_filename, data, root_filename)
        iograft.SetOutput(self.extenstion, data, extension)


def LoadPlugin(plugin):
    node = SplitFileExtension.GetDefinition()
    plugin.RegisterNode(node, SplitFileExtension.Create)
