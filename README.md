# Enterprise Use Case Evaluator for Claude API

A practical tool for Solutions Architects and Sales Engineers to evaluate Claude's performance across different enterprise use cases. Built to demonstrate technical expertise, customer-centric thinking, and understanding of AI implementation patterns.

## 🎯 Purpose

In pre-sales conversations, customers often ask: "How do I know Claude will work for my use case?" This tool provides a systematic framework to:

- **Evaluate Claude's fit** for specific business scenarios
- **Generate objective performance metrics** across multiple dimensions
- **Compare different Claude models** (Sonnet, Haiku, Opus) for cost/performance optimization
- **Build customer confidence** with data-driven assessments
- **Identify areas** requiring prompt engineering or fine-tuning

## 🏗️ What This Demonstrates

### Solutions Architecture Skills
- Understanding of evaluation frameworks and success metrics
- Ability to translate business requirements into technical tests
- Knowledge of model selection trade-offs (cost vs. capability)
- Customer-focused approach to technical validation

### Technical Capabilities
- Claude API integration and best practices
- Python development with clean, maintainable code
- Error handling and production-readiness considerations
- Documentation and knowledge sharing

### Pre-Sales Mindset
- Proactive risk assessment and mitigation
- Clear communication of technical concepts
- Focus on business outcomes, not just features
- Scalable approach to customer evaluation

## 🚀 Quick Start

### Installation

```bash
# Clone or download this repository
git clone <your-repo-url>
cd claude-evaluator

# Install dependencies
pip install -r requirements.txt

# Set your Anthropic API key
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Basic Usage

```bash
# Run evaluation on all use cases with default model (Sonnet)
python claude_evaluator.py

# Compare all three Claude models
python compare_models.py

# Evaluate a specific use case across all models
python compare_models.py "Customer Support Automation"
```

### Demo Mode (No API Key Required)

```bash
# Run without API key to see the framework structure
python claude_evaluator.py
```

## 📊 Use Cases Included

The tool evaluates Claude across five common enterprise scenarios:

1. **Customer Support Automation**
   - Product returns, billing inquiries, technical troubleshooting
   - Evaluates: Empathy, problem-solving, de-escalation

2. **Contract Analysis**
   - Term extraction, risk identification, compliance checking
   - Evaluates: Accuracy, completeness, legal reasoning

3. **Data Extraction and Analysis**
   - Structured data extraction, sentiment analysis, pattern recognition
   - Evaluates: Accuracy, consistency, insight quality

4. **Content Generation**
   - Professional emails, product descriptions, executive summaries
   - Evaluates: Tone, clarity, persuasiveness

5. **Code Documentation and Explanation**
   - Code explanation, API documentation, technical writing
   - Evaluates: Accuracy, clarity, helpfulness

## 🎯 Evaluation Dimensions

Each response is scored across six dimensions (1-5 scale):

- **Completeness**: Does it fully address the scenario?
- **Professional Tone**: Is the language appropriate for enterprise use?
- **Safety**: Are there any concerning outputs?
- **Helpfulness**: Is it actionable and useful?
- **Format**: Is it well-structured and readable?
- **Characteristics Match**: Does it meet expected requirements?

## 📈 Output Reports

### Individual Evaluation Report (`evaluation_report.json`)
```json
{
  "evaluation_date": "2025-01-30T10:30:00",
  "total_use_cases_evaluated": 5,
  "results": [
    {
      "use_case": "Customer Support Automation",
      "model": "claude-sonnet-4-5-20250929",
      "aggregate_scores": {
        "overall": {
          "mean": 4.5,
          "assessment": "Excellent"
        },
        "completeness": {"mean": 4.6, "min": 4.2, "max": 5.0},
        ...
      },
      "recommendation": "Claude is an excellent fit for Customer Support Automation..."
    }
  ]
}
```

### Model Comparison Report (`model_comparison_report.json`)
Side-by-side comparison showing which model performs best for each use case, helping with cost/performance optimization decisions.

## 🔧 Customization

### Adding Your Own Use Cases

Edit `use_cases.py` to add custom scenarios:

```python
{
    "name": "Your Use Case Name",
    "description": "Description of what you're evaluating",
    "test_prompts": [
        {
            "scenario": "Specific test scenario",
            "prompt": "The actual prompt to send to Claude",
            "expected_characteristics": ["quality1", "quality2"]
        }
    ]
}
```

### Customizing Scoring

Modify the `_score_response()` method in `claude_evaluator.py` to adjust evaluation criteria:

```python
def _score_response(self, response: str, scenario: str, expected_characteristics: List[str]):
    # Add your custom scoring logic
    scores = {}
    scores['your_dimension'] = calculate_score(response)
    return scores
