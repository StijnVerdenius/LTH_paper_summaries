# ThiNet: A Filter Level Pruning Method for Deep Neural Network Compression

[link](http://openaccess.thecvf.com/content_ICCV_2017/papers/Luo_ThiNet_A_Filter_ICCV_2017_paper.pdf) 

*Follow up from Filter pruning for effiecient convnets*

 > For instance, the VGG-16 model [28] has 138.34 million parameters, taking up more than 500MB storage space,1and needs 30.94 billion float point operations (FLOPs) to classify a single image.

## Methods

Filter pruning based on next layer output (just like He et al (2017)).

 they have a 4-step pipeline
 
 1. filter selection based on next layer's statistic by some sort of optimisation problem based on reconstruction of output feature maps and L1 or average percentage of zeros in output maps.
 2. prune weak channels 
 3. fine tune

## Results

flops reduction of 3 times, not mentioned how much speedup
stronger generalisability and better transfer learning