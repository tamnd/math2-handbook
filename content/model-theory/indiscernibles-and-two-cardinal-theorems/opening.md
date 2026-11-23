In the ordered field $\R$, the numbers $1, 2, 3, \ldots$ are not alike: $2$ is $1 + 1$, and $4$ is $2 \cdot 2$, so formulas tell the terms of the sequence apart. Pass to a large nonstandard real closed field and take a sequence $a_0 < a_1 < a_2 < \cdots$ of infinite elements, each so much larger than the ones before that $a_{n+1}$ exceeds every value $f(a_0, \dots, a_n)$ of a function defined without parameters. Then all increasing pairs $(a_i, a_j)$ satisfy the same formulas, and the same holds for increasing triples and longer tuples. A sequence like this is called indiscernible: no formula, however complicated, can distinguish one increasing tuple of it from another of the same length. Ramsey's theorem and compactness give such a sequence in a model of every theory with infinite models, and it can be indexed by any infinite linear order.

Ehrenfeucht and Mostowski used these sequences in 1956 to build models with many automorphisms. Take the Skolem hull of an indiscernible sequence indexed by an order $I$: every order-preserving map of $I$ becomes an elementary embedding, and the automorphism group of $I$ sits inside the automorphism group of the model. Morley used the same models over well-orders to bound the number of types they realize, a step in his categoricity theorem, the subject of Chapter 4.12. The second half of the chapter turns to the sizes of models. The structure $(\R, +, \cdot, \Q)$, with a predicate for the rationals, has size $2^{\aleph_0}$ while its predicate is countable. Vaught's two-cardinal theorem then gives a model of the same theory of size $\aleph_1$ in which the predicate is countable.

## What the chapter covers

The chapter is in two groups, read in order.

1. **Indiscernibles and Ehrenfeucht–Mostowski models.** An [indiscernible sequence](/4016QKAHFB/) has the same type on all increasing tuples of each length, and an indiscernible set has it on all tuples of distinct elements. The [existence of indiscernibles](/RG6D2FAS14/) comes from [Ramsey's theorem](/00TQV3F5S4/) and, in Morley's form, from the [Erdős–Rado theorem](/S1BHE358VX/). [Ehrenfeucht–Mostowski models](/TSGB29FJM0/) are the Skolem hulls of indiscernible sequences, with many automorphisms and few types. [Generalized indiscernibles](/RQS808ZC8T/) are indexed by structures other than orders, such as graphs, and their existence is a Ramsey property of the index structure.
2. **Two-cardinal theorems and Hanf numbers.** [Vaught's two-cardinal theorem](/XT227BYP7B/) turns any $(\kappa, \lambda)$-model with $\kappa > \lambda \ge \aleph_0$ into an $(\aleph_1, \aleph_0)$-model, by way of Vaughtian pairs. [Chang's two-cardinal theorem](/4STP69KESQ/) goes up from $(\aleph_1, \aleph_0)$ to $(\kappa^+, \kappa)$ when $\kappa^{<\kappa} = \kappa$, and the gap-$n$ cases depend on set theory. The [Hanf number](/A9XBRF3A7Z/) of a logic is the threshold beyond which a sentence with a model has arbitrarily large models: $\aleph_0$ for first-order logic and $\beth_{\omega_1}$ for $L_{\omega_1\omega}$.

## A first reading

A short course takes these entries in order.

- [Indiscernible sequence](/4016QKAHFB/), for the definitions and the Ehrenfeucht–Mostowski type.
- [Existence of indiscernibles](/RG6D2FAS14/), for the Ramsey form and its proof by compactness. Morley's form, with the families $X_\alpha$ of size at least $\beth_\alpha$, can wait until the Hanf number.
- [Ehrenfeucht–Mostowski models](/TSGB29FJM0/), parts 1 to 4. Part 5, on the types realized over well-orders, is needed for categoricity.
- [Vaught's two-cardinal theorem](/XT227BYP7B/), with the examples that show each hypothesis is needed and the consequence for $\aleph_1$-categoricity.
- [Hanf number](/A9XBRF3A7Z/), with the example of first-order logic.

[Generalized indiscernibles](/RQS808ZC8T/) lead to classification theory and can be read later. [Chang's two-cardinal theorem](/4STP69KESQ/) needs a saturated model of size $\kappa$, so read it after its prerequisites; its remarks on morasses and Chang's conjecture are a survey of set-theoretic results without proofs.

## Before you start

The chapter assumes the following.

- [Elementary extensions and the Löwenheim–Skolem theorems](/2RE7GWWXM5/), above all [Skolem functions and Skolem hulls](/NKQY9NB955/), the [Löwenheim–Skolem theorem](/484M0TZ1S7/) and [elementary chains](/NHCRZ74JHH/).
- [Types and saturated models](/Z772KEC9BY/): [types](/9V71Q3SD1G/), [saturated models](/RMTZ5J64FX/) and the [existence of saturated models](/GSQ833HAZT/), which Chang's theorem uses.
- The [compactness theorem](/1NR3HAWG9D/) of Volume 2, used in every existence proof of the chapter.
- [Cardinal numbers](/0EBACQFAZW/) and [beth numbers](/ZC4BHVHWE9/), for the sizes in the two-cardinal theorems and the Hanf number.
- For generalized indiscernibles, the [Rado graph](/RMXR0FEF54/) and [Ramsey classes](/8XS8FCTF8T/) from Chapter 4.7.
