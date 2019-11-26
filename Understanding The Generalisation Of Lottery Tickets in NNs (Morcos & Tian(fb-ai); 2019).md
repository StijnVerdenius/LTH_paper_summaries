# Understanding The Generalisation Of Lottery Tickets in NNs
[link to article](https://ai.facebook.com/blog/understanding-the-generalization-of-lottery-tickets-in-neural-networks/)

*Summary of recent LTH research at time of writing (late november 2019)*

## Points:
- They think LTH finds networks at the start, which is not entirely true
- They published the [*'one ticket to win them all'*](https://arxiv.org/abs/1906.02773?fbclid=IwAR23RstyluDH90XYNrsfaOzkt6CK3b7BTcsu2fdRsLpf_CnZ-J7eYGQbNNs) paper to show it is transferable among datasets and optimizers. It was dependent on data-set size tho (bigger is better). 
-  They show these properties hold for [ RL and NLP](https://arxiv.org/abs/1906.02768?fbclid=IwAR2ODWjTVzeMQlHgADD2ajQ5LzI8d2rTL79DEbBBkwIsX_sKI7FFfTYZHrI) .
- In student-teacher networks they analysed how the (larger) students networks initialization affects the learning process of mimicing the smaller teacher networks. They see student networks reproduce outputs but also entire neurons of teacher networks.  If the initial weights of a student-neuron happen to be similar to those of some teacher-neurons, then the reproduction will follow more likely. we find certain mathematical properties in the training dynamics resonate with the lottery ticket phenomenon: those weights with a slight advantage in the initialization may have a greater chance of being the winning tickets after training converges. With our teacher-student paradigm, we’ve been able to demonstrate the lottery ticket behavior of lucky initializations mathematically --- beyond empirical experimentation. 

## Open Questions:

- If we can find a way to identify the winning tickets from the start of training (**SNIP?**)
- Are winning tickets label-dependent or simply dependent on the data distribution? 
- How can we generate winning tickets more efficiently?
- Is it possible to transfer winning tickets across architectures?
- And perhaps most interestingly, what makes winning tickets special?