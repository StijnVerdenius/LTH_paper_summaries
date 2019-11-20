# Learning both Weights and Connections for Efficient Neural Networks
[Link to paper](http://papers.nips.cc/paper/5784-learning-both-weights-and-connections-for-efficient-neural-network.pdf) 

*Main foundation of LTH original paper, so worth a read. They introduce the 3-step method of magnitude pruning: train-prune-finetune. they get 90% pruning percentage without drop in accuracy. Running a 1 billion parameter network, at20Hz would require 12.8W just for RAM access. They focus on getting smaller networks for mobile devices. They prune both neurons and connections*

## Related wrok

- Previous wortk mainly focusses on quatization
- or average pooling
- or weight sharing

## Method

1. Train normally with l2 regularization and dropout
2. Prune on magnitude
3. Finetune with l2 regularization, adjusting dropout ratio
*"During retraining, it is better to retain the weights from the initial training phase for the connectionsthat survived pruning than it is to re-initialize the pruned layers"*
4. Don't finetune convolutional layers
5. Redo step 2-4 a desired amount (iterative pruning)
6. After pruning connections, neurons with zero input connections or zero output connections are pruned.

## Results

- ~90% sparcity on lenet, vgg16 and alexnet without losing accuracy if right regularizations, iterative pruning and retaining weights are used, otherwise ~50-80%
- 3-6 times less flops

## Conclusion

- Regularization important
- Retraining weights important
- Iterative pruning most important
- Storage of sparse matric can be reduced greatly with some tricks (important)


## Limitations

- Regularizations are important
- Prune+finetune conv and fc layers separately

