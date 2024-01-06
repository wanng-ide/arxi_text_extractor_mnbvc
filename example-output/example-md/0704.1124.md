MAD-TH-07-02

**Non-commutativity and Open Strings Dynamics**

**in Melvin Universes**

Danny Dhokarh, Akikazu Hashimoto, and Sheikh Shajidul Haque

Department of Physics, University of Wisconsin, Madison, WI 53706

We compute the Moyal phase factor for open strings ending on D3-branes wrapping a NSNS Melvin universe in a decoupling limit explicitly using world sheet formalism in cylindrical coordinates.

Melvin Universe is an exact axially symmetric solution of Einstein gravity in a background with magnetic flux [1]. It arises naturally as a Kaluza-Klein reduction of twisted flat space

\[ds^{2}=-dt^{2}+d\vec{x}^{2}+dr^{2}+r^{2}(d\varphi+\eta dz)^{2}+dz^{2}\ ,\] (1)

along the coordinate \(z\). The twist is parameterized by variable \(\eta\). The fact that \(z\sim z+2\pi R\) is periodic makes the twist deformation physical.

Melvin universes has a natural embedding in string theory [2, 3, 4]. Simply embed (1) in 11-dimensional supergravity. Reducing along \(z\) gives rise to a background in type IIA string theory with a background of magnetic RR 2-form field strength.

Along similar lines, one can embed (1) in type IIA supergravity and T-dualize along \(z\). This gives rise to a background in type IIB string theory

\[ds^{2} = -dt^{2}+d\vec{x}^{2}+dr^{2}+{r^{2}d\varphi^{2}\over 1+\eta^{2}r^{ 2}}+{1\over 1+\eta^{2}r^{2}}d\tilde{z}^{2}\] (2)
\[B = {\eta r^{2}\over 1+\eta^{2}r^{2}}d\varphi\wedge d\tilde{z}\] (3)
\[e^{\phi} = \sqrt{1\over 1+\eta^{2}r^{2}}\] (4)
\[\tilde{z} = \tilde{z}+2\pi\tilde{R},\qquad\tilde{R}={\alpha^{\prime}\over R}\ ,\] (5)

with an axially symmetric magnetic NSNS 3-form field strength in the background. String theories in backgrounds like (5) are very special in that the world sheet theory is exactly solvable [5, 6, 7, 8, 9, 10]. Quantization of open strings in Melvin backgrounds have also been studied and was shown to be exactly solvable [11, 12] as well.

Embedding D-branes in Melvin universes can give rise to interesting field theories in the decoupling limit. A D3-brane extended along \(t\), \(\tilde{z}\), and two of the \(\vec{x}\) coordinates gives rise to a non-local field theory known as the “dipole” theory [13, 14]. Orienting the D3-brane to be extended along the \(t\), \(r\), \(\varphi\), and \(\tilde{z}\) coordinates, on the other hand, gives rise to a non-commutative gauge theory with a non-constant non-commutativity parameter¹[16, 17]. These are field theories, whose Lagrangian [17] is expressed most naturally using the deformation quantization formula of Kontsevich²[19]. Field theories arising as a decoupling limits of various orientations of D-branes in Melvin and related closed string backgrounds along these lines³ were tabulated and classified in Table 1 of [16].⁴

[FOOTNOTE:1][ENDFOOTNOTE]

[FOOTNOTE:2][ENDFOOTNOTE]

[FOOTNOTE:3][ENDFOOTNOTE]

[FOOTNOTE:4][ENDFOOTNOTE]

To show that the decoupled field theory is a non-commutative field theory, the authors of [16] presented the following arguments:

* The application of Seiberg-Witten formula⁵[24] [FOOTNOTE:5][ENDFOOTNOTE] \[(G+{\theta\over 2\pi\alpha^{\prime}})^{\mu\nu}=[(g+B)_{\mu\nu}]^{-1}\] (6) to the closed string background (5) gives the following open string metric and the non-commutativity parameter \[G_{\mu\nu}dx^{\mu}dx^{\nu} = -dt^{2}+dr^{2}+r^{2}d\varphi^{2}+dz^{2}\] (7) \[\theta^{\varphi z} = 2\pi\alpha^{\prime}\eta\] (8) which are finite if \(\alpha^{\prime}\) is scaled to zero keeping \(\Delta=\alpha^{\prime}\eta\) fixed.
* Solution of the classical equations of motion of an open string traveling freely on the D3-brane with angular momentum \(J\) has a dipole structure whose size is given by[16] \[L=\theta^{\varphi z}J\ .\] (9)

