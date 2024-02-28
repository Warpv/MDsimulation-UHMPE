
mol new /Users/niko/Desktop/VSCode/simulation-UHMW-PE-adhesion/xyz_coor_files/sim_md_11A.xyz autobonds no waitfor all


/Users/niko/Desktop/VSCode/simulation-UHMW-PE-adhesion/xyz_coor_files/xyz_coor_files sim_md_11A.xyz

set sel [atomselect top all]
$sel set radius 0.95
$sel set name A
$sel set type A
$sel set mass 1.0



