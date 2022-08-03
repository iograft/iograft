# Copyright 2022 Fabrica Software, LLC

import os
import shutil

import iograft
import iobasictypes


class CopyFiles(iograft.Node):
    """
    Copy a given list of files to the target directory.
    """
    files = iograft.InputDefinition("files", iobasictypes.PathList())
    target_directory = iograft.InputDefinition("target_directory",
                                               iobasictypes.Path())
    preserve_metadata = iograft.InputDefinition("preserve_metadata",
                                                iobasictypes.Bool(),
                                                default_value=True)

    out_files = iograft.OutputDefinition("files", iobasictypes.PathList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("copy_files")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.files)
        node.AddInput(cls.target_directory)
        node.AddInput(cls.preserve_metadata)
        node.AddOutput(cls.out_files)
        return node

    @staticmethod
    def Create():
        return CopyFiles()

    def Process(self, data):
        files = iograft.GetInput(self.files, data)
        target_directory = iograft.GetInput(self.target_directory, data)
        preserve_metadata = iograft.GetInput(self.preserve_metadata, data)

        # Set the copy function.
        copy_func = shutil.copy
        if preserve_metadata:
            copy_func = shutil.copy2

        # Copy the requested files to the target directory.
        out_files = []
        for file in files:
            target_path = os.path.join(target_directory,
                                       os.path.basename(file))
            copy_func(file, target_path)
            out_files.append(target_path)

        # Set the output value.
        iograft.SetOutput(self.out_files, data, out_files)


def LoadPlugin(plugin):
    node = CopyFiles.GetDefinition()
    plugin.RegisterNode(node, CopyFiles.Create)
