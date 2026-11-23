## What to remember

- **[Preservation theorems](/T69D2NS1HP/):** for a construction $\mathsf{C}$ and a class $\Phi$ of sentences, the models of $T$ are closed under $\mathsf{C}$ exactly when $T$ is equivalent to a set of sentences in $\Phi$. Sentences in $\Phi$ survive $\mathsf{C}$ by an induction on formulas; the converse uses compactness.
- **[Łoś–Tarski](/9RN0KYXNT1/):** $\mathrm{Mod}(T)$ is closed under substructures exactly when $T_\forall$ axiomatizes $T$, and closed under extensions exactly when $T_\exists$ does. A sentence preserved by substructures is equivalent to a universal one. The signature matters: groups are a universal class in $\set{\cdot, {}^{-1}, e}$ and not in $\set{\cdot}$.
- **[Chang–Łoś–Suszko](/RK7NK2P75J/):** $\mathrm{Mod}(T)$ is closed under unions of chains, or only of chains indexed by $\N$, exactly when $T_{\forall\exists}$ axiomatizes $T$. Model complete theories are $\forall\exists$-axiomatizable for this reason.
- **[Lyndon](/8DJSRWME2X/):** a sentence is preserved by surjective homomorphisms exactly when it is equivalent to a positive sentence, built from atoms, $\top$ and $\bot$ with $\wedge$, $\vee$, $\forall$, $\exists$. For all homomorphisms the matching class is the existential positive sentences.
- **[Universal classes](/ZSTEZ3PRT9/)** are the classes closed under isomorphisms, substructures and ultraproducts. **[Universal Horn classes](/9A4CYWXPEA/)** are the classes closed under isomorphisms, substructures and reduced products of nonempty families. Their axioms $\forall \bar x \, (\alpha_1 \wedge \cdots \wedge \alpha_n \to \beta)$ and $\forall \bar x \, \neg(\alpha_1 \wedge \cdots \wedge \alpha_n)$ never force a choice between disjuncts.
- **[Horn sentences](/1FF2GRE6VX/)** are, up to equivalence, exactly the sentences preserved under reduced products. Direct products alone do not characterize them.
- **[Beth](/RJBDSA2ETP/):** $P$ is implicitly defined by $T$ exactly when $T \models \forall \bar x \, (P(\bar x) \leftrightarrow \varphi(\bar x))$ for some $\varphi$ without $P$. Padoa's method: two models of $T$ with the same reduct and different $P$ show that $P$ is not definable.
- **Automorphisms:** by [Svenonius's theorem](/JNXY3WRYFY/), $\varphi(\mathcal{M})$ is definable in $\mathcal{M} | L$ without parameters exactly when every automorphism of $\mathcal{N} | L$ fixes $\varphi(\mathcal{N})$ for each elementary extension $\mathcal{N}$ of $\mathcal{M}$. By the [Chang–Makkai theorem](/MFR9Z5PPH4/), in a saturated model of size $\kappa$ a set is definable with parameters exactly when it has at most $\kappa$ automorphic images, and otherwise it has $2^\kappa$.
- **[Pseudo-elementary classes](/YEC1Q3A490/):** reducts of the models of a sentence ($\mathrm{PC}$) or of a theory ($\mathrm{PC}_\Delta$). They are closed under ultraproducts, so the finite sets and the well-orders are not among them. If a class and its complement are both $\mathrm{PC}$, Craig interpolation makes the class basic elementary.

## Constructions and the axioms they match

| Closed under | Axioms | Theorem | Over finite structures |
|---|---|---|---|
| Substructures | universal | [Łoś–Tarski](/9RN0KYXNT1/) | fails |
| Extensions | existential | [Łoś–Tarski](/9RN0KYXNT1/) | fails |
| Unions of chains | $\forall\exists$ | [Chang–Łoś–Suszko](/RK7NK2P75J/) | — |
| Surjective homomorphisms | positive | [Lyndon](/8DJSRWME2X/) | fails |
| All homomorphisms | existential positive | homomorphism preservation | holds |
| Reduced products | Horn | [Keisler and Galvin](/1FF2GRE6VX/) | — |
| Substructures and ultraproducts | universal | [universal classes](/JPGDSW2TAP/) | — |
| Substructures and reduced products | universal Horn | [universal Horn classes](/VCJX55N45K/) | — |

: The preservation theorems of the chapter, for elementary classes. The last column says whether the theorem stays true when only finite structures are allowed; a dash means that the question does not arise or is not treated here.

## Common errors

- **Dropping the hypothesis that the class is elementary.** Well-orders are closed under substructures, and torsion abelian groups under unions of chains, but neither class has first-order axioms at all.
- **Reading the theorem as a statement about given axioms.** The theorems say that some equivalent set of axioms has the form. The field axiom $\forall x \, \exists y \, (x = 0 \lor x y = 1)$ is not universal, but that alone does not show that fields form no universal class; the substructure $\Z \subseteq \Q$ does.
- **Forgetting the signature.** Substructures, homomorphisms and products all depend on it, and so does every answer.
- **Confusing invariance with definability.** In $(\N, <)$ the identity is the only automorphism, yet the even numbers are not definable. Svenonius's theorem needs all elementary extensions, and Chang–Makkai needs a saturated model.
- **Treating a pseudo-elementary class as elementary.** $(\N, <)$ and $(\N, <) + (\Z, <)$ are elementarily equivalent, and only the second is in the class of linear orders that are not well-ordered.
