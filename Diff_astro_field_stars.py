# Calculate differential astrometry error using field objects.
from inputs import fred
import formulae as f
import math
def diff_ref(global_inputs,field,sigma_x,sigma_t):
	noise_err = f.D2(sigma_x['Focal-plane measurement errors']['Noise'],sigma_x['Focal-plane measurement errors']['Noise'],field,fred)
	noise_cal_err = f.D2(sigma_x['Focal-plane measurement errors']['Noise calibration errors'],sigma_x['Focal-plane measurement errors']['Noise calibration errors'],field,fred)
	pix_blur = f.D2(sigma_x['Focal-plane measurement errors']['Pixel blur'],sigma_x['Focal-plane measurement errors']['Pixel blur'],field,fred)
	pix_irr = f.D2(sigma_x['Focal-plane measurement errors']['Pixel irregularities'],sigma_x['Focal-plane measurement errors']['Pixel irregularities'],field,fred)
	det_nl = f.D2(sigma_x['Focal-plane measurement errors']['Detector non-linearity'],sigma_x['Focal-plane measurement errors']['Detector non-linearity'],field,fred)
	PSF_rec = f.D2(sigma_x['Focal-plane measurement errors']['PSF reconstruction'],sigma_x['Focal-plane measurement errors']['PSF reconstruction'],field,fred)
	conf_err = f.D2(sigma_x['Focal-plane measurement errors']['Confusion'],sigma_x['Focal-plane measurement errors']['Confusion'],field,fred)

	FP_err = noise_err + noise_cal_err + pix_blur + pix_irr + det_nl + PSF_rec + conf_err
	# print(math.sqrt(FP_err))

	if field['Nref'] < 3: 
		NGS_pos_err = f.PS1(sigma_t['Opto-mechanical errors']['NGS position errors'],field,global_inputs)
	elif field['Nref'] >= 3:
		NGS_pos_err = 0
	NF_IR_optics = f.D2(sigma_x['Opto-mechanical errors']['NFIAROS_IRIS optics'],sigma_x['Opto-mechanical errors']['NFIAROS_IRIS optics'],field,fred)
	NF_IR_SFE = f.D2(sigma_x['Opto-mechanical errors']['NFIAROS_IRIS surfaces'],sigma_x['Opto-mechanical errors']['NFIAROS_IRIS surfaces'],field,fred)
	QS_dist = f.D2(sigma_x['Opto-mechanical errors']['Quasi_static distortions'],sigma_x['Opto-mechanical errors']['Quasi_static distortions'],field,fred)
	tel_opt = f.D2(sigma_x['Opto-mechanical errors']['Telescope optics'],sigma_x['Opto-mechanical errors']['Telescope optics'],field,fred)
	rot_err = f.D2(sigma_x['Opto-mechanical errors']['Rotator errors'],sigma_x['Opto-mechanical errors']['Rotator errors'],field,fred)
	Act_spikes = f.D2(sigma_x['Opto-mechanical errors']['Actuators diffr spikes'],sigma_x['Opto-mechanical errors']['Actuators diffr spikes'],field,fred)
	Vib_err = f.D2(sigma_x['Opto-mechanical errors']['Vibrations'],sigma_x['Opto-mechanical errors']['Vibrations'],field,fred)
	cop_atm_eff = f.D2(sigma_x['Opto-mechanical errors']['Coupling atm effects'],sigma_x['Opto-mechanical errors']['Coupling atm effects'],field,fred)

	opt_mech_err =NGS_pos_err+  NF_IR_optics + NF_IR_SFE + QS_dist + tel_opt + rot_err + Act_spikes + Vib_err + cop_atm_eff
	# print(math.sqrt(opt_mech_err))

	achr_diff_ref = f.D2(sigma_x['Atmospheric refraction errors']['Achromatic differential refraction'],sigma_x['Atmospheric refraction errors']['Achromatic differential refraction'],field,fred)
	DSO_err = f.D2(sigma_x['Atmospheric refraction errors']['Dispersion obj spectra'],sigma_x['Atmospheric refraction errors']['Dispersion obj spectra'],field,fred)
	DAC_err = f.D2(sigma_x['Atmospheric refraction errors']['Dispersion atm conditions'],sigma_x['Atmospheric refraction errors']['Dispersion atm conditions'],field,fred)
	DADC_pos = f.D2(sigma_x['Atmospheric refraction errors']['Dispersion ADC position'],sigma_x['Atmospheric refraction errors']['Dispersion ADC position'],field,fred)
	Disp_var = f.D2(sigma_x['Atmospheric refraction errors']['Dispersion variability'],sigma_x['Atmospheric refraction errors']['Dispersion variability'],field,fred)

	Atm_ref_err = achr_diff_ref + DSO_err + DAC_err + DADC_pos + Disp_var
	# print(math.sqrt(Atm_ref_err))
	if field['Nref'] <3:
		Diff_TTJ_PS = f.D1(sigma_x['Residual turbulence errors']['Diff TTJ plate scale'],sigma_x['Residual turbulence errors']['Diff TTJ plate scale'],field,field['rsep']/28)
	elif field['Nref'] >=3:
		Diff_TTJ_PS = 0

	Diff_TTJ_HO = f.D2(sigma_x['Residual turbulence errors']['Diff TTJ higher order'],sigma_x['Residual turbulence errors']['Diff TTJ higher order'],field,fred)
	PSF_irr = f.D2(sigma_x['Residual turbulence errors']['PSF irregularities'],sigma_x['Residual turbulence errors']['PSF irregularities'],field,fred)
	PSF_HE = f.D2(sigma_x['Residual turbulence errors']['Halo effect'],sigma_x['Residual turbulence errors']['Halo effect'],field,fred)
#	TC_var = f.D2(sigma_x['Residual turbulence errors']['Turb conditions variability'],sigma_x['Residual turbulence errors']['Turb conditions variability'],field,fred)

	Res_turb_err = Diff_TTJ_PS + Diff_TTJ_HO + PSF_irr + PSF_HE 
	# print(math.sqrt(Res_turb_err))

	if field['Nref']<3:
		pos_err = f.PS1(sigma_t['Reference obj n catalog errors']['Position errors'],field,global_inputs)
		PM_err = f.PS1(sigma_t['Reference obj n catalog errors']['Proper motion errors'],field,global_inputs)
		Abr_grav_err = f.PS1(sigma_t['Reference obj n catalog errors']['Aberration grav deflection'],field,global_inputs)
		other_err = f.PS1(sigma_t['Reference obj n catalog errors']['Other'],field,global_inputs)
	elif field['Nref']>=3:
		pos_err = f.PS2(sigma_t['Reference obj n catalog errors']['Position errors'],field,global_inputs)
		PM_err = f.PS2(sigma_t['Reference obj n catalog errors']['Proper motion errors'],field,global_inputs)
		Abr_grav_err = f.PS2(sigma_t['Reference obj n catalog errors']['Aberration grav deflection'],field,global_inputs)
		other_err = f.PS2(sigma_t['Reference obj n catalog errors']['Other'],field,global_inputs)

	ref_obj_cat_err = pos_err + PM_err + Abr_grav_err + other_err
	# print(ref_obj_cat_err)

	return math.sqrt(FP_err + opt_mech_err + Atm_ref_err + Res_turb_err + ref_obj_cat_err)