1. ◦ With the symbol codes of [Gödel numbering](/MFJXPAF0R0/) ($=$ is $7$, $0$ is $13$, $S$ is $15$, $v_i$ is $21 + 2i$) and the code $2^{c_1} 3^{c_2} \cdots$ of a string, compute the codes of the term $S0$ and of the formula $v_0 = v_0$. Which string has code $2^{15} \cdot 3^{15} \cdot 5^{13}$? Is $2^{13} \cdot 5^{13}$ the code of a string?

2. ◦ Let $T$ have a decidable set of axioms. Is the relation $\mathrm{Prf}_T(y, x)$ decidable? In which of the classes $\Delta_0$, $\Sigma_1$, $\Pi_1$ are the formulas $\mathrm{Prov}_T(x)$, $\mathrm{Con}(T)$ and $\neg \mathrm{Prov}_T(\ulcorner G \urcorner)$, as built in the [provability predicate](/NB2BCZR40F/) entry?

3. ◦ Which of these theories satisfy the hypotheses of [Rosser's theorem](/DH9RQ61GVD/), and so are incomplete? (a) $\mathsf{PA}$; (b) true arithmetic; (c) Presburger arithmetic; (d) $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$; (e) the theory of all sentences.

4. ◦ Let $G$ be a Gödel sentence of $\mathsf{PA}$, so $\mathsf{PA} \vdash G \leftrightarrow \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner G \urcorner)$. Is $G$ true in $\N$? Is it equivalent in $\mathsf{PA}$ to a $\Pi_1$ sentence? Does $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ prove $\neg G$?

5. ◦ Use [Löb's theorem](/3HD30YG3DG/) to show that a consistent $T \supseteq \mathsf{PA}$ does not prove $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner) \to 0 = S0$. Which theorem have you proved again?

6. ◦ The theory $\mathsf{Q} + \exists x\, (0 \cdot x \ne 0)$ is consistent. Is it [$\omega$-consistent](/4S29X1GTV4/)? Say which sentences witness your answer.

7. ◦ By the entry on [partial truth predicates](/Y2MF1EZAM7/), which of these exist? (a) a $\Sigma_2$ formula that is a truth predicate for $\Sigma_2$ sentences; (b) a $\Pi_2$ formula that is a truth predicate for $\Pi_2$ sentences; (c) a $\Sigma_3$ formula that is a truth predicate for $\Pi_3$ sentences; (d) one formula that is a truth predicate for all sentences.

8. ◦ Among the [derivability conditions](/F6H4STF9RG/) D1–D3, which is a rule rather than a sentence that $T$ proves? Which is a case of formalized $\Sigma_1$-completeness? Is "if $T \vdash \mathrm{Prov}_T(\ulcorner\varphi\urcorner)$ then $T \vdash \varphi$" true for $T = \mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA})$?

9. • Let $T \supseteq \mathsf{Q}$ be consistent. Use the [diagonal lemma](/3PRW76471J/) to show that no formula $\mathrm{True}(x)$ has $T \vdash \mathrm{True}(\ulcorner \sigma \urcorner) \leftrightarrow \sigma$ for every sentence $\sigma$.

10. • Show that a consistent, complete theory with a computably enumerable set of axioms is decidable. Combine this with the essential undecidability of $\mathsf{Q}$ to give a proof of the first incompleteness theorem in Rosser's form that uses no self-referential sentence directly.

11. • Show that an $\omega$-consistent extension of $\mathsf{Q}$ proves no false $\Sigma_1$ sentence.

12. • Give a consistent theory $T \supseteq \mathsf{PA}$ with a decidable set of axioms such that $T + \mathrm{Con}(T)$ is inconsistent. Assume $\mathsf{PA}$ is consistent.

13. • Show that any two [Henkin sentences](/SBMQ5QHG9W/) of $\mathsf{PA}$ are equivalent in $\mathsf{PA}$.

14. • Suppose $\mathsf{PA} \vdash \delta \leftrightarrow \neg \square \delta$, where $\square$ is provability in $\mathsf{PA}$. Use D1–D3 to show $\mathsf{PA} \vdash \delta \leftrightarrow \mathrm{Con}(\mathsf{PA})$.

15. • Let $T \supseteq \mathsf{PA}$ be consistent, with a Gödel sentence $G$. Show that $T + \mathrm{Con}(T)$ proves $G$ and is a proper extension of $T$.

16. • Let $T \supseteq \mathsf{PA}$, and let $T \vdash \neg\varphi$. Show that $T + \mathrm{Con}(T)$ proves the [reflection](/NB485KFXKV/) instance $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$.

17. • Show that $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(\mathsf{PA} + \neg\mathrm{Con}(\mathsf{PA}))$. You may use the formalized deduction theorem: $\mathsf{PA} \vdash \square(\neg\psi \to 0 = S0) \leftrightarrow \square \psi$.

18. • Assume $\mathsf{PA}$ is consistent. Show that $\mathsf{Q} \vdash \neg \mathrm{Prf}_{\mathsf{PA}}(\overline n, \ulcorner 0 = S0 \urcorner)$ for every $n$, but $\mathsf{PA} \nvdash \forall y\, \neg \mathrm{Prf}_{\mathsf{PA}}(y, \ulcorner 0 = S0 \urcorner)$.

19. ★ Derive Löb's theorem from the [second incompleteness theorem](/4PZM5GJTR5/): apply the second theorem to $T + \neg\varphi$.

20. ★ The Rosser predicate is $\mathrm{Prov}^R_T(x) := \exists y\, (\mathrm{Prf}_T(y, x) \land \forall z < y\, \neg \mathrm{Prf}_T(z, \mathrm{neg}(x)))$, where $\mathrm{neg}(x)$ is the code of the negation of the formula coded by $x$. Show that every consistent $T \supseteq \mathsf{Q}$ with decidable axioms proves $\neg \mathrm{Prov}^R_T(\ulcorner 0 = S0 \urcorner)$. Why does this not contradict the second incompleteness theorem?

21. ★ Prove the formalized Löb theorem: $\mathsf{PA} \vdash \square(\square\varphi \to \varphi) \to \square\varphi$.

22. ★ Let $T \supseteq \mathsf{Q}$ be consistent with computably enumerable axioms. Show that no computable set of codes contains the codes of all theorems of $T$ and none of the codes of sentences that $T$ refutes. Use a formula that represents the computable set and the diagonal lemma.
