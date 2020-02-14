# Channel Pruning for Accelerating Very Deep Neural Networks

[link](http://openaccess.thecvf.com/content_ICCV_2017/papers/He_Channel_Pruning_for_ICCV_2017_paper.pdf) 

*Follow up from Filter pruning for effiecient convnets*

## Methods

Introduces 2-step algorithm that minimises reconstruction of output feature maps. They hypothesise that the eature maps are perfect as is and we can prune kernels and if the output maps don't change too much everything is okay. ;
	
1. Select most representable input channnels
2. Reproduce the output channels as accuratly as possible 

## Results

They reach 4x speedup from that alone. With quantisation they get more but im not interested in that