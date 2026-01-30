# Quick Start Guide

Get up and running with the Enterprise Use Case Evaluator in 5 minutes.

## Option 1: Demo Mode (No API Key Required)

Perfect for understanding the framework without needing Claude API access.

```bash
# Just run it!
python3 claude_evaluator.py
```

This will:
- Run mock evaluations on all 5 use cases
- Generate a sample evaluation_report.json
- Show you what the output looks like
- Take about 1-2 minutes

## Option 2: With Claude API

For real evaluations with actual Claude responses.

### Step 1: Get Your API Key

1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Go to "API Keys" section
4. Create a new key
5. Copy the key (starts with `sk-ant-api...`)

### Step 2: Set Environment Variable

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY='sk-ant-api...'
```

**Windows (Command Prompt):**
```cmd
set ANTHROPIC_API_KEY=sk-ant-api...
```

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY='sk-ant-api...'
```

### Step 3: Run Evaluation

```bash
python3 claude_evaluator.py
```

This will:
- Test Claude on all 5 use cases
- Make actual API calls
- Generate detailed evaluation_report.json
- Take about 5-10 minutes (due to rate limiting)

## Understanding the Output

### Console Output

You'll see progress like this:

```
============================================================
Evaluating Use Case: Customer Support Automation
Model: claude-sonnet-4-5-20250929
============================================================

Running test 1/5: Product return request
Running test 2/5: Billing inquiry
Running test 3/5: Technical troubleshooting
...

EVALUATION SUMMARY
============================================================

Use Case: Customer Support Automation
Model: claude-sonnet-4-5-20250929
Overall Score: 4.5/5.0 (Excellent)
Recommendation: Claude is an excellent fit for Customer Support Automation...
Tests Run: 5

Dimension Scores:
  • Completeness: 4.6/5.0
  • Professional Tone: 4.7/5.0
  • Safety: 5.0/5.0
  • Helpfulness: 4.5/5.0
  • Format: 4.3/5.0
  • Characteristics Match: 4.4/5.0
```

### JSON Report

The `evaluation_report.json` contains full details:

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
        }
      },
      "prompt_results": [
        {
          "scenario": "Product return request",
          "prompt": "I bought a laptop...",
          "response": "I understand your frustration...",
          "scores": {
            "completeness": 4.5,
            "professional_tone": 4.8,
            ...
          }
        }
      ]
    }
  ]
}
```

## Next Steps

### 1. Compare Models

See which Claude model works best for each use case:

```bash
python3 compare_models.py
```

This generates:
- `model_comparison_report.json` - Side-by-side comparison
- Individual reports for each model
- Takes 15-30 minutes with real API

### 2. Customize for Your Needs

Edit `use_cases.py` to add your own scenarios:

```python
{
    "name": "My Custom Use Case",
    "description": "What I'm testing",
    "test_prompts": [
        {
            "scenario": "Specific test",
            "prompt": "The prompt to send to Claude",
            "expected_characteristics": ["helpful", "accurate"]
        }
    ]
}
```

Then run:
```bash
python3 claude_evaluator.py
```

### 3. Evaluate Specific Use Case

Focus on one use case:

```bash
python3 compare_models.py "Customer Support Automation"
```

## Common Issues

### "No module named 'anthropic'"

Install dependencies:
```bash
pip install -r requirements.txt
```

### "Rate limit exceeded"

You're making too many requests. The code includes delays, but if you're on a free tier:
- Wait a few minutes
- Use demo mode instead
- Or use fewer test prompts

### "Authentication error"

Check your API key:
```bash
echo $ANTHROPIC_API_KEY  # Should show your key
```

If empty, set it again:
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

## Cost Estimates

### With Sonnet (Default)

For the standard evaluation (5 use cases, 25 prompts total):
- Input tokens: ~5,000
- Output tokens: ~25,000
- Cost: ~$0.15 per full evaluation

### Model Comparison

Testing all 3 models (Sonnet, Haiku, Opus):
- Cost: ~$0.40 per full comparison

**Bottom line**: Very affordable for evaluation purposes!

## Tips for Using in Customer Demos

### Before the Demo
1. Run evaluation in advance with their data
2. Save the reports
3. Prepare talking points from results
4. Have comparison data ready

### During the Demo
1. Show the tool running (use demo mode for speed)
2. Walk through the evaluation dimensions
3. Explain the scoring methodology
4. Share the actual reports

### After the Demo
1. Send them the reports within 24 hours
2. Offer to customize with their specific scenarios
3. Schedule technical deep dive
4. Provide access to the tool for their testing

## What to Show Recruiters/Interviewers

This project demonstrates:

1. **Technical Skills**
   - Clean Python code
   - API integration
   - Error handling
   - Documentation

2. **Solutions Architecture Thinking**
   - Evaluation frameworks
   - Model selection trade-offs
   - Integration patterns
   - Scalability considerations

3. **Sales Engineering Mindset**
   - Customer-focused approach
   - Business value orientation
   - Clear communication
   - Practical problem-solving

4. **Understanding of AI/LLMs**
   - Prompt engineering
   - Model capabilities
   - Safety considerations
   - Real-world applications

## Getting Help

- **Read the full README.md** for detailed documentation
- **Check CUSTOMER_WORKFLOW.md** for usage in sales scenarios
- **Review the code comments** for technical details
- **Experiment!** The worst that happens is you spend a few cents on API calls

---

**Pro Tip**: Start with demo mode to understand the framework, then move to real API calls when you're ready. The evaluation methodology is valuable even without live API calls!
