A proof system for first-order logic is a set of rules for writing proofs that a machine can check. Each rule looks only at the shape of formulas, never at their meaning. Take the claim that if some $x$ is related by $R$ to every $y$, then every $y$ has some $x$ related to it: $\exists x\, \forall y\, R(x,y) \to \forall y\, \exists x\, R(x,y)$. A mathematician proves it in two lines. A formal proof of the same claim has to say exactly which rule allows each step, and in particular which variables may be generalized and which constants must be new. The rules for the quantifiers are where all the care goes. A step that is harmless in propositional logic, such as moving a hypothesis across the arrow, can fail once free variables are present.

There is not one proof system but several, built for different purposes. Hilbert systems have many axioms and one rule, so theorems *about* proofs are easy to prove. Natural deduction follows the way people argue. The sequent calculus makes the structure of proofs visible, and its cut-elimination theorem is the starting point of proof theory. Tableaux and resolution search for a refutation, and they are the methods that computers use. All of them prove the same sentences. The completeness theorem of the next chapter says that these sentences are exactly the valid ones.

## What the chapter covers

The chapter is in four groups, read in order.

1. **The Hilbert calculus.** The [Hilbert-style predicate calculus](/N95HV0VWSM/) has six groups of axioms and modus ponens. The [generalization theorem](/VKSK35Y52Z/) and the [deduction theorem](/8M9ZFDR4DH/) are its two working tools, and each has a condition on free variables.
2. **Natural deduction and sequents.** [Natural deduction](/6KT3BJZ7D1/) has an introduction and an elimination rule for each symbol, with eigenvariable conditions on ${\forall}\mathrm{I}$ and ${\exists}\mathrm{E}$. [Fitch-style natural deduction](/2B6XC7XJA8/) writes the same proofs as nested boxes. The [sequent calculus](/W72CA3R9MP/) LK works on sequents $\Gamma \Rightarrow \Delta$, and every provable sequent has a proof without the cut rule.
3. **Refutation methods.** [Semantic tableaux](/WGWBBVE8GX/) break a set of sentences into simpler pieces with the $\alpha, \beta, \gamma, \delta$ rules. An open branch of a finished tableau is a [Hintikka set](/RJNDEG07R1/), and every Hintikka set has a model. [First-order resolution](/DEB3CF4Z2D/) refutes a set of clauses with one rule and unification.
4. **One logic, many calculi.** The [equivalence of proof systems](/A9AAHN4BMH/) proves that all these calculi derive the same sentences, and [rules for equality](/Y90Z13AXY8/) adds the symbol $=$ to each of them.

## A first reading

For a first reading, take these entries in order: [Hilbert-style predicate calculus](/N95HV0VWSM/), [generalization theorem](/VKSK35Y52Z/), [deduction theorem for predicate logic](/8M9ZFDR4DH/), [natural deduction](/6KT3BJZ7D1/), [Fitch-style natural deduction](/2B6XC7XJA8/), [semantic tableaux](/WGWBBVE8GX/), [Hintikka set](/RJNDEG07R1/) and [rules for equality](/Y90Z13AXY8/). Work through the attached examples of each one, especially the examples where a rule is used wrongly: a captured variable, a reused constant, an eigenvariable that escapes. These errors teach the side conditions faster than the rules themselves.

You can leave the sequent calculus, resolution and the equivalence of proof systems for a second pass. The sequent calculus matters most for proof theory, resolution for automated reasoning, and the equivalence proof is easier to follow after the [completeness theorem](/WQ1ZE255SF/) of the next chapter.

## Before you start

You need the syntax of [first-order languages](/PSRDJXRW53/): terms, formulas, free and bound variables, and [substitution](/NCDZ969V7X/) of a term for a variable. You need [structures, satisfaction and truth](/NJDME6F845/), since soundness of every rule is a statement about all structures. The [propositional calculus](/JDK63589SA/) chapter, and the [propositional Hilbert system](/1MGMQX43B8/) in particular, gives the propositional half of each system here. For natural deduction it helps to know the informal [proof strategies by logical form](/872K5XB580/) and the layout of [structured proofs](/H2W8D7BMSW/); the formal rules are those strategies written down exactly.
