import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import Planck, Boltzmann, speed_of_light
from scipy.integrate import quad

# Dokladne wyliczenia
# def planck(wavelength, temperature):
#     a = 8.0 * np.pi * Planck * speed_of_light
#     b = wavelength**5
#     c = np.exp(Planck * speed_of_light / (wavelength * Boltzmann * temperature)) - 1
#     return a / (b * c)

def planck(wavelength, temperature):
    a = 8.0 * np.pi * Planck * speed_of_light
    b = wavelength**5
    exponent = Planck * speed_of_light / (wavelength * Boltzmann * temperature)
    c = np.exp(np.minimum(exponent, 500)) - 1
    return a / (b * c)

def plot_black_body_spectrum(temperature):
    wavelengths = np.linspace(1e-9, 3e-6, 1000)
    plt.plot(wavelengths*1e9, planck(wavelengths, temperature), label=f"T = {temperature} K")

def calculate_power_percentage(temperature, wavelength_range):
    total_power, _ = quad(lambda x: planck(x, temperature), 1e-9, 10e-6)
    power_in_range, _ = quad(lambda x: planck(x, temperature), wavelength_range[0], wavelength_range[1])
    return (power_in_range / total_power) * 100

temperatures = [2800, 4000, 5000]
wavelength_range = [3.8e-7, 6.8e-7]  # Przykładowy zakres długości fali

plt.figure()
for T in temperatures:
    plot_black_body_spectrum(T)
    power_percentage = calculate_power_percentage(T, wavelength_range)
    print(f"Dla T = {T} K, procent mocy emitowanej w zakresie {wavelength_range} m wynosi {power_percentage:.2f}%")

plt.title('Spektralna gęstość energii dla ciała doskonale czarnego')
plt.xlabel('Długość fali (nm)')
plt.ylabel('Gęstość energii (J*s/m^3)')
plt.legend()
plt.show()