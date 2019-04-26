
# The underlying formulae to calculate error variances
def A1(Sx_sci,Sx_ref,field,fred):
	Nref = field['Nref']
	return ((Sx_sci**2+Sx_ref**2/Nref)**0.5*fred)**2

def A2(Sx_sci):
	return (Sx_sci)**2

def D1(Sx_sci_1,Sx_sci_2,field,fred):
	Nref = field['Nref']
	return ((Sx_sci_1**2+Sx_sci_2**2)**0.5*fred)**2

def D2(Sx_sci,Sx_field,field,fred):
	Nfield = field['Nfield']
	return ((Sx_sci**2 + Sx_field**2/Nfield)**0.5*fred)**2

def DR1(S_theta_ref,field,fred,Nmodes):
	Nref = field['Nref']
	return (((Nmodes/Nref)**0.5)*S_theta_ref*fred)**2

def PS1(S_theta_NGS,field,global_inputs):
	Nref = field['Nref']
	rsep = field['rsep']
	rNGS = global_inputs['rngs']
	return ((S_theta_NGS*rsep/rNGS))**2

def PS2(S_theta_ref,field,global_inputs):
	Nref = field['Nref']
	rsep = field['rsep']
	rref = global_inputs['rref']
	return (((3/Nref)**0.5*S_theta_ref*rsep/rref))**2