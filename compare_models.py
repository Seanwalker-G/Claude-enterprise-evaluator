#!/usr/bin/env python3
"""
Multi-Model Comparison Tool
Compare Claude Sonnet, Haiku, and Opus across the same use cases.
"""

import os
import json
from claude_evaluator import ClaudeEvaluator
from use_cases import USE_CASES
from datetime import datetime


def compare_models(use_case_name: str = None):
    """
    Compare multiple Claude models on the same use cases.
    
    Args:
        use_case_name: If provided, only evaluate this specific use case
    """
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    
    if not api_key:
        print("\n⚠️  No ANTHROPIC_API_KEY found.")
        print("Running in MOCK MODE for demonstration.\n")
    
    # Models to compare
    models = [
        {
            "name": "Claude Sonnet 4.5",
            "id": "claude-sonnet-4-5-20250929",
            "description": "Balanced intelligence and speed"
        },
        {
            "name": "Claude Haiku 4.5",
            "id": "claude-haiku-4-5-20251001",
            "description": "Fast and efficient"
        },
        {
            "name": "Claude Opus 4.5",
            "id": "claude-opus-4-5-20251101",
            "description": "Most capable model"
        }
    ]
    
    # Filter use cases if specific one requested
    use_cases_to_test = USE_CASES
    if use_case_name:
        use_cases_to_test = [uc for uc in USE_CASES if uc['name'] == use_case_name]
        if not use_cases_to_test:
            print(f"Error: Use case '{use_case_name}' not found.")
            return
    
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║           Multi-Model Comparison for Claude API           ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    all_results = []
    
    # Evaluate each model
    for model in models:
        print(f"\n{'='*60}")
        print(f"Evaluating: {model['name']}")
        print(f"Description: {model['description']}")
        print(f"{'='*60}")
        
        evaluator = ClaudeEvaluator(api_key=api_key)
        
        for use_case in use_cases_to_test:
            result = evaluator.evaluate_use_case(use_case, model=model['id'])
            result['model_name'] = model['name']
            all_results.append(result)
        
        # Save individual model report
        model_safe_name = model['name'].replace(' ', '_').lower()
        evaluator.generate_report(f"evaluation_{model_safe_name}.json")
    
    # Generate comparison report
    comparison_report = generate_comparison_report(all_results)
    
    with open('model_comparison_report.json', 'w') as f:
        json.dump(comparison_report, f, indent=2)
    
    print_comparison_summary(comparison_report)
    
    print("\n✓ Model comparison complete!")
    print("\nGenerated files:")
    print("  • model_comparison_report.json - Side-by-side comparison")
    print("  • evaluation_claude_sonnet_4.5.json - Sonnet detailed results")
    print("  • evaluation_claude_haiku_4.5.json - Haiku detailed results")
    print("  • evaluation_claude_opus_4.5.json - Opus detailed results")


def generate_comparison_report(results):
    """Generate a structured comparison report."""
    
    # Group results by use case
    by_use_case = {}
    for result in results:
        use_case = result['use_case']
        if use_case not in by_use_case:
            by_use_case[use_case] = []
        by_use_case[use_case].append(result)
    
    # Build comparison
    comparisons = []
    for use_case, use_case_results in by_use_case.items():
        comparison = {
            'use_case': use_case,
            'models': []
        }
        
        for result in use_case_results:
            model_data = {
                'model_name': result['model_name'],
                'overall_score': result['aggregate_scores']['overall']['mean'],
                'assessment': result['aggregate_scores']['overall']['assessment'],
                'recommendation': result['recommendation'],
                'dimension_scores': {
                    dim: scores['mean'] 
                    for dim, scores in result['aggregate_scores'].items() 
                    if dim != 'overall'
                }
            }
            comparison['models'].append(model_data)
        
        # Sort by overall score
        comparison['models'].sort(key=lambda x: x['overall_score'], reverse=True)
        comparison['best_model'] = comparison['models'][0]['model_name']
        
        comparisons.append(comparison)
    
    return {
        'comparison_date': datetime.now().isoformat(),
        'use_case_comparisons': comparisons,
        'summary': generate_summary_insights(comparisons)
    }


def generate_summary_insights(comparisons):
    """Generate high-level insights from the comparison."""
    model_wins = {}
    
    for comparison in comparisons:
        best = comparison['best_model']
        model_wins[best] = model_wins.get(best, 0) + 1
    
    return {
        'total_use_cases_compared': len(comparisons),
        'model_wins': model_wins,
        'overall_best_model': max(model_wins, key=model_wins.get) if model_wins else None
    }


def print_comparison_summary(report):
    """Print a human-readable comparison summary."""
    print("\n" + "="*60)
    print("MODEL COMPARISON SUMMARY")
    print("="*60 + "\n")
    
    for comparison in report['use_case_comparisons']:
        print(f"Use Case: {comparison['use_case']}")
        print(f"Best Model: {comparison['best_model']}")
        print("\nModel Rankings:")
        
        for idx, model in enumerate(comparison['models'], 1):
            print(f"  {idx}. {model['model_name']}")
            print(f"     Score: {model['overall_score']}/5.0 ({model['assessment']})")
            print(f"     Recommendation: {model['recommendation']}")
        
        print("\n" + "-"*60 + "\n")
    
    # Overall summary
    summary = report['summary']
    print("OVERALL INSIGHTS:")
    print(f"  • Use cases evaluated: {summary['total_use_cases_compared']}")
    print(f"  • Overall best performing model: {summary['overall_best_model']}")
    print("\n  Model Win Count:")
    for model, wins in summary['model_wins'].items():
        print(f"    • {model}: {wins} use case(s)")


if __name__ == "__main__":
    import sys
    
    # Check if specific use case requested
    use_case = None
    if len(sys.argv) > 1:
        use_case = ' '.join(sys.argv[1:])
        print(f"\nEvaluating specific use case: {use_case}\n")
    
    compare_models(use_case)
