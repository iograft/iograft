# Copyright 2022 Fabrica Software, LLC

import os
import shutil

import iograft
import iobasictypes


class RemoveDirectory(iograft.Node):
    """
    Remove the given directory.
    """
    directory = iograft.InputDefinition("directory", iobasictypes.Path())
    remove_contents = iograft.InputDefinition("remove_contents",
                                              iobasictypes.Bool(),
                                              default_value=False)
    must_exist = iograft.InputDefinition("must_exist",
                                         iobasictypes.Bool(),
                                         default_value=False)

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("remove_directory")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.directory)
        node.AddInput(cls.remove_contents)
        node.AddInput(cls.must_exist)
        return node

    @staticmethod
    def Create():
        return RemoveDirectory()

    def Process(self, data):
        directory = iograft.GetInput(self.directory, data)
        remove_contents = iograft.GetInput(self.remove_contents, data)
        must_exist = iograft.GetInput(self.must_exist, data)

        if must_exist and not os.path.isdir(directory):
            try:
                FileNotFoundError
            except NameError:
                FileNotFoundError = IOError
            raise FileNotFoundError(
                        "Directory {} does not exist.".format(directory))

        # The directory does not exist; nothing to do.
        if not os.path.isdir(directory):
            return

        # Based on if we are removing contents or not, use shutil or os.
        if remove_contents:
            shutil.rmtree(directory)
        else:
            os.rmdir(directory)


def LoadPlugin(plugin):
    node = RemoveDirectory.GetDefinition()
    plugin.RegisterNode(node, RemoveDirectory.Create)
