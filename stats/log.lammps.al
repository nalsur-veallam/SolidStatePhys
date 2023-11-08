LAMMPS (29 Sep 2021 - Update 2)
atom_style atomic
units metal
variable n equal 5
lattice fcc 4.04
Lattice spacing in x,y,z = 4.0400000 4.0400000 4.0400000
region box block 0 $n 0 $n 0 $n units lattice
region box block 0 5 0 $n 0 $n units lattice
region box block 0 5 0 5 0 $n units lattice
region box block 0 5 0 5 0 5 units lattice
create_box 1 box
Created orthogonal box = (0.0000000 0.0000000 0.0000000) to (20.200000 20.200000 20.200000)
  1 by 1 by 1 MPI processor grid
create_atoms 1 region box
Created 500 atoms
  using lattice units in orthogonal box = (0.0000000 0.0000000 0.0000000) to (20.200000 20.200000 20.200000)
  create_atoms CPU = 0.000 seconds
pair_style eam/fs
pair_coeff * * ./Al_mm.eam.fs Al
neighbor 0.3 bin
region slice block 1.95 2.05 0 $n 0 $n units lattice
region slice block 1.95 2.05 0 5 0 $n units lattice
region slice block 1.95 2.05 0 5 0 5 units lattice
group slice region slice
50 atoms in group slice
displace_atoms slice move 0.05 0.0 0.0 units box
Displacing atoms ...
dump d1 all custom 1 dump id type xs ys zs fx fy fz
run 1
WARNING: No fixes defined, atoms won't move (../verlet.cpp:55)
Neighbor list info ...
  update every 1 steps, delay 10 steps, check yes
  max neighbors/atom: 2000, page size: 100000
  master list distance cutoff = 6.8
  ghost atom cutoff = 6.8
  binsize = 3.4, bins = 6 6 6
  1 neighbor lists, perpetual/occasional/extra = 1 0 0
  (1) pair eam/fs, perpetual
      attributes: half, newton on
      pair build: half/bin/atomonly/newton
      stencil: half/bin/3d
      bin: standard
Per MPI rank memory allocation (min/avg/max) = 4.674 | 4.674 | 4.674 Mbytes
Step Temp E_pair E_mol TotEng Press 
       0            0   -1705.0332            0   -1705.0332     3307.906 
       1            0   -1705.0332            0   -1705.0332     3307.906 
Loop time of 0.00203649 on 1 procs for 1 steps with 500 atoms

Performance: 42.426 ns/day, 0.566 hours/ns, 491.042 timesteps/s
98.6% CPU use with 1 MPI tasks x no OpenMP threads

MPI task timing breakdown:
Section |  min time  |  avg time  |  max time  |%varavg| %total
---------------------------------------------------------------
Pair    | 0.0010929  | 0.0010929  | 0.0010929  |   0.0 | 53.66
Neigh   | 0          | 0          | 0          |   0.0 |  0.00
Comm    | 1.138e-05  | 1.138e-05  | 1.138e-05  |   0.0 |  0.56
Output  | 0.00092723 | 0.00092723 | 0.00092723 |   0.0 | 45.53
Modify  | 4.2e-07    | 4.2e-07    | 4.2e-07    |   0.0 |  0.02
Other   |            | 4.588e-06  |            |       |  0.23

Nlocal:        500.000 ave         500 max         500 min
Histogram: 1 0 0 0 0 0 0 0 0 0
Nghost:        1956.00 ave        1956 max        1956 min
Histogram: 1 0 0 0 0 0 0 0 0 0
Neighs:        19500.0 ave       19500 max       19500 min
Histogram: 1 0 0 0 0 0 0 0 0 0

Total # of neighbors = 19500
Ave neighs/atom = 39.000000
Neighbor list builds = 0
Dangerous builds = 0
Total wall time: 0:00:00
