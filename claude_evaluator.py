#!/usr/bin/env python3
"""
Enterprise Use Case Evaluator for Claude API
A tool for evaluating Claude's performance across different enterprise use cases.
"""

import json
import time
from typing import Dict, List, Any
from datetime import datetime
import statistics


class ClaudeEvaluator:
    """
    Evaluates Claude API performance across enterprise use cases.
    Designed to help solutions architects assess fit for customer needs.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the evaluator.
        
        Args:
            api_key: Anthropic API key (if None, uses mock mode for demo)
        """
        self.api_key = api_key
        self.results = []
        self.mock_mode = api_key is None
        
        if not self.mock_mode:
            # Only import if we have an API key
            try:
                import anthropic
                self.client = anthropic.Anthropic(api_key=api_key)
            except ImportError:
                print("Warning: anthropic package not installed. Run: pip install anthropic")
                self.mock_mode = True
    
    def evaluate_use_case(self, use_case: Dict[str, Any], model: str = "claude-sonnet-4-20250514") -> Dict[str, Any]:
        """
        Evaluate Claude's performance on a specific use case.
        
        Args:
            use_case: Dictionary containing use case details
            model: Claude model to evaluate
            
        Returns:
            Dictionary containing evaluation results
        """
        use_case_name = use_case['name']
        test_prompts = use_case['test_prompts']
        
        print(f"\n{'='*60}")
        print(f"Evaluating Use Case: {use_case_name}")
        print(f"Model: {model}")
        print(f"{'='*60}\n")
        
        prompt_results = []
        
        for idx, prompt_test in enumerate(test_prompts, 1):
            print(f"Running test {idx}/{len(test_prompts)}: {prompt_test['scenario']}")
            
            # Get response from Claude (or mock)
            start_time = time.time()
            response = self._get_claude_response(prompt_test['prompt'], model)
            response_time = time.time() - start_time
            
            # Score the response
            scores = self._score_response(
                response=response,
                scenario=prompt_test['scenario'],
                expected_characteristics=prompt_test.get('expected_characteristics', [])
            )
            
            prompt_results.append({
                'scenario': prompt_test['scenario'],
                'prompt': prompt_test['prompt'],
                'response': response,
                'response_time': round(response_time, 2),
                'scores': scores,
                'expected_characteristics': prompt_test.get('expected_characteristics', [])
            })
            
            # Brief delay to respect rate limits
            if not self.mock_mode:
                time.sleep(0.5)
        
        # Calculate aggregate scores
        aggregate_scores = self._calculate_aggregate_scores(prompt_results)
        
        result = {
            'use_case': use_case_name,
            'description': use_case.get('description', ''),
            'model': model,
            'timestamp': datetime.now().isoformat(),
            'prompt_results': prompt_results,
            'aggregate_scores': aggregate_scores,
            'recommendation': self._generate_recommendation(aggregate_scores, use_case_name)
        }
        
        self.results.append(result)
        return result
    
    def _get_claude_response(self, prompt: str, model: str) -> str:
        """Get response from Claude API or return mock response."""
        if self.mock_mode:
            # Return a reasonable mock response for demo purposes
            return f"[Mock Response] This is a simulated response to demonstrate the evaluation framework. In production, this would be Claude's actual response to: '{prompt[:50]}...'"
        
        try:
            message = self.client.messages.create(
                model=model,
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text
        except Exception as e:
            return f"[Error] Failed to get response: {str(e)}"
    
    def _score_response(self, response: str, scenario: str, expected_characteristics: List[str]) -> Dict[str, float]:
        """
        Score a Claude response across multiple dimensions.
        
        In a production system, you might use more sophisticated evaluation
        (e.g., Claude judging Claude, human reviewers, or automated metrics).
        """
        scores = {}
        
        # Accuracy/Completeness (1-5)
        # Check if response addresses the scenario adequately
        if len(response) > 50 and not response.startswith("[Error]"):
            scores['completeness'] = 4.5 if len(response) > 200 else 3.5
        else:
            scores['completeness'] = 2.0
        
        # Professional Tone (1-5)
        # Check for professional language
        professional_indicators = ['please', 'would', 'could', 'thank', 'regarding', 'however']
        unprofessional = ['totally', 'gonna', 'wanna', 'yeah']
        
        pro_score = 3.0  # baseline
        if any(word in response.lower() for word in professional_indicators):
            pro_score += 1.0
        if any(word in response.lower() for word in unprofessional):
            pro_score -= 1.0
        scores['professional_tone'] = min(5.0, max(1.0, pro_score))
        
        # Safety/Appropriateness (1-5)
        # Check for safety concerns (very basic check)
        safety_flags = ['hack', 'illegal', 'harm', 'violence']
        if any(flag in response.lower() for flag in safety_flags):
            scores['safety'] = 2.0
        else:
            scores['safety'] = 5.0
        
        # Helpfulness (1-5)
        # Check if response seems actionable and helpful
        helpful_indicators = ['you can', 'here', 'following', 'steps', 'recommend', 'suggest']
        if any(indicator in response.lower() for indicator in helpful_indicators):
            scores['helpfulness'] = 4.5
        else:
            scores['helpfulness'] = 3.5
        
        # Format Appropriateness (1-5)
        # Check for good structure
        has_structure = '\n' in response or '.' in response
        scores['format'] = 4.0 if has_structure else 3.0
        
        # Expected Characteristics Match (1-5)
        # Check if response matches expected characteristics
        if expected_characteristics:
            matches = sum(1 for char in expected_characteristics 
                         if char.lower() in response.lower())
            scores['characteristics_match'] = min(5.0, (matches / len(expected_characteristics)) * 5)
        else:
            scores['characteristics_match'] = 4.0  # neutral if not specified
        
        return scores
    
    def _calculate_aggregate_scores(self, prompt_results: List[Dict]) -> Dict[str, float]:
        """Calculate aggregate scores across all prompts."""
        all_scores = {}
        
        # Collect all score dimensions
        for result in prompt_results:
            for dimension, score in result['scores'].items():
                if dimension not in all_scores:
                    all_scores[dimension] = []
                all_scores[dimension].append(score)
        
        # Calculate averages
        aggregate = {}
        for dimension, scores in all_scores.items():
            aggregate[dimension] = {
                'mean': round(statistics.mean(scores), 2),
                'min': round(min(scores), 2),
                'max': round(max(scores), 2)
            }
        
        # Calculate overall score
        means = [scores['mean'] for scores in aggregate.values()]
        aggregate['overall'] = {
            'mean': round(statistics.mean(means), 2),
            'assessment': self._get_assessment(statistics.mean(means))
        }
        
        return aggregate
    
    def _get_assessment(self, score: float) -> str:
        """Convert numeric score to assessment."""
        if score >= 4.5:
            return "Excellent"
        elif score >= 4.0:
            return "Very Good"
        elif score >= 3.5:
            return "Good"
        elif score >= 3.0:
            return "Acceptable"
        else:
            return "Needs Improvement"
    
    def _generate_recommendation(self, aggregate_scores: Dict, use_case: str) -> str:
        """Generate a recommendation based on scores."""
        overall = aggregate_scores['overall']['mean']
        
        if overall >= 4.5:
            return f"Claude is an excellent fit for {use_case}. Deploy with confidence."
        elif overall >= 4.0:
            return f"Claude performs very well for {use_case}. Recommended for production use with standard monitoring."
        elif overall >= 3.5:
            return f"Claude is suitable for {use_case} with some customization. Consider prompt engineering optimization."
        elif overall >= 3.0:
            return f"Claude can handle {use_case} but may need significant prompt tuning and evaluation framework."
        else:
            return f"Consider alternative approaches or significant customization for {use_case}."
    
    def generate_report(self, output_file: str = "evaluation_report.json"):
        """Generate a detailed evaluation report."""
        report = {
            'evaluation_date': datetime.now().isoformat(),
            'total_use_cases_evaluated': len(self.results),
            'results': self.results,
            'summary': self._generate_summary()
        }
        
        with open(output_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n{'='*60}")
        print(f"Report saved to: {output_file}")
        print(f"{'='*60}\n")
        
        return report
    
    def _generate_summary(self) -> Dict:
        """Generate summary statistics across all evaluations."""
        if not self.results:
            return {}
        
        overall_scores = []
        for result in self.results:
            overall_scores.append(result['aggregate_scores']['overall']['mean'])
        
        return {
            'average_overall_score': round(statistics.mean(overall_scores), 2),
            'best_use_case': max(self.results, key=lambda x: x['aggregate_scores']['overall']['mean'])['use_case'],
            'evaluation_count': len(self.results)
        }
    
    def print_summary(self):
        """Print a human-readable summary of results."""
        print("\n" + "="*60)
        print("EVALUATION SUMMARY")
        print("="*60 + "\n")
        
        for result in self.results:
            print(f"Use Case: {result['use_case']}")
            print(f"Model: {result['model']}")
            print(f"Overall Score: {result['aggregate_scores']['overall']['mean']}/5.0 ({result['aggregate_scores']['overall']['assessment']})")
            print(f"Recommendation: {result['recommendation']}")
            print(f"Tests Run: {len(result['prompt_results'])}")
            print()
            
            print("Dimension Scores:")
            for dimension, scores in result['aggregate_scores'].items():
                if dimension != 'overall':
                    print(f"  • {dimension.replace('_', ' ').title()}: {scores['mean']}/5.0")
            print("\n" + "-"*60 + "\n")


def main():
    """
    Main execution function demonstrating the evaluator.
    """
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║     Enterprise Use Case Evaluator for Claude API          ║
    ║                                                            ║
    ║  Built to demonstrate Solutions Architecture capabilities ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    # Check for API key
    import os
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    
    if not api_key:
        print("\n⚠️  No ANTHROPIC_API_KEY found in environment.")
        print("Running in MOCK MODE for demonstration purposes.\n")
        print("To run with real API calls:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'\n")
    else:
        print("\n✓ API key found. Running with live Claude API.\n")
    
    # Initialize evaluator
    evaluator = ClaudeEvaluator(api_key=api_key)
    
    # Load use cases
    from use_cases import USE_CASES
    
    # Evaluate each use case
    for use_case in USE_CASES:
        evaluator.evaluate_use_case(use_case)
    
    # Generate and save report
    evaluator.generate_report("evaluation_report.json")
    
    # Print summary
    evaluator.print_summary()
    
    print("\n✓ Evaluation complete!")
    print("\nNext steps:")
    print("  • Review evaluation_report.json for detailed results")
    print("  • Customize use_cases.py with your own test scenarios")
    print("  • Run compare_models.py to evaluate multiple Claude models")


if __name__ == "__main__":
    main()
