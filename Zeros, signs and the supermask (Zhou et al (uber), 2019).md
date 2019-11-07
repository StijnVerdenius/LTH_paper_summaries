# Zeros, signs and the supermask

Authors perform ablation study on the main components of the LT algorithm, specifically on:

- **mask criteria**: Which weights/when to prune
- **mask-1 actions**: What to do with remaining weights
- **mask-0 actions**: How to prune

Also they discover the existence of Supermasks (masks that produce above-chance results when applied to untrained networks)

### Mask criteria:

Looked at metrics that compare initial wieght with final weight.

![alt text](./figs/Zeros_signs_and_the_supermask/mask-criteria.png )

