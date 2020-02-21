# Picking winning tickets before training by preserving gradient flow

[link](https://arxiv.org/pdf/2002.07376.pdf) 

*follow up to snip, concurrent to orthogonall initialisation, introduce GraSP*

They argue that SNIP, evaluates weights in isolation, which therefore can influence the gradient flow. 

They find that gradient signal gets blocked with snip, and by theoretical foundations show that using a hessian product would increase both stability to pruning and learning.

They outperform snip in high-sparsity regime, not in lower