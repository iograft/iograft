import os

import iograft
import iobasictypes


class CreateDirectory(iograft.Node):
    """
    Create the directory at the path specified.
    """

    directory = iograft.InputDefinition("directory", iobasictypes.String())
    create_sub_dirs = iograft.InputDefinition("create_sub_dirs",
                                              iobasictypes.Bool(),
                                              default_value=False)
    fail_if_exists = iograft.InputDefinition("fail_if_exists",
                                             iobasictypes.Bool(),
                                             default_value=True)
    mode = iograft.InputDefinition("mode", iobasictypes.String(),
                                   default_value="755")

    directory_out = iograft.OutputDefinition("directory",
                                             iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("create_directory")
        node.AddInput(cls.directory)
        node.AddInput(cls.create_sub_dirs)
        node.AddInput(cls.fail_if_exists)
        node.AddInput(cls.mode)
        node.AddOutput(cls.directory_out)
        return node

    @staticmethod
    def Create():
        return CreateDirectory()

    def Process(self, data):
        directory = iograft.GetInput(self.directory, data)
        create_sub_dirs = iograft.GetInput(self.create_sub_dirs, data)
        fail_if_exists = iograft.GetInput(self.fail_if_exists, data)
        mode_str = iograft.GetInput(self.mode, data)

        # Attempt to convert the mode to an integer (parsing as octal).
        mode = int(mode_str, 8)

        if create_sub_dirs:
            os.makedirs(directory, mode, exist_ok=not fail_if_exists)
        else:
            # Check if the directory already exists.
            if os.path.exists(directory):
                if fail_if_exists:
                    raise EnvironmentError("Directory already exists.")
            else:
                os.mkdir(directory, mode)

        iograft.SetOutput(self.directory_out, data, directory)


def LoadPlugin(plugin):
    node = CreateDirectory.GetDefinition()
    plugin.RegisterNode(node, CreateDirectory.Create)
