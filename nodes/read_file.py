# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes


class ReadFile(iograft.Node):
    """
    Read a file. Returns the full file contents as a string.

    The 'read_mode' input allows setting the mode of the file open. This
    can be either 'r' or 'rb' for reading binary files.
    """
    filename = iograft.InputDefinition("filename", iobasictypes.Path())
    read_mode = iograft.InputDefinition("mode", iobasictypes.String(),
                                        default_value="r")
    contents = iograft.OutputDefinition("contents", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("read_file")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.filename)
        node.AddInput(cls.read_mode)
        node.AddOutput(cls.contents)
        return node

    @staticmethod
    def Create():
        return ReadFile()

    def Process(self, data):
        filename = iograft.GetInput(self.filename, data)
        read_mode = iograft.GetInput(self.read_mode, data)

        # Ensure that the read mode is value.
        if read_mode not in ["r", "rb"]:
            raise ValueError("The 'read_mode' must be either 'r' or 'rb'")

        # Read the file.
        with open(filename, read_mode) as f:
            contents = f.read()

        # Set the output value.
        iograft.SetOutput(self.contents, data, contents)


def LoadPlugin(plugin):
    node = ReadFile.GetDefinition()
    plugin.RegisterNode(node, ReadFile.Create)
