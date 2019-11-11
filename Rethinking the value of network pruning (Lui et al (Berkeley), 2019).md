# Rethinking the value of network pruning
[Link to paper](https://arxiv.org/pdf/1810.05270.pdf)

Make several surprising observations which contradict common beliefs.
On top of that, they have a strong background section with papers you should read!

##### Assumptions made by pruning algorithms:

- Starting with training a large, over-parameterized network is important
- Both the pruned architecture and its associated weights are believed to be essential for obtaining the final efficient model (thus many choose fine-tuning).
- We need to train first before pruning

## Claims:

- What matters is the obtained architecture, instead of the preserved weights, despite training the large model is required to find that target architecture. 
- Over-parameterization during the first-stage training is not as beneficial as previously thought.
- Inheriting weights from a large model is not necessarily optimal, and might trap the pruned model into a bad local minimum, even if the weights are considered “important” by the pruning criterion.

*The contradiction between our results and those reported in the literature might be explained by less carefully chosen hyper-parameters, data augmentation schemes and unfair computation budget for evaluating this baseline approach.*

## Methods

- Consider 3 structured pruning menthods and 3 unstructured (LTH not included).
- Use the floating point operations (FLOPs) as a *fair* training budget
- Only evaluates convolutional networks

## Results

### Performance experiments

- For pruning methods with predefined target architectures, training the small models for the same number of epochs as the large model, is often enough to achieve the same accuracy as models output by the three-stage pipeline. Combined with the fact that the target architecture is predefined, in practice one would prefer to train the small model from scratch directly. Moreover, when provided with the same amount of computation budget, can even lead to better performance.
- Unstructured pruning results are similar in all settings. The inherited weights in the pruned architecture are not better than random

### Architecture search

Best contribution of pruning algorithms is architecture search according to authors

- Network slimming is more efficient than uniform-pruning in structured pruning
- For non-structured weight pruning

They attempt at learning better design principals from pruning results (*“Guided Pruning & Guided Sparsifying”*): 

- Performs the same as pruned networks
- Gets to decent performance quicker than other arch-search methods (RL & EC). However, search space limited to subspace on subnetworks.



## Conclusion

- Pruning algorithms make big assumptions/claims and do not train valid baselines
- Main contribution is architecture search, at wwhich it is very efficient
- Under conditions, you can train these architectures from scratch
- Over-parameterization is your enemy



## With respect to LTH: 

Authors note that they could not reproduce the results of the original LTH. However, they use larger learning rates, structured pruning, and evaluate on large networks with large datasets (VGG, ImageNet)

In the case of unstructured pruning on CIFAR, the difference in learning rate explains the contradictory behavior. For structured pruning, regardless of learning rate, the winning ticket does not outperform random initialization.

> **This paper was, however, also written before the 'Stabilizing The Lottery Ticket'-paper**
