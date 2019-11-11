# Learning Sparse Neural Networks Through L0 Regularization
[Link to paper](https://arxiv.org/pdf/1712.01312.pdf)

A practical method for L0-norm regularization for neural networks. 
AIC and BIC, well-known model selection criteria, are special cases of L0-regularization.

**Problem:** L-0 is non differentiable
**Solution:** Inclusion of a collection of non-negative stochastic gates, which collectively determine which weights to set to zero. i.e. Smoothing the binary l0-norm with continous distributions to maintain differentiability but also maintain its behaviour. For this purpose they employ a hard-sigmoid and the hard-concrete

### Hard-concrete:

It is obtained by “stretching” a binary concrete random variable (*see sources in paper, end of intro*) and then passing its samples through a hard-sigmoid.

# *To be continued*