"""
Demonstration of genpark-autonomous-code-skill-synthesis-evaluator-skill
"""

from client import AutonomousSkillSynthesisEvaluatorClient

def main():
    evaluator = AutonomousSkillSynthesisEvaluatorClient()

    synthesized_code = (
        "def calculate_compound_interest(principal, rate, years):\n"
        "    return round(principal * ((1 + rate) ** years), 2)\n"
    )

    report = evaluator.verify_skill_execution(
        code_str=synthesized_code,
        test_call_expr="calculate_compound_interest(1000, 0.05, 3)",
        expected_result=1157.63
    )

    print("=== SYNTHESIZED SKILL VERIFICATION REPORT ===")
    print("Status:", report["status"])
    print("Test Passed:", report["passed"])
    print(f"Result: {report.get('actual')} (Expected: {report.get('expected')})")

if __name__ == "__main__":
    main()