Another suggestive argument is the similarity between \(\alpha^{\prime}\to 0\) limit of critical string theory and the boundary Poisson sigma-model [25] as was pointed out, e.g., in [26]. As was emphasized in [26], however, the two theories are not to be understood as being equivalent or continuously connected. This apparent similarity therefore does not constitute a proof that the decoupled theory is a non-commutative field theory.

A physical criteria for non-commutativity is the Moyal-like phase factor in scattering amplitudes. Scattering amplitudes of open strings ending on a D-brane can be computed along the lines reviewed in [27]. In the case of the constant non-commutativity parameter, one can show very explicitly that

\[\langle e^{ip^{1}x(\tau_{1})}e^{ip^{2}x(\tau_{2})}\ldots e^{ip^{n}x(\tau_{n})} \rangle_{G,\theta}=e^{-{i\over 2}\sum_{n>m}p_{i}^{n}\theta^{ij}p_{j}^{m} \epsilon(\tau_{n}-\tau_{m})}\langle e^{ip^{1}x(\tau_{1})}e^{ip^{2}x(\tau_{2})} \ldots e^{ip^{n}x(\tau_{n})}\rangle_{G,\theta=0}\] (10)

which implies that the scattering amplitudes receive corrections in the form of the Moyal phase factor [28, 29, 24]. The goal of this article is to derive the analogous statement (65) for the model of [16, 17]. Once (65) is established in polar coordinates, the connection to Kontsevich formula follows from performing a change of coordinates to the rectangular coordinate system and a non-local field redefinition as is described in [30, 17].

A useful first step in this exercise is to reproduce the master relation (10) in a slightly different formalism than what was used in [24]. Let us begin by constructing the closed string background as follows. Start with flat space

\[ds^{2}=dy^{\prime 2}+d\tilde{z}^{2}\ ,\] (11)

where \(y\) and \(\tilde{z}\) are compactified with period \(L=2\pi R\). Then,

1. T-dualize along the \(z\) direction so that the metric becomes \[ds^{2}=dy^{\prime 2}+dz^{2}\ .\] (12)
2. Twist by shifting the coordinates \(y^{\prime}=y+\eta z\) \[ds^{2}=(dy+\eta dz)^{2}+dz^{2}\ .\] (13)
3. T-dualize on \(z\) so that \[ds^{2}={1\over 1+\eta^{2}}(dy^{2}+d\tilde{z}^{2}),\qquad B={\eta\over 1+\eta^{ 2}}dy\wedge d\tilde{z}\ .\] (14) The open string metric associated to this background is \[G_{\mu\nu}dx^{\mu}dx^{\nu}=dy^{2}+d\tilde{z}^{2},\qquad\theta^{y\tilde{z}}=2 \pi\Delta^{2}\] (15) if we scale \[\Delta^{2}=\alpha^{\prime}\eta\ .\] (16)

The transformation of the coordinates and the orientation of the branes are illustrated in figure 1. This sequence of dualities was referred to as the “Melvin shift twist” in [16].

[FIGURE:S0.F1][ENDFIGURE]

The approach of [24] was to work directly in the duality frame **III**, but one can just as easily work in a framework which makes the T-duality between duality frame **II** and **III** manifest, by working with a sigma model of the form

\[S={1\over 2\pi\alpha^{\prime}}\int d\sigma_{1}d\sigma_{2}\left[{1\over 2} \delta^{ab}\left(\partial_{a}y\partial_{b}y+2\eta\partial_{a}yV_{b}+(1+\eta^{2 })V_{a}V_{b}\right)+i\epsilon^{ab}\partial_{a}\tilde{z}V_{b}\right]\] (17)

where we have chosen to work in conformal gauge in Eucledian signature. This action utilizes the Bushar’s formulation of T-duality [31]. To see this more explicitly, consider integrating out the field \(\tilde{z}\). This imposes the constraint

\[dV=0\to V_{a}=\partial_{a}z\] (18)

which brings the action (17) into the form

\[S={1\over 2\pi\alpha^{\prime}}\int d\sigma_{1}d\sigma_{2}\left[{1\over 2} \delta^{ab}\left(\partial_{a}y\partial_{b}y+2\eta\partial_{a}y\partial_{b}z+(1 +\eta^{2})\partial_{a}z\partial_{b}z\right)\right]\] (19)

which is the sigma model for the duality frame **II**. On the other hand, integrating out \(V\) first gives rise to a sigma model of the form

