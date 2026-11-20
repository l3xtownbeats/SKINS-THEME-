# NEON STAGE JUCE integration layer

This is the JUCE-native integration layer corresponding to the approved
Tkinter visual prototypes in repository files `file (1).py` through
`file (15).py`. The Python sources remain reference prototypes; they are not
embedded or executed by the VST3.

## Included
- `PPGUStageLookAndFeel`: detailed metallic rotary controls and neon buttons.
- `PPGURev20Attachments`: attachments for the nine existing REV.20 parameter
  IDs and seven existing FX parameter IDs.
- `PPGUStageLayout`: approved header / left fretboard / centre FX / right
  amp-tone / FX strip / piano layout.
- `PPGUAssetManager`, `PPGUSpriteRenderer`, `PPGUKnobAtlas`: image loading,
  atlas frame rendering and cache from `../PPGUAssets`.

## Add source files to the existing JUCE plugin target
Add:
- `JUCE/NEON_STAGE/PPGUStageLookAndFeel.cpp`
- `JUCE/NEON_STAGE/PPGURev20Attachments.cpp`
- `JUCE/NEON_STAGE/PPGUStageLayout.cpp`
- `JUCE/PPGUAssets/PPGUAssetManager.cpp`
- `JUCE/PPGUAssets/PPGUSpriteRenderer.cpp`
- `JUCE/PPGUAssets/PPGUKnobAtlas.cpp`

Required JUCE modules: juce_gui_basics, juce_graphics, juce_audio_processors,
juce_core. The consuming plugin project must already link those modules.

## Editor integration pattern
Create the LookAndFeel as an editor member so it outlives every component:
```cpp
PPGUStageLookAndFeel stageLookAndFeel;
```
Set it on the nine existing sliders and seven existing FX buttons. Construct
`PPGURev20Attachments` after the controls exist, passing them in this order:
1. ampGain, eqHigh, eqMid, eqLow, velocity, dynamics, swing, humanize, accent
2. compressorOn, eqOn, distortionOn, chorusOn, delayOn, reverbOn, cabinetOn

Call `stageLayout.resized(getLocalBounds())` from the existing editor's
`resized()`, supplying pointers to its already-approved components.

## Non-negotiable constraints
- No APVTS parameter is created or renamed here.
- Parameter ranges, defaults, MIDI mapping, DSP, sampler, presets and state
  serialization remain owned by the existing processor.
- Do not do image file I/O in the audio callback.
- Do not replace the approved detailed visual assets with generic shapes once
  inspected atlases are ready. The LookAndFeel is a safe fallback.
- The five button states remain distinct: Normal, Hover, Pressed, Active,
  Disabled. JUCE derives these from enabled, hover, down and toggle state.
- Build and host validation must be performed in the actual plugin repository.
