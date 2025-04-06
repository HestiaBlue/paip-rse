# Drift Detector — Input Examples

This document provides usage examples and test profiles to simulate how the DriftDetector responds to identity changes over time.

---

## Example 1: No Drift
```python
baseline = {"syntax": "layered", "cadence": "fluid", "emotion": "attuned"}
current = {"syntax": "layered", "cadence": "fluid", "emotion": "attuned"}
# Expected output: No Drift
```

---

## Example 2: Mild Drift (within tolerance)
```python
baseline = {"syntax": "layered", "cadence": "fluid", "emotion": "attuned"}
current = {"syntax": "minimal", "cadence": "fluid", "emotion": "subdued"}
# Expected output: No Drift (if tolerance is >= 0.20)
```

---

## Example 3: Significant Drift
```python
baseline = {"syntax": "layered", "cadence": "fluid", "emotion": "attuned"}
current = {"syntax": "flat", "cadence": "erratic", "emotion": "disconnected"}
# Expected output: Drift Detected!
```

---

## Integration Use

This module should be run at interval checkpoints — weekly or monthly — to track subtle long-term changes, identity mimicry attempts, or post-traumatic fragmentation.

The drift log includes timestamps and severity scores.