\[S={1\over 2\pi\alpha^{\prime}}\int d\sigma_{1}d\sigma_{2}\left[\left({1\over 1 +\eta^{2}}\right){1\over 2}\delta^{ab}\left(\partial_{a}y\partial_{b}y+ \partial_{a}\tilde{z}\partial_{b}\tilde{z}\right)+i\left({\eta\over 1+\eta^{2} }\right)\epsilon^{ab}\partial_{a}y\partial_{b}\tilde{z}\right]\] (20)

which is the string action for the duality frame **III**.

In extracting non-commutative gauge theory as a decoupling limit, we are interested in embedding a D-brane extended along the \(y\) and \(\tilde{z}\) coordinates in the duality frame **III**. We must therefore take the sigma model to be defined on a Riemann surface with one boundary, which we take to be the upper half plane. It is also necessary to impose the appropriate boundary condition for all of the world sheet fields. We impose the boundary condition which is free along the \(y\) direction and Dirichlet along the \(z\) direction:

(21)

\[\left.V_{t}\right|_{\partial\Sigma}=\left.\partial_{t}z\right|_{\partial\Sigma }=0\ .\] (22)

Using the equation of motion from the variation of \(V_{a}\) field

\[\eta\partial_{b}y+(1+\eta^{2})V_{b}+i\epsilon_{ab}\partial_{a}\tilde{z}=0\,\] (23)

and (22), we infer

\[\partial_{n}\tilde{z}-i\eta\partial_{t}y=0\ .\] (24)

The boundary conditions (21) and (24) are precisely the boundary condition imposed in the analysis of [24].

In order to complete the derivation of (10), we add a source term

\[e^{-S_{source}}=\prod_{n}e^{ik_{yn}y(\sigma_{n},\bar{\sigma}_{n})+ik_{zn} \tilde{z}(\sigma_{n},\bar{\sigma}_{n})}=e^{\sum_{n}(ik_{yn}y(\sigma_{n},\bar{ \sigma}_{n})+ik_{zn}\tilde{z}(\sigma_{n},\bar{\sigma}_{n}))}\] (25)

to the action (17). Integrating out the \(V\) fields and bringing the sigma model (17) into duality frame **III** would lead to identical computation as what was described in [24] to derive (10). We will show below that the same conclusion can be reached using a slightly different argument which turns out to easily generalize to the case of Melvin deformed theories [16, 17].

The approach we take here is to go to the duality frame **I**. This brings the sigma model (17) to a simpler form

\[S={1\over 2\pi\alpha^{\prime}}\int d\sigma_{1}d\sigma_{2}\left[{1\over 2} \delta^{ab}\left(\partial_{a}y^{\prime}\partial_{b}y^{\prime}+\partial_{a}z \partial_{b}z\right)\right]\ .\] (26)

The \(\tilde{z}\) field in the vertex operator now plays the role of a disorder operator of the dual field \(z\). It has the effect of shifting the Dirichlet boundary condition, incorporating the fact that strings are stretched along the \(z\) direction in frames **I** and **II**. Also, the fact that the periodicity in \((y^{\prime},z)\) coordinate system are twisted

\[(y^{\prime},z)=(y^{\prime}+\eta Ln,z+Ln)\] (27)

requires an insertion of a disorder operator for the \(y^{\prime}(\sigma,\bar{\sigma})\) field as well. We therefore find that the source term has the form

\[e^{-S_{source}}=\prod_{n}e^{ik_{yn}y^{\prime}(\sigma_{n},\bar{\sigma}_{n})+i \eta k_{zn}\tilde{y}^{\prime}(\sigma_{n},\bar{\sigma}_{n})-i\eta k_{yn}z( \sigma_{n},\bar{\sigma}_{n})+ik_{zn}\tilde{z}(\sigma_{n})}\ .\] (28)

The boundary condition is now simply Neumann for \(y^{\prime}\)

\[\left.\partial_{n}y^{\prime}(\sigma,\bar{\sigma})=0\right|_{\partial\Sigma}\ ,\] (29)

and Dirichlet for \(z\)

\[\left.\partial_{t}z(\sigma,\bar{\sigma})=0\right|_{\partial\Sigma}\ .\] (30)

In this form, \(y^{\prime}\) and the \(z\) sector decouple, allowing their correlators to be computed separately. In order to compute the correlation functions involving order and disorder operators with boundary conditions (29) and (30), it is convenient to decompose the fields into holomorphic and anti holomorphic parts

