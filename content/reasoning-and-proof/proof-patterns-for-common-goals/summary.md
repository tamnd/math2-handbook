## What to remember

- **Double inclusion.** $A = B$ holds exactly when $A \subseteq B$ and $B \subseteq A$. Skeleton: "Let $x \in A$. … So $x \in B$." and then the same from $B$ to $A$. A chain of "if and only if" steps proves both at once, but only if every step is reversible.
- **Injective and surjective.** To prove $f \colon A \to B$ injective, assume $f(a) = f(a')$ and derive $a = a'$. To prove it surjective, take $b \in B$, solve $f(a) = b$ in scratch work, and check that the solution lies in $A$. If $g \circ f = \mathrm{id}_A$, then $f$ is injective; if $f \circ g = \mathrm{id}_B$, then $f$ is surjective; a two-sided inverse gives both.
- **Equivalence relations.** Check reflexivity, symmetry and transitivity, each for arbitrary elements. If $x \sim y$ means $h(x) = h(y)$ for a function $h$, all three hold, and the classes are the fibres $h^{-1}(c)$.
- **Two inequalities.** In a partial order, $a \le b$ and $b \le a$ give $a = b$. Choose it when a number has no formula, as for a supremum. For real numbers, if $a \le b + \varepsilon$ for every $\varepsilon > 0$, then $a \le b$.
- **Identities.** Prove $E_1 = E_2$ by a chain $E_1 = F_1 = \dots = E_2$ of justified steps, for arbitrary values in the stated domain. Two polynomials of degree at most $d$ that agree at $d + 1$ distinct points are equal.
- **Epsilon-delta and epsilon over three.** To prove $\lim_{x \to a} f(x) = L$, bound $\abs{f(x) - L} \le C \abs{x - a}$ for $\abs{x - a} < r$ and take $\delta = \min(r, \varepsilon / C)$; $\delta$ may depend on $\varepsilon$ and $a$, never on $x$. To control $f$ through an approximation $g$, fix $g$ close to $f$ at every point first, then pass from $f(x)$ to $g(x)$, $g(y)$ and $f(y)$.
- **Density.** If $f, g \colon X \to \R$ are continuous on a metric space $X$ and agree on a dense subset, then $f = g$.
- **Open-closed and bootstrapping.** In a connected space, a non-empty subset that is open and closed is the whole space. Bootstrapping uses it when a weak bound holds at the start and implies a strictly stronger bound.
- **Proof by algorithm.** Termination: a natural number decreases strictly at each step. Correctness: an invariant holds at the start, each step keeps it, and with the stopping condition it gives the claim.

## Which pattern fits

| Goal | Pattern | First line of the proof |
|---|---|---|
| $A = B$ for sets | double inclusion | "Let $x \in A$." |
| $f$ injective | equal images give equal inputs | "Suppose $f(a) = f(a')$." |
| $f$ surjective | solve for a preimage | "Let $b \in B$." |
| $\sim$ is an equivalence | three checks, or fibres of a function | "Let $x, y, z \in X$." |
| $a = b$ for numbers | two inequalities | "First, $a \le b$." |
| $\lim_{x \to a} f(x) = L$ | scratch work for $\delta$ | "Let $\varepsilon > 0$." |
| $P(x)$ for all $x$ in an interval | open-closed argument | "Let $S = \set{x : P(x)}$." |
| an object exists | algorithm with variant and invariant | "Run the following procedure." |

: The pattern is chosen by the form of the goal; the first line follows from the pattern, and the rest of the proof is the work.

## Common errors

- **One inclusion only.** Showing $A \subseteq B$ and writing $A = B$.
- **Proving the converse of injectivity.** "If $a = a'$, then $f(a) = f(a')$" holds for every function and proves nothing.
- **A preimage outside the domain.** Solving $f(a) = b$ gives a formula for $a$, and it still has to lie in $A$: for $n \mapsto 2n + 1$ on $\Z$, $(b - 1)/2$ is not an integer when $b$ is even.
- **Squaring to prove an identity.** Squaring both sides of the claim can turn a false claim into a true line, as $\sqrt{x^2} = x$ at $x = -1$ shows.
- **A $\delta$ that depends on $x$.** Then no single $\delta$ works for all $x$ near $a$.
- **Choosing $N$ for one point.** An index chosen at the point $c$ does not control $\abs{f(x) - f_N(x)}$ for $x$ near $c$; pointwise convergence is not enough.
- **Symmetric point, symmetric answer.** A problem symmetric in $x$ and $y$ need not have its maximum at $x = y$.
- **A disconnected space.** On $(0, 1) \cup (2, 3)$ a locally constant function can take two values; the open-closed argument needs a connected space.
