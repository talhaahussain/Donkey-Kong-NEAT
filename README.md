# Donkey-Kong-NEAT
A Python program to play the first or second level of Donkey Kong Country (SNES, 1996), Jungle Hijinks or Ropey Rampage, using the genetic algorithm NEAT (NeuroEvolution of Augmenting Topologies) and Gymnasium, a maintained fork of OpenAI's Gym. 

### Prerequisites

Requires a valid ROM file (`.sfc`) of Donkey Kong Country, USA version, Rev 2 (SHA-1 sum: cd606e77ab2034438e06891cd2d067dad69b4d1a). 

**Please check that you have this specific ROM version, as other versions of Donkey Kong may not work.**

pyenv must be installed, as well as Python version 3.8 (through pyenv). Details for how this may be done can be seen [here](https://github.com/pyenv/pyenv).

Prerequisites are viewable in `requirements.txt`.

### Installation

Clone with:

```shell
git clone https://github.com/talhaahussain/Donkey-Kong-NEAT.git dkc-neat
cd dkc-neat/
```

Install prerequisites with:

```shell
bash install.sh
```

### Configuration

The NEAT algorithm can be configured using `config_feedforward.txt`. More information on how to do this can be seen [here](https://neat-python.readthedocs.io/en/latest/index.html), at NEAT-Python’s documentation.

### Usage

Run with:

```shell
python dkc-retro.py
```

### See also

[Flappy-Bird-NEAT](https://github.com/talhaahussain/Flappy-Bird-NEAT)

### Footnote

This project does not infringe on any intellectual property. Always obtain ROMs from an authentic and legal source - piracy is a crime.
