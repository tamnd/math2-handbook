1. (a) A true proposition: $17 = 16 + 1$. (b) Not a proposition but a predicate: its value depends on $x$. (c) A question, so not a proposition. (d) Not a proposition: either truth value contradicts what it says. (e) A proposition whose truth value is unknown today; it is the twin prime conjecture.

2. $p \oplus q \oplus r$ is true: exactly one of the three is true, an odd number. $(p \leftrightarrow q) \leftrightarrow r$ is true: $p \leftrightarrow q$ is false and false $\leftrightarrow$ false is true, as the rule "an even number of the three are false" predicts.

4. Converse: if $5 \mid n$ then $10 \mid n$. Inverse: if $10 \nmid n$ then $5 \nmid n$. Contrapositive: if $5 \nmid n$ then $10 \nmid n$. The statement and its contrapositive are true; the converse and the inverse both fail at $n = 5$.

6. (a) Modus tollens, valid. (b) Affirming the consequent, invalid: $f(x) = |x|$ has true premises and a false conclusion. (c) Disjunctive syllogism, valid.

8. (a) True, with $y = -x$. (b) False: $y$ would have to equal $-x$ for every $x$. (c) False at $x = 0$ and at $x = 2$. (d) True, with $x = 0$.

10. $2^5 = 32$ rows and $2^{2^3} = 256$ truth functions. Of the $16$ binary connectives, six depend on at most one argument (the two constants, $p$, $q$, $\neg p$, $\neg q$), so $10$ depend on both.

13. One answer is $\bigl(p \uparrow (p \uparrow q)\bigr) \uparrow \bigl(q \uparrow (p \uparrow q)\bigr)$. The two inner parts are $\neg p \lor q$ and $p \lor \neg q$, and the stroke of these is the negation of $p \leftrightarrow q$.

14. Induction on the formula. The variables $p$ and $q$ are true in two rows each. If $f$ is true in $k$ rows, $\neg f$ is true in $4 - k$. For $\leftrightarrow$, the number of rows where $f$ and $g$ differ is $k_f + k_g - 2k_{f \land g}$, which is even when $k_f$ and $k_g$ are, and $f \leftrightarrow g$ is true in the other rows. The conjunction $p \land q$ is true in one row.

16. Kleene: $p \to p = \tfrac12$ and $p \lor \neg p = \tfrac12$. Łukasiewicz: $p \to p = 1$ and $p \lor \neg p = \tfrac12$. So in Łukasiewicz's logic $p \to p$ takes the value $1$ everywhere, and excluded middle does not.

17. Write $(p \to q) \to r \equiv (p \land \neg q) \lor r$ and $p \to (q \to r) \equiv \neg p \lor \neg q \lor r$. They agree when $r$ is true; when $r$ is false they differ exactly when $p$ is false. The valuations are $(\mathrm{F}, \mathrm{T}, \mathrm{F})$ and $(\mathrm{F}, \mathrm{F}, \mathrm{F})$.

21. The statements give $a \leftrightarrow \neg b$ and $b \leftrightarrow (a \leftrightarrow b)$. By commutativity and associativity the second is $(b \leftrightarrow b) \leftrightarrow a$, which is equivalent to $a$. So $A$ is a knight, and then $B$ is a knave.

23. For each row where the function is T, form the conjunction of the variables true in that row and the negations of the others. The disjunction of these conjunctions is the formula; if there is no such row, use $p_1 \land \neg p_1$. Then use $\neg p \equiv p \uparrow p$ and $p \land q \equiv (p \uparrow q) \uparrow (p \uparrow q)$, together with De Morgan's laws.

24. The value at the all-T row is fixed and the other $2^n - 1$ rows are free, so $2^{2^n - 1}$; with the all-F row fixed too, $2^{2^n - 2}$. For $n = 2$ the numbers are $8$ and $4$, and the four are $p$, $q$, $p \land q$ and $p \lor q$.

25. A complete connective $f$ cannot be T-preserving or F-preserving, since compositions keep both properties. So $f(\mathrm{T}, \mathrm{T}) = \mathrm{F}$ and $f(\mathrm{F}, \mathrm{F}) = \mathrm{T}$. Of the four ways to fill the other two rows, two give $\uparrow$ and $\downarrow$, and two give $\neg q$ and $\neg p$, which only produce functions of one variable.

26. Assume $\neg(p \lor \neg p)$. Under the further assumption $p$, the rule for $\lor$ gives $p \lor \neg p$, a contradiction, so $\neg p$. Then the rule for $\lor$ gives $p \lor \neg p$ again, a second contradiction, which discharges the first assumption.

27. Induction on the formula, with the four candidates as the base and the induction step checked in a $4 \times 4$ table for $\land$ and for $\lor$, using absorption and idempotence. For example $p \land (p \lor q) \equiv p$ and $(p \land q) \lor q \equiv q$.
