---
name: tensorflow-agents
description: "TF-Agents: A reliable, scalable and easy to use TensorFlow library for Contextual Bandits and"
homepage: https://github.com/tensorflow/agents
metadata:
  openclaw:
    emoji: "🧠"
    auto_generated: true
    requires:
      bins: ["git", "pip"]
---

# Tensorflow Agents

# TF-Agents: A reliable, scalable and easy to use TensorFlow library for Contextual Bandits and Reinforcement Learning.

## Installation

TF-Agents publishes nightly and stable builds. For a list of releases read the
<a href='#Releases'>Releases</a> section. The commands below cover installing
TF-Agents stable and nightly from [pypi.org](https://pypi.org) as well as from a
GitHub clone.

> :warning: If using Reverb (replay buffer), which is very common,
> TF-Agents will only work with Linux.

> Note: Python 3.11 requires pygame 2.1.3+.

## Usage

End-to-end examples training agents can be found under each agent directory.
e.g.:

- DQN:
  [`tf_agents/agents/dqn/examples/v2/train_eval.py`](https://github.com/tensorflow/agents/tree/master/tf_agents/agents/dqn/examples/v2/train_eval.py)

<a id='Installation'></a>
