# Copyright 2023 Fabrica Software, LLC

import os
import iograft
import iobasictypes


class MakeAbsolutePath(iograft.Node):
    """
    Return the absolute path corresponding to the input path. If the input
    path is already an absolute path, this node has not effect. If a
    `base_directory` is provided, the absolute path is resolved relative to
    that `base_directory`. Otherwise, the absolute path is resolved relative
    to the current working directory.
    """
    path = iograft.InputDefinition("path", iobasictypes.Path())
    base_directory = iograft.InputDefinition("base_directory",
                                             iobasictypes.Path(),
                                             default_value="")
    absolute_path = iograft.OutputDefinition("absolute_path",
                                             iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("make_absolute_path")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.path)
        node.AddInput(cls.base_directory)
        node.AddOutput(cls.absolute_path)
        return node

    @staticmethod
    def Create():
        return MakeAbsolutePath()

    def Process(self, data):
        path = iograft.GetInput(self.path, data)
        base_directory = iograft.GetInput(self.base_directory, data)

        # If the base directory is provided, use that to determine the
        # absolute path; otherwise use the current working directory.
        if base_directory:
            absolute_path = os.path.normpath(os.path.join(base_directory, path))
        else:
            absolute_path = os.path.abspath(path)

        iograft.SetOutput(self.absolute_path, data, absolute_path)


def LoadPlugin(plugin):
    node = MakeAbsolutePath.GetDefinition()
    plugin.RegisterNode(node, MakeAbsolutePath.Create)
