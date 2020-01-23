# Handling Sparsity via the Horseshoe 

*Instead of L0 or L1 or L2 regularisation introduces a horse-shoe prior over weights. Which is very long tailed, penalizing not-being-zero more than L1 whilst easy to implement unlike L0* 

## derivation

> skipped the derivation for now

## conclusion

- The horseshoe prior is basedon a novel multivariate-normal scale mixture; it yieldsestimates  that  are  robust  both  to  unknown  sparsitypatterns  and  to  large  outlying  signals,  making  it  anattractive default option.
- Show in practice that it works
- Related to Bayesian model averaging
