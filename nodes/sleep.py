# Copyright 2022 Fabrica Software, LLC

import iograft
import iobasictypes
import time


class Sleep(iograft.Node):
    """
    Sleep for a given number of seconds.
    """
    seconds = iograft.InputDefinition("time", iobasictypes.Int())

    @classmethod
    def GetDefinition(cls):
        node = iograft.NodeDefinition("sleep")
        node.SetMenuPath("General")
        node.AddInput(cls.seconds)
        return node

    @staticmethod
    def Create():
        return Sleep()

    def Process(self, data):
        seconds = iograft.GetInput(self.seconds, data)
        time.sleep(seconds)


def LoadPlugin(plugin):
    node = Sleep.GetDefinition()
    plugin.RegisterNode(node, Sleep.Create)
