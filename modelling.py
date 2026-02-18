import numpy as np
import matplotlib.pyplot as plt


# Define Constants
# -----------------------------
R = 8.314  # Gas constant (J/mol·K)

D0_actual = 1e-5      # Pre-exponential factor (m^2/s)
Q_actual = 80000      # Activation energy (J/mol)


#Generate Temperature Data
# -----------------------------
T = np.linspace(800, 1200, 20)  # Temperature range in Kelvin

# Arrhenius Equation
D = D0_actual * np.exp(-Q_actual / (R * T))


# Transform to Linear Form
# ln(D) = ln(D0) - Q/R * (1/T)
# -----------------------------
x = 1 / T
y = np.log(D)


#  Linear Regression implementation
# -----------------------------
n = len(x)

m = (n * np.sum(x*y) - np.sum(x)*np.sum(y)) / \
    (n * np.sum(x**2) - (np.sum(x))**2)

c = (np.sum(y) - m * np.sum(x)) / n


# Extract Physical Parameters
# -----------------------------
Q_predicted = -m * R
D0_predicted = np.exp(c)

# Results
# -----------------------------
print("Actual Activation Energy (Q):", Q_actual)
print("Predicted Activation Energy (Q):", Q_predicted)

print("Actual D0:", D0_actual)
print("Predicted D0:", D0_predicted)


# Plot Results
# -----------------------------
plt.scatter(x, y, label="Data")
plt.plot(x, m*x + c, color='red', label="Regression Line")
plt.xlabel("1/T (1/K)")
plt.ylabel("ln(D)")
plt.title("Arrhenius Plot with Linear Regression")
plt.legend()
plt.show()