1. $\square p$ and $\lozenge p$ are both true exactly at $1$ and $4$, and $\square\lozenge p$ and $\lozenge\square p$ are both true exactly at $2$ and $3$. So $\square\lozenge p \to \lozenge\square p$ is true at every world of the model. It is also valid on the frame. The worlds $2$, $3$ and $4$ have exactly one successor each, so $\square$ and $\lozenge$ agree there; at $1$, $\square\lozenge p$ forces $p$ at $4$, and then $\square p$ holds at $2$.

3. $R_1$ is serial and nothing more, so only $\mathrm{D}$ is valid. $R_2$ is an equivalence relation, so all five are valid. $R_3$ is serial, transitive and Euclidean but neither reflexive nor symmetric, so $\mathrm{D}$, $\mathrm{4}$ and $\mathrm{5}$ are valid and $\mathrm{T}$ and $\mathrm{B}$ are not: it is a frame for $\mathsf{KD45}$.

6. $\lozenge p$ is true at $n$ iff $n \equiv 2$ and $\lozenge\lozenge p$ iff $n \equiv 1 \pmod 3$, so the classes are the three residues mod $3$. The smallest filtration is the cycle $[0] \to [1] \to [2] \to [0]$: three worlds against the bound $2^3 = 8$.

9. In $\mathsf{S4}$ the formula reduces to $\lozenge\square\lozenge p$, and in $\mathsf{S5}$ to $\lozenge p$. Take worlds $a \leq b$ with $p$ true at $a$ only: then $\lozenge p$ is true at $a$, but $\square\lozenge p$ is false at $b$, hence at every world, so $\lozenge\square\lozenge p$ is false at $a$.

13. If $w R v$ and $v$ is not reflexive, make $p$ false at $v$ and true at every other world. For $\mathsf{T}$, apply necessitation to $\mathrm{T}$. For $\mathsf{K4}$, take the transitive frame with two worlds $0 R 1$ and $p$ false everywhere.

16. In $\Lambda$, $\square\varphi \in \Gamma$ iff $\varphi \in \Gamma$, so $\Gamma R^\Lambda \Delta$ gives $\Gamma \subseteq \Delta$, and maximality gives $\Gamma = \Delta$. Each world of the canonical model generates a submodel with one reflexive world, and generated submodels preserve truth.

17. For the largest filtration, take $W = \set{a, b}$, $R = \emptyset$, $V(p) = \set{b}$ and $\Sigma = \set{p, \square p}$. The classes $A = \set{a}$ and $B = \set{b}$ are related by $R^l$ as $A R^l B$ and $B R^l B$, but not $B R^l A$.

19. To refute the formula at $w$ you need an $R_2$-then-$R_1$ path from $w$ to a world $u$ where $p$ is false, while $p$ holds at the end of every $R_1$-then-$R_2$ path from $w$. Make $p$ false only at $u$.

21. $t(p \vee \neg p) = \square p \vee \square\neg\square p$. In the $\mathsf{S4}$-model $a \leq b$ with $p$ true at $b$ only, both disjuncts fail at $a$.

23. For $\mathrm{B}$, chain $p \to \lozenge p$ with $\mathrm{5}$. For $\mathrm{4}$, use the instance $\square p \to \square\lozenge\square p$ of $\mathrm{B}$, the dual form $\lozenge\square p \to \square p$ of $\mathrm{5}$, and monotonicity of $\square$. For $\mathrm{5}$ in $\mathsf{KB4}$, use $\lozenge p \to \square\lozenge\lozenge p$ and the dual $\lozenge\lozenge p \to \lozenge p$ of $\mathrm{4}$.

24. Force a binary tree of depth $n$. At each depth $k < n$ every world has a successor where the fresh variable $p_{k+1}$ is true and one where it is false, and $\square$ carries the values of $p_1, \ldots, p_k$ down to all later worlds. The worlds at depth $n$ then realize all $2^n$ patterns of $p_1, \ldots, p_n$.

25. Truth in $\mathsf{S5}$ reduces to truth in a universal model. Keep the world where $\varphi$ is true and, for each $\square\psi$ false there, one world where $\psi$ is false. Show by induction that every subformula keeps its truth value at the kept worlds. The certificate is the small model.

26. Put $[w] R^t [v]$ iff for every $\square\psi \in \Sigma$, $w \models \square\psi$ implies $v \models \psi \wedge \square\psi$. Transitivity of $R$ gives the condition (min), and transitivity of $R^t$ follows from the definition at once.

27. With $n + 1$ variables, let $\delta_i$ say that $q_i$ is the only one true, and take $\bigvee_{i=1}^{n+1} \neg\lozenge\delta_i$. On a frame with $n$ worlds some $\delta_i$ is true nowhere. For the second part, combine the finite model property with the reduction to universal models.
