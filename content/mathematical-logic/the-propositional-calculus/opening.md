Take three statements about a program: if the input is sorted then the search succeeds, if the search succeeds then the output is printed, and the output is not printed. It follows that the input is not sorted, and it follows for a reason that has nothing to do with programs. Write $p$, $q$ and $r$ for the three atomic statements. Then every assignment of true and false to $p$, $q$, $r$ that makes $p \to q$, $q \to r$ and $\neg r$ true also makes $\neg p$ true. The propositional calculus is the study of arguments of this kind, where only the connectives matter.

The subject is small enough to be studied completely. There are finitely many valuations of a formula, so truth can be checked by a table. There is a proof system that derives exactly the tautologies. There are normal forms, a precise answer to the question of which connectives are needed, and a decision method, resolution, that runs inside every modern satisfiability solver. Each of these ideas comes back in [first-order logic](/086QKPF0A6/), where it is harder; here it can be seen whole.

## What the chapter covers

The chapter is in seven groups, read in order.

1. **Formulas and their values.** The [propositional formulas](/TT7WT5HPN9/) are built by an inductive rule. [Unique readability](/6KBJX91N7G/) says that each one is built in only one way, so a [truth valuation](/H31CS3HK5P/) is defined by one clause per connective.
2. **Consequence and satisfiability.** [Logical consequence](/1HK0VYWTV7/) and [satisfiability](/QN7M1JCGT9/) are two sides of one notion: $\Gamma \models \varphi$ exactly when $\Gamma \cup \set{\neg \varphi}$ has no model. [Equisatisfiability](/B37TYWXS74/) is the weaker relation that the translations of later groups preserve.
3. **Normal forms and clauses.** [Conjunctive](/0B3D4C8YF2/) and [disjunctive normal form](/0GVDFAY4KW/), [clauses](/T3SXVH3ZZC/) as sets of literals, and [Horn clauses](/QR92EZDTKF/), whose satisfiability takes linear time.
4. **Which connectives are enough.** [Functional completeness](/TDZVCWYJ9F/) and [Post's theorem](/WGBR7JHBV4/), which decides it by five tests.
5. **The Hilbert system.** The [system L](/1MGMQX43B8/) with three axiom schemas and modus ponens, the [deduction theorem](/9X08XK5RV2/), [Peirce's law](/GMSZ75D5WE/), the [implicational calculus](/ZMVBAY7ZZD/), [single axioms](/644XCQAC8C/) and the [independence of axioms](/729RCBPAM3/).
6. **Soundness, completeness and compactness.** [Soundness](/XD629S54CS/) and [completeness](/81ZNY1XKYJ/) say that L derives exactly the consequences. [Compactness](/4X9126SEMM/) follows, with [applications](/S7SW0CZZ9V/) to colorings, orders and matchings.
7. **Resolution and interpolation.** The [resolution](/ZDW6N1PGJ7/) rule, the [Tseitin transformation](/S367PDDP61/) that feeds it, and [Craig interpolation](/TRS2HY57EG/).

## A first reading

For a first reading, take these ten entries in order: [propositional formula](/TT7WT5HPN9/), [truth valuation](/H31CS3HK5P/), [logical consequence](/1HK0VYWTV7/), [satisfiability](/QN7M1JCGT9/), [conjunctive normal form](/0B3D4C8YF2/), [functional completeness](/TDZVCWYJ9F/), [Hilbert system](/1MGMQX43B8/), [deduction theorem](/9X08XK5RV2/), [completeness](/81ZNY1XKYJ/) and [compactness](/4X9126SEMM/). Together they give the language, the semantics, one proof system and the two main theorems about it.

On a first pass you can skip Post's theorem, single axioms, the independence of axioms and Craig interpolation. Read [unique readability](/6KBJX91N7G/) for its statement and come back to the proof when a definition by recursion on formulas needs it. If your interest is in computation rather than proof theory, go from conjunctive normal form to clauses, Horn clauses, resolution and the Tseitin transformation, and leave the Hilbert system for later.

## Before you start

The chapter assumes the informal logic of [propositions, connectives and quantifiers](/PM1AYWABA7/): [truth tables](/05RSK4Q657/), [tautologies](/05006AJ7DZ/) and [logical equivalence](/0JMR2HM2N2/). It uses the vocabulary of [logic, formal systems and foundations](/H8QZY0RZXZ/), in particular [formal systems](/439M8B4DY2/) and the split between [object language and metalanguage](/D9G8M42GKC/).

Most proofs in the chapter are by [structural induction](/12MQ2NJ29A/) on formulas, so make sure that method is familiar; the general habits of [reasoning and proof](/SGSVYFDSYK/) are enough for the rest. The proof of completeness for uncountably many variables uses [Zorn's lemma](/04RXTQA5ZA/), and one proof of compactness uses [Tychonoff's theorem](/0JTRSJKCFB/). Both can be taken on trust: for a countable set of variables there are direct proofs.
