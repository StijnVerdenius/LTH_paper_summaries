## Super-Convergence : Very fast training of NNs using large learning rates

A primary insight is that large learning rates regularize the trainig, hence requiring a reduction of all other forms of regularization to preserve an optimal regularization balance. 

### Super-Convergence
In this work, authors use **CLR** (see Smith paper on CLR). For CLR, one needs to specify a minimum and maximum lr and a stepsize. The stepsize is the number of iterations used for each step, and a cycle consists of two such steps - one in which the lr increases, and one in which the lr decreases. The simplest method (linear change of lr) works fine. 

To determine if super-convergence is possible for an architecture, the **LR range test **can be used. In LR range test, training starts with zero or very small lr which is slowly increased linearly throughout a pre-training run. This provides information on how well the network can be trained over a range of learning rates. Example curve:
![](/home/andrei/Desktop/LTH_paper_summaries/figs/superconvergence/lr_range_test.png) 

With a small lr, the network begins to converge, and, as it increases, the performance will at some point start to decrease. The lr at this peak is chosen as the upper bound. The lower bound can be chosen as the value of the peak divided by a factor of 3 or 4. The optimal lr for a typical (piecewiese constant) training regime usually falls between these minimum and maximum values.

The curves for Resnet-56 for Cifar10 can be seen in Fig 2b. The train acc remains consistently high, even though learning rates up to 3.0 were used. This result prompted the study of the superconvergence phenomenon. **Authors believe this behavior is indicative for potential for superconvergence.**

Authors suggest a slight modificatoin to the original CLR method, namely the use of only one cycle, which is always smaller than the total number of iteration/epochs and allow the lr to decrease several orders of magnitude less than the initial lr for the remaining iterations. 

### Estimating optimal learning rates
Authors use Hessian-free optimization to estimate the optimal learning rates, for demonstrative purposes.