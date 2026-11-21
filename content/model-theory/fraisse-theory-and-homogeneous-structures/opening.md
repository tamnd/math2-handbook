Take the natural numbers as vertices, and for $i < j$ join $i$ to $j$ when the $i$-th binary digit of $j$ is $1$. So $0$ is joined to every odd number, and $5 = 101_2$ is joined to $0$ and $2$. Given disjoint finite sets $U$ and $V$ of vertices, the number $z = 2^{m} + \sum_{u \in U} 2^u$, for $m$ larger than every element of $U \cup V$, is joined to every vertex of $U$ and to none of $V$. That is the whole content of the graph: every finite pattern of adjacencies to old vertices is realized by a new one. A [back-and-forth](/6F2DB4HTJR/) argument then shows that any two countable graphs with this property are isomorphic, and that every isomorphism between finite induced subgraphs of the graph extends to an automorphism. The graph is the [Rado graph](/RMXR0FEF54/). It is also what one gets, up to isomorphism and with probability $1$, by tossing a fair coin for each pair of vertices.

The same pattern runs through much of mathematics. The rationals $(\Q, <)$ are the unique countable dense linear order without endpoints, and every order isomorphism between finite subsets extends to an automorphism. The countable atomless Boolean algebra and the algebraic closure of a finite field behave in the same way. Fraïssé's theorem explains all of these at once. A structure of this kind is determined by its age, the class of finitely generated structures that [embed](/SCRB74SWQN/) into it, and the classes that occur as such ages are exactly those that are closed under [substructures](/676H7EGTKJ/), have countably many isomorphism types and the joint embedding property, and let two members be glued along a common part. The structure built from such a class is its Fraïssé limit.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Ages and the three properties.** The [age](/5FKW715RGJ/) of a structure, the [amalgamation property](/XSCSX39GEZ/) and the [joint embedding property](/59FQ5Q2B8R/), with examples showing that each property can fail while the others hold.
2. **Ultrahomogeneity and Fraïssé's theorem.** An [ultrahomogeneous structure](/H8VM37SSAX/) is one in which every isomorphism between finitely generated substructures extends to an automorphism. [Fraïssé's theorem](/V5CKNFP3HC/) matches these structures with their ages, and the [Fraïssé limit](/HJVRBDQSGG/) collects the standard limits.
3. **Homogeneous graphs and their classification.** The [Rado graph](/RMXR0FEF54/), the [Henson graphs](/TZT25G2YB3/) $G_n$, the [Lachlan–Woodrow theorem](/F7PA1RVBCG/) that lists all countable ultrahomogeneous graphs, and the [classifications beyond graphs](/CWKWP7G6HB/) for partial orders, tournaments and directed graphs.
4. **Automorphism groups.** [Hrushovski's extension property for partial automorphisms](/TA9KGWV9NM/) gives finite graphs in which partial isomorphisms of a smaller graph become automorphisms. The [small index property](/RZAF6NVEXC/) says that the topology of an automorphism group is determined by the abstract group.
5. **Ramsey classes and topological dynamics.** The [Kechris–Pestov–Todorcevic correspondence](/96Q4P7PZVY/) links fixed points of actions of an automorphism group on compact spaces to the [Ramsey property](/8XS8FCTF8T/) of its age.
6. **Hrushovski amalgamation.** [Generic structures](/933BFNKPXF/) are built like Fraïssé limits, but amalgamation is allowed only over self-sufficient substructures, measured by a predimension.

## A first reading

A short course takes these entries in order.

- [Age](/5FKW715RGJ/), with its example of the finite linear orders as the age of $\Q$.
- [Amalgamation property](/XSCSX39GEZ/), with the free amalgamation of graphs and the bipartite graphs that fail it.
- [Ultrahomogeneous structure](/H8VM37SSAX/), with the examples of $\Q$ and $\Z$.
- [Fraïssé's theorem](/V5CKNFP3HC/) and its back-and-forth proof. This is the centre of the chapter.
- [Fraïssé limit](/HJVRBDQSGG/), for the list of standard limits.
- [Rado graph](/RMXR0FEF54/), the first limit to know well.
- [Henson graph](/TZT25G2YB3/), for a limit with a forbidden configuration.
- [Lachlan–Woodrow theorem](/F7PA1RVBCG/), read for its statement.

At first the proof of the Lachlan–Woodrow theorem can be skipped, as can the [classifications beyond graphs](/CWKWP7G6HB/). The groups on automorphism groups and Ramsey classes need a little topology and can be read in either order. Hrushovski amalgamation leads to strongly minimal sets and stable theories, and it can wait until those are familiar.

## Before you start

The chapter assumes the following.

- [Structures](/983GZBQYT4/), [substructures](/676H7EGTKJ/) and [embeddings](/SCRB74SWQN/), from the first chapter of the volume.
- The [back-and-forth method](/6F2DB4HTJR/) and [back-and-forth systems](/EWB8KXZMCV/), with the example that [countable graphs with the extension property are isomorphic](/3713A2H6N4/).
- For the link with first-order theories, [$\aleph_0$-categorical theories](/A22K1X8GKD/) and [quantifier elimination](/7FDDXV3JK7/). The theorem that ties them to [ultrahomogeneity](/ZRWJZK78MD/) is in the chapter on countable models.
- For the groups on automorphism groups, [Polish groups](/9C1WSBNQX9/) and the [topology of pointwise convergence](/FVGB8ZP67B/), and for Ramsey classes, [Ramsey's theorem](/00TQV3F5S4/).
