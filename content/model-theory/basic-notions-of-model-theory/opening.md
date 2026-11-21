The ordered sets $(\Q, <)$ and $(\R, <)$ satisfy exactly the same first-order sentences in the signature $\set{<}$. One is countable and the other is not, one has gaps and the other has none, and still no sentence built from $<$, $=$, the connectives and the quantifiers tells them apart. The groups $(\Z, +)$ and $(\Q, +)$ behave in the opposite way: the sentence $\forall x\, \exists y\, (y + y = x)$ is true in $\Q$ and false in $\Z$, so one line of first-order logic separates them. Model theory is the study of such facts. It looks at structures through the sentences true in them and at theories through their models, and it asks what first-order logic can and cannot see.

The same question applies to subsets. In the field $(\R, +, \cdot)$ the formula $\exists z\, (\neg z = 0 \wedge x + z \cdot z = y)$ says $x < y$, so the order of the reals is already present in the field. In the group $(\Z, +)$ no formula without parameters defines the positive integers, because the map $x \mapsto -x$ is an automorphism, and an automorphism maps every set defined without parameters onto itself. Arguments of these two kinds, a formula that defines a set and an automorphism that moves it, recur in every chapter of the volume.

## What the chapter covers

The chapter is in six groups, read in order.

1. **The subject and its history.** An overview of [model theory](/HFTBG5PMXC/) and a [history of model theory](/JNBJW8RTJD/) from Löwenheim and Skolem to the present.
2. **Maps between structures.** [Substructures](/676H7EGTKJ/), [embeddings](/SCRB74SWQN/) and isomorphisms, and [reducts and expansions](/EY20BF96SJ/), including the expansion of a structure by constants for its elements.
3. **Theories and elementary equivalence.** The [theory of a structure](/X9HV9C6X4F/) and the class of models of a theory, [elementary equivalence](/P3B1V182N4/), and [complete theories](/655K8Y7VS8/) with the main ways to prove completeness.
4. **Elementary classes and axiomatization.** [Elementary classes](/MEC3ZMC4F1/), basic elementary classes and [finitely axiomatizable theories](/JR6XPJ7X56/), with compactness as the main tool for negative results.
5. **Definable sets.** [Definable sets](/CY1TXHF6KQ/) with and without parameters, and the automorphism test for non-definability.
6. **What first-order theories can and cannot say.** A list of [standard first-order theories](/AWASYPREVT/) and a list of [properties that are not first-order](/T1S9T0RKHJ/), with the arguments that rule them out.

## A first reading

For a first reading, take these entries in order: [model theory](/HFTBG5PMXC/), [substructure](/676H7EGTKJ/), [embedding of structures](/SCRB74SWQN/), [theory of a structure](/X9HV9C6X4F/), [elementary equivalence](/P3B1V182N4/), [complete theory](/655K8Y7VS8/), [elementary class](/MEC3ZMC4F1/), [definable set](/CY1TXHF6KQ/) and [properties that are not first-order](/T1S9T0RKHJ/). Work through the attached examples of elementary equivalence and of definable sets with care; the arguments in them are the ones you will use most.

The history, the finer points of reducts, and the entry on finite axiomatizability can wait for a second pass. Read the part of the entry on reducts and expansions that adds constants for elements before the next chapter, because the method of diagrams there is built on it. The list of standard theories is a reference: return to it whenever a later entry names a theory.

## Before you start

The chapter is the first of the volume, and it builds directly on the logic chapters of Volume 2.

- From [first-order languages and syntax](/PSRDJXRW53/) you need [signatures](/WDVVEYD6AT/), [formulas](/HYJ10AF6RT/), [free and bound variables](/9CNGDRAMGC/), [sentences](/DKFGQTRYZE/) and [first-order theories](/92SWXST1ZM/).
- From [structures, satisfaction and truth](/NJDME6F845/) you need [structures](/983GZBQYT4/), the [satisfaction](/2RBQPV02AS/) relation $\mathcal{M} \models \varphi[\bar a]$, [truth in a structure](/K7XDVK5854/), [models](/MVCH6N9SNW/) and [logical consequence](/1HK0VYWTV7/). The [isomorphism invariance of truth](/NDTJ2E895C/) is used in almost every automorphism argument, and the entry on [definable relations](/1DQ1M6ZWS4/) is the starting point for definable sets.
- From [completeness, compactness and interpolation](/FBWW4J1XWG/) you need [Gödel's completeness theorem](/WQ1ZE255SF/), which lets you read $T \models \sigma$ as "$T$ proves $\sigma$", and above all the [compactness theorem](/1NR3HAWG9D/) and its [applications](/PES0S9XQZ5/). The entries on elementary classes, finite axiomatizability and properties that are not first-order all argue by compactness.
- The [proof systems](/TTCRX3NFNY/) themselves are not used; model theory works with $\models$, and completeness turns each statement into one about proofs when that is wanted.

You also need the definitions of groups, rings, fields and linear orders, and the difference between [countable](/0ZG61TFBES/) and uncountable sets.
