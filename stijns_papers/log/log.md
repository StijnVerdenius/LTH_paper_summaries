# **LOG**
<body onLoad="window.scrollBy(0, window.height)">
## **Exploration**-stage

### Monday 04-11-2019

- Hooked up screens
- Install and contracts
- Considered combining lottery ticket hypothesis with Bayesian networks
- Found a supervisor
- accessed das4 account and surfsara. Can only do das4 from desktop because of vpn issues. surfsara is probably part of DL4NLP
- chose a few paper to explore (see commented out):s

Some questions

- What are the algorithmic competitors of lottery ticket hypothesis?
- Can pruning be directly integrated into training?

### Tuesday 05-11-2019

**LTH consists of:**
    - Commensurate Training time: j >= j’
    - Commensurate Accuracy: a <= a’
    - Fewer Parameters: norm(params) >= norm(params’)
**Some questions: **

  - What are the algorithmic competitors of lottery ticket hypothesis?
  - Can pruning be directly integrated into training?
  - What is the contribution of LTH in comparison to the two papers from the heading in this document: ‘Training a pruned model from scratch performs worse‘.
  - Figure 1 in the main paper; why is early stopping criterium met earlier in unpruned networks? Overfitting?

**Some research ideas:**

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


**Split ideas**

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
- Realised that weight pruning might help wiht speedup but not with memory fitting as activations or channels can not be pruned this way.

### Wednesday 13-11-2019

- Read state of sparsity paper, which gave a good overview of recent methods and a paper about distributional shifts that was a bit meh..

##### Meeting patrick:

- seems disinterested in topic and publications
- says perhaps a application is better to pursui
- says we should start trying things out
- might be interesting:
	- Adversarial attacks
	- Weight heuristics on gradient, varriance and uncertainty
- made me say: "I am interested in researching how weight uncertainty relates to them being dropped out and i hypothesize it is a good indication for them. I hope to use that to cut out during training and maybe remove some hyperparameters of the LTH algorithm"
- Asked to share a overleaf of the thesis

### Thursday 14-11-2019 

- ran a approximate l0 regularization experiment. It consists of having a loss term that takes in a parameter set, then with a limit parameter L, which is initialised at the max value of the weight matrix it will take the tensor, substract the limit and then relu, same for the negative tensor and added limit. Then we remain with the entries that are within that limit, which we can then sum up somehow. Not sure if it is valid, im tired. I might just be doing l2 loss.
- Read about variational dropout, still some things unclear but it seems cool. 
- Defined which methods we wanna have a toy experiment on

### Friday 15-11-2019

Recreated experiments on LTH (non stabilized) with a simple 3 layer FC-relu network on MNIST. We found that:

- Restart matters in high sparcity levels (\>80%)
- LTH works in very high level of sparsity (~98%)
- Sparse networks generalize better up to a certain point

**Results:**

TODO

### Monday 18-11-2019

- Worked on logs
- Read SNIP papers
- Started on section 2 of the actual thesis as well as formatting the thesis.
- Read Soft weight sharing

Meeting with Maarten:
	- Didn't seem to be too worried. He figured my experimental designs were actually good starting points. 
	- Maybe I have to become a bit more independent
	- Very important to start documenting all my experiments, maybe ask anton for reproducibility of experiments
	
- Made leren en beslissen projects

### Tuesday 19-11-2019

- Read han et al papers (2015 & 2016)
- picked 3 projects that perhaps will be good for leren en beslissen 
- Started on background section

### Wednesday 20-11-2019

- Read targeted dropout paper 
- Worked out quite a lot for thesis background section, mostly the big picture (done)
- planned for omnimap
- Made project description for datanose 

### Thursday 21-11-2019

- Mostly debugging code for stabilizing
- learned about braincreator-clusters
- rewrote januari projects

### Friday 22-11-2019

work @ omnimap


### Monday 25-11-2019

- Rewrote general background.
- Coaching sessions: talked about positioning in well established fields and the role supervisors should really have 

### Tuesday 26-11-2019

- Wrote most of the L0-reg derivation
- Meeting with Patrick:

we talked about that the contradictions between papers could be dealt with in an ablation study, I should start implementing and collecting all the metrics already as well as saving all model checkpoints so things could be collected later as well. Mostly focus on MNIST, CIFAR, ImageNet so far. Another question was: what kind of task would we want sparsity for? I linked that to my motivations section in my overleaf. in this section there is one about overparametrisation, which I linked to overfittting but apperantly after #params hits #datapoints, network overfitting goes down. he didn't have the paper. I still think generalisation and maybe even adversarial attacks could be interesting but it needs a better brainstrom so patrick advised to start with some baselines based on regularisation first. He said to find MAP estimates of networks with regularisation based on heavy tailed distributions such as heavy distribution, horse shoe, L1, horse-shoe+, inverse gamma-gamma, student log t, student t, LP-regularisation with 1>P>0.

Then we brainstromed about my and patricks ideas: Resnet on weight matrices where each layers weights is the previous weight + an outer product of two vectors. for my idea about bayes by backprop he reccomended going to the addition of something and slab distribution, where you have 3 parameters to govern model parmeters.

- Finalized idea for januari projects
- Read some papers

### Wednesday 27-11-2019

work @ omnimap

### Thursday 28-11-2019

Holiday

### Friday 29-11-2019

Holiday