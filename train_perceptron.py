import neurolab as nl
import numpy as np

# Create train samples
x = np.linspace(-7, 7, 20)
y = np.linspace(-7, 7, 5);

size = len(x)

inp = x.reshape(size / 4,4)
tar = y.reshape(len(y), 1)

# Create network with 2 layers and random initialized
net = nl.net.newff([[-7, 7], [-7, 7], [-7, 7], [-7, 7]],[5, 1])

print inp
# Train network
error = net.train(inp, tar, epochs=500, show=100, goal=0.02)

# Simulate network
out = net.sim(inp)

print out
