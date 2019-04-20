import formulae as f
from inputs import fred
import math

def Error_calculator(global_inputs,field,sigma_x,sigma_t,astrometry_type):
	if astrometry_type == 'Diff. w.r.t ref stars':
		error = diff_ref(global_inputs,field,sigma_x,sigma_t)
	elif astrometry_type == 'Diff. w.r.t Sci. Objects':
		error = diff_sci(global_inputs,field,sigma_x)
	elif astrometry_type == 'Absolute Astrometry':
		error = abs_astrometry(global_inputs,field,sigma_x)
	else:
		print('No option selected. Something went wrong')

	return error

def diff_ref(global_inputs,field,sigma_x,sigma_t):
	noise_err = f.D2(sigma_x['Focal-plane measurement errors']['Noise'],sigma_x['Focal-plane measurement errors']['Noise'],field,fred)
	noise_cal_err = f.D2(sigma_x['Focal-plane measurement errors']['Noise calibration errors'],sigma_x['Focal-plane measurement errors']['Noise calibration errors'],field,fred)
	pix_blur = f.D2(sigma_x['Focal-plane measurement errors']['Pixel blur'],sigma_x['Focal-plane measurement errors']['Pixel blur'],field,fred)
	pix_irr = f.D2(sigma_x['Focal-plane measurement errors']['Pixel irregularities'],sigma_x['Focal-plane measurement errors']['Pixel irregularities'],field,fred)
	det_nl = f.D2(sigma_x['Focal-plane measurement errors']['Detector non-linearity'],sigma_x['Focal-plane measurement errors']['Detector non-linearity'],field,fred)
	PSF_rec = f.D2(sigma_x['Focal-plane measurement errors']['PSF reconstruction'],sigma_x['Focal-plane measurement errors']['PSF reconstruction'],field,fred)
	conf_err = f.D2(sigma_x['Focal-plane measurement errors']['Confusion'],sigma_x['Focal-plane measurement errors']['Confusion'],field,fred)

# needs an if statement
	NGS_pos_err = f.PS1(sigma_t['Opto-mechanical errors']['NGS position errors'],field,global_inputs)

	NF_IR_optics = f.D2(sigma_x['Opto-mechanical errors']['NFIAROS_IRIS optics'],sigma_x['Opto-mechanical errors']['NFIAROS_IRIS optics'],field,fred)

	return math.sqrt(noise_err+noise_cal_err+pix_blur+pix_irr+det_nl+PSF_rec+conf_err+NGS_pos_err+NF_IR_optics)

def diff_sci(global_inputs,field,sigma_x):
	return 2.02

def abs_astrometry(global_inputs,field,sigma_x):
	return 3.03