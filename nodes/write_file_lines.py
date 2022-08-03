# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes


class WriteFileLines(iograft.Node):
    """
    Given a list of strings, write each string to the given file as
    individual lines.

    The 'write_mode' input allows setting the mode of the file write. This
    can be either 'w', 'wb', 'a', or 'ab'.
    """
    filename = iograft.InputDefinition("filename", iobasictypes.Path())
    lines = iograft.InputDefinition("lines", iobasictypes.StringList())
    write_mode = iograft.InputDefinition("mode", iobasictypes.String(),
                                         default_value="w")

    out_filename = iograft.OutputDefinition("filename", iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("write_file_lines")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.filename)
        node.AddInput(cls.lines)
        node.AddInput(cls.write_mode)
        node.AddOutput(cls.out_filename)
        return node

    @staticmethod
    def Create():
        return WriteFileLines()

    def Process(self, data):
        filename = iograft.GetInput(self.filename, data)
        lines = iograft.GetInput(self.lines, data)
        write_mode = iograft.GetInput(self.write_mode, data)

        # Ensure that the read mode is value.
        if write_mode not in ["w", "wb", "a", "ab"]:
            raise ValueError("The 'write_mode' must be either 'w', 'wb',"
                             " 'a', or 'ab'")

        # Write the contents to file.
        with open(filename, write_mode) as f:
            f.writelines(lines)

        # Set the output value.
        iograft.SetOutput(self.out_filename, data, filename)


def LoadPlugin(plugin):
    node = WriteFileLines.GetDefinition()
    plugin.RegisterNode(node, WriteFileLines.Create)
