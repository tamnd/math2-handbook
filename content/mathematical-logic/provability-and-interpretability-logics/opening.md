Provability logic is the [modal logic](/C3RZY20ETK/) in which $\square\varphi$ is read as "$\varphi$ is provable in Peano arithmetic". The idea comes straight from Chapter 2.11. The [provability predicate](/NB2BCZR40F/) of $\mathsf{PA}$ obeys the [Hilbert–Bernays–Löb derivability conditions](/F6H4STF9RG/), and in modal notation these are the familiar laws $\square(p \to q) \to (\square p \to \square q)$ and $\square p \to \square\square p$, together with the rule that from $\varphi$ one may infer $\square\varphi$. [Löb's theorem](/3HD30YG3DG/) becomes the axiom
$$\square(\square p \to p) \to \square p .$$
The normal modal logic with this axiom is called $\mathrm{GL}$, after Gödel and Löb.

The central result is Solovay's arithmetical completeness theorem of 1976. A modal formula is a theorem of $\mathrm{GL}$ exactly when $\mathsf{PA}$ proves every arithmetical translation of it, in which the letters become sentences of arithmetic and $\square$ becomes the provability predicate. So $\mathrm{GL}$ captures all the laws of provability that hold whatever sentences the letters stand for, and questions about them become questions about finite Kripke frames, which for $\mathrm{GL}$ are the finite transitive irreflexive ones. [Gödel's second incompleteness theorem](/4PZM5GJTR5/) becomes the modal theorem $\neg\square\bot \to \neg\square\neg\square\bot$. The fixed-point theorem of de Jongh and Sambin is a modal form of the [diagonal lemma](/3PRW76471J/): it solves equations such as $p \leftrightarrow \neg\square p$ inside the logic.

Interpretability logics add a binary operator $\varphi \rhd \psi$, read "$\mathsf{PA} + \psi$ is interpretable in $\mathsf{PA} + \varphi$". The logic $\mathrm{ILM}$ was shown, by Berarducci and by Shavrukov, to be the interpretability logic of $\mathsf{PA}$.

## What the planned pages will cover

The pages will treat $\mathrm{GL}$ and its Kripke semantics, Solovay's theorems, the fixed-point theorem, polymodal provability logics with one operator for each strength of provability, interpretability logics, and the algebraic semantics by diagonalizable algebras.

## What to read meanwhile

Read Chapter 2.11 first: the [provability predicate](/NB2BCZR40F/), the [derivability conditions](/F6H4STF9RG/), [Löb's theorem](/3HD30YG3DG/), the [Henkin sentence](/SBMQ5QHG9W/) and the [reflection principles](/NB485KFXKV/). For the modal side, see [Kripke semantics](/NGHWZ9Y7ZV/) and the opening of Chapter 2.20. The short page [provability logic](/WJK0YA4GP2/) summarizes the subject, and the [relative consistency proof](/X3G0RG2GPZ/) in Chapter 2.1 shows interpretations at work.
