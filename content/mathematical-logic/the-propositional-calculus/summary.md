## What to remember

- Each [propositional formula](/TT7WT5HPN9/) is a variable, $(\neg \varphi)$, or $(\varphi \circ \psi)$ for a binary connective $\circ$, and by [unique readability](/6KBJX91N7G/) it has exactly one of these forms, with unique parts. So every [valuation](/H31CS3HK5P/) of the variables extends to exactly one valuation of all formulas, and the value of $\varphi$ depends only on the variables that occur in $\varphi$.
- $\Gamma \models \varphi$ means that every valuation that makes all of $\Gamma$ true makes $\varphi$ true. [Logical consequence](/1HK0VYWTV7/) reduces to [satisfiability](/QN7M1JCGT9/): $\Gamma \models \varphi$ if and only if $\Gamma \cup \set{\neg \varphi}$ is unsatisfiable.
- Every formula has an equivalent [CNF](/0B3D4C8YF2/) and an equivalent [DNF](/0GVDFAY4KW/), but the distributive translation can be exponentially long. The [Tseitin transformation](/S367PDDP61/) gives an [equisatisfiable](/B37TYWXS74/) 3-CNF of linear size instead.
- A [Horn clause](/QR92EZDTKF/) has at most one positive literal. A set of Horn clauses is satisfiable if and only if the marking algorithm never marks all the variables of a clause without a positive literal, and a set of definite clauses always has a least model.
- By [Post's theorem](/WGBR7JHBV4/), a set of connectives is [functionally complete](/TDZVCWYJ9F/) if and only if it is not contained in any of the five classes $T_0$, $T_1$, $M$, $S$, $A$: the functions that preserve $0$, that preserve $1$, the monotone, the self-dual and the affine functions.
- The [system L](/1MGMQX43B8/) has the schemas $\varphi \to (\psi \to \varphi)$, $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$, $(\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi)$ and the rule modus ponens. The [deduction theorem](/9X08XK5RV2/) holds: $\Gamma \cup \set{\varphi} \vdash \psi$ if and only if $\Gamma \vdash \varphi \to \psi$.
- [Soundness](/XD629S54CS/) and strong [completeness](/81ZNY1XKYJ/): $\Gamma \vdash \varphi$ if and only if $\Gamma \models \varphi$, for every set $\Gamma$, finite or not.
- [Compactness](/4X9126SEMM/): a set of formulas is satisfiable if and only if each of its finite subsets is. Equivalently, if $\Gamma \models \varphi$, then $\Gamma_0 \models \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.
- [Resolution](/ZDW6N1PGJ7/) is sound and refutation complete: a set of clauses is unsatisfiable if and only if the empty clause $\square$ can be derived from it.

| Set of connectives | Complete | Reason |
|---|---|---|
| $\set{\neg, \land, \lor}$ | yes | every function has a full DNF |
| $\set{\neg, \land}$, $\set{\neg, \lor}$ | yes | De Morgan's laws give the missing connective |
| $\set{\neg, \to}$ | yes | $p \lor q$ is $\neg p \to q$ |
| $\set{\uparrow}$, $\set{\downarrow}$ | yes | each one expresses $\neg$ and $\land$ |
| $\set{\land, \lor}$ | no | every function it expresses is monotone |
| $\set{\to}$ | no | every function it expresses preserves $1$ |
| $\set{\land, \lor, \to, \leftrightarrow}$ | no | every function it expresses preserves $1$ |
| $\set{\neg, \leftrightarrow}$ | no | every function it expresses is affine |

: Some sets of connectives and whether they are functionally complete. Each "no" names one of Post's five classes that contains the whole set. Among the sixteen binary connectives, only $\uparrow$ and $\downarrow$ are complete alone.

## Common errors

- Confusing $\models$ with $\to$. The first is a relation in the metalanguage between a set and a formula; the second is a connective inside formulas. They are linked by the semantic deduction theorem, $\Gamma \cup \set{\varphi} \models \psi$ if and only if $\Gamma \models \varphi \to \psi$.
- Treating equisatisfiable formulas as equivalent. The Tseitin form of $\varphi$ has the same satisfiability as $\varphi$, but it has new variables and is not equivalent to it, and the negation of an equisatisfiable formula need not be equisatisfiable.
- Resolving on two variables at once. Two clauses that clash on two variables give a tautology as their only resolvents, and cutting both literals at once is not sound.
- Forgetting that modus ponens is the only rule of L. Substitution happens in the schemas, and the deduction theorem is a fact about derivations, not a rule.
- Using compactness for sets that are not finite. The applications need each constraint to involve finitely many variables; an infinite family of sets with Hall's condition can fail to have a system of distinct representatives when one of the sets is infinite.
