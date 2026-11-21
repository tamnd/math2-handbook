Differentiation sends $x^3 + 2x$ to $3x^2 + 2$, and it turns a sum into the sum of the derivatives and $c\,p$ into $c\,p'$. Rotating the plane by an angle sends the sum of two arrows to the sum of the rotated arrows. Multiplying a vector by a fixed matrix, taking the trace of a matrix, and evaluating a polynomial at $2$ all behave in the same way. These are linear maps: functions between vector spaces with $T(u + v) = T(u) + T(v)$ and $T(av) = a\,T(v)$. The translation $x \mapsto x + 1$ and the squaring map $x \mapsto x^2$ are not linear.

Linear maps are what linear algebra studies, and matrices are the way to compute with them. Every linear map $F^n \to F^m$ is $x \mapsto Ax$ for exactly one matrix $A$, whose columns are the images of the standard basis vectors, and composing two maps multiplies their matrices. Two subspaces describe what a linear map does: the kernel, which it sends to $0$, and the image, which it reaches. The rank-nullity theorem ties their dimensions together. For a system $Ax = b$ with $n$ unknowns, it says that the number of free parameters of the solutions is $n$ minus the rank of $A$.

## What the chapter covers

The chapter is in six groups, read in order.

1. **Linear maps and their examples.** The [linear map](/0NRYHJPQG2/), the standard [examples](/0SS770NS8B/), [matrix transformations of $F^n$](/W6KB0J3SZZ/), [linear transformations of the plane](/5BXHREC8C8/), and the [composition](/00BKRZKMSS/) of linear maps.
2. **Kernel and image.** The [kernel](/0S23E6YE83/) and the [image](/0WSFKKT6FF/), and the test that a linear map is [injective exactly when its kernel is zero](/0BJBYCGMWE/).
3. **Bases, rank and nullity.** A linear map is [determined by its values on a basis](/0R8X9XA83A/). The [rank](/0ZZXSBTR4J/) and the [nullity](/0APCFW7639/) satisfy the [rank-nullity theorem](/0W4FSW1TVB/).
4. **Isomorphisms.** The [linear isomorphism](/0B8T10CE7N/), the [classification of spaces by dimension](/0VJBSK15SN/), and the equivalence of [injective, surjective and bijective endomorphisms](/0912EEEVCT/) in finite dimension.
5. **Spaces of maps and the algebra of endomorphisms.** The [space of linear maps](/0X9MBPP2Z3/) $\operatorname{Hom}(V, W)$ and [its dimension](/0Z9N1ER0W0/), [endomorphisms](/0J7H0YBFDJ/), and the [algebra of endomorphisms](/5JA4CYT1TB/).
6. **Semilinear maps.** [Semilinear and antilinear maps](/BNPDDM95KF/), which twist the scalars by an automorphism of the field.

## A first reading

For a first reading, take these entries in order: [linear map](/0NRYHJPQG2/), [examples of linear maps](/0SS770NS8B/), [matrix transformations of $F^n$](/W6KB0J3SZZ/), [composition of linear maps](/00BKRZKMSS/), [kernel](/0S23E6YE83/), [image](/0WSFKKT6FF/), [injectivity and the kernel](/0BJBYCGMWE/), [linear maps are determined by a basis](/0R8X9XA83A/), [rank-nullity theorem](/0W4FSW1TVB/), [linear isomorphism](/0B8T10CE7N/) and [classification by dimension](/0VJBSK15SN/). Work through the attached example that computes the kernel, image, rank and nullity of a $3 \times 3$ matrix map; it is the computation used most often.

The space $\operatorname{Hom}(V, W)$, the algebra of endomorphisms and semilinear maps can wait. They matter for dual spaces, for eigenvalues and for the polynomial of an endomorphism, and the semilinear maps return with inner products over $\C$.

## Before you start

You need the previous chapter: [vector spaces](/000AYPA9AJ/), [subspaces](/00YC1D652K/), [span](/0DTY8B9HMS/), [linear independence](/0CRMGPAH83/), [bases](/0KCQ9Y3QKA/) and [dimension](/03GSZ8RTZJ/). From the chapter on matrices you need the [matrix-vector product](/0PDVQEP0ZC/), [matrix multiplication](/032Q9FB8MT/), the [matrix units](/4H93XF4RVH/) and the [matrix ring](/AB2MD5CD13/). From the chapter on systems you need the [homogeneous system](/04KGXJG1A2/) $Ax = 0$, [pivots and free variables](/0J0BBCMJ5W/), and the [structure of solution sets](/PDH3HKXWAZ/). The [invertible matrix theorem](/ACDFDABVQK/) of the chapter on invertible matrices is the matrix form of several results here.
