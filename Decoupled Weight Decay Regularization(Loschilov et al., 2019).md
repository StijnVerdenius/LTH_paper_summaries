## Decoupled weight decay regularization

L2 and weight decay are equivalent for SGD (when re-scaled for the learning rate). However, for adaptive gradient algorithms such as Adam this does not hold true. The modification proposed in this paper recovers the original formulation of wdecay regularization by decoupling the wdecay from the optimization steps taken w.r.t. the loss function. They also investigate whether it's better to use weight decay or L2 regularization for training deep NNs. A major factor of poor generalization of Adam is due to L2 being not nearly as effective as weight decay (in the wrong formulation).


### Decoupling Weight Decay from the gradient-based update
Weight decay is described as
\\(\theta_{t+1} = (1-\lambda)\theta_t - \alpha \nabla f_t(\theta_t) \\)
with \\(\lambda\\) the rate of wdecay per step and \\(\nabla f_t\(\theta_t)\\) is the t-th batch gradient to be multiplied by a learning rate \\(\alpha\\). For standard SGD, it is equivalent to standard \\(L_2\\) regularization. 

**Proposition 1: Weight decay = L2 reg for standard SGD**
**Proposition 2: Weight decay is NOT L2 reg for adaptive gradient algorithms.**

Having shown that L2 reg and wdecay are not equivalent for adaptive gradient algorithms, this raises the question of how they differ and how to interpret their effects. Their equivalence for SGD is clear: both mechanisms push weights closer to zero, at the same rate. For adaptive gradient algorithms they differ:

- For L2 reg the sums of the gradient of the loss and the gradient of the regularizer (i.e. L2 norm of the weights) are adapted
- With decoupled weight decay, only the gradients of the loss function are adapted (with the weight decay step being separated from the adaptive gradient mechanism)

With L2 regularization both types of gradients are normalized by their typical (summed) magnitudes, and therefore the weights x with large typical gradient magnitude s are regularized by a small relative amount than other weights. In contrast, decoupled weight decay regularizes all weights with the same rate, \\(\lambda\\)., effectively regularizing weights x with large s more than standard L2 regularization does. 

### Proposition 3: Weight decay = scale-adjusted L2 reg for adaptive gradient algorithm with fixed preconditioner 
Proof in paper. I will not add it here.

Weight decay is preferred over L2 regularization when viewed through the lens of Bayesian filtering. (theory in this in the paper)


### Experimental Validation
They compare two optimizers: Adam with L2, and Adam with decoupled weight decay (AdamW), using three different learning rate schedules: a fixed learning rate, a drop-step schedule, and a cosine annealing schedule. As Adam already adapts the lr, it is not so common to use a lr schedule with it as it is with other methods, however their results show that it substantially improves the performance of Adam. 
Authors also enhance AdamW with warm restarts (proposed in some of their other work, cited in this paper), creating AdamWR.

### Conclusion
Following suggestions that adaptive gradient methods such as Adam might lead to worse generalization than SGD with momentum, the authors have identified and exposed the inequivalence of L2 and wdecay for Adam. They show that their modified version of Adam with decoupled weight decay yields substantially better generalization performance than the common implementation of Adam with L2. They also propose to use warm restarts for Adam.