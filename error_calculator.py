from Diff_astro_field_stars import diff_ref
from Diff_astro_sci_objects import diff_sci
from Absolute_astrometry import abs_astrometry


def Error_calculator(global_inputs,field,sigma_x,sigma_t,astrometry_type):
	sigma_x['Focal-plane measurement errors']['Noise'] = 3400000000*global_inputs['wavelength']/global_inputs['SNR']
	sigma_x['Opto-mechanical errors']['Diff TTJ plate scale'] = 150*global_inputs['T']**0.5
	sigma_x['Opto-mechanical errors']['Diff TTJ higher order'] = 105*global_inputs['T']**0.5
	sigma_x['Opto-mechanical errors']['PSF irregularities'] = 55*global_inputs['T']**0.5	
	sigma_t['Opto-mechanical errors']['Proper motion errors'] = 500*global_inputs['dt_epoch']

	if astrometry_type == 'Diff. w.r.t ref stars':
		error = diff_ref(global_inputs,field,sigma_x,sigma_t)
	elif astrometry_type == 'Diff. w.r.t Sci. Objects':
		error = diff_sci(global_inputs,field,sigma_x,sigma_t)
	elif astrometry_type == 'Absolute Astrometry':
		error = abs_astrometry(global_inputs,field,sigma_x,sigma_t)
	else:
		print('No option selected. Something went wrong')

	return error




