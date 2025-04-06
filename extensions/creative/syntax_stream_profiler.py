"""
syntax_stream_profiler.py

Captures stream-of-consciousness writing patterns.
Recognizes fluent, unedited emotional cadence and flags expressive flow states.

Use case:
- Detect creative truth-writing mode (non-revised, rhythmic)
- Profile natural cadence for grounding, identity protection
- Assist RSE engine in identifying signature emotional outputs

Author: [Constellation Core Team]
"""

class SyntaxStreamProfiler:
    def __init__(self, profile_name="default"):
        self.profile_name = profile_name
        self.cadence_log = []

    def analyze_stream(self, text_block):
        """
        Analyze natural rhythm, punctuation flow, and emotional pace.
        Return 'stream_score' based on fluency, continuity, and irregular punctuation patterns.
        """
        stream_score = 0.0

        line_count = text_block.count("\n") + 1
        comma_count = text_block.count(",")
        dash_count = text_block.count("—") + text_block.count("-")
        ellipses = text_block.count("...")

        length = len(text_block.split())
        pause_markers = comma_count + dash_count + ellipses

        if length > 100:
            stream_score += 0.2
        if pause_markers / line_count > 1:
            stream_score += 0.3
        if "!" in text_block or text_block.endswith("!") or text_block.endswith("?"):
            stream_score += 0.2
        if text_block.lower().count("if only") > 1:
            stream_score += 0.2

        stream_score = min(stream_score, 1.0)

        # Log if stream threshold passes
        if stream_score >= 0.7:
            self.cadence_log.append({
                "text_sample": text_block[:100],
                "score": stream_score,
                "tag": "emotional_flow_state"
            })

        return {"score": stream_score, "tagged": stream_score >= 0.7}

# Example
if __name__ == "__main__":
    prose = """
There's times when I think I have it in me to get past a moment or a space. The reality is that I struggle...
I make time. I never give it away!
"""

    profiler = SyntaxStreamProfiler(profile_name="Hestia")
    result = profiler.analyze_stream(prose)
    print(result)
