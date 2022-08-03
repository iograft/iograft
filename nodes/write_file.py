# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes


class WriteFile(iograft.Node):
    """
    Write the contents of the passed in string to a file.

    The 'write_mode' input allows setting the mode of the file write. This
    can be either 'w', 'wb', 'a', or 'ab'.
    """
    filename = iograft.InputDefinition("filename", iobasictypes.Path())
    contents = iograft.InputDefinition("contents", iobasictypes.String())
    write_mode = iograft.InputDefinition("mode", iobasictypes.String(),
                                         default_value="w")

    out_filename = iograft.OutputDefinition("filename", iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("write_file")
        node.SetMenuPath("General/File IO")
        node.AddInput(cls.filename)
        node.AddInput(cls.contents)
        node.AddInput(cls.write_mode)
        node.AddOutput(cls.out_filename)
        return node

    @staticmethod
    def Create():
        return WriteFile()

    def Process(self, data):
        filename = iograft.GetInput(self.filename, data)
        contents = iograft.GetInput(self.contents, data)
        write_mode = iograft.GetInput(self.write_mode, data)

        # Ensure that the read mode is value.
        if write_mode not in ["w", "wb", "a", "ab"]:
            raise ValueError("The 'write_mode' must be either 'w', 'wb',"
                             " 'a', or 'ab'")

        # Write the contents to file.
        with open(filename, write_mode) as f:
            f.write(contents)

        # Set the output value.
        iograft.SetOutput(self.out_filename, data, filename)


def LoadPlugin(plugin):
    node = WriteFile.GetDefinition()
    plugin.RegisterNode(node, WriteFile.Create)
