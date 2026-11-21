## What to remember

- **Substructure:** a nonempty $N \subseteq M$ carries a substructure of $\mathcal{M}$ exactly when it contains every constant and is closed under every function of $\mathcal{M}$; the relations are restricted to $N$, and the substructure is then unique. Which subsets qualify depends on the signature: $\N$ is a substructure of $(\Z, +, 0)$ but not of $(\Z, +, -, 0)$.
- **Embedding:** an injective map that preserves constants and functions and both preserves and reflects relations, $R^{\mathcal{M}}(\bar a) \iff R^{\mathcal{N}}(h(\bar a))$. Equivalently, an isomorphism onto a substructure. An injective homomorphism of graphs need not be an embedding.
- **Theory and models:** $\operatorname{Th}(\mathcal{M})$ is the set of sentences true in $\mathcal{M}$, and $\operatorname{Mod}(T)$ the class of models of $T$. The theory of one structure is always complete.
- **Elementary equivalence:** $\mathcal{M} \equiv \mathcal{N}$ when $\operatorname{Th}(\mathcal{M}) = \operatorname{Th}(\mathcal{N})$. Isomorphic structures are elementarily equivalent; $(\Q, <) \equiv (\R, <)$ and $\overline{\Q} \equiv \C$ show that the converse fails for infinite structures.
- **Complete theory:** a satisfiable $T$ with $T \models \sigma$ or $T \models \neg\sigma$ for every sentence $\sigma$; equivalently, all models of $T$ are elementarily equivalent. Standard proofs of completeness use the [Łoś–Vaught test](/ZR7Y5C235P/), quantifier elimination or back-and-forth games.
- **Elementary classes:** $\operatorname{Mod}(T)$ for a theory $T$, and basic elementary when $T$ can be one sentence. A theory is finitely axiomatizable exactly when a finite part of any given axiomatization already has the same models, by the [criterion for finite axiomatizability](/9XKWFMVKJD/).
- **Definable sets:** $X \subseteq M^n$ is definable over $A$ when $X = \set{\bar a : \mathcal{M} \models \varphi(\bar a, \bar b)}$ for a formula $\varphi$ and parameters $\bar b$ from $A$. Every automorphism that fixes $A$ pointwise maps $X$ onto $X$. The converse fails: in $(\N, +, \cdot)$ every set is invariant, yet only countably many sets are definable.
- **Limits of first-order logic:** no set of first-order sentences defines the finite structures, the torsion groups, the well-orders, the connected graphs or the Archimedean ordered fields. Each proof applies compactness, usually after adding new constants.

## Some theories and their properties

| Theory | Finitely axiomatizable | Complete | Why not complete |
|---|---|---|---|
| [Groups](/RX9MB386C5/) | yes | no | $\forall x\, \forall y\, (x \cdot y = y \cdot x)$ holds in $\Z$, fails in $S_3$ |
| Linear orders | yes | no | density holds in $\Q$, fails in $\Z$ |
| [Dense linear orders without endpoints](/2W4S2H4VYA/) | yes | yes | |
| [Infinite sets](/KFWXHKBHYT/), empty signature | no | yes | |
| Fields of characteristic $0$ | no | no | $\exists x\, (x \cdot x + 1 = 0)$ holds in $\C$, fails in $\Q$ |
| [Algebraically closed fields](/0PF6TM8TWT/) | no | no | the characteristic is not fixed |
| [Peano arithmetic](/0QFT7Z76N5/) | no | no | [Gödel's first incompleteness theorem](/X9WYNYE29C/) |

: Seven theories. Finite axiomatizability and completeness are independent: dense linear orders have both, infinite sets have only completeness, groups have only finite axiomatizability, and the last three have neither.

## Common errors

- **Forgetting the signature.** "Substructure", "reduct", "definable" and "elementarily equivalent" all depend on the symbols available. The set $\N$ is closed under $+$ but not under $-$; the order is definable in the field $\R$ but not, without parameters, in the group $(\R, +)$, where $x \mapsto -x$ is an automorphism.
- **Confusing $\equiv$ with $\cong$.** Elementary equivalence is weaker than isomorphism for every infinite structure. Two structures of different sizes can be elementarily equivalent; two countable ones can be too, and still not be isomorphic.
- **Reading "complete" as a property of logic.** A complete theory decides every sentence. Gödel's completeness theorem is about first-order logic, not about any one theory.
- **Using an automorphism that moves a parameter.** The automorphism test proves that a set is not definable over $A$ only if the automorphism fixes $A$ pointwise. In $(\Z, <)$ the set $\N$ is not definable without parameters, but it is definable with the parameter $0$.
- **Taking "invariant" for "definable".** A set fixed by all automorphisms need not be definable. Structures with few automorphisms, such as $(\N, +, \cdot)$, have many invariant sets and only countably many definable ones.
- **Mixing up "not elementary" and "not finitely axiomatizable".** The finite sets form no elementary class at all; the infinite sets form one that needs infinitely many axioms.
