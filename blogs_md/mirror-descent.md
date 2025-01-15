# Mirror Descent: A Fundamental Algorithm in Convex Optimization

**Date:** Jan 19, 2024

Mirror Descent is a powerful algorithm in convex optimization that extends the classic Gradient Descent method by leveraging problem geometry. Its main appeal lies in improved asymptotic complexity and its ability to handle high-dimensional optimization problems efficiently.

## Improvements in Asymptotic Complexity

Mirror Descent achieves better asymptotic complexity in terms of the number of oracle calls required for convergence. Compared to standard Gradient Descent, Mirror Descent exploits a problem-specific *distance-generating function* \\( \\psi \\) to adapt the step direction and size based on the geometry of the optimization problem.

For a convex function \\( f(x) \\) with Lipschitz constant \\( L \\) and strong convexity parameter \\( \\sigma \\), the convergence rate of Mirror Descent under appropriate conditions is:

\\[
f(x_T) - f(x^*) \\leq \\frac{L^2 R^2}{2 \\sigma T},
\\]

where:
- \\( T \\) is the number of iterations (or oracle calls),
- \\( R \\) is the radius of the feasible region, and
- \\( x^* \\) is the optimal solution.

This quadratic improvement in the dependence on \\( T \\) compared to the linear rate of Gradient Descent makes Mirror Descent particularly attractive in large-scale settings.

## Assumptions

For Mirror Descent to achieve these guarantees, several key assumptions must hold:

1. **Convexity**: The objective function \\( f(x) \\) must be convex.
2. **Lipschitz Continuity**: The gradient \\( \\nabla f(x) \\) must satisfy \\( \\|\\nabla f(x_1) - \\nabla f(x_2)\\| \\leq L \\|x_1 - x_2\\| \\) for some constant \\( L \\).
3. **Strong Convexity of \\( \\psi \\)**: The distance-generating function \\( \\psi(x) \\) must be strongly convex with respect to a chosen norm \\( \\|\\cdot\\| \\), i.e.,
\\[
\\psi(y) \\geq \\psi(x) + \\langle \\nabla \\psi(x), y - x \\rangle + \\frac{\\sigma}{2} \\|y - x\\|^2.
\\]

These assumptions ensure that the dual space updates remain stable and that the method converges efficiently.

## Update Step

The core of the Mirror Descent algorithm is the following update step:

1. Compute the gradient of the objective: \\( g_t = \\nabla f(x_t) \\).
2. Update in the dual space using the gradient: \\( z_{t+1} = z_t - \\eta g_t \\), where \\( \\eta \\) is the learning rate.
3. Map back to the primal space via the mirror map (the gradient of \\( \\psi \\)):
\\(\\)

\\[x_{t+1} = \nabla \psi^*(z_{t+1}),\\]

where \\( \\psi^* \\) is the convex conjugate of \\( \\psi \\).

This process ensures that each step respects the underlying geometry of the problem.

## Conclusion

Mirror Descent is a versatile and efficient tool for solving convex optimization problems, particularly when the problem geometry is complex or high-dimensional. By tailoring the distance-generating function \\( \\psi \\), the algorithm can achieve significant improvements in convergence rates while maintaining computational efficiency.

---

If you found this post helpful, feel free to reach out or share your thoughts in the comments!
