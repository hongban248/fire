from pathlib import Path
from astropy.io import fits
from matplotlib import pyplot as plt
import numpy as np

root_path = Path('.')
coconut_dir_path = root_path / 'magellan_fire_long_A' / 'Science.coconuts'
standard_dir_path = root_path / 'magellan_fire_long_A' / 'Science.standard'

sensfunc_path = standard_dir_path / 'sensfunc.fits'

flux_74_path= root_path / 'magellan_fire_long_A' /'74'/'spec1d_fire_0074-COCONUTS-2A_FIRE_85970523T110233.000.fits'
flux_75_path= root_path / 'magellan_fire_long_A' /'75'/'spec1d_fire_0075-COCONUTS-2A_FIRE_85970523T110607.000.fits'
flux_76_path= root_path / 'magellan_fire_long_A' /'76'/'spec1d_fire_0076-COCONUTS-2A_FIRE_85970523T110722.000.fits'
flux_77_path= root_path / 'magellan_fire_long_A' /'77'/'spec1d_fire_0077-COCONUTS-2A_FIRE_85970523T111056.000.fits'

def get_sensfunc_data(path=sensfunc_path):
    hdul=fits.open(path)
    data=hdul[1].data
    wavelength=data['WAVE'][0]
    telluric=data['TELLURIC'][0]
    return wavelength, telluric

def get_flux_data(path):
    hdul=fits.open(path)
    data=hdul[1].data
    wavelength=data['OPT_WAVE']
    flux=data['OPT_FLAM']
    ivar=data['OPT_FLAM_IVAR']
    return wavelength, flux,ivar


def read_txt(file_path,start=-1,end=-1):
    wave, flux, error = np.loadtxt(file_path,
                                     comments='#',      # 跳过所有 # 开头的行
                                     unpack=True)       # 直接拆成三列数组
    
    if start != -1 and end != -1:
        start_id=np.searchsorted(wave, start)
        end_id=np.searchsorted(wave, end)
        wave = wave[start_id:end_id]
        flux = flux[start_id:end_id]
        error = error[start_id:end_id]
    return wave, flux, error

if __name__ == '__main__':
    print(flux_74_path.exists())
    print(flux_75_path.exists())
    print(flux_77_path.exists())

    wave,flux,error=read_txt('code' + '/coadded_spectrum.txt',start=8000,end=25000)

    plt.figure(figsize=(10, 6))
    plt.plot(wave, flux, label='Coadded Spectrum', color='blue')
    plt.show()

    


