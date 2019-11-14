# Variational Dropout and the Local Reparametrization Trick
[Link to paper](https://arxiv.org/pdf/1506.02557.pdf) 

*Proposes Variational Dropout in a reparametrisable way. This is a dropout with per-parameter, learnable dropout rate*

So first there was binary dropout, then came Gaussian dropout which was its approximation with a faster convergence and lower bound properties to the marginal likelihood *(p(x)?)*. Now we get **Variational dropout**

> ***I skipped section 2***

## Related work

Names weight uncertainty paper as a, though successfull and unbiased, high variance estimator for VI.

## Derivation

#### The Idea
Dropout is defined as a multiplication of noise (E) with input-features of a layer (A), before being matrix-multiplied with weights, to produce output (B). 

1. In standard dropout, this noise is binary (bernoulli with global dropout rate *p*), thus forming a mask.
2. In Gaussian dropoiut we use a gaussian distribution for this noise. 
3. Now, we make dropout rates adaptive

#### From Basic Dropout to Gaussian Dropout (3.1)

In *'Gaussian Dropout'* we can say that because the noise matrix is sampled from gaussian, so is outcome (B).  We can therefore analytically formulate the distribution over B and directly sample from it, resulting in speedup. However, this ignored dependencies between B's elements.

#### Towards Correlation (3.2)

Now, we day we won't ignore the dependencies, redefining E as correlated weight noise. We can define new weight matrices such that, for each row *m* in B:


$$B= AW \rightarrow b^m = a^m W  $$ 

Where each column *i*  of W is defined as a multiplication of sampled scalar noise variable \\(s_i\\) with a model-parameter:

$$w_i = s_i \theta_i $$$$s_i \sim q(s_i)$$$$ q(s_i)=N(1, \alpha)$$

- So B rows have correlation now because they are scaled with the same scale parameter s.
- Still one \\(\alpha\\) (=dropout rate) for entire network that is kept constant throughout training.


#### Towards Variational Dropout
 
Now, we will make \\(\alpha\\) trainable by optimizing a new objective (see formula 12 in paper), that is not relevant to the implementation. This wasn't possible before the bayesian interpretation because it ignored variance. 

We can choose to either do a global alpha, per-row, or even per-parameter. However, the alphas should be constrained to be between 0 and 1. 



 > ***I skipped the rest*** 
 
 [Check this video](https://www.youtube.com/watch?v=GIpk4F9VL1U) 
 
## Conclusion

 - Per weight trainable dropout rates possible for both Bernoulli and Gaussian distributions
 - Former dropouts are a special case of this
