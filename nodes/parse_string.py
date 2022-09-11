# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import iopythontypes


class ParseString(iograft.Node):
    """
    Given a 'template_string' and an input string, attempt to parse the
    string based on the provided template using the 'parse' module. This
    node aims to be the inverse of the 'format_string' node.

    Outputs a list of the positional values parsed from the string and
    a dictionary of the named values parsed from the string. An exception
    is raised if the input string could not be parsed with the given
    template; so it is guaranteed that if this node completes, the input
    string was in the provided format.

    Example inputs and outputs:
        template_string - {frame:04d}.{}_{}.txt
        string - 0010.whale_ceramic.txt

        positional_args - ('whale', 'ceramic')
        named_args - {'frame': 10}
    """
    # The template string is a string with placeholders (i.e. {name}_{}.txt)
    # used to parse the input string.
    template_string = iograft.InputDefinition("template_string",
                                              iobasictypes.String())

    formatted_string = iograft.InputDefinition("formatted_string",
                                               iobasictypes.String())

    # Whether or not the parsing should be case sensitive.
    case_sensitive = iograft.InputDefinition("case_sensitive",
                                             iobasictypes.Bool(),
                                             default_value=True)

    # Positional arguments parsed from the string. These are parsed from
    # any empty braces or numbered braces in the template string (i.e. {}
    # or {2}).
    positional_args = iograft.OutputDefinition("positional_args",
                                               iopythontypes.AnyList())

    # Named arguments parsed from the string (i.e. {frame}).
    named_args = iograft.OutputDefinition("named_args", iopythontypes.Dict())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("parse_string")
        node.SetMenuPath("General/String")
        node.AddInput(cls.template_string)
        node.AddInput(cls.formatted_string)
        node.AddInput(cls.case_sensitive)
        node.AddOutput(cls.positional_args)
        node.AddOutput(cls.named_args)
        return node

    @staticmethod
    def Create():
        return ParseString()

    def Process(self, data):
        import parse

        template_string = iograft.GetInput(self.template_string, data)
        formatted_string = iograft.GetInput(self.formatted_string, data)
        case_sensitive = iograft.GetInput(self.case_sensitive, data)

        # Attempt to parse the input string.
        parse_result = parse.parse(template_string, formatted_string,
                                   case_sensitive=case_sensitive)

        # If the parse result is None, then raise an error since the input
        # string did not match the input format.
        if parse_result is None:
            raise ValueError(
                    "The input string did not match the template string.")

        # Otherwise, output the matches args.
        iograft.SetOutput(self.positional_args, data, parse_result.fixed)
        iograft.SetOutput(self.named_args, data, parse_result.named)


def LoadPlugin(plugin):
    node = ParseString.GetDefinition()
    plugin.RegisterNode(node, ParseString.Create)
