[Modal logic](/C3RZY20ETK/) extends propositional logic with an operator $\square$, read "necessarily", and its dual $\lozenge = \neg\square\neg$, read "possibly". Other readings give other subjects: "it is provable that", "it will always be the case that", "the agent knows that". This chapter treats the common core, the syntax of modal formulas, their semantics and the completeness theorems that tie the two together.

The modern subject began with C. I. Lewis, who studied [strict implication](/5JW54NP52K/) in the 1910s, and with the systems S1 to S5 of Lewis and Langford's *Symbolic Logic* of 1932. The systems were given by axioms, and for a long time it was not clear what they meant. Saul Kripke's papers of 1959 and 1963 supplied [Kripke semantics](/NGHWZ9Y7ZV/). A frame is a set of worlds with an [accessibility relation](/XBCYFDPS2F/) $R$, and $\square\varphi$ is true at a world $w$ when $\varphi$ is true at every world that $R$ relates to $w$.

The smallest normal modal logic, $\mathrm{K}$, has the axiom $\square(p \to q) \to (\square p \to \square q)$ and the [rule of necessitation](/G989VP2NGP/), and it is the logic of all frames. The [common modal axioms](/FDFQFWPM4X/) then match properties of $R$. The axiom $\mathrm{T}$, $\square p \to p$, matches reflexivity; $4$, $\square p \to \square\square p$, matches transitivity; and $\mathrm{B}$, $p \to \square\lozenge p$, matches symmetry. So $\mathrm{S4}$ is the logic of reflexive transitive frames and [$\mathrm{S5}$](/VC3A2VWXND/) the logic of frames whose relation is an equivalence.

Completeness is proved with the canonical model. Its worlds are the maximal consistent sets of formulas, obtained by [Lindenbaum's lemma](/SC0BSJ3GT6/) as in the [completeness proof for propositional logic](/81ZNY1XKYJ/). For many logics the canonical frame has the matching property, which gives completeness at once. Filtration collapses a model to a finite one, which proves the finite model property and, with it, decidability.

## What the planned pages will cover

The pages will define the modal language and normal modal logics, set out Kripke models and frames, prove soundness and canonical-model completeness for $\mathrm{K}$, $\mathrm{T}$, $\mathrm{S4}$, $\mathrm{S5}$ and their relatives, and treat filtration, the finite model property, decidability and the complexity of satisfiability.

## What to read meanwhile

The pages [modal logic](/C3RZY20ETK/), [Kripke semantics](/NGHWZ9Y7ZV/), [accessibility relation](/XBCYFDPS2F/), [rule of necessitation](/G989VP2NGP/), [common modal axioms](/FDFQFWPM4X/) and [$\mathrm{S5}$](/VC3A2VWXND/) cover the basics. Read [Lindenbaum's lemma](/SC0BSJ3GT6/) and the [Henkin construction](/RY8KRKR097/) in Chapter 2.7 for the method of the canonical model. The opening of Chapter 2.16 shows a modal logic whose box means provability.
