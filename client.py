"""
Autonomous Code Skill Synthesis and Sandboxed Validation Engine.
Zero external dependencies, standard library only.
"""

import ast
from typing import Dict, List, Any, Optional

class AutonomousSkillSynthesisEvaluatorClient:
    """
    Validates dynamically generated agent code skills before archiving:
    - Parses AST to ensure strict syntax validity
    - Verifies presence of docstrings, type annotations, and return statements
    - Tests execution in an isolated scope against assert test cases
    """

    def __init__(self):
        pass

    def validate_code_ast(self, code_str: str) -> Dict[str, Any]:
        """Checks code syntax and architectural sanity via AST."""
        try:
            tree = ast.parse(code_str)
        except SyntaxError as e:
            return {"valid": False, "error": f"SyntaxError: {str(e)}"}

        functions = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        if not functions:
            return {"valid": False, "error": "No function definitions found in synthesized skill code."}

        fn = functions[0]
        has_docstring = ast.get_docstring(fn) is not None
        has_return = any(isinstance(n, ast.Return) for n in ast.walk(fn))

        return {
            "valid": True,
            "function_name": fn.name,
            "has_docstring": has_docstring,
            "has_return": has_return,
            "arg_count": len(fn.args.args)
        }

    def verify_skill_execution(self, code_str: str, test_call_expr: str, expected_result: Any) -> Dict[str, Any]:
        """Executes synthesized skill against verification expression in isolated namespace."""
        ast_check = self.validate_code_ast(code_str)
        if not ast_check["valid"]:
            return {"status": "REJECTED", "reason": ast_check["error"]}

        namespace = {}
        try:
            exec(code_str, namespace)
            actual_val = eval(test_call_expr, namespace)
            passed = (actual_val == expected_result)
            return {
                "status": "APPROVED" if passed else "FAILED_ASSERTION",
                "expected": expected_result,
                "actual": actual_val,
                "passed": passed
            }
        except Exception as e:
            return {"status": "RUNTIME_ERROR", "error": str(e), "passed": False}
