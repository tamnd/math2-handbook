## What to remember

- A **statement** is a sentence with exactly one truth value, true or false, even if no one knows which. An **open sentence** such as $x^2 = 4$ has a free variable; it becomes a statement when the variable is given a value or bound by a quantifier. Questions and commands such as "let $x = 3$" are not statements.
- In mathematics **"or" is inclusive**: "$P$ or $Q$" is true when at least one of them is true. "But" means "and", with a hint of contrast.
- The **conditional** "if $P$, then $Q$" is false only when $P$ is true and $Q$ is false. So a conditional with a false hypothesis is true, and a statement about all members of an empty set is [vacuously true](/0V4QXPGJQK/).
- "$P$ only if $Q$", "$Q$ if $P$", "$P$ is sufficient for $Q$" and "$Q$ is [necessary](/09BJQQB3VS/) for $P$" all mean $P \Rightarrow Q$. "$P$ if and only if $Q$" means both directions; see the [biconditional](/0S6GMNJ62Y/).
- **Quantifiers** are often hidden: an identity such as $(a + b)^2 = a^2 + 2ab + b^2$ means "for all $a, b$", and the variable of a definition is universally quantified. The [order of quantifiers](/0FYQMKFE77/) matters: $\forall x \, \exists y$ lets $y$ depend on $x$, and $\exists y \, \forall x$ does not.
- **Negation** follows five rules: $\neg \forall x \, P \equiv \exists x \, \neg P$, $\neg \exists x \, P \equiv \forall x \, \neg P$, $\neg(P \wedge Q) \equiv \neg P \vee \neg Q$, $\neg(P \vee Q) \equiv \neg P \wedge \neg Q$ (the [De Morgan laws](/09PKJKA6J0/)), and $\neg(P \Rightarrow Q) \equiv P \wedge \neg Q$.
- "There is exactly one $x$ with $P(x)$", written with the [uniqueness quantifier](/0QAJHFGZZJ/) $\exists! x \, P(x)$, is proved in two parts: existence, and uniqueness ("if $P(x)$ and $P(y)$, then $x = y$"). The statement $\exists! x \, \exists! y \, P(x, y)$ does not say that exactly one pair satisfies $P$.
- In the Wason task with cards $E$, $K$, $4$, $7$ and the rule "if a card has a vowel on one side, then it has an even number on the other", the cards to turn are $E$ and $7$. Fewer than about $10$ percent of people choose exactly these in the abstract form.

## The forms of a conditional

| Sentence | In symbols | Same meaning as "if $P$, then $Q$"? |
|---|---|---|
| $Q$ if $P$; $P$ only if $Q$ | $P \Rightarrow Q$ | yes |
| $P$ is sufficient for $Q$; $Q$ is necessary for $P$ | $P \Rightarrow Q$ | yes |
| [Contrapositive](/04T1CT7212/): if not $Q$, then not $P$ | $\neg Q \Rightarrow \neg P$ | yes |
| Converse: if $Q$, then $P$ | $Q \Rightarrow P$ | no |
| [Inverse](/VB7B8766D2/): if not $P$, then not $Q$ | $\neg P \Rightarrow \neg Q$ | no; it is the contrapositive of the converse |
| $P$ if and only if $Q$ | $P \Leftrightarrow Q$ | no; it also asserts the converse |
| Negation: $P$ and not $Q$ | $P \wedge \neg Q$ | no; it is true exactly when the conditional is false |

: English forms of a conditional and their relation to $P \Rightarrow Q$. In a definition, "if" is read as "if and only if"; everywhere else it means only $P \Rightarrow Q$.

## Common errors

- **Proving the converse.** To prove "$P$ only if $Q$", assume $P$ and derive $Q$, not the other way round.
- **Negating a conditional as a conditional.** The negation of "if $x > 0$ then $x^2 > x$" is "$x > 0$ and $x^2 \leq x$", not "if $x > 0$ then $x^2 \leq x$".
- **Moving "not" without flipping quantifiers.** "Not every prime is odd" says that some prime is even. It does not say that every prime is even.
- **Swapping quantifiers.** In the definition of a limit, $N$ may depend on $\varepsilon$, so "for every $\varepsilon > 0$ there is $N$" cannot be replaced by "there is $N$ such that for every $\varepsilon > 0$".
- **Writing "any".** "$P(x)$ for any $x$" can mean "for every $x$" or "for some $x$". Write "every" or "some".
- **Reading scope by ear.** "All primes are not even" can mean "no prime is even" (false) or "not all primes are even" (true). Rewrite such a sentence so that only one reading is possible.
