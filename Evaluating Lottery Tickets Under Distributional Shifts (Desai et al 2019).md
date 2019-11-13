# Evaluating Lottery Tickets Under Distributional Shifts
[Link to paper](https://arxiv.org/pdf/1910.12708.pdf) 

*Researches the extent to whicha sparse subnetwork obtained in a source domain  can  be  re-trained  in  isolation  in  a  dissimilar, target domain. Mainly, the  focus is on understanding whether the architecture can be transferred, and whether transferring the initialization is required. They show positive results*


- Stabilizing paper is already out.
- Criticism of *Lui et al (2018)* & *Morcos et al (2019)* is taken aboard.
	- But, they want to experiment with transferring architectures to other domain, as well as testing initialisation schems, and find generalisation power in tickets.
- They discover **Phase Transitions** in here


## Contributions:

- Showing tickets exist in textual domains
- Confirming LTH
- Showing transferability of tickets in NLP tasks (LTH trasfer learning?)
- Different than *'one ticket to win them all'*, in the sense that:
	- Here they make a distinction between topologie (= network?) and initial values.
	- Also they do nlp instead of cv.

## Method

1. They define distributional shifts as being the change of datasets in Amazon reviews (e.g. Books, Electronics, etc.. ). *"The differences in unigram frequencies, semantic content, and random noise mimic the type of distributional shiftsthat occur in machine learning."*. They measure the divergence score (=distributional shift) with JS-divergence (= two-way KL). 
2. Define a vocabulary across datasets.
3. Define shared task of sentiment analysis
4. Use 1d-CNNs - with embeddings - as classifier
5. By iterative pruning (LTH), they obtain a subnetwork for each pruning-round (in-between prunings are not thrown away). Then this array of masks is transferred to target domain. 
6. Define some initialisation techniques to test:
	- Use source domain values (So only a different dataset).
	- Use random values (So only mask transfer). 
7. Test the the masks with different inits in target domain.

*"Our transfer task is designed to answer the following question: can the sparse masks found in a source domain, using lottery ticket training, be transferred to a target domain with different initialization strategies match the performance of a ticket obtained in same target domain?"*

## Results

They test initialisations of source domain tickets first and find that both random and init at orginal values (LTH) is the same for most sparsities. But when sparsity becomes REALLY high ( >96% ), then LTH is a lot more stable and they claim a *phase transition*. 

Then they test masks in the target domain with some initialisations. They find tickets trained from start on target (baseline) performs the best. They encounter a few of the biases that NLP suffers from in their categories (not interesting for us). These results  together imply that tickets are notcompletely immune to distributional shifts.

## Conclusion

- LTH and ticket transfer possible in NLP
- Initialisation of tickets doesn't need to be done LTH style unless dealt with insane sparsity
	- they claim a phase transition where init starts mattering

## Limitations

- Distributional shift is only a minor change in data
- Phase transition is not explained
- Only did binary sentiment classification
- Not enough hyperparam tuning