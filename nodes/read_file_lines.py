# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes


class ReadFileLines(iograft.Node):
    """
    Read a file. Returns the contents of the file as a list of strings where
    each string is a line of the file.

    The 'read_mode' input allows setting the mode of the file open. This
    can be either 'r' or 'rb' for reading binary files.
    """
    filename = iograft.InputDefinition("filename", iobasictypes.Path())
    read_mode = iograft.InputDefinition("mode", iobasictypes.String(),
                                        default_value="r")
    lines = iograft.OutputDefinition("lines", iobasictypes.StringList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("read_file_lines")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.filename)
        node.AddInput(cls.read_mode)
        node.AddOutput(cls.lines)
        return node

    @staticmethod
    def Create():
        return ReadFileLines()

    def Process(self, data):
        filename = iograft.GetInput(self.filename, data)
        read_mode = iograft.GetInput(self.read_mode, data)

        # Ensure that the read mode is value.
        if read_mode not in ["r", "rb"]:
            raise ValueError("The 'read_mode' must be either 'r' or 'rb'")

        # Read the file.
        with open(filename, read_mode) as f:
            lines = f.readlines()

        # Set the output value.
        iograft.SetOutput(self.lines, data, lines)


def LoadPlugin(plugin):
    node = ReadFileLines.GetDefinition()
    plugin.RegisterNode(node, ReadFileLines.Create)
