# Stabilizing the Lottery Ticket Hypothesis

Main limitation of LTH is the lack of training for deep networks. This is because of stability issues. Now we train a bit first before applying the algorithm of IMP algorithm after k steps for the first time. *“Rewinding instead of resetting; early but not at time 0” .*

##### They look at two types of instability:


##### - Pruning noise:
> *“the distance between the weights of a subnetwork trained in isolation and the weights of the same subnetwork when trained within the larger network”*

Stability to pruning measures a subnetwork’s ability to train in isolation to final weights that are close to the values they would have reached had they been trained as part of the original network. If we consider the trained weights of the original network to be an ideal destination for optimization, then this metric captures a subnetwork’s ability to approach this point with fewer parameters. 

##### - Data-order noise:
> *“the distance between the weights of two copies of a subnetwork trained with different data orders. Stability to data order captures a subnetwork’s intrinsic ability to consistently reach the same destination despite the gradient noise of SGD.”*

Stability to data-order measures a subnetwork’s ability to reach similar final weights in spite of training with different mini-batch sequences—the gradient noise intrinsic to SGD. This metric is valuable because it provides a way to measure subnetwork stability without reference to the original network.

### some notes

Instability reduces and acc rises with this approach. They hypothesis that this is because ‘tickets’ are more optimised at this point. Also at this point the tickets are more robust against noise from SGD/data order because SGD is very sensitive to randomness early on in training. This might also indicates there are less winning tickets present in initialisation, the deeper the network. Yet again, the broader the network, the more there are.  

Stability seems to correlate with early rewinding and improved accuracy, when compared to random pruning. When rewinding iteration is waited for too long however, we get back to random pruning performance. The paper aims to exploit the temporary ‘stability gap’. 

### Some Questions:


- How to find “small number of steps into training”-benchmarks?
- Can we think of different stability-measures to predict accuracy?


## Limitations:

- Unstructured pruning does not necessarily yield networks that executes more quickly with hardware
- Core pruning technique is still unstructured, magnitude pruning
- Still train a network one or more times to identify a subnetwork
- It is possible that there are equally-capable subnetworks present at initialization, but IMP is unable to find them.


*“However, to the best of our knowledge, our work is the first to show that it is possible to prune(1) so early in training (2) to such extreme levels of sparsity (3) on such large-scale tasks.”*


**Note: Lot of sources mentioned just before the conclusion
Possibly interesting to investigate: can more stable optimizers (i.e. RAdam, Ranger) remove the need for warmup and improve stability even further? (as a side effect this would also make it possible to rewind even earlier during training) Also, does dropout relate in any way to this stability term? (since it prevents co-adaptation of neurons, possibly priming them to be pruned)**
