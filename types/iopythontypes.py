# Copyright 2022 Fabrica Software, LLC

import iograft


class Dict(iograft.PythonType):
    """
    Type representing a Python dict object.
    """
    type_id = iograft.TypeId("PyDict")
    value_type = dict

    def __init__(self):
        super(Dict, self).__init__(Dict.type_id, value_type=Dict.value_type)


class DictList(iograft.PythonListType):
    """
    Type representing a list of Python dict objects.
    """
    def __init__(self):
        super(DictList, self).__init__(Dict.type_id,
                                       base_value_type=Dict.value_type)


class Tuple(iograft.PythonType):
    """
    Type representing a Python tuple object.
    """
    type_id = iograft.TypeId("PyTuple")
    value_type = tuple

    def __init__(self):
        super(Tuple, self).__init__(Tuple.type_id, value_type=Tuple.value_type)


class TupleList(iograft.PythonListType):
    """
    Type representing a list of Python tuple objects.
    """
    def __init__(self):
        super(TupleList, self).__init__(Tuple.type_id,
                                        base_value_type=Tuple.value_type)


class Any(iograft.PythonType):
    """
    Type representing *any* Python object. This type is meant to be used
    during development before specific types may be determined.
    """
    type_id = iograft.TypeId("PyAny")

    def __init__(self):
        super(Any, self).__init__(Any.type_id)


class AnyList(iograft.PythonListType):
    """
    Type representing a list of Python "Any" objects.
    """
    def __init__(self):
        super(AnyList, self).__init__(Any.type_id)


def LoadPlugin(plugin):
    # Register the dict type with iograft.
    dict_type = plugin.RegisterPythonType(Dict.type_id,
                                          Dict(),
                                          iograft.ValueToString,
                                          iograft.ValueFromString,
                                          iograft.SerializeValue,
                                          iograft.DeserializeValue)
    # Also register the list type for dicts.
    plugin.RegisterPythonListType(dict_type,
                                  DictList(),
                                  iograft.ValueToString,
                                  iograft.ValueFromString)

    # Register the tuple type with iograft.
    tuple_type = plugin.RegisterPythonType(Tuple.type_id,
                                           Tuple(),
                                           iograft.ValueToString,
                                           iograft.ValueFromString,
                                           iograft.SerializeValue,
                                           iograft.DeserializeValue)
    # Also register the list type for tuples.
    plugin.RegisterPythonListType(tuple_type,
                                  TupleList(),
                                  iograft.ValueToString,
                                  iograft.ValueFromString)

    # Register the "any" type with iograft.
    any_type = plugin.RegisterPythonType(Any.type_id,
                                         Any(),
                                         iograft.ValueToString,
                                         iograft.ValueFromString,
                                         iograft.SerializeValue,
                                         iograft.DeserializeValue)
    # Register the list type for the "any" type.
    plugin.RegisterPythonListType(any_type,
                                  AnyList(),
                                  iograft.ValueToString,
                                  iograft.ValueFromString)

    # Register a cast to the "Any" type from all other types.
    plugin.RegisterTypeCast(iograft.TypeId(), Any.type_id, iograft.AliasCast)

    # Register a cast to the "Any list" type from all other *list* types.
    all_list_types = iograft.TypeId()
    all_list_types.list_dimension = 1
    plugin.RegisterTypeCast(all_list_types,
                            AnyList().GetTypeId(),
                            iograft.AliasCast)
