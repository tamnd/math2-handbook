Write down the axioms of a dense linear order without endpoints. Every countable model of them is a copy of $(\Q, <)$, by Cantor's theorem, so the axioms describe one countable structure up to isomorphism. They do not describe one structure of size $2^{\aleph_0}$: the orders $\R$ and $\R + \Q$ both satisfy them, and only the first has least upper bounds. The algebraically closed fields of characteristic $0$ behave the other way round. Two such fields of the same uncountable size are isomorphic, because both have transcendence degree equal to their size, while the countable ones are $\overline{\Q}$, $\overline{\Q(t)}$, $\overline{\Q(t_1, t_2)}$ and so on, one for each degree $0, 1, 2, \ldots, \aleph_0$.

A first-order theory with an infinite model has models of every infinite size, by the [Löwenheim–Skolem theorem](/484M0TZ1S7/), so the most it can do is to fix its models of one size. Such a theory is [categorical](/1JJCGNX240/) in that size. The chapter asks which theories are categorical, what categoricity gives, and, for a complete theory in a countable language, how many countable models there are and how they are built. The answers come from the [types](/9V71Q3SD1G/) of Chapter 4.5: the countable models are controlled by which types they realize and which they omit.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Categoricity in a cardinal.** The definition of a [$\kappa$-categorical theory](/1JJCGNX240/), the [Łoś–Vaught test](/ZR7Y5C235P/), which turns categoricity into a proof of completeness, the [theory of dense linear orders](/2W4S2H4VYA/) as the first example, and a table of [standard examples](/20QJANNKP7/) for the four patterns of categoricity.
2. **Atomic and prime models.** An [atomic model](/HSJ4F9J8SM/) realizes only isolated types. A [prime model](/S8W40PYNHX/) embeds elementarily into every model. In a countable language these are the same thing for countable models, and $\overline{\Q}$ and $(\Q, <)$ are the basic examples.
3. **Saturated models and countable categoricity.** A complete theory has a [countable saturated model](/7GN6XF590M/) exactly when it has countably many types. The [Ryll-Nardzewski theorem](/1513J40TKA/) characterizes [$\omega$-categorical theories](/A22K1X8GKD/) by finitely many types in each number of variables, or by an automorphism group with finitely many orbits on $n$-tuples.
4. **The number of countable models.** [Vaught's never-two theorem](/E5W3RRSY5Z/) excludes exactly two countable models, and [Ehrenfeucht's theory](/XT2D23G98S/) has exactly three. [Morley's theorem](/JFG783DEG8/) limits an infinite number to $\aleph_0$, $\aleph_1$ or $2^{\aleph_0}$, and the [Vaught conjecture](/YVBHE2SEE6/), still open, would remove $\aleph_1$ when $\aleph_1 < 2^{\aleph_0}$.
5. **Small theories.** A [small theory](/W6XM5NVNRP/) has countably many types over the empty set. Smallness gives a prime model and a countable saturated model, and a theory that is not small has $2^{\aleph_0}$ countable models.

## A first reading

Take these entries in order.

- [Categorical theory](/1JJCGNX240/), with its two examples: the integer order, categorical in no infinite cardinal, and the vector spaces over $\Q$, categorical in every uncountable one.
- [Łoś–Vaught test](/ZR7Y5C235P/), and why each of its three hypotheses is needed.
- [Theory of dense linear orders](/2W4S2H4VYA/), the model case for everything that follows.
- [Atomic model](/HSJ4F9J8SM/) and [prime model](/S8W40PYNHX/), with the examples $\overline{\Q}$ for $\mathrm{ACF}_0$ and $(\Q, <)$ for dense orders.
- [Ryll-Nardzewski theorem](/1513J40TKA/) and [omega-categorical theory](/A22K1X8GKD/).
- [Vaught's never-two theorem](/E5W3RRSY5Z/) and [Ehrenfeucht's theory](/XT2D23G98S/), read together.
- [Small theory](/W6XM5NVNRP/), with its example of a complete theory that has no prime model.

The [standard examples](/20QJANNKP7/) can be used as a reference table rather than read straight through. The [Vaught conjecture](/YVBHE2SEE6/) and [Morley's theorem on countable models](/JFG783DEG8/) are short, and their proofs use descriptive set theory, so on a first pass read the statements only. The [countable saturated model theorem](/7GN6XF590M/) is needed for the proof of the never-two theorem; read its statement before that proof.

## Before you start

The chapter assumes the following.

- [Complete theories](/655K8Y7VS8/) and [elementary equivalence](/P3B1V182N4/) from Chapter 4.1.
- [Elementary embeddings](/CGH8C8EA9N/), [elementary substructures](/8WZF9SBP39/) and the [Löwenheim–Skolem theorem](/484M0TZ1S7/) from Chapter 4.2.
- The [back-and-forth method](/6F2DB4HTJR/) and [Cantor's isomorphism theorem](/ABN5PTXEHY/) from Chapter 4.4. Most isomorphisms between countable models in this chapter are built this way.
- From Chapter 4.5: [types](/9V71Q3SD1G/), the [Stone space of types](/VDY4PG5WHN/), [isolated types](/A0VNTN725W/), the [omitting types theorem](/7MFGBVDVG9/) and [saturated models](/RMTZ5J64FX/).
- Cardinals and the [compactness theorem](/1NR3HAWG9D/). Some examples use [quantifier elimination](/7FDDXV3JK7/) for algebraically closed fields, which is stated in the entry on [the model theory of algebraically closed fields](/MT8TDVPBXB/).
