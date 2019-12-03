## A Closer Look at Structured Pruning

### Summary
 In this paper, we examine ResNets and DenseNets obtained through structured pruning-and-tuning and make two interesting observations: (i) reduced networks—smaller versions of the original
network trained from scratch—consistently outperform pruned networks; (ii) if
one takes the architecture of a pruned network and then trains it from scratch it
is significantly more competitive. Furthermore, these architectures are easy to
approximate: we can prune once and obtain a family of new, scalable network
architectures that can simply be trained from scratch. Finally, we compare the
inference speed of reduced and pruned networks on hardware, and show that
reduced networks are significantly faster