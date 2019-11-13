## One ticket to win them all
[Link to paper](https://arxiv.org/pdf/1906.02773.pdf) 

*Within the natural images domain, winning tickets generalized across a variety of data-sets*

## Summary of findings
- Authors find that winning ticket initializations can be generalized across domains (datasets, tasks, optimizer etc.)
- Moreover, winning tickets generated using larger datasets consistently transfer better than those generated using smaller datasets
- Authors also find that winning ticket initializations generalize across optimizers with high performance
- These results hint at the fact that winning ticket initializations contain inductive biases generic to neural networks more broadly, which improve training across many settings, providing hope for the development of better initialization methods
(Lottery ticket initialization scheme -> Sparsify the network directly from the initialization scheme?)

## Motivation
Existence of lottery tickets suggests that most commonly used initialization schemes (Glorot, He) are sub-optimal and have room to improve. It also suggests that over-parameterization is not necessary for training, but merely to find a "good" initialization of an appropriately parameterized network. 

If these statements are true, then it hints at the possibility of developing a better, more principled initialization scheme.

Authors, then, try and see whether lottery tickets are indeed general. They do this by studying if they can transfer across datasets and optimizers *(this would imply that lottery tickets capture inductive bias in neural networks)*.

### Approach
- Authors use IMP as their pruning method, late resetting (as in Stabilizing the LTH) and global pruning
- Random tickets are used as baseline
- Two models tested : VGG19, ResNet50
- Tickets are trained on a "source" dataset, and then transferred to a "target" dataset
- When output layer is mismatched between datasets, it is simply replaced and randomly initialized


## Results
- Winning tickets which generalize across all datasets with performance close to ticket generated on the target dataset *can be found* -> substantial amount of inductive bias provided by winning tickets is dataset-independent
- Winning tickets generated on larger, more copmlex datsets generalized substantially better than those generated on small datasets. This is impacted not only by sample size, but also by the number of classes (CIFAR-100 generalized better than CIFAR-10)
- When networks are extremely over-parameterised relative to task complexity (i.e. VGG19 to Fashion-MNIST) transferred tickets dramatically outperformed winning tickets generated on Fashion-MNIST itself at low pruning rates. (REVIEW THIS PARAGRAPH)
- Transfer success roughly similar across VGG19 and ResNet50. However performance on ResNet50 degrades rapidly at 90%+ sparsity, while VGG19 only degrade slightly even at 99.9% sparsity. (suggesting ResNet50 models may have a sharper "pruning cliff" than VGG19 models)
- Transfer across optimizers also works (SGD->Adam and vice-versa) suggesting VGG winning tickets are optimizer independent

## Discussion and conclusion
Winning tickets are not overfit to a particular optimizer or dataset, but rather feature inductive biases which improve training of sparsified models more generally. Also, winning tickets generated against datasets with more samples and more classes transfer better, suggesting that larger datasets encourage more generic winning tickets. Transferability is a function of data-size. 

Winning ticket initializations satisfy, thus, a precondition of generality for the eventual construction of a lottery ticket initializaion scheme.

## Limitations
- Generality of winning tickets only evaluated across datasets within same domain and task (images and object classification). Perhaps winning ticket initializations confer inductive biases which are only good for a specific data type or task structure, and not transfer to other tasks or domains. Maybe not tho? It was not researched.
- Results suggest a small fraction of inductive bias *is* dataset-dependent. However it remains unclear which aspects of winning tickets are dataset-dependent and which are not. This could be a research topic.
- Only situations where network topology is fixed have been evaluated 
	- New winning ticket must be generated for each and every architecture topology. (although experiments suggest a small number of layers can be reinitialized without substantial damage) 
	- Methods for parameterizing winning tickets for novel architectures will be an important direction for future studies