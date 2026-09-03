# Python Piscine — Module 04: Data-Oriented Design & Advanced Paradigms

[![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Linter Flake8](https://img.shields.io/badge/Linter-Flake8-4B8BBE?logo=python&logoColor=white)](https://flake8.pycqa.org/)
[![42 Norm Compliant](https://img.shields.io/badge/42_Norm-Compliant-000000?logo=42&logoColor=white)](https://42.fr/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero_External-success)](#)

Production-grade implementations exploring advanced Python paradigms: variable-argument dispatch tables, stateful lexical closures, parameterized function decorators, and dataclass lifecycle metaprogramming under strict zero-dependency and PEP 8 constraints.

---

## 📌 Academic & Project Context

Developed as the final module of the **42 Network Post-Common Core Python Piscine** (*Module 04: DoD - Data-Oriented Design*). The module focuses on the inner mechanics of the Python runtime: dynamic argument packing/unpacking, closures, function wrappers, and declarative data structures.

### Strict Engineering Constraints
* **Zero External Dependencies:** Only the standard library (`random`, `string`, `dataclasses`, `typing`) is allowed. No numerical engines like NumPy or SciPy.
* **Execution Hygiene:** Zero code in the global scope; all executable logic is strictly encapsulated within functions and classes.
* **Norm & Compliance:** Strict compliance with PEP 8 checked via `flake8` (`max-line-length = 79`, rigorous spacing, no wildcard imports).
* **Self-Documenting Codebase:** Every module, class, method, and nested closure must define a clear and concise `__doc__` docstring.
* **Defensive Fault Isolation:** All calculation exceptions must be trapped and handled gracefully to prevent unhandled runtime aborts.

---

## 🏗️ Architecture & Modules

```text
Python04/
├── ex00/
│   ├── statistics.py    # Arbitrary *args/**kwargs dispatcher & statistical engine
│   └── tester.py        # Functional test harness
├── ex01/
│   ├── in_out.py        # Stateful closures & functional composition
│   └── tester.py        # Iterative execution validator
├── ex02/
│   ├── callLimit.py     # 3-tier parameterized decorator for invocation quotas
│   └── tester.py        # Concurrency & call-quota test harness
└── ex03/
    ├── new_student.py   # PEP 557 dataclass with lifecycle field derivation
    └── tester.py        # Attribute access & init-guard test harness
```

### Module Summary

| Module | Core Concept | Responsibility |
| :--- | :--- | :--- |
| **`ex00/statistics.py`** | Variable Arguments & Dynamic Dispatch | Computes Mean, Median, Quartiles (Q1/Q3 exclusive hinges), Variance, and Standard Deviation from arbitrary `*args` and `**kwargs`. |
| **`ex01/in_out.py`** | Lexical Closures & `nonlocal` State | Implements higher-order functions that encapsulate mutable state across repeated invocations without global variables or classes. |
| **`ex02/callLimit.py`** | Parameterized Function Decorators | Constructs an execution gatekeeper limiting callable execution count, isolating counters per decorated callable. |
| **`ex03/new_student.py`** | Dataclass Metaprogramming (`PEP 557`) | Models student entities with auto-generated logins and randomized IDs, enforcing initialization invariants via `init=False`. |

---

## 🧠 Engineering Highlights & Learnings

### 1. Zero-Dependency Descriptive Statistics & Dispatching (`ex00`)
Instead of relying on NumPy, statistical algorithms were built from mathematical fundamentals:
* **Quantile Partitioning:** Quartile calculations implement exclusive median hinges ($Q1$ and $Q3$ computed over split sub-arrays around the central median), properly handling both even and odd dataset lengths.
* **Locally Scoped Dispatcher:** To satisfy the strict constraint forbidding global execution, the function lookup dictionary is instantiated strictly within `ft_statistics()`, mapping arbitrary keyword arguments to calculation routines while trapping `ValueError` and `TypeError` inputs without crashing.

### 2. Stateful Closures via Lexical Scope (`ex01`)
Demonstrates function-oriented state preservation using the `nonlocal` keyword. Rather than relying on class instances with `__call__` or polluting outer scopes, `outer()` constructs an isolated closure enclosing `x`. Successive calls apply recursive transformations ($f(x) \to x'$) while keeping state private and garbage-collected once dereferenced.

### 3. Multi-Tier Decorator Architecture (`ex02`)
Implements a 3-level higher-order wrapper pattern:
$$\text{callLimit}(\text{limit}) \longrightarrow \text{callLimiter}(\text{function}) \longrightarrow \text{limit\_function}(*\text{args}, **\text{kwargs})$$
* **Per-Instance State Isolation:** The call counter `count` is anchored within the scope of `callLimiter(function)`. This guarantees that if multiple distinct functions are decorated with the same limiter factory, each maintains an independent quota and execution count without state bleed.

### 4. Enforcing Invariants with Dataclass Lifecycle Hooks (`ex03`)
Leverages Python 3.7+ `dataclasses.field(init=False)` and the `__post_init__` hook:
* **Initialization Guard:** Preventing callers from manually passing an `id` or `login` to `Student.__init__()` at instantiation time, raising standard `TypeError` on invalid injection.
* **Deterministic Derivation:** Post-initialization derives attributes internally (`name[0] + surname` and 15-character random token generation) without requiring verbose manual boilerplate.

---

## 🚀 Quick Start

### 1. Environment Setup

Ensure Python 3.10 is installed and activate a virtual environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
pip install flake8
```

### 2. Static Code Analysis (Linter)

Verify that all modules strictly conform to PEP 8:

```bash
flake8 ex00/statistics.py ex01/in_out.py ex02/callLimit.py ex03/new_student.py
```

### 3. Run Test Suites

Execute any module's test harness:

```bash
python3 ex00/tester.py
python3 ex01/tester.py
python3 ex02/tester.py
python3 ex03/tester.py
```

---

## 💻 Showcase

### `ex00`: Statistical Dispatch & Fault Isolation
Handles valid data streams and traps empty or uncomputable requests without unhandled tracebacks:

```bash
$ python3 ex00/tester.py
mean : 95.6
median : 42.0
quartile : [6.0, 212.0]
------
std : 17982.70124086944
var : 323377543.9183673
------
------
ERROR
ERROR
ERROR
ERROR
ERROR
```

### `ex02`: Decorator Invocation Quota Enforcement
Demonstrates independent call counting across decorated targets and graceful throttling:

```bash
$ python3 ex02/tester.py
f()
g()
f()
Error: <function g at 0x102c4a560> call too many times
f()
Error: <function g at 0x102c4a560> call too many times
```

### `ex03`: Dataclass Contract & Init Guard
Verifies automatic field synthesis and rejection of unauthorized attribute overrides:

```bash
$ python3 ex03/tester.py
Student(name='Edward', surname='agle', active=True, login='Eagle', id='ibodyyfespclffp')
Student.__init__() got an unexpected keyword argument 'id'
```
