## Learning with random learning rates

### Summary
Authors introduce alrao (all learning rates at once), a gradient descent method with close-to-optimal performance without learning rate tuning. Alrao is found to be reliable over a range of problems and architectures including convolutional networks, LSTMs or reinforcement learning.
They also compare Alrao to the current default optimizer, Adam, with its default hyperparameters. While Adam can outperform Alrao sometimes, it is generally unreliable across varying architectures or during training.

Main idea behind alrao is that not all neurons in a network are useful anyway, leveraging the redundancy to produce a diversity of behaviours from which good network outputs can be built. 

### Method
Alrao starts with a standard optimization method (i.e. SGD) and a range of possible learning rates. Instead of using one learning rate, we sample once and for all one learning rate for each feature, randomly sampled log-uniformly from \\(\eta_{min}, \eta_{max} \\). Then, these learning rates are used in the usual optimizatoin update:
$$ \theta_{l,i} \leftarrow \theta_{l,i} - \eta_{l,i} \nabla_{\theta_{l,i}} L(\Phi_\theta (x), y)$$
where \\(\theta_{l,i}\\) is the set of parameters used to compute the feature i of layer l from the activations of layer l-1 (the incoming weights of feature i). Thus we build slow-learning and fast-learning features, in hope to get enough features in the "Goldilocks zone".

**What is a feature?** Depends on the type of layers in the model. In FC layer, each component of a layer is considered as a feature: all incoming weights of the same unit share the same learning rate. In a conv layer, however, each conv filter represents a feature. There is one learning rate per filter (or channel) thus maintaining translation invariance over the input image. 

**This method cannot be used in the last layer!**. In classification, for example, it would lead to preferring certain classes over others. Instead, what authors do is, on the last layer, they duplicate it using several learning rates, and use a (Bayesian) model averaging method to obtain the overall network output.
 
The learning rate is set per feature, rather than per parameter, since every feature would have some parameters with large learning rates, and we would expect that even a few large incoming weights would be able to derail a feature.

### Experiments