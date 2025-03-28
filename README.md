# ICSTracker
ICSTracker - desc

## Environment and Dependencies
### Environment
 - ubuntu >= 18.04
 - LLVM >= 14
 - python >= 3.9

### Dependencies
 - Clang >= 14
 - graphviz 

### Usage
#### Download ICSTracker
```
git@github.com:mdrahmed/icstracker.git
export ICSTRACKER=/path_to_icstracker
```

#### Install Dependencies
```
chmod +x install_reqs.sh
./install_reqs.sh
```

#### Instrumentation Pass
```
cd instrumentation_pass
make # will contain passes for 3 different archs - arm32, arm64 and x86-64
```
 Fischertechnik is `arm32`, and miniwater testbed is `arm64`, so, we cross-compiled accordingly. In your case, you might not have the testbed available, so, we have provided the LOGS for you.

##### Fischertechnik-testbed source code compilation
##### Txt Tool Chain
Download and extract the TXT Tool Chain for [Linux](https://github.com/fischertechnik/txt_training_factory/releases/download/v0.7.0/gcc-linaro-7.2.1-2017.11-x86_64_arm-linux-gnueabihf.tar.xz)

##### Using Make and Makefile
```
cd ICSTRACKER/txt_training_factory/
export PASS=/path_to_instrumentation_pass
export TOOLCHAIN_BIN_PATH=/path_to_txt_toolchain_bin
make clean
make
```

For cross-compilation, I have used `--target=arm-linux-gnueabihf` for `arm32` bit. All the other necessary libraies and flags are defined in the Makefile. 

#### LOGS
```
cd Data # contains logs/traces
cd Graphs # contains complex graphs
ls Graphs/hbw-graph # graphs from hbw 
ls Graphs/vgr-graph # sub-graphs of vgr. 
ls Graphs/backtracking_graphs #contains combined sub-graphs of those two.
```
`graphviz` can't generate graphs containing more than 6000 nodes. So,I have divided the whole graph into sub-graphs. 
Each sub-graphs contains 5k nodes. 


#### Graph Generation
Please follow the instructions present in `3-steps/step_1_2/` and `3-steps/step_3` for noise reduction.
The `graph_generation/generate_graph.py` will use updated traces from `3-steps/step_3/output/<updated trace>` after the reduction step.  

