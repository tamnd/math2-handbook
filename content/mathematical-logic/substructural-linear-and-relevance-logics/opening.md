In Gentzen's [sequent calculus](/W72CA3R9MP/), besides the rules for the connectives, there are structural rules that manage the assumptions. Weakening lets one add an unused assumption, contraction lets one use an assumption twice, and exchange lets one reorder assumptions. Substructural logics drop or restrict some of these rules. The result is a family of logics in which assumptions behave like resources that must be used, used once, or used in order.

Relevance logic drops weakening. Its motive is that in classical logic $q \to (p \to q)$ is valid even when $p$ has nothing to do with $q$, one of the oddities of [material implication](/0NMG7W7Q11/). Alan Ross Anderson and Nuel Belnap set out the systems $\mathrm{R}$ and $\mathrm{E}$ in *Entailment* (1975), where an implication $\varphi \to \psi$ is a theorem only if $\varphi$ and $\psi$ share a propositional variable. The Routley–Meyer semantics for these logics uses a ternary relation on worlds. The [Lambek calculus](/5FAC9KX4H0/) of 1958, made for the grammar of natural language, drops all three rules, so that the order of words matters.

[Linear logic](/2P2184B6HE/), introduced by Jean-Yves Girard in 1987, drops weakening and contraction but keeps exchange. Each classical connective splits in two: the multiplicative conjunction $\otimes$ uses both of its resources together, while the additive conjunction $\mathbin{\&}$ offers a choice of one. The exponentials $!$ and $?$ mark formulas that may be reused or discarded, so classical and intuitionistic logic can be translated into linear logic. Linear logic has influenced the theory of programming languages, through the [Curry–Howard correspondence](/A77FER1Q5H/), and of concurrency. [Affine logic](/K67C2N2QAH/) keeps weakening but not contraction. The logic of bunched implications combines intuitionistic and linear implication and is the base of separation logic, used to verify programs that manipulate memory.

On the algebraic side, the full Lambek calculus and its extensions correspond to varieties of [residuated lattices](/E337A6WVH3/), which give a uniform semantics for the whole family.

## What the planned pages will cover

The pages will treat the structural rules and what happens when each is dropped, the Lambek calculus, relevance logics and their semantics, linear logic with its proof nets and phase semantics, affine and bunched logics, residuated lattices, and [cut elimination](/AYRZ98Y0NW/) and decidability for these systems.

## What to read meanwhile

Read the [sequent calculus](/W72CA3R9MP/) in Chapter 2.6 and the [cut-elimination theorem](/AYRZ98Y0NW/), then [linear logic](/2P2184B6HE/), the [Lambek calculus](/5FAC9KX4H0/), [affine logic](/K67C2N2QAH/) and [residuated lattices](/E337A6WVH3/). In Chapter 2.1, the [consequence relation](/J78Y1M4GND/) and the [rule of inference](/QPD3X471Q1/) show where structural assumptions enter the definition of a logic.
