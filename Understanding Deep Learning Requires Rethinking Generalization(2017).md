## Understanding Deep Learning Requires Rethinking Generalization

### Contributions
- **Randomization tests.** Deep neural nets easily fit random labels, achieving 0 trainign error.
- **The role of explicit regularization.** If model architecture itself isn't a sufficient regularizer, how much does explicit regularization help? Authors show that explicit forms of regularization i.e. wdecay, dropout, data augmentation etc. do not adequately explain the generalization error of neural networks, or, put differently: Explicit regularization may improve generalization performance, but is neither necessary or by itself sufficient for controlling generalization error. The absence of regularization does not necessarily imply poor generalization error.
- **Finite sample expressivity.** Empirical observations are complemented with a theoretical construction showing that large NNs can express any labeling of the training data. Authors exhibit a 2-layer relu network with p=2n+d parameters which can express any labeling of any sample of size n in d dimensions.
- **The role of implicit regularization.** Not all models that fit training data generalize well. Authors analyze how SGD acts as an implicit regularizer. Although they show this, they say that more investigation is needed to understand properties of models trained using SGD.

### Effective Model Capacity of Neural Networks
Authors want to understand effecitve model capacity of FFN networks. Toward this goal, they take an arhcitecture and train it (1) on the train data and (2) on a copy of the data in which the true labels were replaced by random labels.

Experiments are run with true labels, partially corrupted labels (a subset of the labels are randomized), random labels, shuffled pixels (for all images the same permutation) and random pixels (different random permutation per image) and Gaussian (random pixels from gaussian distribution with mean and var. matching the dataset). **Models were able to overfit to 0 train loss for cifar10 and 95% acc. for imagenet.**

### The role of regularization
Authors test if data augmentation, wdecay and dropout help. Regularizers restrict the search space of possible hypotheses to a space with lower complexity. Howver, in deep learning it's not clear if this is the case. Data augmentation was shown to help the most.
>So while regularization is important, bigger gains can be achieved by simply changing the model architecture.  It is difficultto say that the regularizers count as a fundamental phase change in the generalization capability ofdeep nets.

Authors also test with/without BatchNorm (they argue it's an implicit regularizer). 
Conclusion: regularizers (when properly tuned) can help improve generalization performance. However it's unlikely that the regularizers are a fundamental reason for generalization, as the networks continue to perform well even in the absence of regularizers.

### Finite Sample Expressivity
As soon as the num. of parameters of a network, p, is greater than n, the number of samples, even simple two-layer NNs can represent any function of the input sample. 
>There exists a two-layer neural network with ReLU activations and 2n+d weights that can represent any function on a sample of size n in d dimensions.

### Implicit Regularization
Authors turn to linear models to see if they can gather any insight w.r.t. the source of generaliaztion for deep neural networks. They use a direct method of finding the global optimum by forming the Gram matrix (aka kernel) on the data \\(K=XX^T\\) and solving the linear system \\(K*\alpha = y\\).  For MNIST with no preprocessing they get 1.2% test error. For CIFAR10 they get 46% (they also applied a Gaussian kernel on the pixels). Preprocessing with a random convnet with 32.000 random filters, test error drops to 17%, adding L2 reduces this further to 15%. (no data augmentation used)

This kernel solution has an appealing interpretation: it is equivalent to the minimum L2-norm solution of \\(Xw=y\\). That is, out of all models that exactly fit the data, SGD will often converge to the solution with minimum norm (??). 

Unfortunately this notion of minimum norm is not predictive of generalization performance. In their experiments, solutions with higher norms had lower test accuracy. While this minimum-norm intuition may provide some guidance, it's only a small piece of the puzzle.

### Conclusion
Authors demonstrate that effective capacity of several succesful neural networks is large enough to shatter the training data. So they can effectively memorize the training data perfectly. Measures of complexity from statistical learning theory struggle to explain the generalization ability of large neural networks. 