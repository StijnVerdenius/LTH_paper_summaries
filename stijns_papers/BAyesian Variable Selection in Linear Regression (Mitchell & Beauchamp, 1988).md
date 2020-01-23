# Bayesian Variable Selection in Linear Regression
 [link to paper](https://www2.stat.duke.edu/courses/Fall05/sta395/joelucas1.pdf) 
 
 *Uses spike and slab as variable selection, related to stijns idea*
 
### spike and slab:

$$p(x) = \pi\delta_{x=0}+(1-\pi)N(x | \mu,\sigma^2) \\\ \text{with} \\\ \pi \in [0,1] \\\ \int\delta_0 = 1  $$

So also writeable as:

 $$ p(z) = Bern(\pi) \\\\ p(x | z = 0) = \delta_{x=0} \quad \wedge \quad p(x | z = 1) = N(x | \mu,\sigma^2) $$
 
Because of the discrete propertie of bernoulli not easily differentiable.


 
## Method
 
considers simple linears regression of one *y*, modelled by serveral components x_J with cofficient b_j and one added bias x_1=1:

$$y= x_1 + \sum \beta_j x_j +\epsilon$$

Now define proprs over beta and epsilon, so as to **compress** the linear regression cofficients beta to become zero. 