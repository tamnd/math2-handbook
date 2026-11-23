A first-order sentence that is true in every structure has a formal proof. This is Gödel's completeness theorem, and it joins the two sides of logic: truth in all structures, which no one can check directly, and derivability, which a machine can check line by line. One consequence follows at once. A proof uses only finitely many hypotheses, so if a set of sentences has no model, some finite part of it already has none. Turned around, this is the compactness theorem, and it is the main tool of model theory. Add to the sentences true in $\N$ a new constant $c$ and the sentences $c > 0$, $c > 1$, $c > 2$, and so on. Every finite subset has a model, namely $\N$ with $c$ read as a large number, so the whole set has a model. That model satisfies every sentence true in $\N$, yet it has an element larger than every natural number.

The chapter proves these theorems and then refines them. Herbrand's theorem says what a proof of an existential sentence must contain. The interpolation theorems of Craig and Lyndon say that when $\varphi$ implies $\psi$, there is a sentence between them that speaks only of what $\varphi$ and $\psi$ have in common. Along the way the chapter sets out what it means for a theory to be axiomatized by an algorithm, and why "complete" means two different things.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Soundness and completeness.** The [soundness theorem](/AVD7T7J063/) shows that every derivable consequence is a logical consequence. [Lindenbaum's lemma](/SC0BSJ3GT6/) extends a consistent set to a maximal one, the [Henkin construction](/RY8KRKR097/) adds witnesses and builds a model from closed terms, and the [model existence theorem](/G0DTR159RN/) results. [Gödel's completeness theorem](/WQ1ZE255SF/) follows from it.
2. **Compactness.** The [compactness theorem](/1NR3HAWG9D/) and its [applications](/PES0S9XQZ5/): infinite models from large finite ones, nonstandard arithmetic, and properties such as finiteness, torsion, connectedness and well-ordering that no set of first-order sentences can express.
3. **Axiomatizable theories.** A [recursively axiomatizable theory](/3ANXZC3BEG/) has a computably enumerable set of theorems, and [Craig's theorem on axiomatizability](/6AN62NQ8AN/) gives the converse.
4. **Herbrand's theorem and interpolation.** [Herbrand's theorem](/VZ21F10WRS/) reduces validity to a propositional tautology among ground instances. The [Craig interpolation theorem](/E2CBFNAVZY/), its signed form, the [Lyndon interpolation theorem](/BRDT1BT7WW/), and [Robinson's joint consistency theorem](/R6AN38DNBD/) describe how sentences in two vocabularies interact.
5. **Two kinds of completeness.** [Completeness versus incompleteness](/28AX3A4N86/) separates the completeness of a logic from the completeness of a theory.

## A first reading

For a first reading, take these entries in order: [soundness theorem](/AVD7T7J063/), [Lindenbaum's lemma](/SC0BSJ3GT6/), [Henkin construction](/RY8KRKR097/), [model existence theorem](/G0DTR159RN/), [Gödel's completeness theorem](/WQ1ZE255SF/), [compactness theorem](/1NR3HAWG9D/), [applications of first-order compactness](/PES0S9XQZ5/), [recursively axiomatizable theory](/3ANXZC3BEG/) and [completeness versus incompleteness](/28AX3A4N86/). The Henkin construction is the longest proof of the chapter and the one most worth working through in detail; its attached examples show why each step is needed.

Herbrand's theorem, the interpolation theorems and Robinson's theorem can wait for a second pass. They matter most for proof theory, automated reasoning and model theory, and they are easier once compactness is familiar.

## Before you start

You need [first-order languages and syntax](/PSRDJXRW53/) and [structures, satisfaction and truth](/NJDME6F845/), including [logical consequence](/1HK0VYWTV7/). The proofs are carried out for the [Hilbert-style predicate calculus](/N95HV0VWSM/) of the previous chapter, with its [generalization theorem](/VKSK35Y52Z/) and [deduction theorem](/8M9ZFDR4DH/); by the [equivalence of proof systems](/A9AAHN4BMH/) they hold for every calculus there. The propositional versions in [the propositional calculus](/JDK63589SA/), especially [propositional compactness](/4X9126SEMM/), are good warm-ups. For languages of any size you need [Zorn's lemma](/04RXTQA5ZA/). The background chapter on [logic, formal systems and foundations](/H8QZY0RZXZ/) explains why these questions were asked.
