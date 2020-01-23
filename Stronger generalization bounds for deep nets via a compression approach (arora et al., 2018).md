# Stronger generalization bounds for deep nets via a compression approach
[Link to paper](https://arxiv.org/pdf/1802.05296.pdf) 

*"Deep nets generalize well despite having more parameters than the number of training samples. Current approaches do not as yet have a metric in sample complexity bounds better than naive parameter counting. Our results also provide some theoretical justification for widespread empiricalsuccess in compressing deep nets."*

## Some Definitions:

**sample complexity** is the number of training-samples that it needs in order to successfully learn a target function, so that the function returned by the algorithm is within an arbitrarily small error of the best possible function, with probability arbitrarily close to 1. 

**Sample Size Upper Bounds**

**Generalisation bounds**

**Probably Approximately Correct (PAC) learnability**: there exists an algorithm that is approximatly correct at any data distribution.

**Rademacher complexity:** can an algorithm fit random labels? (data-dependent). Very related to VC-dimension.

**VC dimension**  is a measure of the capacity (complexity, expressive power, richness, or flexibility) of a space of functions that can be learned by a statistical classification algorithm. It is defined as the cardinality of the largest set of points that the algorithm can shatter. A set of points is said to be shattered by a class of functions if, no matter how we assign a binary label to each point, a member of the class can perfectly separate them. 

## Related work
- Some papers have suggested that nets that generalize well are flat  minima in the optimization landscape.
- Some papers show using experiments that sharp minima correlate with higher generalization error.
- A quantitative version of “flatness” (= stability) was suggested:  the net’s output is stable to noise added  to  the  net’s  trainable  parameters.
	> results were worse than naive counting
- Another method: noise on nodes. (like dropout and batchnorm..)

## Contributions

- Compression framework for proving generalisation bounds
- Identifying new form of noise stability for nets
- Mathematically proven algorithm that reduces parameters and yields generalization bounds that are:
	- better than naive counting
	- simple
	- workable for multiple layer-types


![](./figs/Stronger_GEneralisation_Bounds/fig1.png) 

***to be continued...***