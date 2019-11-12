# Bayesian Compression for Deep Learning
[Link to paper](http://papers.nips.cc/paper/6921-bayesian-compression-for-deep-learning.pdf)
> Predecessor of l0-regularisation
###### *Sparcity induced by priors.*
Use the variational Bayesian approximation for Bayesian inference.  Main contributions:
1.  Use hierachical priors to prune nodes instead of weights
2.  Use the posterior uncertainties to determine the optimal fixed point precision to encode the weights

**Note:** Performance boosting and compression are not always the same thing. e.g. convolutions don't have many parameters, but generate feature maps, which are the real memory footprint holders. However; *"from a Bayesian perspective network pruning and reducing bit precision for the weights is aligned"*

## Related work

Not the first bayesian approach to pruning (2011 untill 2016). Mostly fixed at weights, which is not reducing weight matrix sizes, therefore not speeding up inference. 

There have also been some papers on bayesian structured pruning before training (most in the 90s, one in 2015). 

There has been attempts at reducing per-weight storage, even untill binary precision. Maybe a bit too extreme; best is just to reduce bit-size per weight a little, shown to not lead to too much increase in error

## Derivation

#### What do 'Variational Inference' and 'Minimum Description Lenght' to do with each other?

Informtion theory tells us through **The minimum description lenght principle** that the best model is the one that minimizes complexity cost and data-misfit error under the lowest number of bits. **Variational Inference** is a form of this. 'Information Theory's **entropy** forms a part of the **ELBO**: \\(H(q(w))\\), which is in turn part of the complexity cost in IT.  ELBO itself can be seen as a minimum communication cost concerning targets for any new x, given prior and model.

- By using the right prior, the bayesian mechanism will prune weights going into a neuron, that are not needed for this communication. 
- By going bayesian, through the **Bits-back argument** a uncertain and unprecise weight representation will result in the required information under less cost.

> Look up ELBO, VI and re-parametrization if you forgot about that

#### Bayesian compression

Assume a zero-mean normal prior over **w**, where the variance \\(z^2\\) is governed by some distribution p(z). By treating the variance-parameters of the **w**-distribution  (=\\(z^2\\)) as random variables, we can recover marginal prior distributions *(which are?)*. Specifically, over the parameters that have heavier *(=longer?)* tails and more mass at zero; this subsequently biases the posterior distribution over **w** to be sparse. This family of distributions is known as scale-mixtures of normals.
 
Two priors will be considered, that are both relaxations of a discrete distribution: 
- Hyper-parameter free log uniform
- Half Caushy (horse-shoe distributions)

##### Log-uniform

TODO

##### Horse-shoe

TODO

## Results

Reduces VGG feature maps that are big, quite a bit. Most bit representations are reduced to somewhere between 32 (100%) to 5 bits.

They also compare simply weight compression and weight+bit compression and weight+bit+group compression. Getting similar to state of the art compression at the time of writing. 

They already notice that using preset initialisation works, which is later used in LTH. 

Efficiency advantages are mainly shown with group sparsity and hardly with the weight pruning. 

## Conclusion

- Bayesian compression by prior-induced pruning. 
- Speed-up noticed in group pruning
- Naturally learning bit precision

## Limitations

- Pruning rates quite standard
- Still just doing dropout? -> not sure (TODO)
- Warm-up required among more training tricks
- Lots of params -> not sure (TODO)