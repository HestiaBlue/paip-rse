"""
basic_rse_flow.py

This script simulates a basic RSE identity validation flow.
Input: User message
Output: RSE validation decision based on matching known behavior
"""

def mock_rse_validate(user_input):
    known_syntax = ["breathe", "grief", "syntax", "resonance"]
    score = sum(word in user_input.lower() for word in known_syntax)
    if score >= 2:
        return "Validation Passed (RSE: strong alignment)"
    return "Validation Failed (RSE: insufficient signature)"

# Simulate a user message
user_message = "Sometimes I lose myself in grief but syntax holds me steady"
print("Input:", user_message)
print("RSE Result:", mock_rse_validate(user_message))
