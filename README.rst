===============================================
UFL+ - Unified Form Language with GLP Extension
===============================================

UFL+ is an extension of the Unified Form Language (UFL). It is a domain-specific
lanaugage for a unified declaration of discretizations of partial differential 
equations (PDEs) using the finite element methods (FEMs), generalized finite 
difference (GFD), and adaptive extended-stencil finite-element method (AES-FEM). 
The declarations use variational forms, where the test functions can be traditional 
finite-element basis functions (in the case of FEM and AES-FEM) or Dirac delta 
functions (in the case of GFD). The PDEs are expressed in both and weak forms
that closely resemble the mathematical notation.

UFL is a core component of the [FEniCS project](http://www.fenicsproject.org). 
UFL+ is a core component of UNIFEM, which stands for UNIFied Environment for 
Multiphysics problems. UNIFEM extends and reuses a number of components of the 
FEniCS Project, including UFL.


Documentation
=============

Documentation can be viewed at http://unifem-ufl-plus.readthedocs.org/.

.. image:: https://readthedocs.org/projects/ufl-plus/badge/?version=latest
    :target: http://ufl-plus.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Automated Testing
=================

We will use Travis CI to perform automated testing.

License
=======

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU Lesser General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
  GNU Lesser General Public License for more details.

  You should have received a copy of the GNU Lesser General Public License
  along with this program. If not, see <http://www.gnu.org/licenses/>.
