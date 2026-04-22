# Comments

## Strengths
- Tackles practical failure mode: reward/critic drift during online adaptation.
- Connects implementation to EM interpretation, giving conceptual clarity.
- Strong fit for deployment where streaming test distributions shift.

## Limitations
- Needs a trusted labeled anchor stream for recalibration.
- Sensitive to recalibration frequency and anchor quality.
- Additional compute overhead versus one-shot inference.

## Extension ideas
- Adaptive recalibration schedule based on drift detectors.
- Confidence-weighted anchor sampling.
- Joint calibration over reward and uncertainty heads.
