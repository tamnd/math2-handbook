The statement "every positive real number has a square root" is a sentence about one kind of object, real numbers, and it uses one operation and one relation: $\forall x \, (0 < x \to \exists y \, (y \cdot y = x))$. The statement "every nonempty set of reals that is bounded above has a least upper bound" is different. It quantifies over sets of reals, and no sentence of this kind can say it. [First-order logic](/086QKPF0A6/) is the logic of the first kind of sentence: its variables range over the elements of one domain, and its quantifiers bind only such variables.

This restriction is what gives the logic its theorems. First-order logic has a complete proof system, the compactness theorem and the Löwenheim–Skolem theorem, and [Lindström's theorem](/FYZ3CJGZYV/) says that no stronger logic keeps both compactness and the downward Löwenheim–Skolem property. Groups, rings, orders, graphs, arithmetic and set theory are all written as first-order theories. This chapter builds the language in which they are written. Truth and models come in the next chapter; here everything is a matter of strings and their structure.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Symbols, terms and formulas.** A [signature](/WDVVEYD6AT/) fixes the non-logical symbols and their arities. [Terms](/6D3WA7N2W4/) are built from variables and constants by function symbols, [atomic formulas](/MCZRXR3SVB/) apply relation symbols to terms, and [well-formed formulas](/HYJ10AF6RT/) close the atomic ones under connectives and quantifiers.
2. **Variables, sentences and substitution.** [Free and bound variables](/9CNGDRAMGC/), [sentences](/DKFGQTRYZE/) as the formulas with no free variable, and [substitution](/NCDZ969V7X/) of a term for a variable without capture.
3. **Theories, equality and sorts.** A [first-order theory](/92SWXST1ZM/) is a set of sentences. [Logic with equality](/Q1494G7FBM/) treats $=$ as a logical symbol with axioms of reflexivity and substitution, and [many-sorted logic](/7TDHDN8P96/) reduces to the one-sorted kind.
4. **Normal forms.** [Prenex normal form](/CS82V969DE/) moves all quantifiers to the front; [Skolem normal form](/GCPQGMJYEV/) removes the existential ones at the cost of new function symbols, keeping satisfiability but not equivalence.
5. **Terms that choose and terms that describe.** [Hilbert's epsilon calculus](/TH5ZKCKN3W/) and [definite descriptions](/PD2R4XT79Q/).
6. **The standard languages.** The [signatures](/CG8FE46WJC/) of the common theories, for reference.

## A first reading

For a first reading, take these nine entries in order: [first-order logic](/086QKPF0A6/), [signature](/WDVVEYD6AT/), [term](/6D3WA7N2W4/), [atomic formula](/MCZRXR3SVB/), [well-formed formula](/HYJ10AF6RT/), [free and bound variables](/9CNGDRAMGC/), [sentence](/DKFGQTRYZE/), [substitution](/NCDZ969V7X/) and [first-order logic with equality](/Q1494G7FBM/). They give the whole syntax that the later chapters of the volume use.

Many-sorted logic, the epsilon calculus and definite descriptions can wait. Prenex and Skolem normal forms are needed for Herbrand's theorem and for resolution, so read them before [Herbrand's theorem](/VZ21F10WRS/) or [first-order resolution](/DEB3CF4Z2D/). The list of standard languages is best used for reference: look up a signature when an example needs it.

## Before you start

The chapter assumes [the propositional calculus](/JDK63589SA/): formulas, unique readability, valuations and normal forms. Most of it is reused here with quantifiers added. It also assumes the informal use of [quantifiers](/PM1AYWABA7/), including the [order of quantifiers](/0FYQMKFE77/) and [translation into logical form](/WGZX7GV3PP/), and the vocabulary of [logic, formal systems and foundations](/H8QZY0RZXZ/), above all the split between [object language and metalanguage](/D9G8M42GKC/).

The main proof method is [structural induction](/12MQ2NJ29A/) on terms and on formulas. If you can prove that every propositional formula has as many left as right brackets, you have the skill the chapter needs.
