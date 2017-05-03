# Physics 91SI
# Spring 2017
# Lab 8

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""


    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets x position "pos" is the instance variable
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))

class Molecule:

	def __init__(self, position1, position2, mass1, mass2,sprConstant, equiLength):
		self.p1 = Particle(position1, mass1)
		self.p2 = Particle(position2, mass2)

		self.k = sprConstant
		self.LO = equiLength
		
		self.p1.pos = position1
		self.p2.pos = position2

		self.p1.m = mass1
		self.p2.m = mass2

	def get_displ(self):
		dr = self.p1.pos - self.p2.pos
		return dr

	def get_force(self):
		"""Returns the force acting on particle 1"""
		dr = self.get_displ()
		drMag = np.linalg.norm(dr)
		forceMag = (drMag - self.LO) * self.k
		return forceMag * (dr / drMag) 