#------------------------------------------------------------------------------
# hidraulic python script
# based on hidraulic example @ Ramos Jr. & Vieira [ICECE2000] 
# 
# ricardoaf@lccv.ufal.br (version 17/11/2020)
#------------------------------------------------------------------------------
import discrete_model as mdl
import numpy as np

# input
#------------------------------------------------------------------------------

# element 'stiffness' and connectivities
elem = {'k': np.array([3., 5., 3., 2., 2., 2., 4., 2., 3., 3.]),
		'c': np.array([[1,2],[2,4],[2,3],[2,5],[3,6],
					   [6,5],[4,6],[6,7],[4,5],[3,5]])}

# nodal 'displacements', 'forces' and 'supports'
node = {'u': np.array([10., 0., 0., 0., 0., 0., 0.]),
		'f': np.array([0., 0., 0., 0., 0., 0., -8.]),
		'fix': np.array([1])}

# hidraulic problem
alpha = -1

# solve discrete model
#------------------------------------------------------------------------------
node, elem = mdl.run(node, elem, alpha)

# output
#------------------------------------------------------------------------------
print('Displacements:'), print(node['u'])
print('Forces:'), print(node['f'])
print('Internal forces:'), print(elem['f'])
