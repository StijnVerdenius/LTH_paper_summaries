# LOG

## Exploration

### Monday 04-11-2019


- Hooked up screens
- Install and contracts
- Considered combining lottery ticket hypothesis with Bayesian networks
- Found a supervisor
- accessed das4 account and surfsara. Can only do das4 from desktop because of vpn issues. surfsara is probably part of DL4NLP
- chose a few paper to explore (see commented out):

Some questions

- What are the algorithmic competitors of lottery ticket hypothesis?
- Can pruning be directly integrated into training?

### Tuesday 05-11-2019

LTH consists of:
    - Commensurate Training time: j >= j’
    - Commensurate Accuracy: a <= a’
    - Fewer Parameters: norm(params) >= norm(params’)
Some questions: 

  - What are the algorithmic competitors of lottery ticket hypothesis?
  - Can pruning be directly integrated into training?
  - What is the contribution of LTH in comparison to the two papers from the heading in this document: ‘Training a pruned model from scratch performs worse‘.
  - Figure 1 in the main paper; why is early stopping criterium met earlier in unpruned networks? Overfitting?

Some research ideas:

- Study the winning tickets for particular tasks and design new architectures from that given trends in tickets.
- LTH trains until timestep j and then prunes. However, how do we determine time-step j? Perhaps, in a Bayesian Neural Network, we can indicate by uncertainty which weights are to be pruned and thereby prune every timestep <- Stijn
http://mlg.eng.cam.ac.uk/yarin/blog_3d801aa532c1ce.html
http://proceedings.mlr.press/v37/blundell15.pdf
https://medium.com/@SeoJaeDuk/archived-post-weight-uncertainty-in-neural-networks-4305f2316c68
https://joshfeldman.net/ml/2018/12/17/WeightUncertainty.html
https://joshfeldman.net/ml/2018/12/17/WeightUncertainty.html
- Pruning nodes instead of weights + trying out different pruning mechanisms <- Andrei
- Can LTH be used for generating embeddings
- Can LTH be used for disentangling latent spaces of generative models. Or will it actually hurt it?
- When does a ticket generalise well?
- Can we synthesize a dataset with specific features such that when we take them out we can predict the success of a network. Thereby finding which kinda networks work well for what kind of datasets. Or look for a fixed architecture what structures stay intact over a range of datasets for a single task
- Study whether the LT conjecture holds true: does SGD actually select subnetworks that have the potential to perform well? 
- Describe the subnetwork-space mathematically
- Find the relation between dropout and LTH
- Find the relation between Residual connections and LTH
- Are weights that remain unbtouhed changing much over train-time compared to other weights? I.e. are they close to their final value already?


Split ideas

- Different data-types (NLP vs CV)
- Bayesian vs. Group sparsity <- first approach probably?
- Supervised vs unsupervised

ALSO:

Realised the parameter uncertainty is estimatable.

### Wednesday 06-11-2019 till Friday 08-11-2019

- Met up with Patrick for the first time.
- Did some reading.
- Resolved contract stuff
- First presentation
	- Generally seems good first right research
	- Got criticism that what I do is not gonna be helpfull computationally because of the multiple foward passes we would have to do in bayesian nns
	
### Monday 11-11-2019

- Read criticism on LTH in 'rethinking the value of network pruning', seems to be more on the pruning algorithms in general.
- Read the brain damage/surgion papers that claim magnitude based pruning is bs. Wonder why many papers do that now then? Maybe becasue networks have become too big for these second-order derivative methods that they claim are better.
- Coaching sessions gave some outlook on thesis formatting

### Tuesday 12-11-2019

- Read l0-regularization paper that patrick reccomended, seems to be a good speedup which is theoretically grounded but sparsity is not as high as one would think.
- Prepared meeting with patrick.
- Reading Bayesian compression paper, not really understanding the math. Seems as if they show group sparcity causes speed-up, while weight sparsity only reduces memory space. This doesn't seem right to me but is possible. 

### Wednesday 13-11-2019

