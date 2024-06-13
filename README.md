# MDsimulation-UHMPE
simulation UHMW PE adhesion after argon processing

![alt text]()

# Setup

To start simulation you need to have installed (Lammps)[https://github.com/lammps/lammps]

For more information about lammps see (here)[https://lammps.sandia.gov/doc/Howto_run.html]

For better understanding and convenience you can use (Atomify)[https://github.com/ovilab/atomify], but you should take into account that Atomify uses LAMMPS version 2017


# Run Lammps simulation

To run Lammps simulation:

1. clone repo
```
git clone https://github.com/Warpv/MDsimulation-UHMPE.git

```

2. go to repo folder

```bash
cd PATH_TO_REPO/MDsimulation-UHMPE
```
3. run lammps script

```bash
lmp_serial -in in.file
```

For more information about running LAMMPS see (here)[https://guriang.unpad.ac.id/lammpsdoc/Run_basics.html]

## Atomify

If you chose to use Atomify, then simply open main in.file is [in.main_4step_cycle](https://github.com/Warpv/simulation-UHMW-PE-adhesion/blob/main/lammps/src/in.main_4step_cycle) in Atomify to run the simulation and change YOUR_PATH_TO/MDsimulation-UHMPE in [in.main_4step_cycle](https://github.com/Warpv/simulation-UHMW-PE-adhesion/blob/main/lammps/src/in.main_4step_cycle)

# Save Simulation

main in.file is [in.main_4step_cycle](https://github.com/Warpv/simulation-UHMW-PE-adhesion/blob/main/lammps/src/in.main_4step_cycle)

By deafault all data saves in "restart" and "filnal_save" folders

# At the end

Start struct is looking lake theat:

![alt text](https://github.com/Warpv/MDsimulation-UHMPE/blob/main/images/start_struct/start_struct_1.png)

![alt text](https://github.com/Warpv/simulation-UHMW-PE-adhesion/blob/main/images/start_struct/start_struct_1.1.png)
## GPU is recommended to reduce the time cost


You'll end up with something like this:

![alt text](https://github.com/Warpv/MDsimulation-UHMPE/blob/main/images/after_minimisation/after_script_1.png)
![alt text](https://github.com/Warpv/MDsimulation-UHMPE/blob/main/images/after_minimisation/after_script_3_top.png)
