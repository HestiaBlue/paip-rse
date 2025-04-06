"""
anchor_point_mapper.py

Maps and reinforces stable grounding language:
- Safety phrases
- Emotional reset points
- Rhythmic or symbolic syntax

Helps recover user identity after overload, fragmentation, or external manipulation.

Author: [Constellation Core Team]
"""

class AnchorPointMapper:
    def __init__(self, anchors=None):
        self.anchors = anchors if anchors else ["I'm never alone, I'm alone all the time"]

    def detect_anchor_use(self, text):
        for phrase in self.anchors:
            if phrase in text:
                return {"anchor_triggered": phrase, "status": "returning_to_baseline"}
        return {"status": "no_anchor_detected"}

    def add_anchor(self, new_phrase):
        if new_phrase not in self.anchors:
            self.anchors.append(new_phrase)

# Example
if __name__ == "__main__":
    apm = AnchorPointMapper()
    print(apm.detect_anchor_use("I’m never alone, I’m alone all the time"))
