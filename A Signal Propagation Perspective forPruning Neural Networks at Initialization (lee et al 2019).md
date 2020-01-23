# A Signal Propagation Perspective forPruning Neural Networks at Initialization
[link](https://arxiv.org/pdf/1906.06307.pdf) 

*Follow up from SNIP, considers the pruning problem from a signal propagation perspective, formally characterizing initialization conditions that ensure faithful signal propagation throughout a network. Finds that orthogonal initialisation works better.*


 SNIP assumes a gaussian initialisation. their saliency score (CS) is unreliable in some cases, in that it does not faithfully measure the sensitivity of each connection..  It is important to guarantee that the input and error signals propagates with minimal amplification or attenuation in the forward and backward directions.
 
 - Show that  to ensure faithful CS is layerwise dynamical isometry, which is defined as the singularvalues of the layerwise Jacobians being close to one.
 - Orthogonal initialisation satisfies this, luckily
 - Yet sadly, poses some problems for ReLu's
 
 > "As noted in Lee et al. [SNIP], a variance scaling initializationscheme tends to improve pruning results"
 
##  Aim:
"Since snip prunes at init, we want to understand the effect of initialisation"

## problem confirmation:
 for tanh they find most pruning happens in later layers, unlike for linear activations. Sensitivity by tanh is decreased in later layers, due to the poor signal propagation: an initialization thatleads the forward signal to explode. Linear layers do not have this problem.
 
 > "Note that, signal propagation in a network is said to be faithful if the input signal is propagated to the output with minimal amplification or attenuation in any of its dimensions"
 
 This faithfulness is related to the singular values of the jacobian
 
 ..
 > some math i skipped

..
 
 There are two cases:
 - <u>Linear activations</u>... Make sure the initialisation is close to orthogonal meaning that 
 
 $$ (W^l)^T \cdot W^L = I $$
 
  - <u>NonLinear activations</u>, activations fuck things up a bit. Now you make sure the pre-activations fall into the near-linear region of the activation (related to **mean-field-theory**). aka, let pre-activations be a zero-centered-mean on average. Then we can find a rescaling sigma so that:
  $$\frac{(W^l)^T \cdot W^L}{\sigma_w^2} = I$$
  
 
## looking back at snip
  
- Next they notice that the SNIP saliency is actually the same as elasticity, although they don't name it. However they do notice that in this elasticity:
 $$ \frac{\partial L}{\partial w} w $$
 by multiplying with w, we get a amplification. 
 
 - if different layers have different magnitudes the top-k threshold is not sufficient. This condition is trivially satisfied when the layerwisedynamical isometry is ensured, as each layer is initialized identically
 
## Results

- First of all, the best pruning results are achieved with the orthogonal initialization
-  yield good generalization errors
- random pruning completely destroys signal propagation
- something with loss function i dont really understand
- also something that i don't understand with "condition numbers"


## conclusion
- a step into direction of guarenteed “trainability” of sparse networks from scratch, via clever initialisation
- step forward for snip

## network sculpting??

 "This sparks curiosity of whetherpruning needs to be limited to pre-shaped architectures. In other words, what if pruning starts with a bulky network and is treated as sculptingan architecture?" 
 
 