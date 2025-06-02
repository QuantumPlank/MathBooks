# MathBooks

## Completed

## Ongoing
- How to Prove It: A Structured Approach - Velleman, 3nd Edition.

## Planned
- Precalculus - Stitz, Zeager
- Discrete Mathematics with Applications - Epp
- Linear Algebra - Hefferon
- Calculus - Stewart
- Complex Variables and Applications - Churchill
- Differential Equations and Boundary Value Problems - Zill
- Probability and Statistics - DeGroot, Schervish

## Roadmap
```mermaid
---
title: Books
---

flowchart TD
    Logic_and_Proof_Writing["How to Prove It: A Structured Approach - Velleman"]
    Discrete_Mathematics["Discrete Mathematics with Applications - Epp"]
    Set_Theory["Set Theory"]
    Algebra_and_Trigonometry["Precalculus - Stitz, Zeager"]
    Calculus["Calculus - Stewart"]
    Ordinary_Differential_Equations["Differential Equations and Boundary Value Problems - Zill"]
    Partal_Differential_Equations["Partial Differential Equations"]
    Linear_Algebra["Linear Algebra - Hefferon"]
    Probability_and_Statistics["Probability and Statistics - DeGroot, Schervish"]
    Complex_Analysis["Fundamentals of Complex Analysis - Saff, Snider"]
    Real_Analysis["Real Analysis"]
    Abstract_Algebra["Abstract Algebra"]
    Topology["Topology"]
    Combinatorics["Combinatorics"]
    Numerical_Analysis["Numerical Analysis"]
    Functional_Analysis["Functional Analysis"]
    Graph_Theory["Graph Theory"]

    Logic_and_Proof_Writing --> Algebra_and_Trigonometry

    Algebra_and_Trigonometry --> Discrete_Mathematics
    Algebra_and_Trigonometry --> Linear_Algebra
    Algebra_and_Trigonometry --> Calculus

    Calculus --> Complex_Analysis
    Calculus --> Ordinary_Differential_Equations
    Calculus --> Real_Analysis
    Calculus --> Probability_and_Statistics
    Calculus --> Numerical_Analysis

    Complex_Analysis --> Ordinary_Differential_Equations

    Ordinary_Differential_Equations --> Partal_Differential_Equations

    Real_Analysis --> Functional_Analysis
    Real_Analysis --> Topology
    Real_Analysis --> Abstract_Algebra

    Linear_Algebra --> Ordinary_Differential_Equations
    Linear_Algebra --> Real_Analysis

    Discrete_Mathematics --> Combinatorics
    Discrete_Mathematics --> Graph_Theory
    Discrete_Mathematics --> Set_Theory
```