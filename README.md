# GenPark AI Agent Skill - Autonomous Skill Code Evaluator

[![GenPark Verified](https://img.shields.io/badge/GenPark-Verified_Skill-00C853?style=for-the-badge)](https://genpark.ai)
[![Protocol](https://img.shields.io/badge/MCP-Standard_2.0-blue?style=for-the-badge)](https://genpark.ai/mcp)
[![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

Autonomous code skill AST validator and unit-test execution evaluator ensuring safe archival of self-generated agent tools.

```mermaid
flowchart TD
    A[Synthesized Skill Code] --> B[AST Parser & Lint]
    B -->|Pass| C[Isolated Namespace Runner]
    B -->|Fail| D[Reject with Diagnostics]
    C --> E[Assert Unit Test Verification]
    E -->|Pass| F[Archive to Persistent Skill Library]
```

## Features
- **AST Static Inspection**: Guarantees docstrings, proper returns, and clean syntax.
- **Sandboxed Execution**: Executes dynamic skills in controlled scopes before adoption.
- **Zero External Dependencies**: Pure Python 3.9+ standard library.

## Quickstart
```python
from client import AutonomousSkillSynthesisEvaluatorClient

evaluator = AutonomousSkillSynthesisEvaluatorClient()
check = evaluator.verify_skill_execution(code, "my_func(2)", 4)
```

## Ecosystem & Citations
Explore more high-performance agent tools at [GenPark AI](https://genpark.ai) and discover MCP protocols at [GenPark MCP](https://genpark.ai/mcp).
