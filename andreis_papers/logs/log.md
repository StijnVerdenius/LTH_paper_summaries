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

### Overview


## Notes on what I found
- Only the sign matters when re-initialising the weights for winning tickets
- Winning Lottery tickets can transfer across datasets as well as optimizers succesfully, implying generality. This also possibly hints at the existance of a "lottery ticket" initialization scheme.
- For Winning Lottery tickets to work on large-scale networks and/or datasets, some tricks need to be employed (learning rate warmup and rewinding to a later iteration)
- Early bird tickets (tickets drawn in the early stage of training) exist, can be easily identified and can be exploited for faster training.
- Literature is quite unclear on which pruning methods work best. Different baselines and methodologies are used across papers and results are sometimes conflicting. 
- However, it does seem that the magnitude pruning technique can reach comparable or better results as the more involved Variational Dropout or L0 regularization while being computationally less intensive. 

## Research Idea
In the "Zeros, signs and the supermask" paper, authors discover that the only important thing when re-initializing the network's weights are the signs. They even demonstrate that resetting to an arbitrary constant that has the same sign also works. 
As such, one potential research idea is to monitor how the signs flip during training, and, if a weight flips signs, it can be pruned, and training can continue. This works because it is equivalent to resetting the network where all weights have the same sign. Potentially this can be used in conjunction with magnitude pruning to develop some sort of hybrid criterion. The hope is that this scheme will improve training speed.