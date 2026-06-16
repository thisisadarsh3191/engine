# 2D Rigid Body Physics Sandbox

A deterministic, object-oriented 2D physics simulation engine built from scratch in Python. Designed as a foundational engineering sandbox, this project avoids high-level physics libraries (like Box2D or Pymunk) to explore how classical mechanics equations are translated into discrete, frame-by-frame computer algorithms. 

Rather than relying on algebraic shortcuts that fall short in multi-body environments, the engine models interactions dynamically using impulse-based momentum changes and inverse-mass positional resolutions. The entire system is built with strict modularity, cleanly separating rendering from the core physics execution phases.

---

## ⚙️ Core Engine Architecture

The entire work/algorithm of this engine can be broken down into 5 sequential steps:

### 1. Force Accumulation
Gathers all external forces (such as gravity) acting on a body and stores the resultant vector as a property of the `rigidBody` object.

### 2. Numerical Integration
Evaluates net kinematic parameters using **Semi-Implicit Euler integration**. 

$$
\mathbf{v}_{t + \Delta t} = \mathbf{v}_t + \left(\mathbf{F}_{\text{net}} \cdot m_{\text{inv}}\right) \cdot \Delta t
$$

$$
\mathbf{x}_{t + \Delta t} = \mathbf{x}_t + \mathbf{v}_{t + \Delta t} \cdot \Delta t
$$

*Note: This specific integration order is utilized as it provides a stable, energy-preserving, and computationally efficient way to resolve positions and velocities in discrete game physics.*

### 3. Broad-Phase Collision Detection
Essentially eliminates pairs of particles that are far apart from each other, ensuring the engine only allocates CPU resources to pairs that have a high probability of touching or intersecting at that specific time instant.

### 4. Narrow-Phase Collision Detection
The object pairs that survive the broad-phase filter undergo a fine-grained geometric check. If the engine detects that bodies have penetrated each other during a frame step, they are retraced and pushed apart until they sit flush against each other. 

The displacement magnitude of each particle depends entirely on its **inverse mass** ($m_{\text{inv}}$). 
* **Example:** If a heavy bowling ball collides with a light ping-pong ball, they will likely interpenetrate by a certain distance over a discrete time step. While Newton's Third Law dictates they experience equal and opposite impulse forces, the ping-pong ball has a much higher "movability" due to its low mass. Since positional correction scales with inverse mass ($1/m$), the engine dynamically shifts the ping-pong ball further away while leaving the bowling ball largely undisturbed.

### 5. Impulse & Positional Resolution
*Built using the curriculum frameworks from the [Newcastle University Game Technologies Module](https://research.ncl.ac.uk/game/mastersdegree/gametechnologies/moduleinformationgametechnologies/).*

Once positions are flush, the bodies must be assigned new post-collision velocities. A naive analytical approach using textbook algebraic systems typically causes significant stability bugs in multi-body environments:

* **Analytical Fallacies Encountered:**
  * **Infinite Mass Singularity:** Closed algebraic formulas fail when attempting to divide by an infinite mass (e.g., an unyielding boundary wall).
  * **State Overwriting & Kinetic Explosions:** Closed-form conservation laws model isolated systems in a vacuum perfectly, but fail when bodies are subjected to continuous external constraints and stacked forces, causing the engine to inject artificial energy and explode objects off the screen.

#### The Impulse Solution
To resolve this, the engine switches to **instantaneous impulses** ($\mathbf{J}$), which represent a discrete, moment-driven change in momentum:

$$
\mathbf{J} = \Delta \mathbf{p} = m \Delta \mathbf{v}
$$

1. Find the common collision normal unit vector $\hat{\mathbf{n}}$.
2. Apply equal and opposite linear impulses along this normal axis:

$$
\mathbf{v}_A' = \mathbf{v}_A + \frac{j}{m_A}\hat{\mathbf{n}} = \mathbf{v}_A + j w_A \hat{\mathbf{n}}
$$

$$
\mathbf{v}_B' = \mathbf{v}_B - \frac{j}{m_B}\hat{\mathbf{n}} = \mathbf{v}_B - j w_B \hat{\mathbf{n}}
$$

$$\text{where } w = \frac{1}{m} \text{ (inverse mass)}$$

3. Using Newton's Law of Restitution to relate relative pre-impact normal velocity ($v_{\text{n}}$) to post-impact normal velocity ($v_{\text{n}}'$):

$$
v_{\text{rel}}' \cdot \hat{\mathbf{n}} = -e (v_{\text{rel}} \cdot \hat{\mathbf{n}})
$$

