## Understanding the difficulty of training deep feedforward neural networks

Authors want to understand why standard SGD from random initialization is (was, I guess) doing so poorly with deep neural networks. They first observe the influence of non-linear activation functions, and find that sigmoid activatoins are unsuited for deep NNs with random init. due to its mean value, which can cause saturation in the top hidden layer. So, a new activation function that saturates less often is benefical. Finally, they study how activations and gradients vary across layers and during training, with the idea that training may become harder when the singular values of the Jacobian associated with each layer are far from 1. Based on this, they propose the **Glorot init.**
(Before this, people were using unsupervised pre-training)
Their analysis pertains monitoring activations and gradients across layers and training iterations, seeing the effect that the activation function and initialization procedure has on them. 

### Experimental setup
**Datasets**: shapeset, tiny imagenet, cifar10, mnist
**Models**: feedforward NNs with 1 to 5 hidden layers, 1000 neurons per layer
**Activations used: **sigmoid, tanh, softsign: x/(1+|x|)
**Init used:** uniform \\( W_{ij} \sim U[-\frac{1}{\sqrt(n)}, \frac{1}{\sqrt(n)}]\\), and n is the size of the previous layers (num. of columns of W). Biases were initted to 0.
Hyperarameters were searched separately for each model. 

### Effect of activatoin and saturation during training
#### Experiments with Sigmoid
Sigmoid has been shown to slow down learning because of its non-zero mean that induces important singular values in the Hessian. 
For sigmoid activation, very quickly at the beginning all actiavation values of the last hidden layer are pushed to their lower saturation value of 0. Conversely, the others layers have a mean activation value that is above 0.5, and decreasing as we go from the output layer to the input layer. Wehave found that this kind of saturation can last very long in deeper networks with sigmoid activations, e.g., the depth-five model never escaped this regime during training. Surprisingly, for intermediate number of hidden layers (here four), the saturation regime may be escaped. At the same time that the top hidden layer moves out of saturation, the first hidden layer begins to saturate and therefore to stabilize.
This is behaviour is due to:

- a random initialiazation
- a hidden unit output of 0 corresponds to a saturated sigmoid
The explanation: the transformation that the lower layers of the network initially computes is not useful for classification (unlike the transformation obtained from unsupervised pre-training). The output layer softmax(b+Wh) might at first rely more on the biases. So the error gradient would push Wh to 0, which can be done by pushing h to 0. For symmetric activations like sigmoid, tanh and softsign, that's ok, because it allows gradients to flow backward. Pushing the sigmoid to 0, however, causes it to saturate.

#### Experiments with tanh
Tanh does not suffer from this kind of saturation behavior as sigmoid, due to it being symmetric around 0. However some sequential saturation still happens, starting with layer 1 and propagating up in the network. Why this happens remains to be understood.

### Studying gradients and their propagation
Gradients become smaller as one moves from output to input layer, just after initialization. On networks with linear activations, the variance of the back-propagated gradients decreases as we go backwards in the network. 
Authors derive in the paper the variances w.r.t. input, output and weight init randomness, and assuming linear regime and independent init. 
For forward propagation, we would like the variance of the activation vectors of each layer to be the same. Similarly, for backprop, we'd like the variance of the gradient of the cost function w.r.t. the layer outputs to be the same. After some derivations, to approximately satisfy the objectives of maintaining activation variances and back-propagated gradients variance, as one moves up or down the network, the authors propose the** normalized initialization:**

$$W \sim  U[-\frac{\sqrt 6}{\sqrt{n_j + n_{j+1}}},\frac{\sqrt 6}{\sqrt{n_j + n_{j+1}}}]$$

\\(n_j \\) is the number of incoming connections to the layer (fan_in) and \\(n_{j+1}\\) is the number of outgoing connections from the layer (fan_out).
### Caveats
Assumes linear activations. Derivations may therefore not be optimal.