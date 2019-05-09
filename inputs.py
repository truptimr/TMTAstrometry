# These inputs are inputs to calculations in Absolute_astrometry.py, Diff_astro_sci_objects.py
# Diff_astro_field_stars.py. The inputs are either 1) predefined constants, user inputs from UI or derived from user inputs in  function error_calculator.py
global_inputs = {
"wavelength" : 0.0000022,
"SNR" : 200,
"rngs" : 30,
"rref" : 17,
"T" : 100,
"dt_epoch" : 1}

field = {
"Nref" : 0,
"rsep" : 1,
"Nfield" : 1,
"Nsci" : 1}

sigma_x = {'Focal-plane measurement errors':{
		'Noise' : 1,
		'Noise calibration errors': 4,
		'Pixel blur': 1,
		'Pixel irregularities': 2,
		'Detector non-linearity': 1,
		'PSF reconstruction': 5,
		'Confusion': 5
	},
	'Opto-mechanical errors':{
		'NGS position errors': 0,
		'NFIAROS_IRIS optics': 8,
		'NFIAROS_IRIS surfaces': 7,
		'Quasi_static distortions': 5,
		'Telescope optics': 5,
		'Rotator errors': 3,
		'Actuators diffr spikes': 1,
		'Vibrations': 5,
		'Coupling atm effects': 3
	},
	'Atmospheric refraction errors':{
		'Achromatic differential refraction': 2,
		'Dispersion obj spectra': 5,
		'Dispersion atm conditions': 5,
		'Dispersion ADC position': 1,
		'Dispersion variability': 2
	},
	'Residual turbulence errors':{
		'Diff TTJ plate scale': 15.0,
		'Diff TTJ higher order': 10.5,
		'PSF irregularities': 5.5,
		'Halo effect': 3
#		'Turb conditions variability': 1
	},
	'Reference obj n catalog errors':{
	'Position errors' : 0,
	'Proper motion errors': 0,
	'Aberration grav deflection': 0,
	'Other': 0
	}
}

sigma_t = {'Focal-plane measurement errors':{
		'Noise' : 0,
		'Noise calibration errors': 0,
		'Pixel blur': 0,
		'Pixel irregularities': 0,
		'Detector non-linearity': 0,
		'PSF reconstruction': 0,
		'Confusion': 0
	},
	'Opto-mechanical errors':{
		'NGS position errors': 2000,
		'NFIAROS_IRIS optics': 0,
		'NFIAROS_IRIS surfaces': 0,
		'Quasi_static distortions': 0,
		'Telescope optics': 0,
		'Rotator errors': 0,
		'Actuators diffr spikes': 0,
		'Vibrations': 0,
		'Coupling atm effects': 0
	},
	'Atmospheric refraction errors':{
		'Achromatic differential refraction': 0,
		'Dispersion obj spectra': 0,
		'Dispersion atm conditions': 0,
		'Dispersion ADC position': 0,
		'Dispersion variability': 0
	},
	'Residual turbulence errors':{
		'Diff TTJ plate scale': 0,
		'Diff TTJ higher order': 0,
		'PSF irregularities': 0,
		'Halo effect': 0
#		'Turb conditions variability': 0
	},
	'Reference obj n catalog errors':{
	'Position errors' : 1000,
	'Proper motion errors': 500,
	'Aberration grav deflection': 1,
	'Other': 1
	}
}

fred = 1
