## Delving deep into rectifiers

Authors present PRelu and a new method for initializing neural networks.

**PReLU:** shows performance increase over ReLU. For deep conv nets, interestingly enough, the parameters of PReLU are bigger in the first conv layers and lower in the later ones. Since first channels are Gabor-like filters (edge detectors, texture detectors) so both positive and negative responses of the filters are respected. For deeper ones, coefficients are smaller, meaning activations gradually become "more nonlinear", suggesting that the model tends to keep information from earlier stages and becomes more discriminative in deeper stages. 


**Init. of filter weights for rectifiers:** Authors do similar derivations as in the Glorot paper, and obtain the following distribution:

\\( W \sim \mathcal{N}(0, \sqrt{\frac{2}{n}})\\), where n is fan_in aka the number of incoming connections coming into a given layer from the previous layer's output, and bias tensors are initialized to 0.
For 30-layer CNNs, this init worked out fine, while Xavier init stalled completely, and did not learn at all. 