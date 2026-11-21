[Provability logic](/WJK0YA4GP2/) is the [modal logic](/C3RZY20ETK/) in which $\square\varphi$ is read as "$\varphi$ is provable in [Peano arithmetic](/HACXBCM7SS/)". The [provability predicate](/NB2BCZR40F/) of $\mathsf{PA}$ obeys the [Hilbert–Bernays–Löb derivability conditions](/F6H4STF9RG/), and in modal notation these are the laws $\square(p \to q) \to (\square p \to \square q)$ and $\square p \to \square\square p$, together with the rule that from $\varphi$ one may infer $\square\varphi$. [Löb's theorem](/3HD30YG3DG/) becomes the axiom
$$\square(\square p \to p) \to \square p .$$
The normal modal logic with this axiom is called $\mathsf{GL}$, after Gödel and Löb.

Many facts about provability become short modal calculations. The formalized form of [Gödel's second incompleteness theorem](/4PZM5GJTR5/) is the instance $\square(\square\bot \to \bot) \to \square\bot$ of Löb's axiom, that is $\square\Diamond\top \to \square\bot$: PA proves that if it proves its own consistency $\Diamond\top$, then it is inconsistent. The formula $\square p \to p$ is not a theorem, because with $p = \bot$ it becomes the consistency statement, which PA does not prove. Nor is $\Diamond\top \to \Diamond\Diamond\top$: the consistency of PA does not imply the consistency of $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, by Gödel's theorem applied to that theory. The question of which modal formulas are laws of provability then has an exact answer. By [Solovay's theorem](/1ZRWVDYPX0/) of 1976, a modal formula is a theorem of $\mathsf{GL}$ exactly when PA proves every arithmetical translation of it, in which the letters become sentences and $\square$ becomes the provability predicate.

On the semantic side, $\mathsf{GL}$ is [complete](/1DMFNR7FZT/) for the finite transitive irreflexive frames, so it is decidable. A countermodel to $\square(p \vee q) \to \square p \vee \square q$ needs only a root and two worlds above it, one where $p$ holds and one where $q$ holds. The [fixed-point theorem](/TDDX1NHG8D/) of de Jongh and Sambin is a modal form of the [diagonal lemma](/3PRW76471J/). It solves equations such as $p \leftrightarrow \neg\square p$ inside the logic, with the unique solution $\neg\square\bot$, so every Gödel sentence of PA is provably equivalent to the consistency statement.

Interpretability logics add a binary operator $\varphi \rhd \psi$, read "$\mathsf{PA} + \psi$ is interpretable in $\mathsf{PA} + \varphi$". The logic $\mathsf{ILM}$ was shown, by Berarducci and by Shavrukov, to be the interpretability logic of $\mathsf{PA}$.

## What the chapter covers

The chapter is in four groups, read in order.

1. **GL and its Kripke semantics.** The [logic GL](/WJK0YA4GP2/), [Löb's axiom](/QQ6PZFGGB3/) with its frame condition and its proof of axiom 4, and the [completeness of GL](/1DMFNR7FZT/) for finite transitive irreflexive frames.
2. **Arithmetical completeness and fixed points.** [Solovay's theorems](/1ZRWVDYPX0/) for provability in PA and for truth, and the [de Jongh–Sambin fixed-point theorem](/TDDX1NHG8D/).
3. **Grz and GLP.** The [Grzegorczyk logic](/2Q8E4GQF3B/) of "true and provable" and [Japaridze's polymodal logic](/3EDRQJJHMT/) with one box for each level of provability.
4. **Algebras, interpretability and quantifiers.** [Magari algebras](/PHWAN904PT/), the algebraic models of $\mathsf{GL}$; [interpretability logic](/BGKZTSQN3W/) with Veltman semantics; and [quantified provability logic](/5K9J8R8SCP/), which is $\Pi^0_2$-complete.

## A first reading

For a first reading, take [provability logic](/WJK0YA4GP2/), [Löb's axiom in provability logic](/QQ6PZFGGB3/), [Kripke completeness of GL](/1DMFNR7FZT/), [Solovay's theorem](/1ZRWVDYPX0/), the [fixed-point theorem](/TDDX1NHG8D/) and [interpretability logic](/BGKZTSQN3W/). The completeness theorem and the fixed-point theorem can be read as statements first; their proofs use the finite frames in a direct way and are worth a second pass.

[Japaridze's logic GLP](/3EDRQJJHMT/) and [quantified provability logic](/5K9J8R8SCP/) can wait. GLP needs some ease with the reflection principles, and its proof-theoretic use goes beyond this chapter. The [Grzegorczyk logic](/2Q8E4GQF3B/) and [Magari algebras](/PHWAN904PT/) are short and can be read at any point after the first group.

## Before you start

You need the chapter on [Gödel's incompleteness theorems and related limits](/HXHHWY3328/): the [provability predicate](/NB2BCZR40F/), the [derivability conditions](/F6H4STF9RG/), [Löb's theorem](/3HD30YG3DG/), the [Henkin sentence](/SBMQ5QHG9W/) and the [reflection principles](/NB485KFXKV/). From the chapter on [formal arithmetic and its fragments](/QHCRN4JVG0/) you need PA and its $\Sigma_1$-completeness. For the modal side, the chapter on [syntax, Kripke semantics and completeness of modal logic](/SKY7AQFG1V/) gives [Kripke semantics](/NGHWZ9Y7ZV/) and the canonical model. The [relative consistency proof](/X3G0RG2GPZ/) shows interpretations at work before interpretability logic.
