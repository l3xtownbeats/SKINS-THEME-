# NEON STAGE DEFAULT — Locked integration contract

Preserve the approved component layout:
- TopHeaderBar
- AutoChordsFretboard (left), FXEditModule (centre), AmpToneModule (right)
- FullFXChainBar
- NeonPianoKeyboard (bottom)

MELODY and PATTERN remain the two musical modes. AUTOCHORDS is a helper
inside PATTERN, not a third mode.

## REV.20 controls — existing APVTS IDs only
| Control | ID |
|---|---|
| GAIN | ampGain |
| TREBLE | eqHigh |
| MID | eqMid |
| BASS | eqLow |
| VELOCITY | velocity |
| DYNAMICS | dynamics |
| SWING | swing |
| HUMANIZE | humanize |
| ACCENT | accent |

## Seven primary FX switches
| FX | ID |
|---|---|
| Compressor | compressorOn |
| EQ | eqOn |
| Distortion | distortionOn |
| Chorus | chorusOn |
| Delay | delayOn |
| Reverb | reverbOn |
| Cabinet IR | cabinetOn |

Do not invent, rename or duplicate APVTS parameters. Do not add FLANGER as an
eighth primary switch. Preserve ranges, defaults, MIDI mappings, DSP, sampler,
presets, automation, state serialization and audio callback.

Keep detailed metallic controls, rims, reflections, shadows and neon glow.
Buttons must have distinct Normal, Hover, Pressed, Active and Disabled states.
Missing artwork must fall back safely without crashing. No file I/O or image
decoding in the audio callback.
