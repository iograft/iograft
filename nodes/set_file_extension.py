# Copyright 2022 Fabrica Software, LLC

import os

import iograft
import iobasictypes


class SetFileExtension(iograft.Node):
    """
    Set the file extension of the input filename. Optionally can replace
    the existing extension.
    """
    filename = iograft.InputDefinition("filename", iobasictypes.Path())
    extension = iograft.InputDefinition("extension", iobasictypes.String())

    # If True, remove the existing extension on the filename.
    replace_existing = iograft.InputDefinition("replace_existing",
                                               iobasictypes.Bool(),
                                               default_value=False)

    new_filename =  iograft.OutputDefinition("filename", iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("set_file_extension")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.filename)
        node.AddInput(cls.extension)
        node.AddInput(cls.replace_existing)
        node.AddOutput(cls.new_filename)
        return node

    @staticmethod
    def Create():
        return SetFileExtension()

    def Process(self, data):
        # Get the input filename
        filename = iograft.GetInput(self.filename, data)
        replace_existing = iograft.GetInput(self.replace_existing, data)
        extension = iograft.GetInput(self.extension, data)

        # Ensure that the extension starts with a '.' character.
        if not extension.startswith('.'):
            raise ValueError("The 'extension' must start with a '.' character")

        # If replace_existing is enabled, remove the current extension.
        # The last '.' plus any following string.
        if replace_existing:
            filename, _ = os.path.splitext(filename)

        # Add the extension, if the string is not empty.
        if extension:
            filename = ''.join([filename, extension])

        # Set the output new filename.
        iograft.SetOutput(self.new_filename, data, filename)


def LoadPlugin(plugin):
    node = SetFileExtension.GetDefinition()
    plugin.RegisterNode(node, SetFileExtension.Create)
