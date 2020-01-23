# Single-shot Channel Pruning Based On Alternating Direction Method Of Multipliers
[link](https://arxiv.org/pdf/1902.06382.pdf) 

*Single-shot channel pruning based on ADMM*

> " To the best of our knowledge, this is the first study of single-shot channel pruning"

- Has some references to channel-pruning methods.
- inspired by SNIP

## Method

Says its inspired by SNIP to do the same but then on channels. However, it doesn't look like the snip pipeline. I think they only use the idea of single-shot-ness. Steps:

1. train a cnn with ADMM (= alternating direction method of multipliers) and weight decay
2. remove filters with smallest l1-norm
3. fine-tune

They compare their method to:

- l1 pruning (weight magnitude) only
- mean activations
- taylor-expansion based saliency criterion
- admm weight only
- random

Obvisouly they beat benchmarks..

