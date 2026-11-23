## What to remember

- [Mathematical induction](/0ASJVEFA9J/) proves "$P(n)$ for every integer $n \ge n_0$". Prove $P(n_0)$; then fix an arbitrary $n \ge n_0$, assume $P(n)$ and derive $P(n + 1)$. Choose it when case $n + 1$ is built from case $n$ by one small change.
- [Strong induction](/0KMVFSHFGZ/) proves the same form of statement, but the step assumes $P(k)$ for every $k$ with $n_0 \le k < n$ and derives $P(n)$. Choose it when case $n$ splits into cases that may be far below $n$, as in factoring. If the step uses only $P(n - 1), \dots, P(n - r)$, prove $r$ base cases $P(n_0), \dots, P(n_0 + r - 1)$ directly.
- The [well-ordering principle](/01BX15HSRR/): every nonempty subset of $\N$ has a least element. It fails for $\Z$ and for the positive rationals. Over the base properties (B1) to (B4) of $\N$, it is [equivalent](/J2P9FWBP3Q/) to induction and to strong induction.
- A [minimal counterexample](/JGRCNPKNGG/) proof of "$P(n)$ for all $n \ge n_0$": suppose not, let $m$ be the least $n$ with $P(n)$ false, and build from $m$ a failure at some $m'$ with $n_0 \le m' < m$. [Infinite descent](/0EFYCFHYFG/) proves that no object of a kind exists: give each object a size in $\N$ and show that every object yields one of smaller size.
- [Strengthening the hypothesis](/F94KJC2RXP/): when the step for $P$ is stuck, find $Q$ with $Q(n) \Rightarrow P(n)$ for every $n$ and prove $Q$ by induction. A typical $Q$ replaces a fixed bound by a bound that tightens with $n$, or asks for every position where $P$ asked for one.
- [Double induction](/AABX4YPKRR/) proves $P(m, n)$ for all pairs in $\N \times \N$ by induction along a well-order of the pairs: on $m + n$, nested on $m$ then $n$, or lexicographic. The step for $(m, n)$ may use only pairs that come earlier in the chosen order. [Forward-backward induction](/QC9FKGZH1V/) proves $P(n)$ for all $n$ in an infinite set (often the powers of $2$) and then $P(n) \Rightarrow P(n - 1)$ for every $n \ge 2$.
- [Structural induction](/12MQ2NJ29A/) proves $P(x)$ for every $x$ in an [inductively defined](/AM4GQQMZ3C/) set $X$, the smallest set that contains the base elements and is closed under the constructors: one case per base element, and one case per constructor with the hypothesis on its parts. A recursive definition on $X$ is well defined when each element is built in exactly one way.
- [Induction on size](/B2D8PTFNN1/) proves a claim about all objects (graphs, sets, polynomials) by induction on a number attached to them. $P(n)$ must read "every object of size $n$ has the property". The step starts from an arbitrary object of size $n + 1$ and removes something; it does not build up from a special object of size $n$.

## Which form to use

| Form | Statement proved | The step may use | Base cases |
|---|---|---|---|
| Ordinary induction | $P(n)$ for $n \ge n_0$ | $P(n)$ only | $P(n_0)$ |
| Strong induction | $P(n)$ for $n \ge n_0$ | $P(k)$ for all $n_0 \le k < n$ | every case the step cannot reach |
| Minimal counterexample | $P(n)$ for $n \ge n_0$ | a least failure $m$ | none separately; $m = n_0$ is a case of the argument |
| Infinite descent | no object exists | an object of smallest size | none |
| Double induction | $P(m, n)$ for all pairs | pairs earlier in a fixed well-order | the least pairs of that order |
| Structural induction | $P(x)$ for all $x \in X$ | $P$ for the parts of $x$ | one per base element |

: The forms of induction and what each step is allowed to assume

## Common errors

- **No base case.** "$n^2 + n$ is odd" has a valid step and no true case.
- **Too few base cases.** A step from $P(n - 2)$ to $P(n)$ with only $P(0)$ proved covers only the even $n$.
- **A step that fails for small $n$.** In the horses proof the step from $1$ to $2$ uses two groups that share no horse. Test the step at its smallest value of $n$.
- **Building up instead of breaking down.** Adding a vertex to a special graph of size $n$ reaches only some graphs of size $n + 1$.
- **Well-ordering where it fails.** A set of rationals or of all integers need not have a least element.
- **A recursion with an ambiguous build.** A rule on strings where some string is built in two ways can assign it two values.
