# Using the Enterprise Use Case Evaluator in Customer Conversations

## Pre-Sales Discovery Workflow

### Phase 1: Initial Discovery Call (Week 1)

**Objective**: Understand customer's AI needs and use cases

**Conversation Flow:**
1. **Ask about current challenges**: "What repetitive tasks are your teams spending time on?"
2. **Identify AI opportunities**: "Have you considered using AI for any of these workflows?"
3. **Gather specific examples**: "Can you walk me through a typical customer support interaction?"

**Action Items:**
- Document 3-5 specific use cases
- Get sample data/prompts from customer
- Understand success criteria

---

### Phase 2: Custom Evaluation (Week 2)

**Objective**: Demonstrate Claude's capabilities with customer's actual scenarios

**Technical Work:**
1. **Customize use_cases.py** with customer scenarios:
```python
{
    "name": "[Customer Company] Customer Support",
    "description": "Real scenarios from [Customer]",
    "test_prompts": [
        {
            "scenario": "Actual customer ticket example",
            "prompt": "[Real customer inquiry from their system]",
            "expected_characteristics": ["responds in under 30 seconds", "includes policy links"]
        }
    ]
}
```

2. **Run evaluation**:
```bash
python claude_evaluator.py
```

3. **Generate results** customized for their criteria

**Customer Presentation:**
- Show the systematic evaluation approach
- Present objective scores
- Discuss where Claude excels and where it needs tuning
- Compare with their current solution (if applicable)

---

### Phase 3: Technical Deep Dive (Week 3)

**Objective**: Address technical questions and integration concerns

**Discussion Topics:**

#### Architecture Integration
- "How would Claude integrate with our existing ticketing system?"
- Show API integration patterns
- Discuss authentication, rate limits, error handling

#### Model Selection
```bash
# Compare models for their use case
python compare_models.py "Customer Support Automation"
```

**Present trade-offs:**
- Sonnet: Best balance of speed and quality
- Haiku: Fastest, most cost-effective for simple tasks
- Opus: Highest quality for complex scenarios

**ROI Discussion:**
- Current cost: X support agents × $Y salary
- With Claude: Reduction in ticket volume by Z%
- Cost of Claude API: Calculate based on expected usage

#### Safety and Compliance
- Discuss evaluation framework for monitoring quality
- Show safety scoring dimension
- Address data privacy concerns
- Explain Constitutional AI approach

---

### Phase 4: Proof of Concept (Week 4-6)

**Objective**: Run live pilot with real data

**Setup:**
1. **Define success metrics** (agreed with customer):
   - Response quality score > 4.0/5.0
   - First response time < 30 seconds
   - Customer satisfaction > 85%
   - Escalation rate < 15%

2. **Deploy evaluation framework**:
```python
# Add to their test environment
evaluator = ClaudeEvaluator(api_key=api_key)
result = evaluator.evaluate_use_case(customer_use_case)

# Set up automated monitoring
if result['aggregate_scores']['overall']['mean'] < 4.0:
    alert_team("Quality threshold not met")
```

3. **Weekly review meetings**:
   - Review evaluation reports
   - Identify prompt improvements
   - Adjust evaluation criteria
   - Track progress toward success metrics

---

## Sample Customer Presentation Outline

### Slide 1: The Challenge
"Your support team handles 10,000 tickets/month. 60% are routine inquiries that could be automated."

### Slide 2: Our Approach
"We've built a systematic evaluation framework to test Claude against your specific scenarios."

### Slide 3: Evaluation Methodology
- 5 use cases tested
- 25 real scenarios from your support tickets
- 6 quality dimensions measured
- Objective scoring (1-5 scale)

### Slide 4: Results Overview
```
Overall Score: 4.5/5.0 (Excellent)
- Completeness: 4.6/5.0
- Professional Tone: 4.7/5.0
- Helpfulness: 4.5/5.0
- Safety: 5.0/5.0
```

### Slide 5: Example Scenarios
Show 2-3 specific examples:
- Customer inquiry → Claude response → Score breakdown
- What Claude did well
- Where it needed improvement

### Slide 6: Model Comparison
"We tested three models to find the best fit for your needs:"
- Sonnet: 4.5/5.0, $3 per 1M tokens
- Haiku: 4.2/5.0, $0.25 per 1M tokens
- Opus: 4.8/5.0, $15 per 1M tokens

