# Second order derivatives for network pruning: Optimal Brain Surgeon
[Link to paper](http://papers.nips.cc/paper/647-second-order-derivatives-for-network-pruning-optimal-brain-surgeon.pdf)

## Claim:

Our method, Optimal Brain Surgeon (OBS), is Significantly better than magnitude-based methods and Optimal Brain Damage.
OBS permits the pruning of more weights than other methods (for the same error on the training set), and thus yields better generalization on test data. 

#### What's different than OBD?

Make less assumptions about the hessian. OBD assumes that the Hessian matrix is diagonal: in fact. however, Hessians for every problem we have considered are strongly non-diagonal. OBS makes no assumptions about the form of the network's Hessian. Moreover, unlike other methods, OBS does not demand (typically slow) retraining after the pruning of a weight.

## Method

Starts the same as OBD with defining taylor expansion, but then they add a lagrangian constraint on certain weights to go to zero.


1. Compute Inv(H)
2. Find the q that gives the smallest saliency with the diagonal If this candidate error increase is much smaller than E, then the weight should be deleted, and we proceed to step 3; otherwise go to step 4. 
3. Use the q from step 2 to update all weights (Eq. 5). Go to step 2. 
4. No more weights can be deleted without large increase in E. (At this point it may be desirable to retrain the network.)

**They actually calculate the inverse of the hessian, which is very slow**

> How? Since inverting a matrix of thousands or millions of terms seems computationally intractable. 

First:
- Equations 12 and 14 show that H is the sample covariance matrix associated with the gradient variable X.
- Equation 12 also shows that for the single output case we can calculate the full Hessian by sequentially adding in successive "component" Hessians.

Then for the inverse:
- This inverse can be calculated using a standard matrix inversion fonnula
- Equation 17 permits the calculation of Inv(H) using a single sequential pass through the training data

> Some proofs are given for avoidance of singularities in the matrix and the possibility for backprop in these networks.

## Results

- Show okay results.
- However, Mainly tested on small problems
- A plus for the simple approach: they demonstrate for weight based pruning that it chooses the wrong weight. *(not sure about their reasoning tbh..)*
	- Question is if their conclusion that this is very fatal for big networks is true because they are actually better at overcoming this.
	- Magnitude based actually did better than OBD in this setting

## Conclusion

- Weight based methods are inferior
- OBD makes a too big assumption
- Rather than pruning a weight (parameter) by setting it to zero, one can instead reduce a degree of freedom by projecting onto an arbitrary plane (**idea worth researching**)
- Fisher matrix could be used instead of Hessian..