# OICSR: Out-In-Channel Sparsity Regularization for Compact Deep Neural Networks

[link](https://arxiv.org/pdf/1905.11664v5.pdf) 

*Paper about using both input-weights-row as output-weights-column as 1 single group. Old methods  apply  structured  sparsity  regularization  on  eachlayer separately where the correlations between consecu-tive  layers are omitted. OICSR measures channel importance basedon statistics computed from two consecutive layers, not individually. Then prunes greedily. *

> **quote**: 
> "regularization-based channel pruning [24, 34] is a pop-ular direction of structured sparsity pruning.  These worksintroduce structured sparsity regularization (structured reg-ularization) into optimization objective of model training.Training with structured regularization transfers importantfeatures into a small quantity of channels and automaticallyobtains  structure-sparse  model.    Pruning  structure-sparsemodels  keeps  more  features/accuracy  compared  with  di-rectly pruning non-sparse models. For channel-levelpruning,  existing  regularization-based  works  apply  struc-tured regularization on each layer separately, and only en-force channel-level sparsity in out-channels. "

Pruning one out-channel in current layer results in  a  dummy  zero  output  feature  map  that  in  turn  prunes a  corresponding  in-channel  in  next  layer  together


## Method

- define groups based on out-in-channels.
- use these concatenated groups as groups to get statistics from.
- as well as to apply regularisation on said groups as units.
- prune after training based on energy
- also transfer some features of pruned channels to remaining channels
- do iterativly untill desired flops is reached
- limit each layer to maximum 50% pruning
- fine-tune

not very clear how the transfer of features is done

## results

best in the world, of course

- little accuracy drop
- faster convergence speed

