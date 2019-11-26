## Pruning Filters for Efficient Convnets
Turns out that for big CNNs (such as VGG, AlexNet etc), even though 90% of the weights are in the fully-connected layers, they contribute less than 1% of the overall FLOPs.

### Method
The importance of a filter is measured by calculating the sum of its absolute weights \\( \sum |\mathcal{F}_{i,j}|  \\) i.e. the L1 norm. Since the num. of input channels is the same across filters, the sum of the filter weights also represents the average magnitude of its kernel weights. This value gives an expectation of the magnitude of the output feature map. Filters with small kernel weights tend to produce feature maps with weak activations as compared to the other filters in that layer. 
Procedure can be summarised as follows:

- For each filter, calculate sum of its absolute kernel weights
- Sort the filters by this sum
- Prune m filters with the smallest sum and their corresponding feature maps. The kernels in the next convolutional layer corresponding to the pruned feature maps are also removed.
- A new kernel matrix is created for both the i-th and (i+1)-th layer, and the remaining kernel weights are copied to the new model.

To prune filters across multiple layers, two strategies for layer-wise filter selection are considered:

- Independent pruning : determine which filter should be pruned at each layer independent of other layers
- Greedy pruning : take into account the filters that have been removed in the previous layer. This strategy does not consider the kernels for the previously pruned feature maps whilecalculating the sum of absolute weights.

For ResNets, filter pruning not so straightforward. Special steps must be taken (see Section 3.3 in paper).
Can drop many filters from VGG-16 with no effect on accuracy, and have a 34% FLOP reduction, with 50% of filters being pruned in layer 1 and from 8 to 13. Also works well for ResNet-110 and other big models+datasets. Also around 30% FLOP reduction. All this while using one-shot pruning and retraining.
### Caveats
Number of filters to prune for each conv. layer is determined empirically by measuring the network's sensitivity to pruning filters from each layer. Authors use the same prune percentage for layers which have same feature map size (section 3.2).