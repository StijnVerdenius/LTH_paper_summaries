## A closer look at structured pruning for neural network compression
### Summary
Authors show that:

- Reduced networks, smaller versions of the original network trained from scratch, consistently outperform pruned networks
- If one takes the architecture of a pruned network and then trains it from scratch it is significantly more competitive.
- These architectures are easy to approximate: we can prune once and obtain a family of new, scalable network atchitectures that can simply be trained from scratch
- Compare inference speed of reduced and pruned networks on hardware, and show that reduced networks are significantly faster

### Methods
Authors use L1-based norm pruning and Fisher pruning.