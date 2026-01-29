import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

os.makedirs('figs', exist_ok=True)
plt.figure()
plt.plot([1, 2, 3], [1, 2, 3])
plt.title("Test")
plt.savefig('figs/test_gen.png')
print("Test generation complete.")
