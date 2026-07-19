# Forge Bootcamp

## From Software Engineer to LLM Systems Engineer

> Mission: Build a production-style AI application while learning the
> engineering practices behind modern LLM systems.

------------------------------------------------------------------------

# Overall Roadmap

1.  Development Environment
2.  Core LLM
3.  Prompt Engineering
4.  Configuration
5.  Code Reviewer v1
6.  Architecture Refactor
7.  Loop Engineering
8.  Tool Use
9.  Multi-Agent Design
10. Memory
11. Harness Engineering
12. Experimentation
13. Production Readiness

------------------------------------------------------------------------

# Standard Template for Every Stage

Each stage contains: - 🎯 Objective - 🧠 Concepts - 📚 Reading - 🛠
Tasks - ✅ Acceptance Criteria - ⭐ Stretch Goal - 💭 Reflection - 📂
Project Structure - 📝 Git Milestone - ⏱ Estimated Time

------------------------------------------------------------------------

# Stage 0 --- Development Environment

## 🎯 Objective

Create a professional Python project that will serve as the foundation
for all future work.

## 🧠 Concepts

-   Project structure
-   Git
-   Virtual environments
-   uv
-   pyproject.toml
-   Dependency management
-   Environment variables
-   Ruff formatting/linting
-   Basic testing

## 📚 Reading

-   uv documentation
-   Python packaging (pyproject.toml)
-   Git basics

## 🛠 Tasks

1.  Install Python (latest stable supported version).
2.  Install uv.
3.  Create project folder `forge/`.
4.  Initialize Git.
5.  Initialize project with uv.
6.  Create folders:
    -   src/
    -   tests/
    -   prompts/
    -   docs/
    -   data/
    -   scripts/
7.  Create `.env.example`.
8.  Create `.gitignore`.
9.  Install Ruff and pytest.
10. Create README.md.

## ✅ Acceptance Criteria

-   `uv run` works.
-   Git repository initialized.
-   Project structure created.
-   Dependencies managed with uv.
-   README explains the project.

## ⭐ Stretch Goal

Set up pre-commit hooks.

## 💭 Reflection

-   Why use uv instead of pip?
-   Why is pyproject.toml important?
-   Why keep prompts outside Python code?

## 📂 Structure

    forge/
    ├── src/
    ├── tests/
    ├── prompts/
    ├── docs/
    ├── data/
    ├── scripts/
    ├── pyproject.toml
    ├── uv.lock
    ├── .env.example
    ├── .gitignore
    └── README.md

## 📝 Git Milestone

`feat: initialize Forge project`

## ⏱ Estimated Time

2--3 hours

------------------------------------------------------------------------

# Stages 1--13 Overview

Each remaining stage follows the same template.

## Stage 1 --- Core LLM

Build `hello_llm.py` using a direct API call. No frameworks.

## Stage 2 --- Prompt Engineering

Store prompts as versioned assets. Compare prompt strategies.

## Stage 3 --- Configuration

Centralize model settings, API keys, temperature, and timeouts.

## Stage 4 --- Code Reviewer v1

Single-pass code review application.

## Stage 5 --- Architecture Refactor

Separate responsibilities into modules.

## Stage 6 --- Loop Engineering

Implement Review → Critique → Improve → Judge.

## Stage 7 --- Tool Use

Add file reading, Python execution, tests, and documentation lookup.

## Stage 8 --- Multi-Agent Design

Introduce specialist agents and a coordinating judge.

## Stage 9 --- Memory

Add short-term and long-term memory.

## Stage 10 --- Harness Engineering

Build evaluation datasets, automated metrics, and reports.

## Stage 11 --- Experimentation

Benchmark prompts, loops, and models.

## Stage 12 --- Production Readiness

Improve logging, configuration, packaging, and documentation.

------------------------------------------------------------------------

# Engineering Rules

1.  Build one capability at a time.
2.  Measure before optimizing.
3.  Keep every stage runnable.
4.  Commit after every milestone.
5.  Prefer understanding over abstraction.
6.  Record every experiment.
7.  Let evidence guide decisions.

------------------------------------------------------------------------

# End Goal

By the end of Forge you will be able to: - Design robust prompts - Build
iterative LLM workflows - Engineer agent systems - Create evaluation
harnesses - Run reproducible experiments - Measure quality, latency, and
cost - Structure production-ready AI applications

This repository should become your reference architecture for future AI
projects.
