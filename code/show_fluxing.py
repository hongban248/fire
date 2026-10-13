import fire
from fire import *

def temp_read(path='magellan_fire_long_A。back2/flux1/spec1d_fire_0074-COCONUTS-2A_FIRE_85970523T110233.000_tellcorr.fits'):
    hdul=fits.open(path)
    data=hdul[1].data
    wavelength=data['wave']
    flux=data['flux']
    return wavelength, flux

print(flux_74_path.exists())

wavelength, telluric = get_sensfunc_data()
wave_74, flux_74,ivar_74 = get_flux_data(flux_74_path)
wave_75, flux_75,ivar_75 = get_flux_data(flux_75_path)
wave_76, flux_76,ivar_76 = get_flux_data(flux_76_path)
wave_77, flux_77,ivar_77 = get_flux_data(flux_77_path)

#flux_74_corrected = flux_74 / telluric

#wave_temp,flux_temp = temp_read()

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(wave_74, flux_74, label='Flux 74', color='orange')
plt.plot(wave_75, flux_75, label='Flux 75', color='green')
plt.plot(wave_76, flux_76, label='Flux 76', color='blue')
plt.plot(wave_77, flux_77, label='Flux 77', color='red')

#plt.plot(wave_74, flux_74_corrected, label='Corrected Flux 74', color='green')
#plt.plot(wave_temp, flux_temp, label='Temp Read Flux', color='blue')
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux')
plt.title('Sensfunc and Flux 74 Comparison')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(wave_74, flux_74*np.sqrt(ivar_74), label='Flux 74', color='orange')
plt.plot(wave_75, flux_75*np.sqrt(ivar_75), label='Flux 75', color='green')
plt.plot(wave_76, flux_76*np.sqrt(ivar_76), label='Flux 76', color='blue')
plt.plot(wave_77, flux_77*np.sqrt(ivar_77), label='Flux 77', color='red')
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('errors')
plt.title('errors Comparison')
plt.legend()

#plt.savefig('sensfunc_flux_comparison.png')
plt.show()