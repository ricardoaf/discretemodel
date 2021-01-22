#------------------------------------------------------------------------------
# mechanical julia script
# based on mechanical example @ Ramos Jr. & Vieira [ICECE2000] 
# 
# ricardoaf@lccv.ufal.br (version 21/01/2021)
#------------------------------------------------------------------------------
include("DiscreteModel.jl")

function Mechanical()

	node, elem, α = init(
		connectivity=[1 2; 2 3; 2 3; 2 4; 3 4],
		stiffness=[300, 200, 300, 200, 300],
		displacement=[0, 0, 0, 0],
		force=[0, 0, 0, 10],
		fixnode=[1],
		type="mechanic")

	node, elem = run!(node, elem, α)

	println("  Displacements: ", node.u)
	println("         Forces: ", node.f)
	println("Internal forces: ", elem.f)
end
