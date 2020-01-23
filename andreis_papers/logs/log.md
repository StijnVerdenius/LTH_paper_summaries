# Andrei's log
## Log Week 1
### Papers Read & Summarised:
(in no particular order)

- The Lottery Ticket Hypothesis
- Deconstructing the Lottery Tickets: Zeros, signs and the supermask
- Stabilizing the Lottery Ticket Hypothesis
- Rethinking the value of neural network pruning
- The state of sparsity in Deep NNs
- Rethinking the value of neural network pruning
### Overview
Understood the lottery ticket hypothesis and its implications as well as some attempts to explain these results from the follow-up papers. Got a birds-eye view on the field of model compression in general, and researched into what are the current state-of-the-art methods out there. (variational dropout, L0 regularization, simple magnitude pruning). 

##Log Week 2

### Papers read & summarised:
- Drawing Early Bird Tickets
- One ticket to win them all
- Targeted dropout
- Learning Sparse Neural Networks Through L0 reg. (mostly skimmed the equations, just wanted to get general idea)
- Evaluating Lottery Tickets under Distributional Shifts
- Sparse Training from Scratch : Faster Training without Losing Performance
- Variational Dropout (Kingma, Welling) (needs revisiting)
- Variational Dropout Sparsifies Neural Networks (needs revisiting)

### Implementation
- Worked with Stijn on reproducing the lottery ticket hypothesis and running some experiments with that.

## Log Week 3

### Papers read & summarised:
- To prone or not to prune: exploring the efficacy of neural network pruning
- Deep Compression : Pruning, Trained Quantization, Huffman Coding
- Global Sparse Momentum SGD for pruning very deep NNs
- Learning both Weights and Connections for Efficient Neural Networks
- Soft weight-sharing for neural network compression (needs revisiting)
- Optimal Brain Damage
- Optimal Brain Surgeon (needs revisiting)

## Log Week 4

### Papers read & summarised:
- Pruning Filters for Efficient Convnets
- Group Sparse Regularization for deep neural networks
- Learning Structured Sparsity in Deep Neural Networks
- Rigging the Lottery : Making all tickets winners


## Log Week 5
### Papers Read & Summarised
- Deep Rewiring
- A closer look at structured pruning
- Adding Gradient Noise Improves learning for very deep networks

## Log week 6
### Papers Read & Summarised
- Xavier init.
- Kaiming init.
- Learning with random learning rates (in progress)

### Overview
## Notes on what I found
- Only the sign matters when re-initialising the weights for winning tickets
- Winning Lottery tickets can transfer across datasets as well as optimizers succesfully, implying generality. This also possibly hints at the existance of a "lottery ticket" initialization scheme.
- For Winning Lottery tickets to work on large-scale networks and/or datasets, some tricks need to be employed (learning rate warmup and rewinding to a later iteration)
- Early bird tickets (tickets drawn in the early stage of training) exist, can be easily identified and can be exploited for faster training.
- Literature is quite unclear on which pruning methods work best. Different baselines and methodologies are used across papers and results are sometimes conflicting. 
- However, it does seem that the magnitude pruning technique can reach comparable or better results as the more involved Variational Dropout or L0 regularization while being computationally less intensive. 

## Research Ideas
### Monitoring Sign-flips
In the "Zeros, signs and the supermask" paper, authors discover that the only important thing when re-initializing the network's weights are the signs. They even demonstrate that resetting to an arbitrary constant that has the same sign also works. 
As such, one potential research idea is to monitor how the signs flip during training, and, if a weight flips signs, it can be pruned, and training can continue. Potentially this can be used in conjunction with magnitude pruning to develop some sort of hybrid criterion. The hope is that this scheme will improve training speed.
This can initially be tested on a small-scale dataset and model e.g. a simple conv-net on CIFAR-10 or even a fully connected network on MNIST dataset. Implementation would be done using PyTorch, and emulating hyperparameters from the original Lottery Tikcet Hypothesis to ensure fair comparison.

### Neuron Fusion
While unstructured pruning can help save storage space, it is not quite so effective at reducing computational cost. As such, it's natural to wonder if you can convert a sparse matrix into dense form. One idea to do this is by fusing neurons. The basic idea is to first obtain a sparse network (by using any regular pruning method) and then fuse neurons together. There are quite a few degrees of freedom to this problem, which are worth exploring: (1) which criterion to use when fusing neurons? how many? (2) how should the neurons be fused together? (3) is retraining required? (4) is it dependant on network structure, sparsity levels, hyperparameters, etc?