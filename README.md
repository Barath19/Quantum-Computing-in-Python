# Quantum-Computing-in-Python
Generating Random numbers in a quantum computer
Requirements: Projectq

To install projectq:  pip install projectq


A qubit is a quantum system consisting of two energy levels, labeled |0⟩ and |1⟩. The |0⟩ state is often called the ground state because it is the lower of the two energies. Together, |0⟩ and |1⟩ make up what we call “standard basis vectors”. Like all vectors, they point in a direction and have a magnitude. Defining basis vectors is a really useful trick we have borrowed from linear algebra. The basic idea is that once you have defined these vectors, you can construct any other vector from a linear combination of the basis vectors.


Additionally, qubits also have a “phase”, which results from the fact that superpositions can be complex. To represent these superpositions, we put a coefficient such as a or b in front of the state like so: a|0⟩+b|1⟩. Here’s what the formula is saying: “The state is made up of a linear combination of |0⟩ and |1⟩, where the proportion of each depends on the coefficients a and b.” The coefficients a and b could be positive, negative, or even complex. If we take the absolute value of a or b and square it (e.g. |a|2‘﻿or:math:‘|b|2 ), we get the probability of measuring the 0 or 1 outcome, respectively.
