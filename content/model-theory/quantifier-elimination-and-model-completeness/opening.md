Over the complex numbers, the formula $\exists x \, (a x^2 + b x + c = 0)$ says the same about $a, b, c$ as the formula $a \ne 0 \lor b \ne 0 \lor c = 0$, which has no quantifier. Over the reals the same formula is equivalent to $(a \ne 0 \land b^2 - 4ac \ge 0) \lor (a = 0 \land (b \ne 0 \lor c = 0))$, which has no quantifier but uses the order. Over the integers with addition, $\exists y \, (x = y + y)$ has no quantifier-free equivalent in $+$, $0$, $1$ and $<$, and one adds a predicate $D_2$ for "even" to get one. In each case a statement about the existence of an element became a statement about the given parameters alone. A theory in which this works for every formula has [quantifier elimination](/7FDDXV3JK7/). Its definable sets are then Boolean combinations of the sets cut out by atomic formulas: constructible sets for algebraically closed fields, semialgebraic sets for real closed fields. Its models can be compared through their substructures.

Abraham Robinson found the weaker notion that carries most of the algebra. A theory is [model complete](/YR6HCMABTE/) when every embedding between its models is elementary. The [existentially closed models](/6M98MCW575/) of a theory are the ones in which every system of equations and inequations with a solution in an extension already has one; for fields these are the algebraically closed fields, and this gives the Nullstellensatz. A [model companion](/68GG7QKN7C/) is a model complete theory of such closed models. Fields, linear orders and ordered fields have one, and groups do not.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Quantifier elimination and its tests.** The definition of [quantifier elimination](/7FDDXV3JK7/), and the [tests](/Q1CGE4DWXQ/) that reduce it to a single existential quantifier or to extending embeddings into $\omega$-saturated models.
2. **Model completeness.** [Model complete theories](/YR6HCMABTE/) and [Robinson's test](/QHEADWYQ64/): model completeness holds exactly when every formula is equivalent to an existential one, and exactly when every formula is equivalent to a universal one.
3. **Existentially closed models and model companions.** [Existentially closed models](/6M98MCW575/), the [model companion](/68GG7QKN7C/) and the model completion, and [inductive theories](/G8TRE2KSRV/), the theories closed under unions of chains, in which existentially closed models always exist.
4. **When there is no model companion.** The [theory of groups](/5GS2AE651W/) has none, because conjugacy of elements of infinite order defeats compactness. [Robinson forcing](/2TYY0ZP7YQ/) gives generic models in its place.
5. **Elimination for fields.** [Algebraically closed fields](/2NBBJADY5N/) and [real closed fields](/FSJ9NGRRPA/) eliminate quantifiers, and [cylindrical algebraic decomposition](/GE8FCGKPTR/) does the real elimination by computation.
6. **Groups and relative elimination.** [$\Z$-groups](/VKC9CR37FT/), that is Presburger arithmetic with divisibility predicates, and [divisible torsion-free abelian groups](/BFK4T1WK38/) eliminate quantifiers. [Relative elimination](/WMC3J66FAY/) reduces a theory to a chosen set of formulas.

## A first reading

A short course takes these entries in order.

- [Quantifier elimination](/7FDDXV3JK7/), with the dense linear orders as the first example.
- [Tests for quantifier elimination](/Q1CGE4DWXQ/). The one-quantifier test is the one used by hand, and the extension test is the one used in proofs.
- [Quantifier elimination for algebraically closed fields](/2NBBJADY5N/), the main algebraic example.
- [Model complete theory](/YR6HCMABTE/), with the real closed fields in the ring signature.
- [Robinson's test](/QHEADWYQ64/).
- [Existentially closed model](/6M98MCW575/), with the fields and the linear orders.
- [Model companion](/68GG7QKN7C/).
- [Quantifier elimination for real closed fields](/FSJ9NGRRPA/).
- [Quantifier elimination for $\Z$-groups](/VKC9CR37FT/).

[Inductive theories](/G8TRE2KSRV/) can be read with the model companion, as the hypothesis under which existentially closed models exist. The theory of groups and [Robinson forcing](/2TYY0ZP7YQ/) can wait until the model companion is familiar. [Cylindrical algebraic decomposition](/GE8FCGKPTR/) is for readers who want an algorithm, and [relative elimination](/WMC3J66FAY/) leads to the model theory of valued fields, which is not yet in this book.

## Before you start

The chapter assumes the following.

- [Basic notions of model theory](/AY09KYSW81/): [substructures](/676H7EGTKJ/), [embeddings](/SCRB74SWQN/), [definable sets](/CY1TXHF6KQ/) and [complete theories](/655K8Y7VS8/).
- [Elementary extensions and the Löwenheim–Skolem theorems](/2RE7GWWXM5/): [elementary substructures](/8WZF9SBP39/), the [diagram lemmas](/EP5E317TNW/) and the [elementary chain theorem](/NHCRZ74JHH/).
- [Types and saturated models](/Z772KEC9BY/): [saturated models](/RMTZ5J64FX/), used in the extension test.
- The [compactness theorem](/1NR3HAWG9D/) of Volume 2.
- Some algebra: [algebraically closed fields](/0PF6TM8TWT/), [ordered fields](/0P3VCBDEE2/) and real closed fields, and abelian groups.
- The [theory of dense linear orders](/2W4S2H4VYA/) and [Fraïssé limits](/HJVRBDQSGG/) from Chapters 4.6 and 4.7 give more examples, but are not needed.
