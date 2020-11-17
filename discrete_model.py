#------------------------------------------------------------------------------
# discrete_model python module
# (using partition method for solving linear equations)
# 
# ricardoaf@lccv.ufal.br (version 17/11/2020)
#------------------------------------------------------------------------------
import numpy as np

#------------------------------------------------------------------------------
def run (node, elem, alpha):

	# global stiffness matrix
	kg = kglobal (elem)

	# partition method
	node = partition (node, kg)

	# eval element forces
	elem = internalf (node, elem, alpha)

	# return nodes and elements
	return node, elem

#------------------------------------------------------------------------------
def kglobal (elem):

	nelem = len(elem['k'])
	nnode = max(elem['c'].flatten())

	# init matrix
	k = np.zeros((nnode, nnode))

	# element loop
	for i in range(nelem):

		# local matrix
		ke = elem['k'][i] * np.array([[1,-1], [-1, 1]])

		# global assemble
		conn = elem['c'][i]-1
		k[np.ix_(conn, conn)] += ke

	# return matrix
	return k

#------------------------------------------------------------------------------
def partition (node, k):

	# free nodes
	fix = node['fix']-1
	dof = np.setdiff1d(np.arange(len(node['u'])), fix)

	# sub matrices
	kdd, kdf, kff = k[np.ix_(dof,dof)], k[np.ix_(dof,fix)], k[np.ix_(fix,fix)]

	# solve unknowns
	node['u'][dof] = np.linalg.solve(kdd, node['f'][dof] - kdf @ node['u'][fix])
	node['f'][fix] = kdf.T @ node['u'][dof] + kff @ node['u'][fix]

	# return nodes
	return node

#------------------------------------------------------------------------------
def internalf (node, elem, alpha):

	# i and j nodes from all elements
	i = elem['c'][:, 0]-1
	j = elem['c'][:, 1]-1

	# calc relative u and element f
	du = node['u'][np.ix_(j)] - node['u'][np.ix_(i)]
	elem['f'] = alpha * elem['k'] * du

	# return elements
	return elem