**Recommendation**: Start with Sonnet for optimal balance

### Slide 7: Integration Architecture
```
[Customer Ticketing System]
        ↓
    [API Gateway]
        ↓
    [Claude API]
        ↓
    [Evaluation Framework] → [Monitoring Dashboard]
        ↓
    [Response to Customer]
```

### Slide 8: ROI Projection
```
Current State:
- 10,000 tickets/month
- 20 support agents
- $50K/month in labor

With Claude:
- 6,000 tickets automated (60%)
- 12 support agents needed
- $30K/month labor + $2K/month Claude = $32K
- Savings: $18K/month ($216K/year)
- Payback period: Immediate
```

### Slide 9: Risk Mitigation
"How we ensure quality and safety:"
- Continuous evaluation monitoring
- Human review for edge cases
- Escalation protocols
- Regular model fine-tuning

### Slide 10: Next Steps
1. ✅ Evaluation complete (Week 1-2)
2. 📋 Technical deep dive (Week 3)
3. 🚀 POC with 100 tickets (Week 4-6)
4. 📊 Review results and decide (Week 7)
5. 🎯 Production deployment (Week 8+)

---

## Handling Common Objections

### "How do we know it will work for our specific use case?"
"That's exactly why we built this evaluation framework. We don't ask you to take our word for it - we test Claude with your actual scenarios and show you objective results."

### "What about errors or inappropriate responses?"
"Our evaluation includes a safety dimension, and in testing, Claude scored 5.0/5.0 on safety. We also recommend keeping human review for complex cases and implementing monitoring."

### "This seems expensive compared to our current solution."
"Let's look at total cost of ownership. Our evaluation framework helps you select the right model - Haiku for simple tasks, Sonnet for complex ones. Most customers see ROI within the first month."

### "How long will implementation take?"
"Based on similar customers, integration typically takes 2-4 weeks. The evaluation framework we're using today can become your ongoing monitoring system."

### "What if Claude's performance degrades over time?"
"The evaluation framework we've built runs continuously. You can set quality thresholds and get alerts if performance drops. Plus, we'll work with you on prompt optimization."

---

## Technical Tips for Solutions Architects

### Before the Meeting
- Run evaluations with customer's sample data
- Prepare comparison reports
- Have architecture diagrams ready
- Calculate ROI based on their numbers

### During the Meeting
- Lead with business value, not features
- Show objective data, not opinions
- Be honest about limitations
- Focus on their success criteria

### After the Meeting
- Send evaluation reports within 24 hours
- Include next steps and timeline
- Offer to customize further
- Set up follow-up technical session

### Red Flags to Watch For
- Customer expects 100% automation without review
- No clear success metrics defined
- Unrealistic timeline expectations
- Insufficient data for proper evaluation

---

## Success Metrics Dashboard (Suggested)

Track these metrics during POC:

```python
# Example monitoring code
def monitor_performance():
    daily_scores = evaluate_last_24_hours()
    
    metrics = {
        'avg_quality_score': calculate_average(daily_scores),
        'below_threshold_count': count_below_threshold(daily_scores, 4.0),
        'customer_satisfaction': get_csat_scores(),
        'escalation_rate': calculate_escalation_rate(),
        'cost_per_interaction': calculate_cost()
    }
    
    # Alert if thresholds breached
    if metrics['avg_quality_score'] < 4.0:
        send_alert("Quality score below threshold")
    
    return metrics
```

**Weekly Report Should Include:**
- Quality trends
- Cost analysis
- Error patterns
- Improvement opportunities
- Customer feedback

---

## Building Long-Term Partnership

### Month 1-3: POC and Initial Deployment
- Focus on proving value
- Regular check-ins
- Quick iteration on prompts
- Build trust through data

### Month 4-6: Optimization
- Expand to additional use cases
- Fine-tune for cost efficiency
- Share best practices
- Executive business reviews

### Month 7-12: Strategic Expansion
- Identify new opportunities
- Scale successful patterns
- Become trusted advisor
- Plan for next year

---

**Remember**: The evaluation framework isn't just a sales tool - it's the foundation of a healthy, data-driven customer relationship that ensures mutual success.
