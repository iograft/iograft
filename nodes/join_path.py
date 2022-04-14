# Copyright 2021 Fabrica Software, LLC

import os

import iograft
import iobasictypes


class JoinPath(iograft.Node):
    """
    Join two paths. Wrapper around os.path.join() for two paths.
    """
    dirname = iograft.InputDefinition("dirname", iobasictypes.Path())
    basename = iograft.InputDefinition("basename", iobasictypes.String())
    path = iograft.OutputDefinition("path", iobasictypes.Path())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("join_path")
        node.AddInput(JoinPath.dirname)
        node.AddInput(JoinPath.basename)
        node.AddOutput(JoinPath.path)
        return node

    @staticmethod
    def Create():
        return JoinPath()

    def Process(self, data):
        dirname = iograft.GetInput(self.dirname, data)
        basename = iograft.GetInput(self.basename, data)

        # Join the components.
        path = os.path.join(dirname, basename)
        iograft.SetOutput(self.path, data, path)


def LoadPlugin(plugin):
    node = JoinPath.GetDefinition()
    plugin.RegisterNode(node, JoinPath.Create)
