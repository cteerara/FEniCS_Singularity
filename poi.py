"""
FEniCS tutorial demo program: Poisson equation with Dirichlet conditions.
Test problem is chosen to give an exact solution at all nodes of the mesh.
  -Laplace(u) = f    in the unit square
            u = u_D  on the boundary
  u_D = 1 + x^2 + 2y^2
    f = -6
"""

from __future__ import print_function
from fenics import *
import matplotlib.pyplot as plt
import numpy as np

# Create mesh and define function space
mesh = UnitSquareMesh(10,10)
V = FunctionSpace(mesh, 'P', 1)

# Define boundary condition
u_D = Expression('2 + x[0]*x[0] + 2*x[1]*x[1]', degree=2)

def boundary(x, on_boundary):
    return on_boundary

bc = DirichletBC(V, u_D, boundary)

# Define variational problem
u = TrialFunction(V)
v = TestFunction(V)
f = Constant(-6.0)
a = dot(grad(u), grad(v))*dx
L = f*v*dx

# Compute solution
u = Function(V)
solve(a == L, u, bc, solver_parameters={'linear_solver': 'mumps'})

#print(u.vector().max())
#print(u.vector().min())


#vtd = V.tabulate_dof_coordinates()
#print('haii')
#print(vtd)
#arr = u.vector().get_local()
#coor = mesh.coordinates()
#values = list()
#for i, dum in enumerate(coor):
#    values.append([arr[vtd[2*i]], arr[vtd[2*i+1]]])
#values = np.array(values)
#print(values)




## Plot solution and mesh
#ctr = plot(u, title = "Haiiii")
#clb = plt.colorbar(ctr,orientation='vertical')
#
## Save solution to file in VTK format
#vtkfile = File('poisson/solution.pvd')
#vtkfile << u
#
## Compute error in L2 norm
#error_L2 = errornorm(u_D, u, 'L2')
#
## Compute maximum error at vertices
#vertex_values_u_D = u_D.compute_vertex_values(mesh)
#vertex_values_u = u.compute_vertex_values(mesh)
#import numpy as np
#error_max = np.max(np.abs(vertex_values_u_D - vertex_values_u))
#
## Print errors
#print('error_L2  =', error_L2)
#print('error_max =', error_max)
#
### Hold plot
