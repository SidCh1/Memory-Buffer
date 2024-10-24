# How to Distribute Quantum Memory Cells in Repeaters?

This repository contains a Monte Calro algorithm to simulate waiting time of repeater chains with multiple memory cells at the repeater stations. We aim to compare different memory cell distributions. 
The simulation was used in the paper [How to Distribute Quantum Memory Cells in Repeaters?, by
Lina Vandré, ..., arXiv: 2412.... (2024)](https://arxiv.org/abs/2412...).


## Getting started

### Prerequisites
This software was written for `Python 3`. The following packages are required:
```
numpy, statistics, matplotlib, csv, math

```

### Installation
Clone the repository, following the [instruction provided by GitLab](https://docs.gitlab.com/ee/user/project/repository/). Or download it using the corresponding menu button.


### Usage

To obtain waiting times for certain repeater chains, one has to call the function `get_statistics()` from the files `memory_buffer_doubling.py` or `memory_buffer_doubling_coherence_time.py`. They can be run with the command `python memory_buffer_doubling.py` or `python memory_buffer_doubling_coherence_time.py`, respectively. This scripts output an everage waiting time and the standard derivation on the mean value. The simulation parameters can be changed in the file.

The figures in the paper mentioned above were obtained by repeatavly calling the function `get_statistics()` and writing the outputs into a data file. 
The code is provided in the directory `Examples`. They need to get executed in the same directory as `memory_buffer_doubling.py`. 



## Files overview
- `memory_buffer_doubling.py` contains functions to obtain waiting times through simulation of a repeater chain with a given memory cell distribution. The memory cells are assumed to be perfect.
- `python memory_buffer_doubling_coherence_time.py` contains functions to obtain waiting times through simulation of a repeater chain with a given memory cell distribution. The memory cells are assumed to store quantum states for a given amount of time steps.

In `Examples`:
- ...








