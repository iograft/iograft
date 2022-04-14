# Copyright 2021 Fabrica Software, LLC

import tempfile

import iograft
import iobasictypes


class CreateTempDirectory(iograft.Node):
    """
    Create a temporary directory by default in the operating systems
    standard temp area.
    """
    base_dir = iograft.InputDefinition("base_dir", iobasictypes.Path(),
                                       default_value="")
    suffix = iograft.InputDefinition("suffix", iobasictypes.String(),
                                     default_value="")
    directory_out = iograft.OutputDefinition("directory",
                                             iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("create_temp_directory")
        node.AddInput(cls.base_dir)
        node.AddInput(cls.suffix)
        node.AddOutput(cls.directory_out)
        return node

    @staticmethod
    def Create():
        return CreateTempDirectory()

    def Process(self, data):
        base_dir = iograft.GetInput(self.base_dir, data)
        suffix = iograft.GetInput(self.suffix, data)

        mkdtemp_args = {}
        if suffix:
            mkdtemp_args["suffix"] = suffix
        if base_dir:
            mkdtemp_args["dir"] = base_dir

        # Execute the tempdir creation.
        directory = tempfile.mkdtemp(**mkdtemp_args)
        iograft.SetOutput(self.directory_out, data, directory)


def LoadPlugin(plugin):
    node = CreateTempDirectory.GetDefinition()
    plugin.RegisterNode(node, CreateTempDirectory.Create)
