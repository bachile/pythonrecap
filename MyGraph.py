# Step 1
# Create virtual environment
# mac - python 3 -m venv _____
# pc - py -3 -m venv _____

# Step 2
# Activate virtual environment
# mac - source myvenv/bin/activate
# pc - myvenv\scripts\activate

# Step 3
# Install 3rd party library/module
# pip3 install {library} (in terminal)

# Git config (for new account)
# git config --global user.name "Brando"
# git config --global user.email "brando_lezzana1@baylor.edu"
# (in terminal)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")

