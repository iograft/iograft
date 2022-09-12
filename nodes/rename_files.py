# Copyright 2022 Fabrica Software, LLC

import shutil

import iograft
import iobasictypes


class RenameFiles(iograft.Node):
    """
    Given a list of 'files', rename them to the the passed in list of
    'target_files'. If 'copy' is True, leave the original files unchanged,
    copy the original files, and rename the copies.

    Note: The 'files' and 'target_files' inputs must have the same length
    or this node will fail.
    """
    files = iograft.InputDefinition("files", iobasictypes.PathList())
    target_files = iograft.InputDefinition("target_files",
                                           iobasictypes.PathList())

    # Whether or not to copy the files. This will leave the original files
    # unchanged and rename the copied files.
    copy_files = iograft.InputDefinition("copy", iobasictypes.Bool(),
                                         default_value=False)

    preserve_metadata = iograft.InputDefinition("preserve_metadata",
                                                iobasictypes.Bool(),
                                                default_value=True)

    out_files = iograft.OutputDefinition("files", iobasictypes.PathList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("rename_files")
        node.SetMenuPath("General/File System")
        node.AddInput(cls.files)
        node.AddInput(cls.target_files)
        node.AddInput(cls.copy_files)
        node.AddInput(cls.preserve_metadata)
        node.AddOutput(cls.out_files)
        return node

    @staticmethod
    def Create():
        return RenameFiles()

    def Process(self, data):
        files = iograft.GetInput(self.files, data)
        target_files = iograft.GetInput(self.target_files, data)
        copy_files = iograft.GetInput(self.copy_files, data)
        preserve_metadata = iograft.GetInput(self.preserve_metadata, data)

        # Ensure that the two file lists have the same length.
        if len(files) != len(target_files):
            raise ValueError("The input 'files' and 'target_files' are not the"
                             " same length. 'files': {}, 'target_files':"
                             " {}".format(len(files), len(target_files)))

        # Set the copy function.
        copy_func = shutil.copy
        if preserve_metadata:
            copy_func = shutil.copy2

        # Rename the requested files to the target files.
        out_files = []
        for index, file in enumerate(files):
            target_path = target_files[index]

            # If 'copy' is True, copy the files to the target, otherwise
            # move the originals.
            if copy_files:
                copy_func(file, target_path)
            else:
                shutil.move(file, target_path, copy_function=copy_func)
            out_files.append(target_path)

        # Set the output value.
        iograft.SetOutput(self.out_files, data, out_files)


def LoadPlugin(plugin):
    node = RenameFiles.GetDefinition()
    plugin.RegisterNode(node, RenameFiles.Create)
