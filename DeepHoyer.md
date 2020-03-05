## DeepHoyer: learning sparse neural nets with differentiable scale-invariant sparsity measures

Link: https://openreview.net/attachment?id=rylBK34FDS&name=original_pdf

Hoyer regularizer is the ratio between L1 and L2 norms of the weight. It approximates the L0 regularizer, while being differentiable. Also, unlike L1, it does not equally penalize all weights (it is scale invariant). For the Hoyer regularizer, weights which are lower than the value of the regularizer will be pushed to 0, while those higher will be pushed away from 0 (automatically induced trimming effect). Since it's differentiable you can straight up optimize it with SGD. 
Also, unlike L1 which has a single minimum at the origin, Hoyer has minima along the axes, the structure of which resembles L0. The gradients of Hoyer are purely radial, i.e. they will lead to "rotations" towards the nearest axis. While it is non-convex, it is shown to not hurt performance.

Can be used for structural or element-wise pruning. 

Experimental results seem good. They claim SOTA for LeNet300 and LeNet5 MNIST.

Easy to implement, code available at: https://github.com/yanghr/DeepHoyer