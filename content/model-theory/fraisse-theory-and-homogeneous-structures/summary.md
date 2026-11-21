## What to remember

- **[Age](/5FKW715RGJ/):** $\operatorname{Age}(M)$ is the class of finitely generated structures that embed into $M$. It has the hereditary property (HP) and the [joint embedding property](/59FQ5Q2B8R/) (JEP).
- **[Amalgamation](/XSCSX39GEZ/):** $\mathcal{K}$ has AP when for embeddings $f \colon A \to B$ and $g \colon A \to C$ in $\mathcal{K}$ there are $D \in \mathcal{K}$ and embeddings $f' \colon B \to D$, $g' \colon C \to D$ with $f' f = g' g$. It is strong when the images of $B$ and $C$ meet only in the image of $A$, and free when it is strong and adds no relations between the two sides.
- **[Ultrahomogeneity](/H8VM37SSAX/):** every isomorphism between finitely generated substructures of $M$ extends to an automorphism of $M$. For countable $M$ this is equivalent to the extension property: if $A \subseteq B$ are in $\operatorname{Age}(M)$, every embedding $A \to M$ extends to an embedding $B \to M$.
- **[Fraïssé's theorem](/V5CKNFP3HC/):** a nonempty class of finitely generated structures with countably many isomorphism types, HP, JEP and AP is the age of a countable ultrahomogeneous structure, unique up to isomorphism, its [Fraïssé limit](/HJVRBDQSGG/). Conversely, the age of every countable ultrahomogeneous structure has these properties.
- **The link with theories:** in a finite relational signature, a countably infinite structure is ultrahomogeneous exactly when its theory is [$\aleph_0$-categorical](/A22K1X8GKD/) and has quantifier elimination ([this theorem](/ZRWJZK78MD/)).
- **Graphs:** the [Rado graph](/RMXR0FEF54/) is the limit of all finite graphs, and the [Henson graph](/TZT25G2YB3/) $G_n$ is the limit of the finite $K_n$-free graphs. By the [Lachlan–Woodrow theorem](/F7PA1RVBCG/), a countably infinite ultrahomogeneous graph is a disjoint union $m \cdot K_n$ of equal complete graphs with $mn$ infinite, a Henson graph, the Rado graph, or the complement of one of these.
- **Automorphism groups:** finite graphs have [EPPA](/TA9KGWV9NM/): a graph on $n$ vertices lies in a graph on $n 2^{n-1}$ vertices where every partial isomorphism of the smaller graph extends to an automorphism. EPPA is the key step in the proof that the Rado graph has the [small index property](/RZAF6NVEXC/): every subgroup of its automorphism group of index less than $2^{\aleph_0}$ is open.
- **Ramsey classes:** every member of a [Ramsey class](/8XS8FCTF8T/) is rigid, so the finite graphs are not a Ramsey class but the finite ordered graphs are. For an ordered Fraïssé class, the Ramsey property holds exactly when the automorphism group of the limit is extremely amenable ([KPT](/96Q4P7PZVY/)).
- **[Hrushovski amalgamation](/933BFNKPXF/):** with $\delta(A) = \abs{A} - \abs{E(A)}$, write $A \le B$ when $\delta(A') \ge \delta(A)$ for all $A \subseteq A' \subseteq B$. The finite graphs with $\delta \ge 0$ on all subgraphs amalgamate freely over self-sufficient sets, which gives a generic structure.

## Standard Fraïssé classes

| Class of finite structures | Strong AP | Limit | Ramsey, colouring embeddings |
|---|---|---|---|
| Sets, empty signature | yes, free | countable set | no |
| Linear orders | yes | $(\Q, <)$ | yes |
| Graphs | yes, free | Rado graph | no |
| Ordered graphs | yes | ordered Rado graph | yes |
| $K_n$-free graphs, $n \ge 3$ | yes, free | Henson graph $G_n$ | no |
| Tournaments | yes | random tournament | no |
| Boolean algebras | yes | countable atomless Boolean algebra | no |
| Fields of characteristic $p$ | no | algebraic closure of $\F_p$ | no |

: Some Fraïssé classes and their limits. A class that contains a structure with a nontrivial automorphism is never a Ramsey class in the sense of embeddings; adding a linear order removes the automorphisms.

## Common errors

- **Reading AP of the age as ultrahomogeneity.** The age of $(\Z, <)$ is the class of finite linear orders, which has AP, but $(\Z, <)$ is not ultrahomogeneous. The ultrahomogeneous structure with this age is $\Q$.
- **Confusing the two meanings of homogeneous.** A [homogeneous model](/4NJS7W57VK/) in the sense of types extends maps that preserve complete types, not all isomorphisms of substructures. The two agree for countable relational structures with quantifier elimination.
- **Assuming the amalgam is strong.** In finite fields of characteristic $p$ the copies of $B$ and $C$ may have to overlap in more than $A$, since a finite field has only one subfield of each order.
- **Dropping complements from the graph list.** The complements of $m \cdot K_n$, the complete multipartite graphs such as $K_{\aleph_0, \aleph_0}$, are ultrahomogeneous and belong on the Lachlan–Woodrow list.
- **Amalgamating over any subset in the Hrushovski setting.** The free amalgam over a set that is not self-sufficient can leave the class $\mathcal{K}_0$, so the relation $\le$ is part of the construction.
- **Mixing copies and embeddings.** For a class of rigid structures, colouring copies and colouring embeddings give the same Ramsey property. Otherwise they differ: the finite sets satisfy only the copy version.
