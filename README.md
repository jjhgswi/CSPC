# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.

## PW1 LAB A - Reproducible Foundations: Environment, Git & GitHub.

** Environment **
The project uses a Conda environment named "cspc".
Python 3.11, NumPy and pytest were used for this lab.

** How to run? **
You can run the tests by:
bash pytest -v

Run the speed comparison by:
bash python speed.by

Go to the Lab A folder:
cd "PW1/LAB A"

** What I built **
A radioactive decay simulation using Python and NumPy.
Added tests and compared the speed of the Python loop and NumPy versions.

** Speed comparison **
The speed comparison was done with N0=200000 and lam=0.4

Results(in seconds):
Pure Python time: 3.8543474560001414
NumPy time 0.00035238899999967543
Speedup: 10937.763255957738

Observation: The NumPy version was much faster than the pure Python one.

** Tests **
The following tests were added:
    The simulation starts with N0;
    A negative decay rate raises a ValueError;
    tyhe average simulation result is close to the analytical decay law.
All 3 tests passed successfully.

** Conclusion **
I learned how to use Git, GitHub, Conda environments and pytest.
Also I tested the radioactive decay simulation and compared the speed between the versions.
Al tests passeed, NumPy version was the fastest.