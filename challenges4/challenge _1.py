import numpy as np

températures =np.array([15, 20, 18, 17, 46, 14])

moyenne = np.mean(températures)
media = np.median(températures)
std = np.std(températures)


print(f"Température moyenne: {moyenne:.2f} °C")
print(f"Température media: {media:.2f} °C")
print(f"Température std: {std:.2f} °C")

