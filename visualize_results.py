#!/usr/bin/env python3
"""
Visualization Script for Claude Evaluation Data
Generates charts and graphs to better understand evaluation results.
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
import numpy as np
from pathlib import Path


class EvaluationVisualizer:
    """Creates visualizations from evaluation reports."""
    
    def __init__(self, report_file='evaluation_report.json'):
        """Load evaluation data from JSON report."""
        with open(report_file, 'r') as f:
            self.data = json.load(f)
        
        self.results = self.data.get('results', [])
        
        # Color scheme - professional and accessible
        self.colors = {
            'excellent': '#2E7D32',    # Green
            'very_good': '#66BB6A',    # Light Green
            'good': '#FDD835',         # Yellow
            'acceptable': '#FFA726',   # Orange
            'needs_improvement': '#EF5350'  # Red
        }
        
        self.dimension_colors = {
            'completeness': '#1976D2',
            'professional_tone': '#388E3C',
            'safety': '#D32F2F',
            'helpfulness': '#7B1FA2',
            'format': '#F57C00',
            'characteristics_match': '#0097A7'
        }
    
    def create_all_visualizations(self, output_dir='visualizations'):
        """Generate all visualization types."""
        Path(output_dir).mkdir(exist_ok=True)
        
        print("🎨 Generating visualizations...\n")
        
        # 1. Overall scores comparison
        self.plot_overall_scores(f"{output_dir}/1_overall_scores.png")
        
        # 2. Dimension breakdown by use case
        self.plot_dimension_breakdown(f"{output_dir}/2_dimension_breakdown.png")
        
        # 3. Radar chart for each use case
        self.plot_radar_charts(f"{output_dir}/3_radar_charts.png")
        
        # 4. Heatmap of all scores
        self.plot_heatmap(f"{output_dir}/4_score_heatmap.png")
        
        # 5. Score distribution
        self.plot_score_distribution(f"{output_dir}/5_score_distribution.png")
        
        # 6. Executive summary dashboard
        self.plot_executive_dashboard(f"{output_dir}/6_executive_dashboard.png")
        
        print(f"\n✅ All visualizations saved to '{output_dir}/' directory")
        print("\nGenerated files:")
        print("  1. overall_scores.png - Bar chart comparing use cases")
        print("  2. dimension_breakdown.png - Detailed dimension scores")
        print("  3. radar_charts.png - Radar view of each use case")
        print("  4. score_heatmap.png - Heatmap of all scores")
        print("  5. score_distribution.png - Score distribution across tests")
        print("  6. executive_dashboard.png - One-page summary view")
    
    def plot_overall_scores(self, filename):
        """Bar chart of overall scores by use case."""
        print("  📊 Creating overall scores chart...")
        
        fig, ax = plt.subplots(figsize=(12, 6))
        
        use_cases = [r['use_case'] for r in self.results]
        scores = [r['aggregate_scores']['overall']['mean'] for r in self.results]
        assessments = [r['aggregate_scores']['overall']['assessment'] for r in self.results]
        
        # Color bars based on assessment
        colors = []
        for assessment in assessments:
            if assessment == 'Excellent':
                colors.append(self.colors['excellent'])
            elif assessment == 'Very Good':
                colors.append(self.colors['very_good'])
            elif assessment == 'Good':
                colors.append(self.colors['good'])
            elif assessment == 'Acceptable':
                colors.append(self.colors['acceptable'])
            else:
                colors.append(self.colors['needs_improvement'])
        
        bars = ax.barh(use_cases, scores, color=colors, edgecolor='black', linewidth=1.5)
        
        # Add score labels on bars
        for i, (bar, score, assessment) in enumerate(zip(bars, scores, assessments)):
            width = bar.get_width()
            ax.text(width + 0.05, bar.get_y() + bar.get_height()/2, 
                   f'{score:.2f} ({assessment})',
                   ha='left', va='center', fontweight='bold', fontsize=10)
        
        ax.set_xlabel('Overall Score (out of 5.0)', fontsize=12, fontweight='bold')
        ax.set_title('Claude Performance by Use Case', fontsize=14, fontweight='bold', pad=20)
        ax.set_xlim(0, 5.5)
        ax.axvline(x=4.0, color='gray', linestyle='--', alpha=0.5, label='Very Good threshold')
        ax.grid(axis='x', alpha=0.3)
        ax.legend()
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_dimension_breakdown(self, filename):
        """Grouped bar chart showing all dimensions for each use case."""
        print("  📊 Creating dimension breakdown chart...")
        
        fig, ax = plt.subplots(figsize=(14, 8))
        
        use_cases = [r['use_case'] for r in self.results]
        
        # Get all dimension names (excluding 'overall')
        dimensions = [d for d in self.results[0]['aggregate_scores'].keys() if d != 'overall']
        
        x = np.arange(len(use_cases))
        width = 0.12  # Width of bars
        
        # Plot each dimension
        for i, dimension in enumerate(dimensions):
            scores = [r['aggregate_scores'][dimension]['mean'] for r in self.results]
            offset = (i - len(dimensions)/2) * width
            ax.bar(x + offset, scores, width, 
                  label=dimension.replace('_', ' ').title(),
                  color=self.dimension_colors.get(dimension, '#999999'),
                  edgecolor='black', linewidth=0.5)
        
        ax.set_ylabel('Score (out of 5.0)', fontsize=12, fontweight='bold')
        ax.set_title('Performance Breakdown by Evaluation Dimension', fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels([uc.replace(' ', '\n') for uc in use_cases], fontsize=9)
        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))
        ax.set_ylim(0, 5.5)
        ax.grid(axis='y', alpha=0.3)
        ax.axhline(y=4.0, color='gray', linestyle='--', alpha=0.5)
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_radar_charts(self, filename):
        """Radar charts for each use case showing dimension scores."""
        print("  📊 Creating radar charts...")
        
        n_cases = len(self.results)
        fig, axes = plt.subplots(2, 3, figsize=(15, 10), subplot_kw=dict(projection='polar'))
        axes = axes.flatten()
        
        dimensions = [d for d in self.results[0]['aggregate_scores'].keys() if d != 'overall']
        n_dims = len(dimensions)
        angles = np.linspace(0, 2 * np.pi, n_dims, endpoint=False).tolist()
        angles += angles[:1]  # Complete the circle
        
        for idx, result in enumerate(self.results):
            ax = axes[idx]
            
            # Get scores
            scores = [result['aggregate_scores'][d]['mean'] for d in dimensions]
            scores += scores[:1]  # Complete the circle
            
            # Plot
            ax.plot(angles, scores, 'o-', linewidth=2, label=result['use_case'])
            ax.fill(angles, scores, alpha=0.25)
            
            # Customize
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels([d.replace('_', '\n').title() for d in dimensions], fontsize=8)
            ax.set_ylim(0, 5)
            ax.set_yticks([1, 2, 3, 4, 5])
            ax.grid(True)
            ax.set_title(result['use_case'], fontsize=10, fontweight='bold', pad=20)
        
        # Hide extra subplot
        if n_cases < 6:
            for idx in range(n_cases, 6):
                axes[idx].axis('off')
        
        plt.suptitle('Dimension Scores by Use Case (Radar View)', 
                    fontsize=14, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_heatmap(self, filename):
        """Heatmap showing all scores across dimensions and use cases."""
        print("  📊 Creating score heatmap...")
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        use_cases = [r['use_case'] for r in self.results]
        dimensions = [d for d in self.results[0]['aggregate_scores'].keys() if d != 'overall']
        
        # Build score matrix
        scores = []
        for result in self.results:
            row = [result['aggregate_scores'][d]['mean'] for d in dimensions]
            scores.append(row)
        
        scores = np.array(scores)
        
        # Create heatmap
        im = ax.imshow(scores, cmap='RdYlGn', aspect='auto', vmin=0, vmax=5)
        
        # Set ticks
        ax.set_xticks(np.arange(len(dimensions)))
        ax.set_yticks(np.arange(len(use_cases)))
        ax.set_xticklabels([d.replace('_', '\n').title() for d in dimensions])
        ax.set_yticklabels(use_cases)
        
        # Rotate x labels
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
        
        # Add text annotations
        for i in range(len(use_cases)):
            for j in range(len(dimensions)):
                text = ax.text(j, i, f'{scores[i, j]:.2f}',
                             ha="center", va="center", color="black", fontweight='bold')
        
        ax.set_title('Score Heatmap: All Dimensions × Use Cases', 
                    fontsize=14, fontweight='bold', pad=20)
        
        # Colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Score (out of 5.0)', rotation=270, labelpad=20, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_score_distribution(self, filename):
        """Distribution of scores across all individual tests."""
        print("  📊 Creating score distribution...")
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.flatten()
        
        dimensions = [d for d in self.results[0]['aggregate_scores'].keys() if d != 'overall']
        
        for idx, dimension in enumerate(dimensions):
            ax = axes[idx]
            
            # Collect all individual scores for this dimension
            all_scores = []
            for result in self.results:
                for prompt_result in result['prompt_results']:
                    all_scores.append(prompt_result['scores'][dimension])
            
            # Create histogram
            ax.hist(all_scores, bins=20, range=(0, 5), 
                   color=self.dimension_colors.get(dimension, '#999999'),
                   edgecolor='black', alpha=0.7)
            
            ax.set_xlabel('Score', fontsize=10, fontweight='bold')
            ax.set_ylabel('Frequency', fontsize=10, fontweight='bold')
            ax.set_title(f'{dimension.replace("_", " ").title()}\nMean: {np.mean(all_scores):.2f}', 
                        fontsize=11, fontweight='bold')
            ax.set_xlim(0, 5)
            ax.grid(axis='y', alpha=0.3)
            ax.axvline(x=np.mean(all_scores), color='red', linestyle='--', 
                      linewidth=2, label=f'Mean: {np.mean(all_scores):.2f}')
            ax.legend()
        
        plt.suptitle('Score Distribution Across All Tests', 
                    fontsize=14, fontweight='bold', y=0.995)
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
    
    def plot_executive_dashboard(self, filename):
        """One-page executive summary dashboard."""
        print("  📊 Creating executive dashboard...")
        
        fig = plt.figure(figsize=(16, 10))
        gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)
        
        # Title
        fig.suptitle('Claude Evaluation Executive Dashboard', 
                    fontsize=18, fontweight='bold', y=0.98)
        
        # 1. Overall Scores (top left, spans 2 columns)
        ax1 = fig.add_subplot(gs[0, :2])
        use_cases = [r['use_case'][:25] for r in self.results]  # Truncate long names
        scores = [r['aggregate_scores']['overall']['mean'] for r in self.results]
        bars = ax1.barh(use_cases, scores, color='#1976D2', edgecolor='black', linewidth=1.5)
        for bar, score in zip(bars, scores):
            ax1.text(score + 0.05, bar.get_y() + bar.get_height()/2, 
                    f'{score:.2f}', va='center', fontweight='bold')
        ax1.set_xlabel('Overall Score', fontweight='bold')
        ax1.set_title('Overall Performance by Use Case', fontweight='bold', pad=10)
        ax1.set_xlim(0, 5.5)
        ax1.grid(axis='x', alpha=0.3)
        
        # 2. Summary Stats (top right)
        ax2 = fig.add_subplot(gs[0, 2])
        ax2.axis('off')
        
        avg_score = np.mean(scores)
        total_tests = sum(len(r['prompt_results']) for r in self.results)
        
        summary_text = f"""
        SUMMARY STATISTICS
        
        Average Score: {avg_score:.2f}/5.0
        
        Total Use Cases: {len(self.results)}
        
        Total Tests: {total_tests}
        
        Evaluation Date:
        {self.data.get('evaluation_date', 'N/A')[:10]}
        
        Assessment: {self._get_assessment(avg_score)}
        """
        
        ax2.text(0.1, 0.5, summary_text, transform=ax2.transAxes,
                fontsize=11, verticalalignment='center',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3),
                family='monospace', fontweight='bold')
        
        # 3. Dimension Comparison (middle, spans all columns)
        ax3 = fig.add_subplot(gs[1, :])
        dimensions = [d for d in self.results[0]['aggregate_scores'].keys() if d != 'overall']
        
        # Calculate average for each dimension across all use cases
        dim_averages = []
        for dimension in dimensions:
            avg = np.mean([r['aggregate_scores'][dimension]['mean'] for r in self.results])
            dim_averages.append(avg)
        
        bars = ax3.bar(range(len(dimensions)), dim_averages, 
                      color=[self.dimension_colors.get(d, '#999999') for d in dimensions],
                      edgecolor='black', linewidth=1.5)
        
        for bar, avg in zip(bars, dim_averages):
            ax3.text(bar.get_x() + bar.get_width()/2, avg + 0.1,
                    f'{avg:.2f}', ha='center', fontweight='bold')
        
        ax3.set_xticks(range(len(dimensions)))
        ax3.set_xticklabels([d.replace('_', '\n').title() for d in dimensions])
        ax3.set_ylabel('Average Score', fontweight='bold')
        ax3.set_title('Average Performance by Dimension', fontweight='bold', pad=10)
        ax3.set_ylim(0, 5.5)
        ax3.axhline(y=4.0, color='gray', linestyle='--', alpha=0.5, label='Very Good threshold')
        ax3.grid(axis='y', alpha=0.3)
        ax3.legend()
        
        # 4. Top Performers (bottom left)
        ax4 = fig.add_subplot(gs[2, 0])
        sorted_results = sorted(self.results, 
                               key=lambda x: x['aggregate_scores']['overall']['mean'], 
                               reverse=True)
        top_3 = sorted_results[:3]
        
        ax4.axis('off')
        top_text = "TOP PERFORMERS\n\n"
        for i, r in enumerate(top_3, 1):
            score = r['aggregate_scores']['overall']['mean']
            top_text += f"{i}. {r['use_case'][:30]}\n   Score: {score:.2f}/5.0\n\n"
        
        ax4.text(0.05, 0.95, top_text, transform=ax4.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.3),
                family='monospace')
        
        # 5. Areas for Improvement (bottom middle)
        ax5 = fig.add_subplot(gs[2, 1])
        ax5.axis('off')
        
        # Find lowest scoring dimensions
        dim_scores = [(d, np.mean([r['aggregate_scores'][d]['mean'] for r in self.results])) 
                     for d in dimensions]
        dim_scores.sort(key=lambda x: x[1])
        
        improve_text = "AREAS FOR IMPROVEMENT\n\n"
        for dimension, score in dim_scores[:3]:
            improve_text += f"• {dimension.replace('_', ' ').title()}\n  Score: {score:.2f}/5.0\n\n"
        
        ax5.text(0.05, 0.95, improve_text, transform=ax5.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.3),
                family='monospace')
        
        # 6. Recommendations (bottom right)
        ax6 = fig.add_subplot(gs[2, 2])
        ax6.axis('off')
        
        recommendations = "RECOMMENDATIONS\n\n"
        if avg_score >= 4.5:
            recommendations += "✓ Excellent performance\n✓ Ready for production\n✓ Consider scaling"
        elif avg_score >= 4.0:
            recommendations += "✓ Very good performance\n• Monitor edge cases\n• Optimize prompts"
        elif avg_score >= 3.5:
            recommendations += "• Good baseline\n• Prompt engineering needed\n• Focus on weak areas"
        else:
            recommendations += "• Needs improvement\n• Reevaluate use cases\n• Consider alternatives"
        
        ax6.text(0.05, 0.95, recommendations, transform=ax6.transAxes,
                fontsize=10, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3),
                family='monospace')
        
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
    
    def _get_assessment(self, score):
        """Convert score to assessment."""
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


def main():
    """Main execution function."""
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║        Claude Evaluation Data Visualizer                  ║
    ║                                                            ║
    ║  Generates professional charts and graphs from reports    ║
    ╚════════════════════════════════════════════════════════════╝
    """)
    
    import sys
    
    # Check for report file
    report_file = 'evaluation_report.json'
    if len(sys.argv) > 1:
        report_file = sys.argv[1]
    
    if not Path(report_file).exists():
        print(f"❌ Error: Report file '{report_file}' not found.")
        print("\nPlease run one of these first:")
        print("  python3 claude_evaluator.py")
        print("  python3 compare_models.py")
        return
    
    print(f"📂 Loading data from: {report_file}\n")
    
    # Create visualizer
    viz = EvaluationVisualizer(report_file)
    
    # Generate all visualizations
    viz.create_all_visualizations()
    
    print("\n✨ Visualization complete!")
    print("\nThese charts are perfect for:")
    print("  • Customer presentations")
    print("  • Executive summaries")
    print("  • Technical documentation")
    print("  • Your job application portfolio")


if __name__ == "__main__":
    main()
