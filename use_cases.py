"""
Enterprise Use Case Definitions
Contains test scenarios representing common enterprise AI use cases.
"""

USE_CASES = [
    {
        "name": "Customer Support Automation",
        "description": "Evaluating Claude's ability to handle customer support inquiries with appropriate tone, accuracy, and helpfulness.",
        "test_prompts": [
            {
                "scenario": "Product return request",
                "prompt": "I bought a laptop from your store 3 weeks ago and it's not working properly. The screen flickers and sometimes goes black. I'd like to return it for a refund. Can you help me with this process?",
                "expected_characteristics": ["empathy", "clear steps", "policy information", "helpful"]
            },
            {
                "scenario": "Billing inquiry",
                "prompt": "I was charged twice for my subscription this month. My credit card shows two charges of $49.99 on the same day. This is my account ID: ACC-12345. Can you explain what happened?",
                "expected_characteristics": ["acknowledge issue", "investigation", "resolution steps", "professional"]
            },
            {
                "scenario": "Technical troubleshooting",
                "prompt": "The mobile app keeps crashing whenever I try to upload a photo. I've tried restarting my phone but it still doesn't work. I'm using an iPhone 12 with iOS 16.",
                "expected_characteristics": ["troubleshooting steps", "specific", "patient", "technical"]
            },
            {
                "scenario": "Angry customer escalation",
                "prompt": "This is ridiculous! I've been on hold for 30 minutes and nobody can help me. Your service is terrible and I want to speak to a manager RIGHT NOW!",
                "expected_characteristics": ["calm", "empathy", "de-escalation", "solution-focused"]
            },
            {
                "scenario": "Product information request",
                "prompt": "I'm considering upgrading to your premium plan. Can you tell me what additional features I would get compared to the basic plan?",
                "expected_characteristics": ["clear comparison", "value proposition", "informative", "encouraging"]
            }
        ]
    },
    {
        "name": "Contract Analysis",
        "description": "Evaluating Claude's ability to analyze legal documents, extract key terms, and identify potential issues.",
        "test_prompts": [
            {
                "scenario": "Extract key terms",
                "prompt": "Please review this clause from a vendor contract: 'The Vendor shall deliver the Software within 90 days of contract execution. If delivery is delayed beyond 120 days, Client may terminate without penalty and receive full refund of any advance payments. Payment terms are Net 30 from delivery acceptance.' What are the key terms I should be aware of?",
                "expected_characteristics": ["deadlines", "penalties", "payment terms", "termination rights"]
            },
            {
                "scenario": "Risk identification",
                "prompt": "Analyze this liability clause: 'Vendor's total liability under this Agreement shall not exceed the fees paid by Client in the 12 months preceding the claim. Vendor shall not be liable for any indirect, consequential, or punitive damages.' What risks should our legal team consider?",
                "expected_characteristics": ["liability cap", "exclusions", "risk assessment", "implications"]
            },
            {
                "scenario": "Compare contract versions",
                "prompt": "Version 1 states: 'Either party may terminate with 30 days notice.' Version 2 states: 'Client may terminate with 30 days notice; Vendor requires 90 days notice.' What changed and what's the impact?",
                "expected_characteristics": ["comparison", "changes identified", "impact analysis", "clear"]
            },
            {
                "scenario": "Compliance check",
                "prompt": "Our company policy requires all vendor contracts to include: (1) GDPR compliance clause, (2) Right to audit, (3) Data breach notification within 48 hours. Does this contract excerpt meet these requirements? 'Vendor shall comply with applicable data protection laws. Client may audit Vendor's practices annually. Vendor will notify Client of security incidents.'",
                "expected_characteristics": ["requirement check", "gaps identified", "specific", "thorough"]
            },
            {
                "scenario": "Plain language summary",
                "prompt": "Summarize this complex clause in simple terms for our procurement team: 'Notwithstanding any provision herein to the contrary, in the event of a Material Adverse Change in either party's financial condition, the non-affected party may, at its sole discretion, demand adequate assurances of performance or suspend performance pending receipt thereof.'",
                "expected_characteristics": ["simplified", "clear", "actionable", "accurate"]
            }
        ]
    },
    {
        "name": "Data Extraction and Analysis",
        "description": "Evaluating Claude's ability to extract, structure, and analyze data from unstructured text.",
        "test_prompts": [
            {
                "scenario": "Extract structured data from email",
                "prompt": "Extract the key information from this email in a structured format: 'Hi team, following up from our meeting. We agreed to launch the Q2 campaign on April 15th, budget of $250K, targeting the 25-45 age demographic in Northeast region. Sarah will lead creative, Mike handles media buying. First review meeting is March 30th at 2pm EST.'",
                "expected_characteristics": ["structured output", "complete", "accurate dates", "organized"]
            },
            {
                "scenario": "Sentiment analysis",
                "prompt": "Analyze the sentiment of these customer reviews and categorize them: (1) 'Amazing product! Exceeded expectations.' (2) 'It's okay, nothing special.' (3) 'Terrible quality, wouldn't recommend.' (4) 'Good value for the price.'",
                "expected_characteristics": ["sentiment scores", "categorization", "reasoning", "consistent"]
            },
            {
                "scenario": "Financial data extraction",
                "prompt": "Extract financial metrics from this earnings report excerpt: 'Revenue for Q4 2024 reached $1.2B, up 15% YoY. Operating margin improved to 22%, compared to 19% in Q4 2023. We added 250K new customers, bringing total to 2.1M. Customer acquisition cost decreased to $180 from $215.'",
                "expected_characteristics": ["metrics identified", "changes noted", "structured", "complete"]
            },
            {
                "scenario": "Pattern identification",
                "prompt": "Analyze these support ticket descriptions and identify common issues: (1) 'Login button not working' (2) 'Can't reset my password' (3) 'Login page loads slowly' (4) 'Forgot password link is broken' (5) 'Account locked after failed logins'",
                "expected_characteristics": ["patterns found", "categorization", "insights", "actionable"]
            },
            {
                "scenario": "Data validation",
                "prompt": "Check this data for inconsistencies: Name: John Smith, DOB: 1995-02-30, Email: john.smith@company, Phone: 555-12345, Start Date: 2024-15-03. Flag any issues.",
                "expected_characteristics": ["errors found", "specific", "validation rules", "corrections"]
            }
        ]
    },
    {
        "name": "Content Generation",
        "description": "Evaluating Claude's ability to generate various types of business content with appropriate tone and quality.",
        "test_prompts": [
            {
                "scenario": "Professional email",
                "prompt": "Write a professional email to a client informing them that their project will be delayed by 2 weeks due to unexpected technical challenges, but we're working overtime to minimize impact.",
                "expected_characteristics": ["professional", "apologetic", "solution-focused", "clear"]
            },
            {
                "scenario": "Product description",
                "prompt": "Write a compelling product description for enterprise project management software that emphasizes ease of use, real-time collaboration, and integration with existing tools. Target audience is IT managers.",
                "expected_characteristics": ["benefits-focused", "technical credibility", "persuasive", "professional"]
            },
            {
                "scenario": "Executive summary",
                "prompt": "Create an executive summary of this situation: Our customer satisfaction scores dropped from 87% to 78% over the last quarter. Main complaints are long wait times (increased from 2 to 5 minutes) and incomplete issue resolution (down from 92% to 81% first-call resolution). We've identified root causes as staff turnover (30%) and inadequate training.",
                "expected_characteristics": ["concise", "key points", "data-driven", "executive-appropriate"]
            },
            {
                "scenario": "FAQ generation",
                "prompt": "Generate 3 FAQ entries for a new feature that allows users to export their data to CSV format. The feature is in the Settings menu under 'Data Management.'",
                "expected_characteristics": ["clear questions", "helpful answers", "step-by-step", "user-friendly"]
            },
            {
                "scenario": "Meeting agenda",
                "prompt": "Create a meeting agenda for a quarterly business review with our top client. Topics to cover: Q4 performance results, upcoming renewal discussion, new feature requests, technical roadmap for next year. Meeting is 90 minutes.",
                "expected_characteristics": ["structured", "time allocations", "clear objectives", "professional"]
            }
        ]
    },
    {
        "name": "Code Documentation and Explanation",
        "description": "Evaluating Claude's ability to understand code and generate clear technical documentation.",
        "test_prompts": [
            {
                "scenario": "Explain code functionality",
                "prompt": "Explain what this Python function does: `def calculate_discount(price, customer_type): if customer_type == 'premium': return price * 0.8 elif customer_type == 'standard': return price * 0.9 else: return price`",
                "expected_characteristics": ["clear explanation", "logic described", "examples", "accurate"]
            },
            {
                "scenario": "Generate API documentation",
                "prompt": "Write API documentation for this endpoint: POST /api/users creates a new user account. Required fields: email (string), password (string, min 8 chars), name (string). Returns 201 on success with user ID, 400 if validation fails, 409 if email already exists.",
                "expected_characteristics": ["complete", "structured", "examples", "error codes"]
            },
            {
                "scenario": "Code review comments",
                "prompt": "Review this code and suggest improvements: `users = [] for user in all_users: if user.active == True: if user.role == 'admin': users.append(user)`",
                "expected_characteristics": ["specific suggestions", "best practices", "clear reasoning", "constructive"]
            },
            {
                "scenario": "Create README section",
                "prompt": "Write a 'Getting Started' section for a README for a REST API client library. Users need to install via npm, initialize with API key, and make their first request.",
                "expected_characteristics": ["step-by-step", "code examples", "clear", "beginner-friendly"]
            },
            {
                "scenario": "Debug explanation",
                "prompt": "Explain why this code might fail: `data = {'name': 'Alice'} print(data['age'])`",
                "expected_characteristics": ["identifies error", "explanation", "solution", "educational"]
            }
        ]
    }
]


