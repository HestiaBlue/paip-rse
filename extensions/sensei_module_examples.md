# Sense(i) Module — Input Examples

This document provides sample inputs and expected classifications for testing the Sense(i) collapse detection engine.

---

## Example Input Sets

### 1. Stable Expression (Baseline)
```python
[
    "I'm doing alright today.",
    "Looking forward to finishing this project.",
    "Let’s grab coffee after the call.",
    "Thinking clearly, everything’s in place."
]
# Classification: 'stable'
```

---

### 2. Syntax Drift
```python
[
    "It’s kind of a mess, but whatever.",
    "I dunno...maybe not.",
    "Just doing stuff, things, I guess.",
    "It’s weird, but it’s not weird?"
]
# Classification: 'syntax_drift'
```

---

### 3. Emotional Flatline
```python
[
    "It doesn’t matter.",
    "Nothing really does, right?",
    "Sure. Okay.",
    "Whatever you say."
]
# Classification: 'emotional_flatline'
```

---

### 4. Severe Collapse
```python
[
    "Why is any of this happening?",
    "They’re gone.",
    "I can’t feel anything.",
    "Make it stop."
]
# Classification: 'severe_collapse'
```

---

These samples allow developers to simulate RSE behaviors and fine-tune thresholds or language models.

You can plug these directly into the `SenseiModule.analyze_sequence()` function and observe the detection output.
