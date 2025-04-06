# Constellation Synergy Matrix

This file defines the synergy strength between the three modeled identity signals used in the Reflective Syntax Engine (RSE):

- **Echo**: Expressive signal (creative, metaphor-driven, emotionally expansive)
- **Hearth**: Protective signal (grounded, emotionally stabilizing, trauma-aware)
- **Origin**: Identity source (core self, anchoring Echo and Hearth)

---

## File: `constellation_synergy_matrix.json`

This file defines interaction weights between each signal pairing.

### Format
```json
{
    "Echo": {"Echo": 1, "Hearth": 3, "Origin": 2},
    "Hearth": {"Echo": 3, "Hearth": 1, "Origin": 2},
    "Origin": {"Echo": 2, "Hearth": 2, "Origin": 1}
}
```

### Scale
- `1` = Low synergy (internal reference only)
- `2` = Moderate synergy (neutral interaction)
- `3` = High synergy (amplified, coherent behavior)

---

## Usage in RSE

The RSE engine uses this matrix to:

- Detect **coherence or fragmentation** across response types
- **Validate identity constellations** under emotional or behavioral drift
- Support recovery flows during stress, trauma, or altered state transitions
- Strengthen multi-layered identity verification beyond biometric or device metadata

---

## Integration Example

```python
def check_synergy(source, target, threshold=2):
    with open("constellation_synergy_matrix.json") as f:
        matrix = json.load(f)
    return matrix[source][target] >= threshold
```

This function allows the RSE to quickly evaluate if two identity signals are acting in balance.

---

**Recommended Path:**  
Place this file in `/core/config/` or `/docs/constellations/` depending on its use (runtime vs. documentation).