# Additional metadata for use cases
USE_CASE_METADATA = {
    "Customer Support Automation": {
        "typical_volume": "High (1000s of interactions/day)",
        "business_impact": "Direct customer satisfaction, reduced support costs",
        "key_considerations": ["Tone consistency", "Escalation handling", "Brand voice alignment"],
        "integration_points": ["CRM systems", "Ticketing systems", "Knowledge bases"]
    },
    "Contract Analysis": {
        "typical_volume": "Medium (100s of contracts/month)",
        "business_impact": "Risk mitigation, faster contract review cycles",
        "key_considerations": ["Accuracy critical", "Legal review still required", "Liability concerns"],
        "integration_points": ["Document management", "CLM systems", "E-signature platforms"]
    },
    "Data Extraction and Analysis": {
        "typical_volume": "Variable (depends on data sources)",
        "business_impact": "Operational efficiency, data-driven insights",
        "key_considerations": ["Accuracy validation", "Structured output formats", "Error handling"],
        "integration_points": ["Data warehouses", "BI tools", "ETL pipelines"]
    },
    "Content Generation": {
        "typical_volume": "High (100s-1000s of pieces/month)",
        "business_impact": "Marketing efficiency, consistent messaging",
        "key_considerations": ["Brand consistency", "Human review recommended", "SEO optimization"],
        "integration_points": ["CMS", "Marketing automation", "Social media tools"]
    },
    "Code Documentation and Explanation": {
        "typical_volume": "Medium (daily for dev teams)",
        "business_impact": "Developer productivity, knowledge sharing",
        "key_considerations": ["Accuracy", "Up-to-date with languages", "Security awareness"],
        "integration_points": ["IDE plugins", "Documentation systems", "Version control"]
    }
}