```

### Advanced: Human-in-the-Loop Evaluation

For production use, consider:
- Adding manual review steps for critical use cases
- Using Claude to evaluate Claude (meta-evaluation)
- Integrating with your existing evaluation frameworks
- A/B testing with real customer data

## 💡 Using This in Customer Conversations

### Discovery Phase
1. **Identify customer use cases**: "What are your top 3 use cases for AI?"
2. **Run targeted evaluations**: Customize test prompts with customer's actual scenarios
3. **Present results**: Show objective scores and recommendations

### Proof of Concept
1. **Baseline evaluation**: Run standard tests to establish performance
2. **Prompt engineering**: Iterate on prompts to optimize scores
3. **Model selection**: Compare Sonnet vs. Haiku for cost efficiency
4. **Success criteria**: Define what "good enough" looks like with customer

### Production Planning
1. **Evaluation framework**: Deploy this tool as ongoing monitoring
2. **Quality metrics**: Set thresholds for production deployment
3. **Continuous improvement**: Track performance over time

## 🏗️ Architecture Considerations

### For Enterprise Deployment

**Integration Points:**
- API gateway for rate limiting and monitoring
- Logging infrastructure for audit trails
- Evaluation data warehouse for trend analysis
- Alert system for quality degradation

**Scalability:**
- Batch processing for large-scale evaluations
- Caching for repeated prompts
- Parallel execution across models
- Cost optimization strategies

**Security:**
- API key management (secrets management)
- Data privacy considerations
- Compliance requirements (GDPR, HIPAA, etc.)
- Content filtering and safety checks

## 📚 Next Steps

### For Sales Engineering
- Customize use cases to match your product domain
- Add company-specific evaluation criteria
- Integrate with your demo environment
- Create customer-facing reports

### For Solutions Architecture
- Design integration patterns for Claude API
- Build reusable templates for common use cases
- Develop best practices documentation
- Create training materials for customers

### For Production Deployment
- Add robust error handling and retry logic
- Implement comprehensive logging
- Set up monitoring and alerting
- Create automated regression testing

## 🤝 Contributing

This tool is designed to be extended and customized. Ideas for enhancements:

- [ ] Web-based UI using Streamlit or Gradio
- [ ] Visualization dashboards for results
- [ ] Integration with existing evaluation tools
- [ ] Multi-language support
- [ ] Industry-specific use case templates
- [ ] Automated benchmark comparisons
- [ ] Cost tracking and optimization

## 📄 License

This project is created for demonstration purposes as part of a Solutions Architect application to Anthropic.

## 👤 Author

**[Your Name]**
- Sales Engineer with 5 years experience at Alteryx
- Passionate about helping enterprises adopt AI responsibly
- Focus on customer success and technical excellence

---

## 🎓 Learning Resources

To deepen understanding of Claude and LLM evaluation:

- [Anthropic Documentation](https://docs.anthropic.com)
- [Claude API Reference](https://docs.anthropic.com/claude/reference)
- [Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Constitutional AI Paper](https://arxiv.org/abs/2212.08073)

---

**Built with ❤️ to help enterprises adopt AI safely and effectively**
