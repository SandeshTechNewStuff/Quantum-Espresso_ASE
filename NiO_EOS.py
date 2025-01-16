import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io.trajectory import Trajectory
from ase.eos import EquationOfState
from ase.io import read
from ase.units import kJ


a = 4.186  

NiO = read('NiO.cif')


NiO.calc = EMT()


traj = Trajectory('NiO.traj', 'w')


cell = NiO.get_cell()


for x in np.linspace(0.95, 1.05, 5):  
    NiO.set_cell(cell * x, scale_atoms=True)
    NiO.get_potential_energy()  
    traj.write(NiO)  


configs = read('NiO.traj@0:5')  


volumes = [NiO.get_volume() for NiO in configs]
energies = [NiO.get_potential_energy() for NiO in configs]


eos = EquationOfState(volumes, energies, eos='taylor')
#taylor
#murnaghan
#birch
#birchmurnaghan
#pouriertarantola
#vinet
#antonschmidt
#p3
v0, e0, B = eos.fit()


bulk_modulus_gpa = B / kJ * 1.0e24
lattice_constant = (v0 )** (1/3)  # Convert volume to lattice constant (cubic root)


print(f"Equilibrium lattice constant: {lattice_constant:.4f} Å")
print(f"Bulk modulus: {bulk_modulus_gpa:.2f} GPa")


eos.plot('NiO-eos.png')