\[y^{\prime}(\sigma,\bar{\sigma})=y^{\prime}(\sigma)+\bar{y}^{\prime}(\bar{ \sigma})\ ,\qquad\tilde{y}^{\prime}(\sigma,\bar{\sigma})=y^{\prime}(\sigma)- \bar{y}^{\prime}(\bar{\sigma})\ ,\] (31)

\[z(\sigma,\bar{\sigma})=z(\sigma)+\bar{z}(\bar{\sigma})\ ,\qquad\tilde{z}^{ \prime}(\sigma,\bar{\sigma})=z(\sigma)-\bar{z}(\bar{\sigma})\ .\] (32)

Their correlation functions are given by

\[\langle y^{\prime}(\sigma_{1})y^{\prime}(\sigma_{2})\rangle=-{1\over 2}\alpha^ {\prime}\log(\sigma_{1}-\sigma_{2})\] (33)

\[\langle\bar{y}^{\prime}(\sigma_{1})\bar{y}^{\prime}(\sigma_{2})\rangle=-{1 \over 2}\alpha^{\prime}\log(\bar{\sigma}_{1}-\bar{\sigma}_{2})\] (34)

\[\langle\bar{y}^{\prime}(\bar{\sigma}_{1})y^{\prime}(\sigma_{2})\rangle=-{1 \over 2}\alpha^{\prime}\log(\bar{\sigma}_{1}-\sigma_{2})\] (35)

\[\langle z(\sigma_{1})z(\sigma_{2})\rangle=-{1\over 2}\alpha^{\prime}\log( \sigma_{1}-\sigma_{2})\] (36)

\[\langle\bar{z}(\bar{\sigma}_{1})\bar{z}(\bar{\sigma}_{2})\rangle=-{1\over 2} \alpha^{\prime}\log(\bar{\sigma}_{1}-\bar{\sigma}_{2})\] (37)

\[\langle\bar{z}(\bar{\sigma}_{1})z(\sigma_{2})\rangle={1\over 2}\alpha^{\prime} \log(\bar{\sigma}_{1}-\sigma_{2}),\] (38)

from which we infer

\[\langle y^{\prime}(\sigma_{1},\bar{\sigma}_{1})y^{\prime}(\sigma_{2},\bar{ \sigma}_{2})\rangle=-{1\over 2}\alpha^{\prime}(\log(\sigma_{1}-\sigma_{2})+ \log(\sigma_{1}-\bar{\sigma}_{2})+\log(\bar{\sigma}_{1}-\sigma_{2})+\log(\bar{ \sigma}_{1}-\bar{\sigma}_{2}))\] (39)

\[\langle\tilde{y}^{\prime}(\sigma_{1},\bar{\sigma}_{1})y^{\prime}(\sigma_{2}, \bar{\sigma}_{2})\rangle=-{1\over 2}\alpha^{\prime}(\log(\sigma_{1}-\sigma_{2} )+\log(\sigma_{1}-\bar{\sigma}_{2})-\log(\bar{\sigma}_{1}-\sigma_{2})-\log( \bar{\sigma}_{1}-\bar{\sigma}_{2}))\] (40)

\[\langle\tilde{y}^{\prime}(\sigma_{1},\bar{\sigma}_{1})\tilde{y}^{\prime}( \sigma_{2},\bar{\sigma}_{2})\rangle=-{1\over 2}\alpha^{\prime}(\log(\sigma_{1} -\sigma_{2})-\log(\sigma_{1}-\bar{\sigma}_{2})-\log(\bar{\sigma}_{1}-\sigma_{2 })+\log(\bar{\sigma}_{1}-\bar{\sigma}_{2}))\] (41)

\[\langle\tilde{z}(\sigma_{1},\bar{\sigma}_{1})\tilde{z}(\sigma_{2},\bar{\sigma} _{2})\rangle=-{1\over 2}\alpha^{\prime}(\log(\sigma_{1}-\sigma_{2})+\log( \sigma_{1}-\bar{\sigma}_{2})+\log(\bar{\sigma}_{1}-\sigma_{2})+\log(\bar{ \sigma}_{1}-\bar{\sigma}_{2}))\] (42)

\[\langle z(\sigma_{1},\bar{\sigma}_{1})\tilde{z}(\sigma_{2},\bar{\sigma}_{2}) \rangle=-{1\over 2}\alpha^{\prime}(\log(\sigma_{1}-\sigma_{2})+\log(\sigma_{1} -\bar{\sigma}_{2})-\log(\bar{\sigma}_{1}-\sigma_{2})-\log(\bar{\sigma}_{1}- \bar{\sigma}_{2}))\] (43)

