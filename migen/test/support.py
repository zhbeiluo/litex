from migen.fhdl.std import *
from migen.sim import Simulator
from migen.fhdl import verilog


class SimCase:
    def setUp(self, *args, **kwargs):
        self.tb = self.TestBench(*args, **kwargs)

    def test_to_verilog(self):
        verilog.convert(self.tb)

    def run_with(self, generator):
        Simulator(self.tb, generator).run()
