import time
from decay import simulate_loop, simulate
N0=200000
lam=0.4
start=time.perf_counter()
simulate_loop(N0, lam)
loop_time=time.perf_counter()-start
start=time.perf_counter()
simulate(N0, lam)
numpy_time=time.perf_counter()-start
print("Pure Python time:", loop_time)
print("NumPy time", numpy_time)
print("Speedup:", loop_time/numpy_time)