\[\langle z(\sigma_{1},\bar{\sigma}_{1})z(\sigma_{2},\bar{\sigma}_{2})\rangle=-{ 1\over 2}\alpha^{\prime}(\log(\sigma_{1}-\sigma_{2})-\log(\sigma_{1}-\bar{ \sigma}_{2})-\log(\bar{\sigma}_{1}-\sigma_{2})+\log(\bar{\sigma}_{1}-\bar{ \sigma}_{2}))\ .\] (44)

In terms of these correlation functions, one can easily show that

\[\langle{\cal O}(\sigma_{1},\bar{\sigma}_{1}){\cal O}(\sigma_{2}, \bar{\sigma}_{2})\rangle\]
\[= {1\over 2}\alpha^{\prime}(k_{y1}k_{y2}+k_{z1}k_{z2})(\log(\sigma_ {1}-\sigma_{2})+\log(\sigma_{1}-\bar{\sigma}_{2})+\log(\bar{\sigma}_{1}-\sigma _{2})+\log(\bar{\sigma}_{1}-\bar{\sigma}_{2}))\]
\[-\eta\alpha^{\prime}(k_{y1}k_{z2}-k_{y2}k_{z1})(\log(\sigma_{1}- \bar{\sigma}_{2})-\log(\bar{\sigma}_{1}-\sigma_{2}))\]
\[+{1\over 2}\eta^{2}\alpha^{\prime}(k_{y1}k_{y2}+k_{z1}k_{z2})( \log(\sigma_{1}-\sigma_{2})-\log(\sigma_{1}-\bar{\sigma}_{2})-\log(\bar{\sigma }_{1}-\sigma_{2})+\log(\bar{\sigma}_{1}-\bar{\sigma}_{2}))\]

for

\[{\cal O}_{n}(\sigma_{n},\bar{\sigma}_{n})=ik_{yn}y^{\prime}(\sigma_{n},\bar{ \sigma}_{n})+i\eta k_{zn}\tilde{y}^{\prime}(\sigma_{n},\bar{\sigma}_{n})-i\eta k _{yn}z(\sigma_{n},\bar{\sigma}_{n})+ik_{zn}\tilde{z}(\sigma_{n},\bar{\sigma}_{ n})\ .\] (46)

When these operators are pushed toward the boundary

\[\sigma\rightarrow\tau+0^{+}i\ ,\] (47)

the correlation function (S0.Ex4) reduces to

\[\langle{\cal O}(\tau_{1}){\cal O}(\tau_{2})\rangle=2\alpha^{\prime}(k_{y1}k_{y 2}+k_{z1}k_{z2})\log(\tau_{1}-\tau_{2})-\pi i\eta\alpha^{\prime}(k_{y1}k_{z2}- k_{y2}k_{z1})\epsilon(\tau_{2}-\tau_{1})\] (48)

where \(\epsilon(\tau)\), following the notation of [24], is a function which takes the values \(\pm 1\) depending on the sign of \(\tau\). The term of order \(\eta^{2}\) vanishes in this limit. From these results, we conclude that

\[\langle\prod e^{O_{n}(\tau_{n})}\rangle=e^{\sum_{m<n}\langle O_{m}(\tau_{m})O_ {n}(\tau_{n})\rangle}\] (49)

from which the main statement (10) follows immediately.

Finally, let us discuss the generalization of (10) to D3-brane embedded into Melvin universe background (5) along the lines of [16, 17]. We will consider the simplest case of embedding (5) into bosonic string theory. For the Melvin universe background (5), it is convenient to prepare a vertex operator that corresponds to tachyons in cylindrical basis

\[V(\nu,m,\vec{k}) = \int dk_{1}\,dk_{2}\,\delta(\nu^{2}-k_{1}^{2}-k_{2}^{2})e^{im \theta}e^{ik_{1}x_{1}(\sigma,\bar{\sigma})+k_{2}x_{2}(\sigma,\bar{\sigma})+ \vec{k}\vec{x}(\sigma,\bar{\sigma})}\] (50)
\[= e^{i\vec{k}\vec{x}(\sigma,\bar{\sigma})}J_{\nu}(r(\sigma,\bar{ \sigma}))e^{im\varphi(\sigma,\bar{\sigma})}\] (51)

where

\[r^{2}=x_{1}^{2}+x_{2}^{2},\qquad\varphi=\arg(x_{1}+ix_{2}),\qquad\theta=\arg(k _{1}+ik_{2})\ .\] (52)

