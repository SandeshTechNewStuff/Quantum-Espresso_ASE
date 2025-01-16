# Quantum-Espresso_ASE

# Bulk Modulus and Equilibrium Lattice Constant Calculation for NiO

This project demonstrates how to calculate the **bulk modulus** and **equilibrium lattice constant** for a NiO crystal structure using the Atomic Simulation Environment (ASE). It involves reading the crystal structure from a `.cif` file, performing a series of energy calculations, and fitting the results to an equation of state.

## Overview

The code:
1. Reads the NiO crystal structure from a `.cif` file.
2. Assigns an EMT (Effective Medium Theory) potential calculator.
3. Varies the cell volume and computes the potential energy for each configuration.
4. Fits the computed data to an equation of state (EOS) to derive:
   - Equilibrium lattice constant.
   - Bulk modulus in GPa.
5. Outputs a plot of the EOS fit and the calculated properties.

## Requirements

- Python 3.7 or higher
- ASE (Atomic Simulation Environment)
- NumPy

## Setup

1. Install the required packages:
   ```bash
   pip install ase numpy matplotlib
2. Place the NiO.cif file in the same directory as the script.
3. Run the script:python script_name.py
4. Key Features

    Supports multiple EOS models:
        Taylor
        Murnaghan
        Birch
        Birch-Murnaghan
        Pourier-Tarantola
        Vinet
        Anton-Schmidt
        Polynomial (P3)
