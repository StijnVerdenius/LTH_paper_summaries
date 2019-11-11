# The State of Sparsity in Deep Neural Netoworks

### Contributions:
- Authors perform a comprehensive evaluation of variational dropout, L0 regularization and magnitude pruning on large-scale networks. They show that L0 and VD perform incosistently for such large-scale networks, and magnitude pruning can attain comparable results
- They achieve SOTA sparsity-accuracy trade-off for RESNET50 by only using magnitude pruning
- They repeat the lottery ticket (Frankle & Carbin, 2018) and scratch (Liu et al., 2018) experiments on Transformer and ResNet-50 across a full range of sparsity levels, showing that unstructured sparse architectures learned through pruning cannot be trained from scratch to the same test set performance as a model trained with pruning as part of the optimization process.

### Comparing the 3 methods
- When applied to the Transformer, at high levels of sparsity, magnitude pruning outperforms both L0 and variational dropout. It is also much faster to train (1.24 and 1.65x respectively)
- L0 cannot produce sparse ResNet50 models without signifcant damage to quality.
- Results of VD and L0 across large networks are inconsistent (for ResNet50, VD produces models as good as or better than magnitude pruning, while L0 cannot produe sparse models at all, while for Transformer the l0-regularization performs best, on par or better than magnitude pruning)
- VD and L0 much more costly to train in terms of memory and compute
- VD on ResNet50 much more costly to train in terms of memory and compute
- MP on ResNet50 with hand-crafted pruning was, at the time, SOTA in terms of sparsity-accuracy tradeoff.

### Per-layer Distributions
- For L0 and VD, per-layer pruning distribution is learned, while authors use a uniform distribution for MP. 
- Pruning methods that are integrated into the otpimization process (L0, VD) do not sparsify the input and output layers as much (they are known to disproportionately influence the performance of the network)
- Using a hand-crafted distribution and more training time (although training time probably not as important), MP performs even better, outperforming both VD and L0 at all but the absolute highest sparsity levels tested while also using less resources (VD's performance at the highest sparsity levels still notable)
- It is likely that performance is tied to precise allocation of weights across layers, thus VD performs better on high sparsity levels on Resnet due to it learning this distribution -> This result indicates that efficient sparsification techniques that are able to learn the distribution of sparsity across layers are a promising direction for future work


### Pruning as architecture search
- Authors provide strong counterexamples to two recently proposed theories that models learned through pruning techniques can be trained from scratch to the same testset performance of a model learned with sparsification aspart of the optimization process.(???)
- Authors were not able to reproduce the results of the original LTH paper. However, they experimented with large datasets and models. This was before the stability paper got out which fixed that

## REVIEW LATER:
"Model trained" with sparsity as part of the optimization process" -> Not entirely sure what that means atm. Does it refer to VD and L0? How does that tie into their experiments?
