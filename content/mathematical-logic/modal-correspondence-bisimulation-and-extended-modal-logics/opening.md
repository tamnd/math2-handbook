Take a world with one arrow back to itself, and a second model with two worlds that point at each other, with every propositional variable false in both. No modal formula is true at one and false at the other: from every world of both models there is an arrow, and after it the situation looks the same again. A relation between the worlds of two models that matches atomic facts and moves along the arrows in both directions is a [bisimulation](/X27BR4YP2Y/), and modal formulas cannot tell bisimilar worlds apart. First-order logic can: $R x x$ holds in the first model and fails in the second.

A Kripke model is a relational structure, so modal logic can be compared directly with first-order logic. The [standard translation](/YW6YGBMVQY/) turns each modal formula into a first-order formula $\varphi(x)$ with one free variable, by reading $\square\psi$ as $\forall y\,(R x y \to \psi(y))$. Modal logic then becomes a fragment of first-order logic, and Johan van Benthem's theorem says which one: a first-order formula is equivalent to a translation exactly when its truth is preserved by bisimulation. Modal logic shares good properties, such as decidability, with other fragments of first-order logic, including the [two-variable fragment](/S7C3C7DJRF/) and the [guarded fragment](/Y7YS1C3GAE/).

On frames, where every valuation counts, the picture changes. A modal formula then states a second-order condition on the relation. The axiom $\lozenge\square p \to \square\lozenge p$ says that any two successors of a world have a common successor, a first-order property, while Löb's axiom says that the relation is transitive with no infinite ascending chain, which no first-order sentence says. S. K. Thomason and Kit Fine found in 1974 normal modal logics that are complete for no class of frames at all.

Many logics extend the basic language: the [modal $\mu$-calculus](/MZ0M2KR9S0/), introduced by Dexter Kozen in 1983, adds fixed points, dynamic logic adds programs, hybrid logic adds names for worlds, and quantified modal logic adds objects. Topological semantics reads $\square$ as interior, and McKinsey and Tarski proved in 1944 that $\mathsf{S4}$ is the logic of the real line in this sense.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Bisimulation and expressive power.** [Bisimulation](/X27BR4YP2Y/), the [Hennessy–Milner theorem](/DBDNYXA7ME/) on image-finite models, and the [van Benthem characterization theorem](/Y89MGMWE4H/).
2. **Correspondence and definability.** [Modal correspondence theory](/3RYBWYPJVD/), [Sahlqvist's theorem](/S4SSDMETJM/) on first-order correspondents and canonicity, and the [Goldblatt–Thomason theorem](/GX5E3GNRCS/) on modally definable classes of frames.
3. **General frames, incompleteness and the lattice of logics.** [General and descriptive frames](/6W9MEGN982/), [Kripke incompleteness](/W67YJQTT50/), the [McKinsey formula](/4N4ZNWZRE2/) and the [lattice of normal modal logics](/EZ011FT3GT/).
4. **Quantified modal logic.** [Quantified modal logic](/D2H3S12V7X/) with varying domains, and the [Barcan formula](/9PYDNBA5X4/) and its converse.
5. **Fixed points, programs and names.** The [modal $\mu$-calculus](/MZ0M2KR9S0/), [propositional dynamic logic](/VJ78A0Q22R/) and [hybrid logic](/NVPQ9W9DED/).
6. **Topology and intuitionistic logic.** [Topological semantics](/HWJXMBNHQ0/), the [McKinsey–Tarski theorem](/2VF0546VXK/), the [Gödel–McKinsey–Tarski translation](/BXVNEN55MR/) and the [Blok–Esakia theorem](/BB9TA5Q9PN/).
7. **Products and impossible worlds.** [Products of modal logics](/JA2EBWVW8A/) and the [impossible worlds](/8PAJMAN8DM/) of non-normal semantics.

## A first reading

Take bisimulation, the Hennessy–Milner theorem, the van Benthem theorem, correspondence theory and Sahlqvist's theorem first; these are the core of the chapter. Then read Kripke incompleteness, the modal $\mu$-calculus, propositional dynamic logic and the Gödel–McKinsey–Tarski translation, which show the main extensions and the link with intuitionistic logic. The attached examples of the loop and the two-cycle, of confluence for $\lozenge\square p \to \square\lozenge p$, and of reachability as a least fixed point are worth working by hand.

General and descriptive frames, the Goldblatt–Thomason theorem, the lattice of normal modal logics, the Blok–Esakia theorem and products can wait for a second pass: they use duality with modal algebras and ultrafilter extensions. Quantified modal logic, hybrid logic and impossible worlds stand on their own and can be read in any order after the first group.

## Before you start

You need Chapter 2.20 on [syntax, Kripke semantics and completeness](/SKY7AQFG1V/): [modal logic](/C3RZY20ETK/), [Kripke semantics](/NGHWZ9Y7ZV/), [canonical models](/TVE4F04KME/) and [filtration](/6ZZSHAKG5F/). From model theory you need [first-order logic](/086QKPF0A6/) and its [structures](/NJDME6F845/), the [compactness theorem](/1NR3HAWG9D/), [ultraproducts](/AX9Q86GB8M/) and the [Löwenheim–Skolem theorem](/484M0TZ1S7/). The algebraic side uses [algebraic logic](/QYA4H5Y7VR/), and the last groups use [intuitionistic logic](/Q11N8X99FK/) and [Grzegorczyk's logic](/2Q8E4GQF3B/). The links with automata go through [monadic second-order logic](/3WHQFSHR58/), [Rabin's tree theorem](/PXKKP038RG/) and [model checking](/VNY0VXVZ53/).
