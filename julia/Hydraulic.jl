#------------------------------------------------------------------------------
# hydraulic julia script
# based on mechanical example @ Ramos Jr. & Vieira [ICECE2000] 
# 
# ricardoaf@lccv.ufal.br (version 21/01/2021)
#------------------------------------------------------------------------------
include("DiscreteModel.jl")

function Hydraulic()

	node, elem, α = init(
		connectivity=[1 2; 2 4; 2 3; 2 5; 3 6; 6 5; 4 6; 6 7; 4 5; 3 5],
		stiffness=[3, 5, 3, 2, 2, 2, 4, 2, 3, 3],
		displacement=[10, 0, 0, 0, 0, 0, 0],
		force=[0, 0, 0, 0, 0, 0, -8],
		fixnode=[1],
		type="hydraulic")

	node, elem = run!(node, elem, α)

	println("     Pressures: ", node.u)
	println("         Flows: ", node.f)
	println("Internal flows: ", elem.f)
end
