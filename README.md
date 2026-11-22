# AISR Laboratory Work (CSAI4014)

## Algorithms for Intelligent Systems and Robotics

**School of Computer Science, UPES Dehradun**
B.Tech CSE (AI & ML), Semester VII | Autumn Semester 2026–27

---

## Student Information

- **Student Name:** Srishti Batham
- **SAP ID:** 500124490
- **Roll Number:** R2142231748
- **Batch / Cohort:** B2
- **Partner Details:** Individual
- **Course Teacher:** Dr. Resham Raj Shivwanshi

---

## Repository Structure & Index

```text
Robotics-Lab-Work/
│
├── README.md
├── AISR_SrishtiBatham_500124490_LabReport.docx
│
├── Exp1/
│   ├── exp01.ipynb
│   └── figs/
│
├── Exp2/
│   ├── exp02.ipynb
│   └── figs/
│
├── Exp3/
│   ├── exp03.ipynb
│   └── figs/
│
├── Exp4/
│   ├── exp04.ipynb
│   └── figs/
│
├── Exp5/
│   ├── exp05.ipynb
│   └── figs/
│
├── Exp6/
│   ├── exp06.ipynb
│   └── figs/
│
├── Exp7/
│   ├── controllers/
│   ├── runs/
│   ├── figs/
│   └── NOTES.md
│
└── Exp8/
    ├── results/
    ├── figs/
    ├── exercises/
    └── NOTES.md
```

---

## Experiments Summary

### Exp 1: Time and Frequency Domain, and the Pendulum

- Generated multi-frequency composite signals (5 Hz, 20 Hz and 50 Hz).
- Analysed frequency components using Discrete Fourier Transform (DFT).
- Demonstrated signal aliasing through under-sampling.
- Studied nonlinear pendulum dynamics with different damping coefficients and initial angles.

### Exp 2: The Eight Queens Problem

- Formulated the Eight Queens problem as a Constraint Satisfaction Problem (CSP).
- Implemented recursive backtracking with pruning.
- Compared backtracking with the Generate-and-Test approach.
- Evaluated performance for board sizes from N = 4 to 10.

### Exp 3: Breadth-First Search (BFS) and Depth-First Search (DFS)

- Implemented BFS and DFS for 2D maze navigation.
- Compared FIFO queue and LIFO stack-based approaches.
- Analysed path length, memory usage and node expansions.
- Demonstrated BFS shortest-path guarantees and DFS exploration behaviour.

### Exp 4: Hill Climbing

- Implemented Hill Climbing for the Eight Queens problem and continuous optimization landscapes.
- Studied local optima, plateaus and ridges.
- Implemented Random-Restart Hill Climbing.
- Compared success rates across multiple restarts.

### Exp 5: Reinforcement Learning (Q-Learning)

- Implemented tabular Q-Learning in a 5 × 5 Grid World.
- Defined rewards for goals, traps and movement.
- Evaluated different exploration rates (epsilon values).
- Analysed learning curves and the optimal policy.

### Exp 6: A Simple Neural Network

- Implemented a 2-4-1 Multi-Layer Perceptron (MLP) using NumPy.
- Applied forward propagation and backpropagation.
- Trained the network to solve the XOR problem.
- Analysed different learning rates, loss curves and decision boundaries.

### Exp 7: Mobile Robot Simulation in Webots

- Simulated a five-robot e-puck swarm using reactive obstacle avoidance.
- Implemented Pioneer 3-DX robot navigation using 2D LiDAR.
- Applied the Follow-The-Gap navigation algorithm.
- Evaluated cruise speed, safety bubble size and obstacle avoidance performance.

### Exp 8: Cross-Embodiment Transfer of Manipulation Skills

- Evaluated policy transfer across four different robotic arms using PyBullet.
- Compared joint-space trajectory replay and task-space control.
- Studied cross-embodiment transfer performance.
- Demonstrated the effectiveness of Cartesian end-effector velocity control for zero-shot transfer.

---

## Sources & AI Tools Declaration (Appendix B)

1. *Laboratory Report Guidelines & AISR Sample Lab Report*, Dr. Resham Raj Shivwanshi, UPES Dehradun, 2026.
2. Russell, S. and Norvig, P., *Artificial Intelligence: A Modern Approach*, 4th Edition, Pearson, 2020.
3. Sutton, R. S. and Barto, A. G., *Reinforcement Learning: An Introduction*, 2nd Edition, MIT Press, 2018.
4. Google Antigravity Assistant (AI Agent): Used for generating simulation scaffolding, automated parameter sweep scripts and document formatting. All code was independently verified and executed.
