import fire
from fire import *


wave_74, flux_74, ivar_74 = get_flux_data(flux_74_path)
wave_75, flux_75, ivar_75 = get_flux_data(flux_75_path)
wave_76, flux_76, ivar_76 = get_flux_data(flux_76_path)
wave_77, flux_77, ivar_77 = get_flux_data(flux_77_path)

#wave_sens, telluric = get_sensfunc_data(sensfunc_path)

wave_74 = np.asarray(wave_74, dtype=float).squeeze()
flux_74 = np.asarray(flux_74, dtype=float).squeeze()
ivar_74 = np.asarray(ivar_74, dtype=float).squeeze()
wave_75 = np.asarray(wave_75, dtype=float).squeeze()
flux_75 = np.asarray(flux_75, dtype=float).squeeze()
ivar_75 = np.asarray(ivar_75, dtype=float).squeeze()
wave_76 = np.asarray(wave_76, dtype=float).squeeze()
flux_76 = np.asarray(flux_76, dtype=float).squeeze()
ivar_76 = np.asarray(ivar_76, dtype=float).squeeze()
wave_77 = np.asarray(wave_77, dtype=float).squeeze()
flux_77 = np.asarray(flux_77, dtype=float).squeeze()
ivar_77 = np.asarray(ivar_77, dtype=float).squeeze()

scale_75_to_74 = np.median(flux_74) / np.median(flux_75)
scale_76_to_74 = np.median(flux_74) / np.median(flux_76)
scale_77_to_74 = np.median(flux_74) / np.median(flux_77)

#print(f"Scale factor for flux_75 to flux_74: {scale_77_to_74}")

flux_75 = flux_75 * scale_75_to_74
flux_76 = flux_76 * scale_76_to_74
flux_77 = flux_77 * scale_77_to_74

ivar_75 = ivar_75 / (scale_75_to_74 ** 2)
ivar_76 = ivar_76 / (scale_76_to_74 ** 2)
ivar_77 = ivar_77 / (scale_77_to_74 ** 2)

def interpolate_to_74(wave, flux, ivar):
	order = np.argsort(wave)
	wave = wave[order]
	flux = flux[order]
	ivar = ivar[order]
	return (
		wave_74,
		np.interp(wave_74, wave, flux, left=0.0, right=0.0),
		np.interp(wave_74, wave, ivar, left=0.0, right=0.0),
	)


wave_75, flux_75, ivar_75 = interpolate_to_74(wave_75, flux_75, ivar_75)
wave_76, flux_76, ivar_76 = interpolate_to_74(wave_76, flux_76, ivar_76)
wave_77, flux_77, ivar_77 = interpolate_to_74(wave_77, flux_77, ivar_77)

wave=wave_74

flux=[(flux_74[i]*ivar_74[i]+flux_75[i]*ivar_75[i]+flux_76[i]*ivar_76[i]+flux_77[i]*ivar_77[i])/(ivar_74[i]+ivar_75[i]+ivar_76[i]+ivar_77[i]) for i in range(len(wave_74))]
error=[np.sqrt(1/(ivar_74[i]+ivar_75[i]+ivar_76[i]+ivar_77[i])) for i in range(len(wave_74))]
print(len(flux))
def interpolate_to_sensfunc(wave, flux,error, telluric):
    
    return (
        wave_sens,
        np.interp(wave_sens, wave, flux, left=0.0, right=0.0) / telluric,
        np.interp(wave_sens, wave, error, left=0.0, right=0.0) / telluric
    )

#wave, flux ,error= interpolate_to_sensfunc(wave, flux, error, telluric)

def make_txt(wave, flux, error, output_path):
    with open(output_path, 'w') as f:
        f.write("# Wavelength (um)    Flux    Error\n")
        for w, fl, err in zip(wave, flux, error):
            f.write(f"{w/1e4}    {fl/1e17}    {err/1e17}\n")

make_txt(wave, flux, error, "code/coadded_spectrum.txt")

plt.figure(figsize=(10, 6))
plt.plot(wave, flux, label='Coadded Spectrum', color='blue')
plt.plot(wave, flux_74, label='Flux 74', color='orange', alpha=0.5)
plt.plot(wave, flux_75, label='Flux 75', color='green', alpha=0.5)
plt.plot(wave, flux_76, label='Flux 76', color='blue', alpha=0.5)
plt.plot(wave, flux_77, label='Flux 77', color='red', alpha=0.5)
plt.xlabel('Wavelength (Angstroms)')
plt.ylabel('Flux')
plt.title('Coadded Spectrum from Flux 74, 75, 76, and 77')
plt.legend()
plt.grid()
plt.show()


