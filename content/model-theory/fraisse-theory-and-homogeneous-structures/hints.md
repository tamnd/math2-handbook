2. Eight types: the empty graph, $K_1$, $K_2$, $2K_1$, the path $P_3$, $K_2 \sqcup K_1$, the path $P_4$ and $C_5$. The types $K_2 \sqcup K_1$, $P_4$ and $C_5$ are not in $\operatorname{Age}(C_4)$, whose six types are the empty graph, $K_1$, $K_2$, $2K_1$, $P_3$ and $C_4$. Only $C_4$ is in $\operatorname{Age}(C_4)$ and not in $\operatorname{Age}(C_5)$.

3. There are three: $a < b < c < a'$, $a < c < b < a'$, and the order $a < b < a'$ with $b$ and $c$ identified. The first two are strong. In the third the images of $B$ and $C$ meet in three points.

4. $K_4$, $C_4$ and $2K_2$ are ultrahomogeneous. In $P_4$, map an end vertex to an inner vertex. In $K_{2,3}$, map a vertex of degree $3$ to a vertex of degree $2$. In $K_1 \sqcup K_2$, map the isolated vertex to an end of the edge. Automorphisms preserve degrees, so none of these maps extends.

5. (a) $0$ and $2$, since $5 = 101_2$ and no number up to $10$ has a $1$ in binary position $5$. (b) $m = 4$ and $z = 16 + 2 + 8 = 26$. The smallest such vertex is $10 = 1010_2$.

7. In the path, the self-sufficient subsets are $\emptyset$, the four singletons, the three edges $\set{a, b}$, $\set{b, c}$, $\set{c, d}$, the two paths $\set{a, b, c}$, $\set{b, c, d}$, and the whole path. In $C_4$, only $\emptyset$ and the whole cycle are self-sufficient, since every proper subset has $\delta \ge 1$ and $\delta(C_4) = 0$. Both graphs are in $\mathcal{K}_0$.

14. For non-adjacent $x, y$ and any finite set $W$, the graph on $\set{x, y, z}$ with $z$ joined to both is triangle-free, so the extension property gives such a $z$ outside $W$. A common neighbour of adjacent vertices makes a triangle. The Rado graph has adjacent vertices with a common neighbour. The complement of $G_3$ has a triangle, because $G_3$ contains three independent vertices.

15. $\operatorname{Aut}(\Q, <)$ has $3$ orbits on pairs and $13$ on triples, one for each way to order three labelled points with ties allowed. $\operatorname{Aut}(R)$ has $3$ orbits on pairs and $1 + 3 \cdot 2 + 2^3 = 15$ on triples. By ultrahomogeneity an orbit of $n$ distinct vertices is a labelled graph on $n$ vertices, so there are $2^{n(n-1)/2}$ orbits.

17. Any amalgam is a finite field, and it has only one subfield with $p^2$ elements, so the two copies of $\F_{p^2}$ coincide. The images of $\alpha$ are roots of its minimal polynomial over $\F_p$, which are $\alpha$ and $\alpha^p$, and the Frobenius map sends one to the other.

18. If $H$ were open it would contain the pointwise stabilizer of a finite set; take an integer $n$ larger than that set and the automorphism that is the identity up to $n$ and $x \mapsto n + (x - n)/2$ above $n$. For the index, the cosets of $H$ correspond to the sets $g(\Z)$. For each $\varepsilon \in \set{0, 1}^{\N}$ the set $\set{n \in \Z : n \le 0} \cup \set{n + \varepsilon_n/2 : n \ge 1}$ is such an image, since consecutive gaps are open intervals of $\Q$ and any two such intervals are order isomorphic.

19. A vertex $(a, f)$ is adjacent to $(b, g)$ for each $b \ne a$ and each $g$ with $g(a) = 1 + f(b)$, which leaves $2^{n-2}$ choices of $g$. For $n = 2$, $H$ is two disjoint edges, $e(a) = (a, 1)$ and $e(b) = (b, 0)$, and the automorphism sends $(a, x) \mapsto (b, 1 + x)$ and $(b, x) \mapsto (a, 1 + x)$.

21. There are at most $\sum_{j \le k} \binom{n}{j} 2^j$ pairs $(U, V)$, and each fails with probability at most $(1 - 2^{-k})^{n-k}$, so the expected number of failures tends to $0$. The extension axioms axiomatize the theory of the Rado graph. A single sentence implying them would follow from one $E_k$, and so would hold in a finite graph, but it implies that the model is infinite.

22. Given $f \colon A \to B$ and $g \colon A \to C$, take $D$ with embeddings $u \colon B \to D$ and $v \colon C \to D$ by JEP, and $E$ with $E \to (D)^A_2$. Colour $e \colon A \to E$ red if $e = h f$ for some embedding $h \colon B \to E$. A copy $d$ of $D$ on which the colour is constant contains the red embedding $d u f$, so $d v g$ is red, which gives $h$ with $h f = d v g$.

23. For $A \cap C \subseteq X \subseteq C$, submodularity gives $\delta(A \cup X) + \delta(A \cap C) \le \delta(A) + \delta(X)$, and $\delta(A \cup X) \ge \delta(A)$. For transitivity, compare $\delta(X)$ with $\delta(X \cap B)$ in the same way. Then $A_1 \cap A_2 \le A_2 \le B$.

24. For $X \subseteq D$, the edges of $X$ are those of $X \cap B$ and of $X \cap C$, with those of $X \cap A$ counted twice, so $\delta(X) = \delta(X \cap B) + \delta(X \cap C) - \delta(X \cap A)$. Since $X \cap A \le X \cap B$ by the previous exercise, this is at least $\delta(X \cap C)$.