As long as \(\vec{k}^{2}+\nu^{2}\) are taken to satisfy the on-shell condition of the tachyon, (51) is linear combination of operators of boundary conformal dimension 1, and must itself be an operator of boundary conformal dimension one. Such construction of vertex operator as a linear superposition is similar in spirit to what was considered in [32, 33].

\[S={1\over 2\pi\alpha^{\prime}}\int d\sigma_{1}d\sigma_{2}\left[{1\over 2} \delta^{ab}\left(\partial_{a}r\partial_{b}r+r^{2}\partial_{a}\varphi\partial_{ b}\varphi+2\eta r^{2}\partial_{a}\varphi V_{b}+(1+\eta^{2}r^{2})V_{a}V_{b} \right)+i\epsilon^{ab}\partial_{a}\tilde{z}V_{b}\right]\] (53)

on the upper half plane. Integrating out \(\tilde{z}\) brings this action to the form appropriate for the analogue of **II**

\[S={1\over 2\pi\alpha^{\prime}}\int d\sigma_{1}d\sigma_{2}\left[{1\over 2} \delta^{ab}\left(\partial_{a}r\partial_{b}r+r^{2}\partial_{a}\varphi\partial_{ b}\varphi+2\eta r^{2}\partial_{a}\varphi\partial_{b}z+(1+\eta^{2}r^{2}) \partial_{a}z\partial_{b}z\right)\right]\ .\] (54)

The vertex operators can be represented as a source term

\[e^{-S_{source}}=\prod_{n}J_{v_{n}}(r(\sigma_{n},\bar{\sigma}_{n}))e^{im_{n} \varphi(\sigma_{n},\bar{\sigma}_{n})+ik_{zn}\tilde{z}(\sigma_{n},\bar{\sigma}_ {n})}\] (55)

where \(\tilde{z}\) is a disorder operator. Now, if we let

\[\varphi^{\prime}(\sigma,\bar{\sigma})=\varphi(\sigma,\bar{\sigma})+\eta z( \sigma,\bar{\sigma})\ ,\] (56)

the action becomes

\[S={1\over 2\pi\alpha^{\prime}}\int d\sigma_{1}d\sigma_{2}\left[{1\over 2} \delta^{ab}\left(\partial_{a}r\partial_{b}r+r^{2}\partial_{a}\varphi^{\prime} \partial_{b}\varphi^{\prime}+\partial_{a}z\partial_{b}z\right)\right]\] (57)

with

\[e^{-S_{source}}=\prod_{n}J_{v_{n}}(r(\sigma_{n},\bar{\sigma}_{n}))e^{{\cal O}_ {n}}\] (58)

and

\[{\cal O}_{n}=im_{n}\varphi^{\prime}(\sigma_{n},\bar{\sigma}_{n})+i\eta k_{zn} \tilde{\varphi}^{\prime}(\sigma_{n},\bar{\sigma}_{n})-i\eta m_{n}z(\sigma_{n}, \bar{\sigma}_{n})+ik_{zn}\tilde{z}(\sigma_{n},\bar{\sigma}_{n})\] (59)

where

\[\tilde{\varphi}^{\prime}(\sigma,\bar{\sigma})\] (60)

is the disorder field for \(\varphi^{\prime}\) satisfying the relation

\[\partial^{a}\tilde{\varphi}^{\prime}=i\epsilon^{ab}r^{2}\partial_{b}\varphi^{\prime}\] (61)

which follows naturally from the Busher rule applied to the \(\varphi\) fields.

This time, the problem is slightly complicated by the fact that \((r,\varphi^{\prime})\) sector is interacting. It is still the case that \((\varphi^{\prime},z)\) sector, for some fixed \(r(\sigma,\bar{\sigma})\), is non-interacting. We will exploit this fact and do the path integral in the order where we integrate over \(\varphi^{\prime}\) and \(z\) first. The two point function of \(\varphi^{\prime}\) formally has the form

\[\langle\varphi^{\prime}(\sigma_{1},\bar{\sigma}_{1})\varphi^{\prime}(\sigma_{2 },\bar{\sigma}_{2})\rangle=(\partial r^{2}(\sigma,\bar{\sigma})\partial)^{-1}\ .\] (62)

Then, it follows that

\[\langle\varphi^{\prime}(\sigma_{1},\bar{\sigma}_{1})\partial^{a}\tilde{\varphi }^{\prime}(\sigma_{2},\bar{\sigma}_{2})\rangle=i\epsilon^{ab}(\partial^{b})^{-1}\] (63)

