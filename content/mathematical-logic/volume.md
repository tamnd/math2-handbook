Mathematical logic studies the reasoning of mathematics with the methods of mathematics. Its objects are [formal languages](/5MFZ4VNY6D/), the [formal systems](/439M8B4DY2/) that derive formulas of these languages, and the [structures](/983GZBQYT4/) in which the formulas are true or false. It asks what can be expressed in a language, what can be proved in a system, and how proof and truth are related. It is a branch of mathematics with its own theorems, and also a [foundation](/EFFRJFW67Y/) that gives exact meaning to "statement", "proof" and "theorem".

In computer science, SAT solvers decide large instances of the [Boolean satisfiability problem](/3QKF32ZAKN/), which is NP-complete. Hardware and software are verified by [model checking](/VNY0VXVZ53/) in [modal](/C3RZY20ETK/) and temporal logics. The [Curry–Howard correspondence](/A77FER1Q5H/) identifies proofs with programs and underlies [proof assistants](/YM6PRDE88V/). This volume holds proof theory and the logics themselves; model theory, set theory and computability theory have volumes of their own.

## What the volume teaches

- **Syntax and semantics are separate.** A formula is a string built by rules; its truth in a structure is defined by [satisfaction](/2RBQPV02AS/). Keeping the two apart, and the [object language apart from the metalanguage](/D9G8M42GKC/), is the first lesson.
- **Proof matches truth in first-order logic.** By [Gödel's completeness theorem](/WQ1ZE255SF/) a sentence is provable exactly when it is true in every model, and the [compactness theorem](/1NR3HAWG9D/) follows.
- **Expressive power has a price.** [Second-order logic](/G6X7SZSNC5/) characterizes the natural numbers up to isomorphism and loses completeness and compactness.
- **Some questions have no algorithm.** By [Church's theorem](/VA6BNNY2YC/) first-order validity is undecidable, while [Presburger arithmetic](/4W0E9G7PPV/) is decidable.
- **Formal systems have limits.** By the [first](/X9WYNYE29C/) and [second incompleteness theorems](/4PZM5GJTR5/), a consistent, computably axiomatized theory with enough arithmetic leaves sentences undecided and does not prove its own consistency. By [Tarski's theorem](/YRV6SYK2BY/) arithmetical truth is not definable in arithmetic.
- **Proofs are objects too.** By the [cut-elimination theorem](/AYRZ98Y0NW/) proofs have normal forms, and an ordinal such as [$\varepsilon_0$](/KT50SMH3EC/) measures the strength of a theory.
- **There is more than one logic.** Modal, intuitionistic, many-valued, substructural and paraconsistent logics change classical logic for definite reasons. [Kripke semantics](/NGHWZ9Y7ZV/) serves several of them, and [algebraic logic](/Z3DE4R4RET/) treats each as a class of algebras.
- **Truth needs care.** By the liar paradox, the naive schema $T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ is inconsistent over arithmetic; theories of truth keep parts of it.

## The chapters

**Chapter 2.1, Logic, formal systems and foundations**, gives the general notions: [rules of inference](/QPD3X471Q1/), [consequence relations](/J78Y1M4GND/), [consistency](/VM8TQ70CVJ/), [soundness](/4A84VHDTHV/), [conservative extensions](/N238J43XNE/) and [Hilbert's program](/P1RW6JWX73/).

**Chapter 2.2, Propositions, connectives and quantifiers**, treats the connectives as truth functions, [truth tables](/05RSK4Q657/), [tautologies](/05006AJ7DZ/), [logical equivalence](/0JMR2HM2N2/), and the [quantifiers](/0GHS47PDAQ/) with their [order](/0FYQMKFE77/) and negation.

**Chapter 2.3, The propositional calculus**, studies [formulas](/TT7WT5HPN9/), [valuations](/H31CS3HK5P/), [normal forms](/0B3D4C8YF2/), the [Hilbert system](/1MGMQX43B8/) with the [deduction theorem](/9X08XK5RV2/), [completeness](/81ZNY1XKYJ/), [compactness](/4X9126SEMM/) and [resolution](/ZDW6N1PGJ7/).

**Chapter 2.4, First-order languages and syntax**, builds [first-order logic](/086QKPF0A6/): [signatures](/WDVVEYD6AT/), [terms](/6D3WA7N2W4/), [formulas](/HYJ10AF6RT/), [free and bound variables](/9CNGDRAMGC/), [substitution](/NCDZ969V7X/), and the [prenex](/CS82V969DE/) and [Skolem](/GCPQGMJYEV/) normal forms.

**Chapter 2.5, Structures, satisfaction and truth**, gives the semantics: [structures](/983GZBQYT4/), [models](/MVCH6N9SNW/), [validity](/5SDS9T8E7J/), [Herbrand structures](/HKW429DSDK/) and [definable relations](/1DQ1M6ZWS4/).

**Chapter 2.6, Proof systems for first-order logic**, presents the [Hilbert-style calculus](/N95HV0VWSM/), [natural deduction](/6KT3BJZ7D1/), the [sequent calculus](/W72CA3R9MP/), [tableaux](/WGWBBVE8GX/) and [first-order resolution](/DEB3CF4Z2D/), and shows that [they prove the same sentences](/A9AAHN4BMH/).

**Chapter 2.7, Completeness, compactness and interpolation**, joins proof and truth through [Lindenbaum's lemma](/SC0BSJ3GT6/), the [Henkin construction](/RY8KRKR097/) and the completeness theorem, then treats compactness, [Herbrand's theorem](/VZ21F10WRS/) and [Craig interpolation](/E2CBFNAVZY/).

**Chapter 2.8, Second-order logic and extensions of first-order logic**, covers [Henkin semantics](/KWEJFK5943/), [monadic second-order logic](/3WHQFSHR58/), [Frege's theorem](/J36EHBHF6J/), and [branching](/KMNVEGS34N/) and [generalized quantifiers](/MFV98WTF4G/).

**Chapter 2.9, Decidability of logics and theories**, starts from the [Entscheidungsproblem](/DJNYM72Z4G/) and maps the decidable cases: the [two-variable](/S7C3C7DJRF/) and [guarded](/Y7YS1C3GAE/) fragments, and the theorems of [Büchi](/YPDXVTH5JR/) and [Rabin](/PXKKP038RG/).

**Chapter 2.10, Formal arithmetic and its fragments**, defines [Robinson arithmetic](/3K1AKGXF8A/) and [Peano arithmetic](/HACXBCM7SS/), the [arithmetical hierarchy of formulas](/GE43CSZTS9/), [representability](/BJF29XET83/), [primitive recursive arithmetic](/WCXH72T8D8/) and [fragments of PA](/T70PYM1F36/).

**Chapter 2.11, Gödel's incompleteness theorems and related limits**, proves the [diagonal lemma](/3PRW76471J/), both incompleteness theorems, [Rosser's theorem](/DH9RQ61GVD/), Tarski's theorem and [Löb's theorem](/3HD30YG3DG/), and ends with [what the theorems mean](/PT61MFHC13/).

**Chapter 2.12, Natural independence results and fast-growing functions**, gives true statements about numbers that PA cannot prove, such as [Goodstein's theorem](/XQMNJF241J/) and the [Paris–Harrington theorem](/509ZWA0R26/). Each says that a certain function is total, and it grows faster than every [provably total function](/Z742YPHPNS/) of PA, as the [fast-growing hierarchy](/R6ZC4BJGXV/) measures.

**Chapter 2.13, Structural proof theory**, studies the shape of proofs: the [cut rule](/DAMGTSY6VV/) and its elimination, the [subformula property](/Z2NXKDK06G/), [normalization](/W33WAE1XTC/) of natural deduction, [proof-theoretic semantics](/K97KZB5R7N/) and the [epsilon substitution method](/F5HTHB46SH/).

**Chapter 2.14, Ordinal analysis and ordinal notations**, measures theories by ordinals. Gentzen's [consistency proof](/QPV0HNP22S/) for PA uses induction up to $\varepsilon_0$, the [proof-theoretic ordinal](/C72RBH0CDR/) of PA, and [Veblen functions](/JQFAE9S2F4/) and [collapsing functions](/8S6CT4TMB7/) name the ordinals of stronger theories.

**Chapter 2.15, Proof interpretations and conservation results**, reads computational content off classical proofs: the [double-negation translation](/HGJVM49PA4/), [Friedman's A-translation](/6CCK0TT69P/), Gödel's [Dialectica interpretation](/HZ17ES9PDY/) into [system T](/A4WR995XZP/), and [Parsons's theorem](/2VYJXZZDGB/) that $\mathrm{I}\Sigma_1$ is $\Pi^0_2$-conservative over primitive recursive arithmetic.

**Chapter 2.16, Provability and interpretability logics**, reads $\square\varphi$ as "$\varphi$ is provable in PA". The [logic GL](/WJK0YA4GP2/) is [complete](/1DMFNR7FZT/) for finite transitive irreflexive frames, and by [Solovay's theorem](/1ZRWVDYPX0/) it proves exactly the modal laws of provability in PA. [Interpretability logic](/BGKZTSQN3W/) adds a binary operator.

**Chapter 2.17, Reverse mathematics and subsystems of second-order arithmetic**, asks which axioms a theorem needs. Over [$\mathsf{RCA}_0$](/XQENB067R3/), most ordinary theorems are provable or equivalent to one of four stronger systems, such as [$\mathsf{WKL}_0$](/7W9EG02T79/) and [$\mathsf{ACA}_0$](/NAASTN80QN/); [Ramsey's theorem for pairs](/ZT5KV6KJ3E/) is an exception.

**Chapter 2.18, Bounded arithmetic**, studies theories whose provably total functions are feasible. [Parikh's theorem](/YPQPC1WJMV/) bounds those of $\mathsf{I}\Delta_0$ by polynomials, and [Buss's witnessing theorem](/RH4R7GTTAX/) matches $S^1_2$ with polynomial time.

**Chapter 2.19, Propositional proof complexity**, asks how long proofs of tautologies must be. By the [Cook–Reckhow theorem](/YS1T29B00B/) some proof system has polynomial-size proofs exactly when NP = coNP. [Haken's theorem](/4PCEYEW3JG/) shows that [resolution](/6JSH907W5R/) needs exponential size on the [pigeonhole formulas](/RJ571F7FF0/); for [Frege systems](/J2BAR09TPF/) the question is open.

**Chapter 2.20, Syntax, Kripke semantics and completeness of modal logic**, matches modal axioms with properties of the [accessibility relation](/XBCYFDPS2F/), treats [S4](/N60RVXSA5W/), [S5](/VC3A2VWXND/) and other [normal modal logics](/D1TJYZZDCY/), and proves completeness by the [canonical model](/TVE4F04KME/) and decidability by [filtration](/6ZZSHAKG5F/).

**Chapter 2.21, Modal correspondence, bisimulation and extended modal logics**, compares modal with first-order logic through [bisimulation](/X27BR4YP2Y/), the [van Benthem theorem](/Y89MGMWE4H/) and [Sahlqvist's theorem](/S4SSDMETJM/), and adds the [modal $\mu$-calculus](/MZ0M2KR9S0/) and the [Gödel–McKinsey–Tarski translation](/BXVNEN55MR/) of intuitionistic logic into S4.

**Chapter 2.22, Applied modal logics**, fixes readings of the box: time in [linear temporal logic](/RMJ56ZPA63/) and [computation tree logic](/F6JA5C5BJX/), knowledge in [epistemic logic](/EA34W4ERRE/), and obligation in [deontic logic](/7B74J6J5JV/).

**Chapter 2.23, Intuitionistic and intermediate logics**, treats the logic of constructive proof: [intuitionistic logic](/Q11N8X99FK/), its [Kripke](/5GTQ69W47T/) and [Heyting algebra](/JM1XJXWZYH/) semantics, the [disjunction property](/YTRVX6F3FX/), [Glivenko's theorem](/B9M3P61ZVA/), and the [intermediate logics](/H5NSKEP3P2/) such as [Gödel–Dummett logic](/FA88H7FDPY/).

**Chapter 2.24, Many-valued and fuzzy logics**, adds truth values. [Strong Kleene logic](/SZHA10A9X7/), [Łukasiewicz's three-valued logic](/1CE2TGM6MQ/) and [first-degree entailment](/KXTP4P3GHT/) are finite [logical matrices](/P7E926JK13/). [Łukasiewicz infinite-valued logic](/NFCEM44XYH/) takes values in $[0, 1]$, and fuzzy logics such as [Hájek's BL](/3AQ5GHTXA4/) come from [t-norms](/VR6D8JXX1W/).

**Chapter 2.25, Substructural, linear and relevance logics**, drops or controls [weakening](/VHRXX0T5XT/), [contraction](/V0MZVC2XA9/) and [exchange](/YAFD18WYJ8/), over the [full Lambek calculus](/V5XVVN16GS/). Girard's [linear logic](/2P2184B6HE/) counts formulas as resources and has [proof nets](/HN6WN1VE39/); [relevance logic](/KXTCZ2FY5M/) makes premises share variables with the conclusion and is undecidable by [Urquhart's theorem](/X7F69S7QPX/).

**Chapter 2.26, Paraconsistent, free, non-monotonic and other non-classical logics**, changes one classical assumption at a time. [Paraconsistent logics](/C7YWCR87QJ/) reject [explosion](/TTKZGJEEK7/), and [dialetheism](/3P0FM0AQF3/) accepts some true contradictions. [Free logic](/Y0CNMRXHVJ/) allows terms that denote nothing, and in [default logic](/K4AYFFKY2D/) new premises can remove conclusions.

**Chapter 2.27, Algebraic logic**, studies logics through algebras, starting from the [Lindenbaum–Tarski algebra](/QC9M3Q8B8Q/). Classical logic goes with [Boolean algebras](/KG7730QZMQ/), modal logics with [modal algebras](/3H85NSFWHK/), Łukasiewicz logic with [MV-algebras](/8T4M7RN9AC/) and substructural logics with [residuated lattices](/E337A6WVH3/); [algebraizable logics](/CESWST3NWA/) make this exact.

**Chapter 2.28, Truth and the semantic paradoxes**, starts from the [liar paradox](/KBYY281V8T/). The [Tarskian hierarchy](/Z6MCGB0ZFX/) keeps classical logic, [Kripke's theory of truth](/ES71QTSTNV/) lets the liar lack a value, and the [revision theory](/ZQ4TWM7K6E/) revises classical hypotheses. [Axiomatic theories of truth](/KE8ZX8KVA3/) vary in strength, and [McGee's theorem](/GQW8RQVZJ4/) limits the type-free ones.

## How to read this volume

If this is your first course in logic, read these entries in this order: [formal system](/439M8B4DY2/), [truth table](/05RSK4Q657/), [propositional calculus](/09K9MWD2QQ/), [deduction theorem](/9X08XK5RV2/), [completeness for propositional logic](/81ZNY1XKYJ/), [first-order logic](/086QKPF0A6/), [satisfaction](/2RBQPV02AS/), [natural deduction](/6KT3BJZ7D1/), [Gödel's completeness theorem](/WQ1ZE255SF/), [compactness](/1NR3HAWG9D/), [Peano arithmetic](/HACXBCM7SS/), the [diagonal lemma](/3PRW76471J/) and the [first](/X9WYNYE29C/) and [second](/4PZM5GJTR5/) incompleteness theorems. Do the ◦ and • exercises of Chapters 2.3, 2.6, 2.7 and 2.11.

After the core, the limits of formal systems continue in Chapters 2.9 to 2.12; Chapter 2.8 can be read at any time.

For proof theory, read the [cut-elimination theorem](/AYRZ98Y0NW/) in Chapter 2.13; [ordinal analysis](/C5E5TG8PGP/), [Gentzen's consistency proof](/QPV0HNP22S/) and the [proof-theoretic ordinal](/C72RBH0CDR/) in Chapter 2.14; [Goodstein's theorem](/XQMNJF241J/) in Chapter 2.12; the [Dialectica interpretation](/HZ17ES9PDY/) in Chapter 2.15; and [reverse mathematics](/7SQS69T17R/) in Chapter 2.17. Chapters 2.16, 2.18 and 2.19 can follow in any order; 2.16 also needs the start of Chapter 2.20.

For modal and intuitionistic logic, the propositional core is enough. Read [modal logic](/C3RZY20ETK/), [Kripke semantics](/NGHWZ9Y7ZV/), the [common modal axioms](/FDFQFWPM4X/), the [canonical model](/TVE4F04KME/) and [filtration](/6ZZSHAKG5F/) in Chapter 2.20; [bisimulation](/X27BR4YP2Y/) in Chapter 2.21; then [intuitionistic logic](/Q11N8X99FK/), its [Kripke semantics](/5GTQ69W47T/) and [Glivenko's theorem](/B9M3P61ZVA/) in Chapter 2.23. Chapter 2.22 applies these tools.

For other logics, read [many-valued logic](/DWYCKAKXZD/), [substructural logic](/ZZKTJY5J4T/), [paraconsistent logic](/C7YWCR87QJ/) and the [Lindenbaum–Tarski algebra](/QC9M3Q8B8Q/) in Chapters 2.24 to 2.27. For truth, after Chapter 2.11, read the [liar paradox](/KBYY281V8T/), [Kripke's theory of truth](/ES71QTSTNV/) and the [axiomatic theories of truth](/KE8ZX8KVA3/) in Chapter 2.28.

Each entry stands on its own; its facts box lists what it needs, with the number of the entry that explains it.

## What you need first

You should be able to read and write proofs, as [Volume 1](/SGSVYFDSYK/) teaches, including [mathematical induction](/0ASJVEFA9J/), [structural induction](/12MQ2NJ29A/), the language of [statements](/S9MHMRAX88/) and [quantifiers](/EGTZPA6QH3/), and basic [sets](/0BSJ7RQ9BW/) and [functions](/0EPAT51DXQ/). The incompleteness theorems use the idea of an algorithm and the [halting problem](/Z7TN2B35B0/), and ordinal analysis uses [ordinal numbers](/0YSCSX5YZC/) and [Cantor normal form](/6GD30FGYDZ/).

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ test close reading, such as computing a truth table; those marked • use an idea in a new place, such as building a countermodel; those marked ★ are harder, and some ask for a known theorem in your own words. Many have hints in the appendix *Hints to the exercises*.
