Prove $p \wedge q \Rightarrow q \wedge p$ in Gentzen's [sequent calculus](/W72CA3R9MP/). Start from the axioms $q \Rightarrow q$ and $p \Rightarrow p$, weaken each to $p, q \Rightarrow q$ and $p, q \Rightarrow p$, join them with the right rule for $\wedge$ into $p, q \Rightarrow q \wedge p$, and turn the antecedent into $p \wedge q$ with the left rule. Every formula in this derivation is $p$, $q$, $p \wedge q$ or $q \wedge p$, a part of the end sequent. Now prove instead some lemma $L$ and use it: from $\Rightarrow L$ and $L \Rightarrow C$ the [cut rule](/DAMGTSY6VV/) gives $\Rightarrow C$. The lemma $L$ can be anything. Gentzen's [cut-elimination theorem](/AYRZ98Y0NW/) of 1934 says that in pure logic every lemma can be removed, so every derivable sequent has a derivation built only from its own parts.

Structural proof theory studies formal proofs as finite objects: trees of sequents or formulas that can be cut apart, rearranged and reduced. Its questions are about the shape of proofs: which normal forms exist, what a proof in normal form looks like, and what can be read off from it. A cut-free derivation has the [subformula property](/Z2NXKDK06G/), and short consequences follow. The empty sequent has no cut-free derivation, so the calculus is consistent. [Herbrand's theorem](/VZ21F10WRS/) and [Craig interpolation](/E2CBFNAVZY/) come from the shape of a cut-free proof. The price is length: removing cuts can make a derivation longer by a tower of exponentials.

For [natural deduction](/6KT3BJZ7D1/) the counterpart is [normalization](/W33WAE1XTC/). A derivation is reduced until no introduction rule is followed at once by an elimination of the same connective. Read as a typed program, a derivation is evaluated by this process.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Proofs and the cut rule.** The subject of [proof theory](/N4EDJNMTEF/), the [cut rule](/DAMGTSY6VV/) in its two forms, and the [cut-elimination theorem](/AYRZ98Y0NW/) for LK and LJ.
2. **What cut-free proofs give.** The [subformula property](/Z2NXKDK06G/), the [normalization theorem](/W33WAE1XTC/) for natural deduction, and the [midsequent theorem](/1FPWTGE14W/).
3. **Calculi without structural rules, and the cost of cuts.** The [inversion lemma](/EXMS77F2XN/), Kleene's [contraction-free sequent calculi](/KP5KA51FC4/) G3cp and G3ip with Dyckhoff's LJT, and the [complexity of cut elimination](/B5F5HB4YK7/).
4. **Meaning from rules.** [Proof-theoretic semantics](/K97KZB5R7N/), harmony, and tonk.
5. **Beyond sequents.** The [hypersequent calculus](/3PR9PEMXJ4/) for Gödel-Dummett logic, the [display calculus](/1X7D5CBXB7/) for tense logic, the [labelled sequent calculus](/VW8XP95XCB/) for modal logics, and [deep inference](/4ZW0SHW2RG/).
6. **Proof search and identity.** [Focusing](/AMMKNENT3R/) in linear logic, and the problem of the [identity of proofs](/G7B4XWMS7Q/).
7. **Hilbert's method.** The [epsilon substitution method](/F5HTHB46SH/), the consistency method of the Hilbert school.

## A first reading

For a first reading, take these entries in order: [cut rule](/DAMGTSY6VV/), [cut-elimination theorem](/AYRZ98Y0NW/), [subformula property](/Z2NXKDK06G/), [normalization theorem](/W33WAE1XTC/), [midsequent theorem](/1FPWTGE14W/), [contraction-free sequent calculi](/KP5KA51FC4/), [inversion lemma](/EXMS77F2XN/) and [proof-theoretic semantics](/K97KZB5R7N/). Work through the small derivations in each entry by hand. Backward search in G3cp is a good exercise, because it decides classical propositional logic and needs no ingenuity.

The four formats of the fifth group are independent of one another, so you can read only the one that serves the logic you care about. Deep inference, focusing and the identity of proofs lead into current research and can wait. The epsilon substitution method belongs with the consistency proofs of the next chapter, on [ordinal analysis](/C5E5TG8PGP/).

## Before you start

The proof systems themselves are in Chapter 2.6: the [Hilbert-style calculus](/N95HV0VWSM/), [natural deduction](/6KT3BJZ7D1/) with its [Fitch-style](/2B6XC7XJA8/) form, the [sequent calculus](/W72CA3R9MP/), [semantic tableaux](/WGWBBVE8GX/) and the [equivalence of the proof systems](/A9AAHN4BMH/). The general notions of a [rule of inference](/QPD3X471Q1/) and of [logicality](/2QQ7Q5SKP8/) are in Chapter 2.1, and [prenex normal form](/CS82V969DE/) and the [epsilon calculus](/TH5ZKCKN3W/) are in Chapter 2.4. Herbrand's theorem and Craig interpolation are in Chapter 2.7. Some entries use [intuitionistic logic](/Q11N8X99FK/), Kripke models for modal logic, and the simply typed lambda calculus, at the level of definitions. The epsilon method also needs [Gödel's second incompleteness theorem](/4PZM5GJTR5/) and the ordinal [$\varepsilon_0$](/KT50SMH3EC/).