from which it follows

\[\langle\tilde{\varphi}^{\prime}(\sigma_{1},\bar{\sigma}_{1})\varphi^{\prime}( \sigma_{2},\bar{\sigma}_{2})\rangle=-{1\over 2}\alpha^{\prime}(\log(\sigma_{1} -\sigma_{2})+\log(\sigma_{1}-\bar{\sigma}_{2})-\log(\bar{\sigma}_{1}-\sigma_{2 })-\log(\bar{\sigma}_{1}-\bar{\sigma}_{2}))\] (64)

in complete analogy with (40). The correlator (64) tells us that while the field-field correlator \(\langle\varphi^{\prime}\varphi^{\prime}\rangle\) is complicated and \(r\) dependent, the field/disorder field correlator \(\langle\tilde{\varphi}^{\prime}\varphi^{\prime}\rangle\) stays simple and topological.

We can then proceed to compute the analogue of (48) and (49) for the operator (59) in the \((\varphi^{\prime},z)\) sector. While we do not explicitly compute the \(\langle\tilde{\varphi}^{\prime}\tilde{\varphi}^{\prime}\rangle\) correlator which appear at order \(\eta^{2}\) in (48), it is clear that the boundary condition forces this term to vanish as was the case in the earlier example. The term of order \(\eta\) in the exponential can be made to take the Moyal-like form

\[e^{{i\over 2}\sum_{a<b}(2\pi\Delta)(m_{a}k_{zb}-k_{za}m_{b})\epsilon(\tau_{b}- \tau_{a})}\] (65)

which is finite in the scaling limit \(\alpha^{\prime}\to 0\) with

\[\eta={\Delta\over\alpha^{\prime}}\] (66)

keeping \(\Delta\) finite. This is precisely the scaling considered in [16, 17]. The dependence on \(r(\sigma,\bar{\sigma})\) drops out for this term of order \(\eta\), allowing us to further path integrate over this field trivially, with the only effect of \(\eta\) being the overall phase factor (65). This establishes that the decoupled theory of D-branes in Melvin universes considered in [16, 17] has an effective dynamics which includes the Moyal-like phase factor involving the angular momentum quantum number \(m\) and the momentum \(k_{z}\). In Cartesian coordinates, this Moyal phase corresponds to a position dependent non-commutativity [16, 17]. This analysis extends straight forwardly to other simple models of position dependent non-commutativity, such as⁶ the “Melvin Null Twist” [15] and “Null Melvin Twist” [34]. It would be interesting to extend this analysis to superstrings and to consider the scattering of states other than the open string tachyon.

[FOOTNOTE:6][ENDFOOTNOTE]

## Acknowledgements

We would like to thank I. Ellwood and O. Ganor for discussions. This work was supported in part by the DOE grant DE-FG02-95ER40896 and funds from the University of Wisconsin.

## References

