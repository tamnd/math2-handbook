The sentence $\forall x \, \exists y \, (x < y)$ is true in $(\N, <)$ and false in the order $\set{0, 1, 2}$ with its usual $<$, where $2$ has nothing above it. The sentence did not change; the structure did. The previous chapter defined sentences as strings. This chapter says what they mean: a [structure](/983GZBQYT4/) gives a domain and interprets each symbol, and [satisfaction](/2RBQPV02AS/) says, clause by clause, which formulas hold in it.

Everything that follows in the volume rests on this definition. The completeness theorem compares provability with truth in all structures. Model theory studies the classes of structures that satisfy a theory, and decidability asks whether truth in a structure, or in all structures, can be computed. The definition is short, but small details matter: domains are nonempty, functions are total, and a formula with free variables is true or false only once its variables have values.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Structures and satisfaction.** A [structure](/983GZBQYT4/) for a signature, Tarski's definition of [satisfaction](/2RBQPV02AS/) $\mathcal{M} \models \varphi[s]$ under an assignment $s$, and [truth](/K7XDVK5854/) of a sentence, with the theory $\mathrm{Th}(\mathcal{M})$ of a structure.
2. **Models and validity.** A [model](/MVCH6N9SNW/) of a theory and the class $\mathrm{Mod}(T)$ of its models; [validity](/5SDS9T8E7J/), its link with satisfiability and consequence, and why the set of valid sentences is computably enumerable but, in general, not decidable.
3. **Three basic lemmas.** The [coincidence lemma](/FM580NZ9W6/), the [substitution lemma](/A7S460KHBM/) and [isomorphism invariance](/NDTJ2E895C/).
4. **Structures made of terms.** The [Herbrand universe](/NFW38QJ3A7/) of closed terms and [Herbrand structures](/HKW429DSDK/), the bridge to Herbrand's theorem and resolution.
5. **Games, definability and a puzzle.** [Game-theoretic semantics](/D45Z7HETDA/), [definable relations](/1DQ1M6ZWS4/) and the automorphism method, and the [drinker paradox](/8BMQTZZEWB/).

## A first reading

For a first reading, take these eight entries in order: [structure](/983GZBQYT4/), [satisfaction](/2RBQPV02AS/), [truth in a structure](/K7XDVK5854/), [model](/MVCH6N9SNW/), [validity](/5SDS9T8E7J/), [coincidence lemma](/FM580NZ9W6/), [substitution lemma](/A7S460KHBM/) and [isomorphism invariance](/NDTJ2E895C/). These are the definitions and tools that the chapters on proof systems and on completeness use at every step.

The Herbrand entries can wait until you reach [Herbrand's theorem](/VZ21F10WRS/) or [first-order resolution](/DEB3CF4Z2D/). Game-theoretic semantics is an alternative view that you can skip at first, unless you plan to read about [independence-friendly logic](/DPMKT2KRB8/). Definable relations matter most for model theory; the drinker paradox is a short example that can be read at any time.

## Before you start

The chapter assumes the syntax of [first-order languages](/PSRDJXRW53/): signatures, terms, formulas, free variables and substitution. It reuses the semantics of [the propositional calculus](/JDK63589SA/), since the clauses for the connectives are the same as for truth valuations. The arguments are the ordinary ones of [reasoning and proof](/SGSVYFDSYK/), with [structural induction](/12MQ2NJ29A/) on terms and formulas as the main tool.

Some examples use familiar mathematical structures: the orders $(\N, <)$, $(\Z, <)$, $(\Q, <)$ and $(\R, <)$, the [Peano axioms](/0QFT7Z76N5/), [groups](/G5S1M9/) and [graphs](/00C0BR7D7H/). You do not need any of their theory beyond the definitions.
