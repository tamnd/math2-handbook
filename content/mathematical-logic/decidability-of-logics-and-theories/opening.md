Given a first-order sentence, is it true in every structure? The [completeness theorem](/WQ1ZE255SF/) says that the valid sentences are exactly the provable ones, so we can list them by listing proofs. But listing is not deciding. If a sentence is not valid, the search for a proof never ends, and no amount of waiting tells us to stop. This chapter is about the line between the questions that a machine can settle and those it cannot, for logics and for theories.

The answers are often sharp. Validity is undecidable as soon as the signature has one binary relation symbol, but it is decidable when every symbol is unary. The theory of $(\N, +)$ is decidable, and so is the theory of $(\N, \cdot)$, but the theory of $(\N, +, \cdot)$ is not. Monadic second-order logic is decidable on words, on infinite words and on the infinite binary tree, and, with edge-set quantifiers, it is decidable on a class of graphs only if the class has bounded treewidth. The methods are a small set: small models, quantifier elimination, automata, and reduction from a known undecidable problem.

## What the chapter covers

The chapter is in six groups, read in order.

1. **The decision problem and its negative answer.** The [Entscheidungsproblem](/DJNYM72Z4G/), what a [decidable theory](/HWC687ES0Q/) is, [Church's theorem](/VA6BNNY2YC/) that validity is undecidable, and [Trakhtenbrot's theorem](/XP6FW2WDWT/) that validity over finite structures is not even computably enumerable.
2. **Decidable fragments of first-order logic.** The [monadic predicate calculus](/SERN6CRVWW/), the [decidable prefix classes](/ZF79MZRQ8V/), [two-variable logic](/S7C3C7DJRF/) and the [guarded fragment](/Y7YS1C3GAE/). Each is decidable because its satisfiable sentences have small or tree-like models.
3. **Decidable arithmetics.** [Presburger arithmetic](/4W0E9G7PPV/) for addition, [Skolem arithmetic](/X86G2FXTPC/) for multiplication, and [Büchi arithmetic](/NSTECGT93D/), where addition and a base-$k$ predicate give exactly the sets that automata recognize.
4. **Monadic second-order logic and automata.** The [Büchi-Elgot-Trakhtenbrot theorem](/AK66XQ59Z3/) on finite words, [Büchi's theorem](/YPDXVTH5JR/) on infinite words and [Rabin's tree theorem](/PXKKP038RG/) on the binary tree.
5. **Graphs of bounded treewidth.** [Courcelle's theorem](/DD4JB8XJ5A/) and its converse in spirit, [Seese's theorem](/RT898AFHWT/).
6. **Transferring undecidability.** [Essential undecidability](/9JDDFN8PT7/), the property that lets one undecidable theory make many others undecidable.

## A first reading

For a first reading, take these nine entries in order: [the Entscheidungsproblem](/DJNYM72Z4G/), [decidable theory](/HWC687ES0Q/), [Church's theorem](/VA6BNNY2YC/), [Trakhtenbrot's theorem](/XP6FW2WDWT/), [the monadic predicate calculus](/SERN6CRVWW/), [Presburger arithmetic](/4W0E9G7PPV/), [the Büchi-Elgot-Trakhtenbrot theorem](/AK66XQ59Z3/), [Büchi's theorem on S1S](/YPDXVTH5JR/) and [essential undecidability](/9JDDFN8PT7/). They give the negative answer, one decidable fragment, one decidable arithmetic, the automata method and the main tool for proving undecidability.

The two-variable and guarded fragments, Skolem and Büchi arithmetic, Rabin's theorem and the two graph theorems can wait. Rabin's theorem in particular rests on tree automata and games, and its proof is the hardest in the chapter.

## Before you start

You need [structures and satisfaction](/NJDME6F845/) and the [completeness and compactness theorems](/FBWW4J1XWG/). From [computability theory](/ZNC3817RA6/) you need [computable and computably enumerable sets](/24YMRP8DF5/), the [halting problem](/Z7TN2B35B0/), and [many-one reductions](/C86MFEQJN8/), since every undecidability result here is a reduction from the halting problem or a relative of it. For the automata groups it helps to know [regular languages](/18WVBDCS38/) and finite automata. The roadmap below lists every entry of the chapter with its kind and level.
