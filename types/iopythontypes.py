# Copyright 2021 Fabrica Software, LLC

import iograft


class Dict(iograft.PythonType):
    """
    Type representing a Python dict object.
    """
    type_id = iograft.TypeId("PyDict")

    def __init__(self):
        super(Dict, self).__init__(Dict.type_id)


class DictList(iograft.PythonListType):
    """
    Type representing a list of Python dict objects.
    """
    def __init__(self):
        super(DictList, self).__init__(Dict().GetTypeId())


class Tuple(iograft.PythonType):
    """
    Type representing a Python tuple object.
    """
    type_id = iograft.TypeId("PyTuple")

    def __init__(self):
        super(Tuple, self).__init__(Tuple.type_id)


class TupleList(iograft.PythonListType):
    def __init__(self):
        super(Tuple, self).__init__(Tuple().GetTypeId())


def LoadPlugin(plugin):
    # Register the dict type with iograft.
    dict_type = plugin.RegisterPythonType(Dict.type_id,
                                          iograft.ValueToString,
                                          iograft.ValueFromString,
                                          iograft.SerializeValue,
                                          iograft.DeserializeValue)
    # Also register the list type for dicts.
    plugin.RegisterPythonListType(dict_type)

    # Register the tuple type with iograft.
    tuple_type = plugin.RegisterPythonType(Tuple.type_id,
                                           iograft.ValueToString,
                                           iograft.ValueFromString,
                                           iograft.SerializeValue,
                                           iograft.DeserializeValue)
    # Also register the list type for tuples.
    plugin.RegisterPythonListType(tuple_type)
