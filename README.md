# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:

    conda env create -f PW<n>/Lab\ <X>/environment.yml
    conda activate cspc
---

## PW1 LAB A - Reproducible Foundations: Environment, Git & GitHub.

**Environment**

The project uses a Conda environment named "cspc".
Python 3.11, NumPy and pytest were used for this lab.

**How to run?**

You can run the tests by:
    pytest -v

Run the speed comparison by:
    python speed.py

Go to the Lab A folder:
    cd "PW1/LAB A"

**What I built**

A radioactive decay simulation using Python and NumPy.
Added tests and compared the speed of the Python loop and NumPy versions.

**Speed comparison**

The speed comparison was done with N0=200000 and lam=0.4

Results(in seconds):
Pure Python time: 3.8543474560001414
NumPy time 0.00035238899999967543
Speedup: 10937.763255957738

Observation: The NumPy version was much faster than the pure Python one.

**Tests**

The following tests were added:
    The simulation starts with N0;
    A negative decay rate raises a ValueError;
    tyhe average simulation result is close to the analytical decay law.
All 3 tests passed successfully.

**Conclusion**

I learned how to use Git, GitHub, Conda environments and pytest.
Also I tested the radioactive decay simulation and compared the speed between the versions.
Al tests passeed, NumPy version was the fastest.

---

## PW1 LAB B - Data, Plotting, and Automation.

**Data** 

The observed decay data was read from decay_observed.csv.
The data contains time and count values.

**Plot**

I compared the observed data with the analytical exponential decay law.
The observed data followed the general decreasing shape of the analytical curve, but the observed points did not match the curve exactly.

**What I built**

A Python script called plot.py that reads the observed data and creates a figure with two plots:
the observed data on the left and the analytical decay curve on the right.

**Snakemake**

I created a Snakefile to automate the plotting process.
The pipeline uses decay_observed.csv as input and runs plot.py to create figure.png.
Snakemake only runs the step again when the input files or the script have changed.

**Conclusion**

I learned how to read data from a CSV file, plot observed and analytical data with Python, and use Snakemake to automate the process.

---

## PW2 LAB A - Motion from Tracking Data.

**Data**

The free-fall data was read from freefall.csv.
The data contains time and position values.

**What I built**

A Python script called analysis.py that reads the free-fall data and calculates velocity and acceleration using numerical differentiation with NumPy.
Velocity was calculated from position using np.gradient.
Acceleration was calculated from velocity using np.gradient again.

**Acceleration**

The theoretical gravitational acceleration is approximately -9.81 m/s^2

Mean acceleration: -8.57968750000008 m/s^2
Standard deviation: 28.7161257217062 m/s^2

The acceleration data was noisy because numerical differentiation amplifies noise.

**Integration**

I used cumulative_trapezoid to integrate the acceleration and recover velocity and position.
The recovered velocity was calculated from the acceleration, and the recovered position was calculated from the recovered velocity.

**Plot**

I created a figure called motion.png with three plots: position, velocity and acceleration versus time.
A dashed line at -9.81 m/s^2 was added to the acceleration plot to show the theoretical gravitational acceleration.

**Conclusion**

I learned how to read motion data from a CSV file, calculate velocity and acceleration using numerical differentiation, and integrate acceleration to recover velocity and position.
I also learned that differentiation can amplify noise in experimental data.

---

## PW2 LAB B - Optimization in Chemistry.

**Data**

The lab contains several Python scripts for optimization and chemical calculations.
The data and calculations were used to study kinetics, chemical equilibrium and titration.

**Comparison of optimization methods**

Three methods were compared in the warmup part.

For 2A:
Gradient descent: 2.9999963220107015
Newton: 3.0
SLSQP: 3.0

For 2B:
Gradient descent: 1.1309102497941645
Newton: 1.1309011226299859
d2g: 9.347248189989148
SLSQP: -1.3006394477423422

For 2A, all three methods gave almost the same result.
For 2B, gradient descent and Newton gave very similar results, while SLSQP found a different minimum.

**Kinetics**

A Python script called kinetics.py was created to fit the rate constant k for a first-order reaction.
The reaction follows:
C(t) = C0 * exp(-k*t)
The SLSQP optimization method was used to find the value of k.

Result:
SLSQP: 0.26176032098825625

The program also produced kinetics.png with the measured data and the fitted curve.

**Equilibrium**

A Python script called equilibrium.py was created for the reaction:
H2 + I2 <=> 2 HI
The equilibrium extent x was found using two different methods.

Newton result: 0.6638476669609822
SLSQP result: 0.6638476153090014

The two methods gave almost the same result.

The equilibrium amounts were:
H2: 0.3361523330390178 mol
I2: 0.3361523330390178 mol
HI: 1.3276953339219644 mol

The equilibrium plot was saved as equilibrium.png.

**Titration**

The titration.py script was used to find the equivalence point.
Equivalence point: 50.0
The titration plot was saved as titration.png.

**Conclusion**

I learned how to use optimization methods in Python for chemical problems.
I used SLSQP and Newton's method to solve different problems.
I also fitted a reaction rate constant, calculated chemical equilibrium and found the equivalence point in a titration.