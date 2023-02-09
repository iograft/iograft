# Copyright 2023 Fabrica Software, LLC

import os
import iograft
import iobasictypes


class MakeRelativePath(iograft.Node):
    """
    Return the relative path corresponding to the input path. If the
    `base_directory` is set, the output path with be relative to that
    directory. Otherwise, the output path will be relative to the
    current working directory.
    """
    path = iograft.InputDefinition("path", iobasictypes.Path())
    base_directory = iograft.InputDefinition("base_directory",
                                              iobasictypes.Path(),
                                              default_value="")
    relative_path = iograft.OutputDefinition("relative_path",
                                             iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("make_relative_path")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.path)
        node.AddInput(cls.base_directory)
        node.AddOutput(cls.relative_path)
        return node

    @staticmethod
    def Create():
        return MakeRelativePath()

    def Process(self, data):
        path = iograft.GetInput(self.path, data)
        base_directory = iograft.GetInput(self.base_directory, data)

        cmd_kwargs = {}
        if base_directory:
            cmd_kwargs["start"] = base_directory

        # Convert to a relative path.
        relative_path = os.path.relpath(path, **cmd_kwargs)
        iograft.SetOutput(self.relative_path, data, relative_path)


def LoadPlugin(plugin):
    node = MakeRelativePath.GetDefinition()
    plugin.RegisterNode(node, MakeRelativePath.Create)
