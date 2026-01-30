#!/bin/bash

# Enterprise Use Case Evaluator - Setup Script
# This script helps you get started quickly

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     Enterprise Use Case Evaluator for Claude API          ║"
echo "║                    Setup Script                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

if [ $? -ne 0 ]; then
    echo "❌ Python 3 is required but not found."
    echo "   Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found"
echo ""

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies."
    exit 1
fi

echo "✓ Dependencies installed"
echo ""

# Check for API key
echo "Checking for ANTHROPIC_API_KEY..."
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "⚠️  No ANTHROPIC_API_KEY found in environment"
    echo ""
    echo "To use real Claude API:"
    echo "  export ANTHROPIC_API_KEY='your-api-key-here'"
    echo ""
    echo "Or get your API key from: https://console.anthropic.com/"
    echo ""
    echo "You can still run in demo mode without an API key."
    echo ""
else
    echo "✓ API key found"
    echo ""
fi

# Run a test
echo "Running a quick test..."
echo ""

python3 claude_evaluator.py

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                     Setup Complete!                        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Next steps:"
echo "  1. Review the generated evaluation_report.json"
echo "  2. Try: python3 compare_models.py"
echo "  3. Customize use_cases.py with your own scenarios"
echo "  4. Review README.md for detailed documentation"
echo ""
echo "For customer demos:"
echo "  • Show the systematic evaluation approach"
echo "  • Discuss how to customize for their use cases"
echo "  • Explain model selection trade-offs"
echo "  • Walk through the reporting and insights"
echo ""