4. Solving directly for the scalar impulse magnitude $j$:

$$
j = \frac{-(1 + e)v_{\text{n}}}{w_A + w_B}
$$

$$\text{where } v_{\text{n}} = (\mathbf{v}_A - \mathbf{v}_B) \cdot \hat{\mathbf{n}}$$

---

##  Module Design Blueprint

The project structure keeps state evaluation and interaction rules isolated across dedicated system modules:

### 1. `vector.py` (Mathematical Substrate)
Encapsulates 2D mathematical vector objects containing coordinate properties `x` and `y`. It overloads native arithmetic dunder methods (`__add__`, `__sub__`, `__mul__`, `__rmul__`) to abstract component-wise tracking away from core physics equations.

* **Magnitude Guard:** Includes a protective safety check inside the normalization sequence (`.unit()`). If the distance between two overlapping bodies evaluates to exactly `0.0`, it manually forces a baseline mock unit vector heading of `vector(1.0, 0.0)`. This completely averts a destructive `ZeroDivisionError` and supplies a valid axis for positional pushback.
* **Scalar Commutativity:** Explicitly maps right-side scalar expressions (`__rmul__`) back to standard multiplication routines, insulating kinematic updates regardless of whether expressions are authored as `velocity * dt` or `dt * velocity`.

### 2. `rigidbody.py` (Kinematic Container)
Defines physical entities using native structural properties: `centerX` (float), `centerY` (float), `radius` (float), `mass` (float), and `color` (RGB tuple).

* **The Infinite Mass Trick:** Mass properties are internally calculated and stored straight away as an inverse scalar ($m_{\text{inv}} = 1/m$). While active rigid bodies hold dynamic decimals, immovable static anchors (like border bounds, floors, or solid obstacles) are initialized with a mass of `0.0`, rendering an explicit inverse mass of exactly `0.0`. This allows the physics loops to automatically multiply forces by zero, keeping static elements permanently anchored in space without adding messy `if/else` conditional logic.

### 3. `collision.py` (Stateless Physics Solver)
A purely stateless module responsible for inspecting spatial boundaries and modifying structural attributes inline. It contains explicit separation routines for boundary containment (`wallCollisionX`, `wallCollisionY`) and particle-to-particle intersections (`particleCollision`, `particleResolution`).

* *Roadmap Note:* In upcoming updates, native screen border bounds will be refactored into static `infiniteMass` objects placed at the screen edges to eliminate procedural redundancy.

---

##  Pre-Emptive Operational Safeguards

To prevent chaotic structural bugs unique to discrete physics frameworks, the engine architecture integrates two primary algorithmic guards:

* **The Variable Time Step Catastrophe:** This engine **never** passes dynamic or raw hardware frame intervals straight into numerical integrations. A sudden drop in hardware frame rate spikes $\Delta t$, injecting artificial, exponential kinetic energy into the integration steps and launching elements out of bounds. The engine enforces a rock-solid, hardcoded time delta substrate (e.g., `dt = 0.01666` for a uniform $60\text{ Hz}$ update tick).
* **The Relative Closing Speed Guard:** Impulse calculations are explicitly gated behind an impact axis velocity evaluation. If the projection $v_{\text{normal}} \ge 0$, the elements are mathematically confirmed to be already separating or naturally flying apart. The solver exits early, preventing the engine from firing an erroneous bounce calculation that would reverse their directions, lock them together, or cause frantic vibrational stuttering.

---

##  Academic Sourcing & Credits

While the structural module architecture and object encapsulation are custom configurations designed from the ground up, the underlying linear algebra operations and narrow-phase vector projections utilized within the collision solvers are based on the foundational research paper:

* **Title:** *Game Technologies Tutorial 4 - Collision Detection*
* **Institution:** Newcastle University (School of Computing Science)
* **Author/Publisher:** Dr. Rich Davison (Game Technologies Course Archive)
* **Resource URL:** [Newcastle University Research Repository](https://research.ncl.ac.uk/game/mastersdegree/gametechnologies/previousinformation/physics4collisiondetection/2017%20Tutorial%204%20-%20Collision%20Detection.pdf)

---

## 💬 Contributing & Support
If you find any bugs, edge-case structural explosions, or want to talk about rigid-body dynamics optimization, feel free to open an issue or reach out directly at [adarsh.deen@gmail.com](mailto:adarsh.deen@gmail.com).

Thanks for checking out the sandbox!
