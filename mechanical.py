#------------------------------------------------------------------------------
# mechanical python script
# based on mechanical example @ Ramos Jr. & Vieira [ICECE2000] 
# 
# ricardoaf@lccv.ufal.br (version 17/11/2020)
#------------------------------------------------------------------------------
import discrete_model as mdl
import numpy as np

# input
#------------------------------------------------------------------------------

# element stiffness and connectivities
elem = {'k': np.array([300., 200., 300., 200., 300.]),
		'c': np.array([[1,2],[2,3],[2,3],[2,4],[3,4]])}

# nodal displacements, forces and supports
node = {'u': np.array([0., 0., 0., 0.]),
		'f': np.array([0., 0., 0., 10.]),
		'fix': np.array([1])}

# mechanical problem
alpha = 1

# solve discrete model
#------------------------------------------------------------------------------
node, elem = mdl.run(node, elem, alpha)

# output
#------------------------------------------------------------------------------
print('Displacements:'), print(node['u'])
print('Forces:'), print(node['f'])
print('Internal forces:'), print(elem['f'])
