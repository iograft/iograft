# Copyright 2022 Fabrica Software, LLC

import os

import iograft
import iobasictypes


class SetEnvironmentVariable(iograft.Node):
    """
    Set the value of an environment variable via the `os.environ`
    dictionary.
    """
    variable_name = iograft.InputDefinition("variable_name",
                                            iobasictypes.String())
    value = iograft.InputDefinition("value", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("set_environment_var")
        node.SetMenuPath("General/Environment")
        node.AddInput(cls.variable_name)
        node.AddInput(cls.value)
        return node

    @staticmethod
    def Create():
        return SetEnvironmentVariable()

    def Process(self, data):
        variable_name = iograft.GetInput(self.variable_name, data)
        value = iograft.GetInput(self.value, data)

        # Set the environment variable.
        os.environ[variable_name] = value


def LoadPlugin(plugin):
    node = SetEnvironmentVariable.GetDefinition()
    plugin.RegisterNode(node, SetEnvironmentVariable.Create)
