# Rethinking the value of network pruning
[Link to paper](https://arxiv.org/pdf/1810.05270.pdf)

make several surprising observations which contradict common beliefs.

##### Assumptions made by pruning algorithms:

- Starting with training a large, over-parameterized network is important
- Both the pruned architecture and its associated weights are believed to be essential for obtaining the final efficient model (thus many choose fine-tuning).
- We need to train first before pruning

##### Claims:

- What matters is the obtained architecture, instead of the preserved weights, despite training the large model is required to find that target architecture. 
- Over-parameterization during the first-stage training is not as beneficial as previously thought.
- Inheriting weights from a large model is not necessarily optimal, and might trap the pruned model into a bad local minimum, even if the weights are considered “important” by the pruning criterion.

*The contradiction between our results and those reported in the literature might be explained by less carefully chosen hyper-parameters, data augmentation schemes and unfair computation budget for evaluating this baseline approach.*




##### with respect to LTH: 

Authors note that they could not reproduce the results of the original LTH. However, they use larger learning rates, structured pruning, and evaluate on large networks with large datasets (VGG, ImageNet)

In the case of unstructured pruning on CIFAR, the difference in learning rate explains the contradictory behavior. For structured pruning, regardless of learning rate, the winning ticket does not outperform random initialization.

> **this was, however, also before the Stabilizing the lottery ticket paper**