* [1] M. A. Melvin, “Pure magnetic and electric geons,” _Phys. Lett._**8** (1964) 65–70.
* [2] F. Dowker, J. P. Gauntlett, D. A. Kastor, and J. H. Traschen, “Pair creation of dilaton black holes,” _Phys. Rev._**D49** (1994) 2909–2917, hep-th/9309075.
* [3] F. Dowker, J. P. Gauntlett, S. B. Giddings, and G. T. Horowitz, “On pair creation of extremal black holes and Kaluza-Klein monopoles,” _Phys. Rev._**D50** (1994) 2662–2679, hep-th/9312172.
* [4] K. Behrndt, E. Bergshoeff, and B. Janssen, “Type II Duality Symmetries in Six Dimensions,” _Nucl. Phys._**B467** (1996) 100–126, hep-th/9512152.
* [5] J. G. Russo and A. A. Tseytlin, “Constant magnetic field in closed string theory: An Exactly solvable model,” _Nucl. Phys._**B448** (1995) 293–330, hep-th/9411099.
* [6] A. A. Tseytlin, “Melvin solution in string theory,” _Phys. Lett._**B346** (1995) 55–62, hep-th/9411198.
* [7] J. G. Russo and A. A. Tseytlin, “Exactly solvable string models of curved space-time backgrounds,” _Nucl. Phys._**B449** (1995) 91–145, hep-th/9502038.
* [8] A. A. Tseytlin, “Exact solutions of closed string theory,” _Class. Quant. Grav._**12** (1995) 2365–2410, hep-th/9505052.
* [9] J. G. Russo and A. A. Tseytlin, “Heterotic strings in uniform magnetic field,” _Nucl. Phys._**B454** (1995) 164–184, hep-th/9506071.
* [10] J. G. Russo and A. A. Tseytlin, “Magnetic flux tube models in superstring theory,” _Nucl. Phys._**B461** (1996) 131–154, hep-th/9508068.
* [11] E. Dudas and J. Mourad, “D-branes in string theory Melvin backgrounds,” _Nucl. Phys._**B622** (2002) 46–72, hep-th/0110186.
* [12] T. Takayanagi and T. Uesugi, “D-branes in Melvin background,” _JHEP_**11** (2001) 036, hep-th/0110200.
* [13] A. Bergman and O. J. Ganor, “Dipoles, twists and noncommutative gauge theory,” _JHEP_**10** (2000) 018, hep-th/0008030.
* [14] A. Bergman, K. Dasgupta, O. J. Ganor, J. L. Karczmarek, and G. Rajesh, “Nonlocal field theories and their gravity duals,” _Phys. Rev._**D65** (2002) 066005, hep-th/0103090.
* [15] A. Hashimoto and S. Sethi, “Holography and string dynamics in time-dependent backgrounds,” _Phys. Rev. Lett._**89** (2002) 261601, hep-th/0208126.
* [16] A. Hashimoto and K. Thomas, “Dualities, twists, and gauge theories with non-constant non-commutativity,” _JHEP_**01** (2005) 033, hep-th/0410123.
* [17] A. Hashimoto and K. Thomas, “Non-commutative gauge theory on D-branes in Melvin universes,” _JHEP_**01** (2006) 083, hep-th/0511197.
* [18] L. Cornalba and R. Schiappa, “Nonassociative star product deformations for D-brane worldvolumes in curved backgrounds,” _Commun. Math. Phys._**225** (2002) 33–66, hep-th/0101219.
* [19] M. Kontsevich, “Deformation quantization of Poisson manifolds, I,” _Lett. Math. Phys._**66** (2003) 157–216, q-alg/9709040.
* [20] R.-G. Cai, J.-X. Lu, and N. Ohta, “NCOS and D-branes in time-dependent backgrounds,” _Phys. Lett._**B551** (2003) 178–186, hep-th/0210206.
* [21] R.-G. Cai and N. Ohta, “Holography and D3-branes in Melvin universes,” _Phys. Rev._**D73** (2006) 106009, hep-th/0601044.
* [22] O. J. Ganor, “A new Lorentz violating nonlocal field theory from string theory,” hep-th/0609107.
* [23] O. J. Ganor, A. Hashimoto, S. Jue, B. S. Kim, and A. Ndirango, “Aspects of Puff Field Theory,” hep-th/0702030.
* [24] N. Seiberg and E. Witten, “String theory and noncommutative geometry,” _JHEP_**09** (1999) 032, hep-th/9908142.
* [25] A. S. Cattaneo and G. Felder, “A path integral approach to the Kontsevich quantization formula,” _Commun. Math. Phys._**212** (2000) 591–611, math.qa/9902090.
* [26] L. Baulieu, A. S. Losev, and N. A. Nekrasov, “Target space symmetries in topological theories. I,” _JHEP_**02** (2002) 021, hep-th/0106042.
* [27] A. Hashimoto and I. R. Klebanov, “Scattering of strings from D-branes,” _Nucl. Phys. Proc. Suppl._**55B** (1997) 118–133, hep-th/9611214.
* [28] C.-S. Chu and P.-M. Ho, “Noncommutative open string and D-brane,” _Nucl. Phys._**B550** (1999) 151–168, hep-th/9812219.
* [29] V. Schomerus, “D-branes and deformation quantization,” _JHEP_**06** (1999) 030, hep-th/9903205.
* [30] B. L. Cerchiai, “The Seiberg-Witten map for a time-dependent background,” _JHEP_**06** (2003) 056, hep-th/0304030.
* [31] T. H. Buscher, “Path integral derivation of quantum duality in nonlinear sigma models,” _Phys. Lett._**B201** (1988) 466.
* [32] H. Liu, G. W. Moore, and N. Seiberg, “Strings in a time-dependent orbifold,” _JHEP_**06** (2002) 045, hep-th/0204168.
* [33] H. Liu, G. W. Moore, and N. Seiberg, “Strings in time-dependent orbifolds,” _JHEP_**10** (2002) 031, hep-th/0206182.
* [34] L. Dolan and C. R. Nappi, “Noncommutativity in a time-dependent background,” _Phys. Lett._**B551** (2003) 369–377, hep-th/0210030.

