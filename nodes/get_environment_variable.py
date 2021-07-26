import os

import iograft
import iobasictypes


class GetEnvironmentVariable(iograft.Node):
    """
    Get the value of an environment variable. Wrapper around an os.environ
    dict loopup.
    """
    var_name = iograft.InputDefinition("variable_name", iobasictypes.String())
    var_value = iograft.OutputDefinition("value", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("get_environment_var")
        node.AddInput(GetEnvironmentVariable.var_name)
        node.AddOutput(GetEnvironmentVariable.var_value)
        return node

    @staticmethod
    def Create():
        return GetEnvironmentVariable()

    def Process(self, data):
        var_name = iograft.GetInput(self.var_name, data)

        # Get the value of the environment variable.
        value = os.environ[var_name]

        # Set the output data to be sent back to iograft.
        iograft.SetOutput(self.var_value, data, value)


def LoadPlugin(plugin):
    node = GetEnvironmentVariable.GetDefinition()
    plugin.RegisterNode(node, GetEnvironmentVariable.Create)
