import fnmatch
import re
import os

import iograft
import iobasictypes


class FilterFiles(iograft.Node):
    """
    Filter a list of files using either Python regex format or a shell style
    matching with fnmatch. Return the list of files that match the query
    string.
    """
    files = iograft.InputDefinition("files", iobasictypes.StringList())
    regex = iograft.InputDefinition("regex", iobasictypes.String())

    # If shell style is set to true, use fnmatch to filter the files.
    # Otherwise, use Python's re module for the filtering.
    shell_style = iograft.InputDefinition("shell_style",
                                          iobasictypes.Bool(),
                                          default_value=True)
    basename_only = iograft.InputDefinition("basename_only",
                                            iobasictypes.Bool(),
                                            default_value=True)
    out_files = iograft.OutputDefinition("files", iobasictypes.StringList())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("filter_files")
        node.AddInput(cls.files)
        node.AddInput(cls.regex)
        node.AddInput(cls.shell_style)
        node.AddInput(cls.basename_only)
        node.AddOutput(cls.out_files)
        return node

    @staticmethod
    def Create():
        return FilterFiles()

    def Process(self, data):
        files = iograft.GetInput(self.files, data)
        regex = iograft.GetInput(self.regex, data)
        shell_style = iograft.GetInput(self.shell_style, data)
        basename_only = iograft.GetInput(self.basename_only, data)

        # Compile the regex.
        re_test = re.compile(".*")
        if not shell_style:
            re_test = re.compile(r'{}'.format(regex))

        out_files = []
        for filepath in files:
            test_path = filepath

            # If only comparing the base names, update the filepath.
            if basename_only:
                test_path = os.path.basename(filepath)

            if shell_style:
                if fnmatch.fnmatch(test_path, regex):
                    out_files.append(filepath)
            elif re_test.match(test_path) is not None:
                out_files.append(filepath)

        # Set the output value.
        iograft.SetOutput(self.out_files, data, out_files)


def LoadPlugin(plugin):
    node = FilterFiles.GetDefinition()
    plugin.RegisterNode(node, FilterFiles.Create)
