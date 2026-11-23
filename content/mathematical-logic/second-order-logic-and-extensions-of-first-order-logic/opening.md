First-order logic cannot say that a structure is finite. The [compactness theorem](/1NR3HAWG9D/) gives an infinite model to every set of sentences with arbitrarily large finite models, so no first-order sentence, and no set of them, holds in exactly the finite structures. One quantifier over relations is enough to say it. A set $M$ is finite exactly when every injective map from $M$ to itself is onto, and with a variable $F$ for binary relations this becomes a single sentence: for every $F$ that is the graph of an injective function, that function is surjective. In the same way, the induction axiom with a quantifier over all sets, $\forall X\, \big((X(0) \land \forall x\, (X(x) \to X(S(x)))) \to \forall x\, X(x)\big)$, makes the [Peano axioms](/0QFT7Z76N5/) categorical: every model is isomorphic to $\N$.

The gain has a price. A logic that pins down $\N$ up to isomorphism cannot be compact, cannot satisfy the [Löwenheim–Skolem theorem](/484M0TZ1S7/), and by [Gödel's incompleteness theorem](/X9WYNYE29C/) cannot have an effective proof system that proves all its valid sentences. [Lindström's theorem](/FYZ3CJGZYV/) says that this is no accident: first-order logic is the strongest logic with compactness and downward Löwenheim–Skolem. Every extension in this chapter gives up something, and the chapter is a survey of what each one gains and what it loses.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Second-order logic and its two semantics.** [Second-order logic](/G6X7SZSNC5/) with the full semantics, where relation variables range over all relations; the [Henkin semantics](/KWEJFK5943/), where they range over a family fixed by the model; and the [comprehension schema](/5GS6DRJ5SY/), which says which relations a Henkin model must contain.
2. **Higher orders and Frege's arithmetic.** [Higher-order logic](/K40YJX8K1G/) adds relations of relations and so on through the finite types. [Frege's theorem and Hume's principle](/J36EHBHF6J/) derive the Peano axioms in second-order logic from one principle about the numbers of concepts.
3. **Monadic second-order logic.** [Monadic second-order logic](/3WHQFSHR58/) quantifies only over sets. On words it defines exactly the regular languages, and on graphs it expresses connectivity, bipartiteness and 3-colorability.
4. **Branching, independence and dependence.** The [branching quantifier](/KMNVEGS34N/), [independence-friendly logic](/DPMKT2KRB8/) and [dependence logic](/DNAPTJ98WD/) change which variables an existential choice may depend on. Each has the power of existential second-order logic.
5. **Generalized and plural quantifiers.** A [generalized quantifier](/MFV98WTF4G/) is any isomorphism-closed class of structures, such as "infinitely many" or "most". [Plural quantification](/DZVEFDYYZX/) reads set variables as "some things" and so avoids sets.

## A first reading

For a first reading, take these entries in order: [second-order logic](/G6X7SZSNC5/), [Henkin semantics](/KWEJFK5943/), [comprehension schema](/5GS6DRJ5SY/), [monadic second-order logic](/3WHQFSHR58/), [branching quantifier](/KMNVEGS34N/), [dependence logic](/DNAPTJ98WD/) and [generalized quantifier](/MFV98WTF4G/). The first entry carries the main contrast of the chapter, between the full semantics, which is strong and badly behaved, and the Henkin semantics, which is first-order logic in disguise. Most later entries return to it: monadic second-order logic is a fragment of it, and the branching quantifier and dependence logic reach exactly its existential part.

Higher-order logic, Frege's theorem, independence-friendly logic and plural quantification can wait for a second pass. Frege's theorem belongs to the philosophy of mathematics as much as to logic, and independence-friendly logic is easier once dependence logic is familiar, since the two have the same power on sentences.

## Before you start

You need [first-order logic](/086QKPF0A6/), with [structures, satisfaction and truth](/NJDME6F845/). The negative results about second-order logic rest on the [completeness theorem](/WQ1ZE255SF/), the compactness theorem and the Löwenheim–Skolem theorem for first-order logic, from the previous chapters, and on the first incompleteness theorem. Some examples use the [power set](/00E0YZCERH/), [Cantor's theorem](/0WTEMGYV2C/) and the [continuum hypothesis](/0MN2MER9WN/) from set theory. For the monadic group, the definition of a [regular language](/18WVBDCS38/) helps, but the entry recalls what it uses.
