Structural proof theory studies formal proofs as finite combinatorial objects: trees of sequents or formulas that can be cut apart, rearranged and reduced. Its questions are about the shape of proofs. Can every proof be put in a normal form? What does a proof in normal form look like? What can be read off from it?

The subject starts with Gerhard Gentzen, who introduced [natural deduction](/6KT3BJZ7D1/) and the [sequent calculus](/W72CA3R9MP/) in 1934 and 1935. His main theorem, the [cut-elimination theorem](/AYRZ98Y0NW/), says that every derivation in the classical sequent calculus LK, and in the intuitionistic calculus LJ, can be turned into one that does not use the cut rule. The cut rule is the formal version of using a lemma, so the theorem says that pure logic never needs lemmas. A cut-free derivation has the *subformula property*: every formula in it is a subformula of a formula in its conclusion, up to the substitution of terms. Short consequences follow. The empty sequent has no cut-free derivation, so LK is consistent; and [Craig interpolation](/E2CBFNAVZY/) and [Herbrand's theorem](/VZ21F10WRS/) have short proofs from a cut-free derivation. The price is length: removing cuts can make a derivation super-exponentially longer.

For natural deduction the counterpart is normalization: a derivation can be reduced until no introduction rule is followed at once by an elimination of the same connective. Through the [Curry–Howard correspondence](/A77FER1Q5H/) a derivation is a typed program, and normalization is the evaluation of the program.

## What the planned pages will cover

The pages will give the cut-elimination theorem with its proof by double induction, normalization for natural deduction, the subformula property and its uses, refined sequent systems in which the structural rules are built into the logical rules, and proof-theoretic semantics, which takes the rules of inference as giving the meaning of the connectives.

## What to read meanwhile

The proof systems themselves are in Chapter 2.6: [natural deduction](/6KT3BJZ7D1/), the [Fitch-style](/2B6XC7XJA8/) form of it, the [sequent calculus](/W72CA3R9MP/), [semantic tableaux](/WGWBBVE8GX/) and the [equivalence of the proof systems](/A9AAHN4BMH/). The general notions of a [rule of inference](/QPD3X471Q1/) and of [logical constants](/2QQ7Q5SKP8/) are in Chapter 2.1. For the wider subject, see [proof theory](/N4EDJNMTEF/) and [proof-theoretic validity](/J2883WWC3M/).
