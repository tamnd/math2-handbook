## What to remember

- **[Quantifier elimination](/7FDDXV3JK7/):** $T$ has it when every formula $\varphi(\bar x)$ is equivalent modulo $T$ to a quantifier-free $\psi(\bar x)$. Every definable set is then a Boolean combination of atomic sets, and in a signature without constants a consistent theory with quantifier elimination is complete.
- **[Tests](/Q1CGE4DWXQ/):** it suffices to eliminate $\exists y$ in front of a conjunction of literals. Equivalently, whenever $A$ is a finitely generated substructure of $M \models T$, $f \colon A \to N$ is an embedding into an $\omega$-saturated $N \models T$ and $b \in M$, the map $f$ extends to $\langle A, b \rangle$.
- **[Model completeness](/YR6HCMABTE/):** every embedding between models of $T$ is elementary. By [Robinson's test](/QHEADWYQ64/) this holds exactly when $M \subseteq N$ with both models of $T$ implies $M \preceq_1 N$, exactly when every formula is $T$-equivalent to a universal formula, and exactly when every formula is $T$-equivalent to an existential one.
- **[Existentially closed models](/6M98MCW575/):** $M \models T$ is e.c. when every existential formula with parameters in $M$ that holds in some extension $N \supseteq M$ with $N \models T$ already holds in $M$. The e.c. fields are the algebraically closed fields, and the e.c. linear orders are the dense ones without endpoints.
- **[Model companion](/68GG7QKN7C/):** a model complete $T^*$ such that every model of $T$ embeds in a model of $T^*$ and conversely. It is unique when it exists. For an [inductive](/G8TRE2KSRV/) $T$ it exists exactly when the e.c. models form an elementary class, and it is their theory. It is a model completion when $T^* \cup \mathrm{Diag}(M)$ is complete for each $M \models T$. For universal $T$ this holds exactly when $T$ has amalgamation, and exactly when $T^*$ has quantifier elimination.
- **No companion:** the [theory of groups](/5GS2AE651W/) is universal, but in an e.c. group any two elements of the same order are conjugate. Compactness then gives two non-conjugate elements of infinite order, so the e.c. groups are not an elementary class. [Robinson forcing](/2TYY0ZP7YQ/) gives the finite and infinite forcing companions $T^f$ and $T^F$ instead.
- **The algebraic examples:** [ACF](/2NBBJADY5N/) in $\set{+, -, \cdot, 0, 1}$ and [RCF](/FSJ9NGRRPA/) in $\set{+, -, \cdot, 0, 1, <}$ have quantifier elimination. A [cylindrical algebraic decomposition](/GE8FCGKPTR/) adapted to the polynomials of a formula computes the real elimination, in doubly exponential time in the worst case. [$\Z$-groups](/VKC9CR37FT/) need the predicates $D_n$, and [divisible torsion-free abelian groups](/BFK4T1WK38/) need nothing extra.
- **[Relative elimination](/WMC3J66FAY/):** every formula is a Boolean combination of formulas from a chosen set $\Delta$. Plain quantifier elimination is the case where $\Delta$ is the set of atomic formulas.

## Theories and their elimination properties

| Theory | Signature | Quantifier elimination | Model complete | Model companion of |
|---|---|---|---|---|
| [DLO](/2W4S2H4VYA/) | $<$ | yes | yes | linear orders (a completion) |
| [ACF](/2NBBJADY5N/) | $+, -, \cdot, 0, 1$ | yes | yes | fields (a completion) |
| [RCF](/FSJ9NGRRPA/) | $+, -, \cdot, 0, 1, <$ | yes | yes | ordered fields (a completion) |
| [RCF](/G3GGANFA7C/) | $+, -, \cdot, 0, 1$ | no | yes | formally real fields (not a completion) |
| [$\Z$-groups](/VKC9CR37FT/) | $0, 1, +, -, <, D_n$ | yes | yes | — |
| [Divisible torsion-free abelian groups](/BFK4T1WK38/) | $+, -, 0$ | yes | yes | — |
| [$\mathrm{Th}(\Z, +, -, 0)$](/HMXD4AM0Y9/) | $+, -, 0$ | no | no | — |
| [Groups](/5GS2AE651W/) | $\cdot, {}^{-1}, 1$ | no | no | no theory: there is none |

: Some theories of the chapter. Quantifier elimination depends on the signature; model completeness survives the removal of the order from RCF.

## Common errors

- **Forgetting the signature.** The real field has quantifier elimination with $<$ and not without it, since $\exists y \, (x = y \cdot y)$ defines $[0, \infty)$, which no quantifier-free ring formula in $x$ defines.
- **Testing on one model.** Model completeness is about all pairs $M \subseteq N$ of models. The inclusion $2\Z \subseteq \Z$ of groups is not elementary, although both are models of $\mathrm{Th}(\Z, +, -, 0)$.
- **Confusing existentially closed with complete.** Existential closedness is relative to a class. The e.c. models of a theory can have different complete theories, as for groups.
- **Assuming that a companion has quantifier elimination.** RCF in the ring signature is model complete and has no quantifier elimination. For a universal $T$, elimination in the companion corresponds to amalgamation in $T$.
- **Missing the inductive hypothesis.** An e.c. extension is built as the union of a chain, so it needs $T$ to be preserved under unions of chains. The discrete linear orders without endpoints are not.
