#------------------------------------------------------------------------------
# discrete_model julia file
# (using partition method for solving linear equations)
# 
# ricardoaf@lccv.ufal.br (version 21/01/2021)
#------------------------------------------------------------------------------

struct Node; u::Vector{Float64}; f::Vector{Float64}; fix::Vector{Int}; end
struct Elem; c::Array{Int,2}; k::Vector{Float64}; f::Vector{Float64}; end

function init(;connectivity, stiffness, displacement, force, fixnode, type="mechanic")
	Node(Float64.(displacement), Float64.(force), Int.(fixnode)),
	Elem(Int.(connectivity), Float64.(stiffness), zeros(length(stiffness))),
	type ≢ "hydraulic" ? 1. : -1.
end

function run!(node, elem, α)
	# global stiffness matrix and partition method	
	partition!(node, kglobal(elem))
	# eval element forces
	internalf!(elem, node, α)
	# return
	node, elem
end

function kglobal(elem)
	# number of nodes and elements
	nnode, nelem = maximum(elem.c), length(elem.k)
	# init matrix
	k = zeros(nnode, nnode)
	# element loop: global assemble from local matrix
	for i = 1:nelem
		k[elem.c[i, :], elem.c[i, :]] += elem.k[i] * [1 -1; -1 1.]
	end
	k # return k
end

function partition!(node, k)
	# free nodes
	fix, dof = node.fix, setdiff(1:length(node.u), node.fix)
	# solve unknowns
	node.u[dof] = k[dof, dof] \ (node.f[dof] - k[dof, fix] * node.u[fix])
	node.f[fix] = k[fix, dof] * node.u[dof] + k[fix, fix] * node.u[fix]
end

function internalf!(elem, node, α)
	# i and j nodes from all elements
	i, j = elem.c[:, 1], elem.c[:, 2]
	# calc element force from relative disp
	@. elem.f = α * elem.k * (node.u[j] - node.u[i])
end
