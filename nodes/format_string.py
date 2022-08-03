# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class FormatString(iograft.Node):
    """
    Given a 'template_string' and an object to use to fill that template
    string, call Python's format operator to generate a formatted string.

    The object used to fill the template string is a AnyList since the
    format string takes a variety of possible input types.
    """
    # The template string is a string with placeholders (i.e. {name}_{}.txt)
    # that will be filled by this format operation.
    template_string = iograft.InputDefinition("template_string",
                                              iobasictypes.String())

    # Positional arguments to the format function.
    positional_args = iograft.InputDefinition("positional_args",
                                              iopythontypes.AnyList(),
                                              default_value=[])

    # Named arguments to the format function. These fill any empty braces
    # or numbered braces in the template string (i.e. {} or {2}).
    named_args = iograft.InputDefinition("named_args", iopythontypes.Dict(),
                                         default_value={})

    output = iograft.OutputDefinition("formatted_string", iobasictypes.String())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("format_string")
        node.SetMenuPath("General/String")
        node.AddInput(cls.template_string)
        node.AddInput(cls.positional_args)
        node.AddInput(cls.named_args)
        node.AddOutput(cls.output)
        return node

    @staticmethod
    def Create():
        return FormatString()

    def Process(self, data):
        template_string = iograft.GetInput(self.template_string, data)
        positional_args = iograft.GetInput(self.positional_args, data)
        named_args = iograft.GetInput(self.named_args, data)

        # Run the format operation.
        formatted_string = template_string.format(*positional_args,
                                                  **named_args)

        # Set the output value.
        iograft.SetOutput(self.output, data, formatted_string)


def LoadPlugin(plugin):
    node = FormatString.GetDefinition()
    plugin.RegisterNode(node, FormatString.Create)
