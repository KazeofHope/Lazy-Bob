# This is a simulation of the impact the vectors of Lazy Bob's wheel will have on the body of Lazy Bob.

from manimlib import *
import numpy as np

class Simulation(Scence):
    Lazy_Bob = Triangle()
    Lazy_Bob.set_fill(color = BLUE, opacity = 0.5)
    Lazy_Bob.set_stroke(color = BLUE, width = 3)

    self.play(ShowCreation(Lazy_Bob))
    self.wait()
    