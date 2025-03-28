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
In `instrumentation_pass`, run `make` to get the instrumentation pass. It will contain passes for 3 different architechture - arm64, arm32 and x86-64. We have used 2 different testbeds, fischertechnik is `arm32`, and miniwater testbed is `arm64`, so, we have used those respectively. In your case, you might not have the testbed available, so, we have provided the LOGS for you.

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
All the logs/traces are present in the Data folder. Using some of those logs, we have created the graphs. I have used `graphviz` to generate those graphs. But `graphviz` can't generate graphs containing more than 6000 nodes. I have divided the whole graph in sub-graphs. Each sub-graphs contains 5k nodes. 
The `hbw-graph` folder has graphs from `hbw` and `vgr-graph` contains all sub-graphs of `vgr`. The `backtracking_graphs` folder contains combined sub-graphs of those two.


#### Graph Generation
The 
