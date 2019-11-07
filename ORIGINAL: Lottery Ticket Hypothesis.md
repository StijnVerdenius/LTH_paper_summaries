# Lottery Ticket Hypothesis:

A randomly-initialized, dense neural network contains a subnet-work that is initialized such that—when trained in isolation—it can match the test accuracy of the original network after training for at most the same number of iterations.

## Properties


- Commensurate Training time: j >= j’
- Commensurate Accuracy: a <= a’
- Fewer Parameters: norm(params) >= norm(params’)
- One shot approach vs. iterative : (fig 4c) one-shot pruning less costly to use, however is not as effective at higher sparsity levels as iterative pruning
- Global pruning must be used for bigger networks, otherwise smaller layers become bottlenecks
- Warmup also required for big networks (i.e. VGG-19) and a lower than normal lr (0.01)

## Conditions:


- No re-initialisation of weights
- Structure alone is not enough -> initialization matters

## Pruning

- Magnitude based

## Limitations:

- large networks
- Unstructured pruning does not necessarily yield networks that executes more quickly with hardware
- Core pruning technique is still unstructured, magnitude pruning
- Still train a network one or more times to identify a subnetwork
- It is possible that there are equally-capable subnetworks present at initialization, but IMP is unable to find them.
