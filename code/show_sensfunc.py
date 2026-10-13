import fire
from fire import *


hdul=fits.open(sensfunc_path)
#print(hdul[1].data)

data=hdul[1].data
print(data.dtype.names)

wavelength=data['WAVE'][0]
telluric=data['TELLURIC'][0]

print(wavelength)
print(telluric)

plt.figure(figsize=(10, 6))
plt.plot(wavelength, telluric, color='blue', label='Telluric Sensitivity Function')
plt.legend()
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Telluric')
plt.title('Telluric Sensitivity Function')
plt.show()



        