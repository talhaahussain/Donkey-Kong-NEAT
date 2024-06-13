# Donkey-Kong-NEAT
A Python program to play the first or second level of Donkey Kong Country (SNES, 1996), Jungle Hijinks or Ropey Rampage, using the genetic algorithm NEAT (NeuroEvolution of Augmenting Topologies) and Gymnasium, a maintained fork of OpenAI's Gym. 

### Prerequisites

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
pip install -r requirements.txt
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
