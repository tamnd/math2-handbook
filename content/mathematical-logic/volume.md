Mathematical logic studies the reasoning of mathematics with the methods of mathematics. Its objects are [formal languages](/5MFZ4VNY6D/), the [formal systems](/439M8B4DY2/) that derive formulas of these languages, and the [structures](/983GZBQYT4/) in which the formulas are true or false. It asks what can be expressed in a language, what can be proved in a system, and how proof and truth are related. Logic is a branch of mathematics with its own theorems and open problems, and it is also a [foundation](/EFFRJFW67Y/): it gives exact meaning to "statement", "proof" and "theorem".

Logic shows up well beyond its own field. SAT solvers decide large instances of the [Boolean satisfiability problem](/3QKF32ZAKN/), the first problem shown to be NP-complete. Hardware and software are verified by [model checking](/VNY0VXVZ53/) in [modal](/C3RZY20ETK/) and temporal logics. The [Curry–Howard correspondence](/A77FER1Q5H/) identifies proofs with programs and underlies [proof assistants](/YM6PRDE88V/). This volume holds proof theory and the logics themselves; model theory, set theory and computability theory have volumes of their own.

## What the volume teaches

- **Syntax and semantics are separate.** A formula is a string built by rules; its truth is defined in a structure by [satisfaction](/2RBQPV02AS/). Keeping the two apart, and the [object language apart from the metalanguage](/D9G8M42GKC/), is the first lesson.
- **Proof matches truth in first-order logic.** [Gödel's completeness theorem](/WQ1ZE255SF/) says that a sentence is provable exactly when it is true in every model, and the [compactness theorem](/1NR3HAWG9D/) follows.
- **Expressive power has a price.** [Second-order logic](/G6X7SZSNC5/) can characterize the natural numbers up to isomorphism, and it loses completeness and compactness in exchange.
- **Some questions have no algorithm.** [Church's theorem](/VA6BNNY2YC/) shows that first-order validity is undecidable, while [Presburger arithmetic](/4W0E9G7PPV/) is decidable.
- **Formal systems have limits.** The [first](/X9WYNYE29C/) and [second incompleteness theorems](/4PZM5GJTR5/) show that a consistent, computably axiomatized theory with enough arithmetic leaves sentences undecided and does not prove its own consistency. [Tarski's theorem](/YRV6SYK2BY/) shows that arithmetical truth is not definable in arithmetic.
- **There is more than one logic.** Intuitionistic, modal, many-valued and substructural logics change classical logic for definite reasons, and each has its own semantics.

## The chapters

**Chapter 2.1, Logic, formal systems and foundations**, gives the general notions: the [history of logic](/WP3602P9EH/), [Aristotle's syllogistic](/MZBNX2T6Q6/), [formal systems](/439M8B4DY2/), [rules of inference](/QPD3X471Q1/), [consequence relations](/J78Y1M4GND/), [consistency](/VM8TQ70CVJ/), [soundness](/4A84VHDTHV/), [conservative extensions](/N238J43XNE/) and [Hilbert's program](/P1RW6JWX73/).

**Chapter 2.2, Propositions, connectives and quantifiers**, treats the connectives as truth functions, [truth tables](/05RSK4Q657/), [tautologies](/05006AJ7DZ/), [logical equivalence](/0JMR2HM2N2/), the classical laws and rules of inference, and the [quantifiers](/0GHS47PDAQ/) with their [order](/0FYQMKFE77/) and negation.

**Chapter 2.3, The propositional calculus**, studies the logic of connectives as a formal system: [formulas](/TT7WT5HPN9/), [valuations](/H31CS3HK5P/), [normal forms](/0B3D4C8YF2/), [functional completeness](/TDZVCWYJ9F/), the [Hilbert system](/1MGMQX43B8/) and the [deduction theorem](/9X08XK5RV2/), [completeness](/81ZNY1XKYJ/), [compactness](/4X9126SEMM/) and [resolution](/ZDW6N1PGJ7/).

**Chapter 2.4, First-order languages and syntax**, builds [first-order logic](/086QKPF0A6/): [signatures](/WDVVEYD6AT/), [terms](/6D3WA7N2W4/), [formulas](/HYJ10AF6RT/), [free and bound variables](/9CNGDRAMGC/), [substitution](/NCDZ969V7X/), and the [prenex](/CS82V969DE/) and [Skolem](/GCPQGMJYEV/) normal forms.

**Chapter 2.5, Structures, satisfaction and truth**, gives the semantics: [structures](/983GZBQYT4/), [satisfaction](/2RBQPV02AS/), [models](/MVCH6N9SNW/), [validity](/5SDS9T8E7J/), [Herbrand structures](/HKW429DSDK/) and [definable relations](/1DQ1M6ZWS4/).

**Chapter 2.6, Proof systems for first-order logic**, presents the [Hilbert-style calculus](/N95HV0VWSM/), [natural deduction](/6KT3BJZ7D1/), the [sequent calculus](/W72CA3R9MP/), [tableaux](/WGWBBVE8GX/) and [first-order resolution](/DEB3CF4Z2D/), and shows that [they prove the same sentences](/A9AAHN4BMH/).

**Chapter 2.7, Completeness, compactness and interpolation**, joins proof and truth through [Lindenbaum's lemma](/SC0BSJ3GT6/), the [Henkin construction](/RY8KRKR097/) and [Gödel's completeness theorem](/WQ1ZE255SF/), then treats [compactness](/1NR3HAWG9D/), [Herbrand's theorem](/VZ21F10WRS/) and [Craig interpolation](/E2CBFNAVZY/).

**Chapter 2.8, Second-order logic and extensions of first-order logic**, covers [second-order logic](/G6X7SZSNC5/) and [Henkin semantics](/KWEJFK5943/), [monadic second-order logic](/3WHQFSHR58/), [Frege's theorem](/J36EHBHF6J/), and logics with [branching](/KMNVEGS34N/) and [generalized quantifiers](/MFV98WTF4G/).

**Chapter 2.9, Decidability of logics and theories**, starts from the [Entscheidungsproblem](/DJNYM72Z4G/) and [Church's theorem](/VA6BNNY2YC/), then maps the decidable cases: [prefix classes](/ZF79MZRQ8V/), the [two-variable](/S7C3C7DJRF/) and [guarded](/Y7YS1C3GAE/) fragments, [Presburger arithmetic](/4W0E9G7PPV/) and the theorems of [Büchi](/YPDXVTH5JR/) and [Rabin](/PXKKP038RG/).

**Chapter 2.10, Formal arithmetic and its fragments**, defines [Robinson arithmetic](/3K1AKGXF8A/) and [Peano arithmetic](/HACXBCM7SS/), the [arithmetical hierarchy of formulas](/GE43CSZTS9/), [representability](/BJF29XET83/) and the weak systems from [primitive recursive arithmetic](/WCXH72T8D8/) to the [fragments of PA](/T70PYM1F36/).

**Chapter 2.11, Gödel's incompleteness theorems and related limits**, proves the [diagonal lemma](/3PRW76471J/), the [first](/X9WYNYE29C/) and [second](/4PZM5GJTR5/) incompleteness theorems, [Rosser's theorem](/DH9RQ61GVD/), [Tarski's theorem](/YRV6SYK2BY/) and [Löb's theorem](/3HD30YG3DG/), and ends with [what the theorems mean](/PT61MFHC13/).

The remaining chapters have no entries yet, and the book prints their openings only.

**Chapter 2.12** treats true statements that Peano arithmetic cannot prove, such as Goodstein's theorem, and fast-growing functions. **Chapter 2.13** studies the structure of proofs: cut elimination, normalization and proof search. **Chapter 2.14** measures theories by ordinals, as Gentzen did for arithmetic with $\varepsilon_0$. **Chapter 2.15** covers proof interpretations such as Gödel's Dialectica interpretation and conservation results. **Chapter 2.16** treats the modal logic of provability. **Chapter 2.17** covers reverse mathematics, which finds the axioms needed for ordinary theorems. **Chapter 2.18** covers weak theories of arithmetic matched with complexity classes. **Chapter 2.19** asks how long propositional proofs must be. **Chapter 2.20** gives the syntax, Kripke semantics and completeness of modal logic. **Chapter 2.21** treats correspondence theory, bisimulation and extended modal logics. **Chapter 2.22** covers temporal, epistemic and deontic logics. **Chapter 2.23** treats intuitionistic logic and the logics between it and classical logic. **Chapter 2.24** covers many-valued and fuzzy logics. **Chapter 2.25** treats logics without some structural rules, such as linear and relevance logic. **Chapter 2.26** covers paraconsistent, free and non-monotonic logics. **Chapter 2.27** studies logics through classes of algebras. **Chapter 2.28** treats theories of truth and the liar paradox.

## How to read this volume

If this is your first course in logic, read these entries in this order: [formal system](/439M8B4DY2/), [truth table](/05RSK4Q657/), [logical equivalence](/0JMR2HM2N2/), [propositional calculus](/09K9MWD2QQ/), [truth valuation](/H31CS3HK5P/), [Hilbert system](/1MGMQX43B8/), [deduction theorem](/9X08XK5RV2/), [completeness for propositional logic](/81ZNY1XKYJ/), [propositional compactness](/4X9126SEMM/), [first-order logic](/086QKPF0A6/), [free and bound variables](/9CNGDRAMGC/), [structure](/983GZBQYT4/), [satisfaction](/2RBQPV02AS/), [natural deduction](/6KT3BJZ7D1/), [Gödel's completeness theorem](/WQ1ZE255SF/), [compactness](/1NR3HAWG9D/), [Peano arithmetic](/HACXBCM7SS/), the [diagonal lemma](/3PRW76471J/) and the [first](/X9WYNYE29C/) and [second](/4PZM5GJTR5/) incompleteness theorems. Do the ◦ and • exercises of Chapters 2.3, 2.6, 2.7 and 2.11.

After that core, choose a line: the limits of formal systems (Chapters 2.9 to 2.12), proof theory (2.13 to 2.19, after the incompleteness theorems), non-classical logics (2.20 to 2.26), or algebra and truth (2.27 and 2.28). Chapter 2.8 can be read at any time after the core.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read and write proofs, as [Volume 1](/SGSVYFDSYK/) teaches. In particular you need [mathematical induction](/0ASJVEFA9J/), [structural induction](/12MQ2NJ29A/) for proofs about formulas, and the language of [statements](/S9MHMRAX88/) and [quantifiers](/EGTZPA6QH3/). Some familiarity with [sets](/0BSJ7RQ9BW/) and [functions](/0EPAT51DXQ/) helps, and the incompleteness theorems use the idea of an algorithm and the [halting problem](/Z7TN2B35B0/). Proofs of completeness for uncountable languages use [Zorn's lemma](/04RXTQA5ZA/).

## The exercises

Each chapter with entries ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely: compute a truth table, find the free variables of a formula, decide whether a structure satisfies a sentence; each takes a few minutes. Exercises marked • ask you to use an idea in a new place, such as deriving a formula in a proof system, building a countermodel or applying compactness; each takes some thought. Exercises marked ★ are harder; some ask for a known theorem in your own words. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
