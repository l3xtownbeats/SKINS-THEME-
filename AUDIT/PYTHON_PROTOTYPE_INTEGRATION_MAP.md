# Python prototype audit and JUCE migration map (file (1).py–file (15).py)

This is a source-level audit of the repository files. It does not claim that the
Tkinter prototypes are part of the VST3 binary. The native JUCE layer is being
added alongside them so the Python reference files remain intact.

| Source | Existing responsibility | JUCE migration / integration |
|---|---|---|
| file (1).py | Earlier Tkinter master window | Superseded visually by the approved full layout from file (14).py; do not use as the final layout. |
| file (2).py | TopHeaderBar / preset and status labels | Preserve header composition; replace hard-coded CPU/RAM figures and decorative actions with real data/actions only when backend exists. |
| file (3).py | AutoChordsFretboard | Retain as left-column component; port drawing/interaction to a native JUCE Component. |
| file (4).py | NeonPianoKeyboard | Visual keyboard prototype; mouse clicks are not a substitute for MIDI note events. Native port must send/reflect MIDI through the existing plugin path. |
| file (5).py | FXEditModule / compressor graph and controls | Preserve visual layout; each control must attach to its real existing parameter or remain explicitly display-only. |
| file (6).py | NeonVUMeter | Port as a paint-only JUCE meter; read audio values through a safe UI update mechanism, not by touching UI from processBlock. |
| file (7).py | Pillow sheet slicing and dark-background alpha conversion | Do not use destructive luminance-to-alpha conversion on master artwork. Preserve original RGBA alpha; crop only after measured cell boundaries are known. |
| file (8).py | FX-chain/control demo | Treat as visual reference; no processor/APVTS binding is established in this prototype. |
| file (9).py | NeonFXButton, NeonToggle, CompressorDisplay | Replaced by JUCE LookAndFeel button states and existing APVTS ButtonAttachments; compressor graph still needs live parameter/GR metering wiring. |
| file (10).py | Vector NeonKnob | Replaced by JUCE metallic rotary LookAndFeel; optional inspected atlas can be drawn via PPGUKnobAtlas. |
| file (11).py | Duplicate of file.py (SkinCard / SkinsGalleryPanel) | Gallery is a design prototype; preview/search/favourite require a real skin registry/backend before being enabled. |
| file (12).py | SettingsModule / NeonCheckBox | Visual mockup only. Tabs, dropdowns and reset label are not functional settings controls; do not imply they change audio or host configuration. |
| file (13).py | Seven-item FullFXChainBar | Preserve the seven approved FX items and connect them to the seven existing APVTS IDs only. |
| file (14).py | NeonStageUltimate complete layout | Authoritative approved layout: header, left AutoChords, centre FX Edit, right Amp/Tone, FX strip, bottom keyboard. Source has unresolved external class dependencies and geometry string uses a comma rather than the Tk geometry separator 'x'. |
| file (15).py | SpriteSheetLoader, sprite NeonKnob, five-state NeonButton, NeonRadar | Native asset manager, sprite renderer, knob atlas and button-state rendering added under JUCE. Python remains a prototype, not runtime code in the VST3. |

## Concrete source issues to resolve before using the Python prototypes standalone

### file (7).py
The background-removal approach based on pixel brightness can erase dark metal,
shadow and fine artwork and can damage glow/alpha. Preserve source alpha and
use an explicitly authored mask only when a specific image requires keying.

### file (9).py
The FX button has no disabled or pressed state; its hover appearance is only
partially represented. NeonToggle has no hover/disabled handling. The
CompressorDisplay is a fixed illustrative curve, not a live compressor display.

### file (10).py
The rotary ratio divides by (max_val - min_val) without guarding equal bounds.
The initial value is not clamped and there is no parameter/host attachment.

### file (12).py
The file uses `tk` but does not import tkinter itself, so it is not standalone
unless another module injects that name. Tabs, dropdowns and Reset are labels,
not functioning controls.

### file (14).py
The source depends on AppState, TopHeaderBar, AutoChordsFretboard, FXEditModule,
AmpToneModule, FullFXChainBar and NeonPianoKeyboard being imported/defined
elsewhere. The supplied file alone is not runnable. Its geometry string
`"1180, 780"` should be `"1180x780"` in Tkinter.

### file (15).py (and identical file (16).py)
- SpriteSheetLoader does not validate positive cell sizes, frame counts, source
  bounds or empty grids; Pillow can silently pad out-of-range crops.
- NeonKnob fails if the frame list is empty; value and frame-count constraints
  are not fully validated.
- NeonButton assumes a `normal` image exists; missing state art can raise
  KeyError. It has no public disabled-state API, and release handling does not
  distinguish release outside the widget.
- NeonRadar fails for an empty frame list or non-positive FPS and has no public
  stop method/cancellation path for its scheduled callback.
- file (16).py has the same SHA-1 as file (15).py and is a duplicate, not a
  separate implementation.

## What has been integrated in this branch

- JUCE metallic/neon rotary and button LookAndFeel.
- Five distinct button state visuals: Normal, Hover, Pressed, Active, Disabled.
- APVTS SliderAttachment/ButtonAttachment adapter using the exact nine + seven
  locked IDs; it does not create parameters.
- Approved six-part NEON STAGE layout adapter.
- JUCE image cache, sprite-atlas renderer, knob-atlas helper and skin palette.
- Locked design contract, parameter contract, asset manifest and read-only
  manifest validator.

## Still blocked by missing source / evidence

- Actual plugin processor/editor project and its build files are not in this
  skin-gallery repository. Therefore these classes cannot yet be wired into
  the real AudioProcessorEditor or compiled against the project's exact JUCE
  version here.
- The source artwork binaries have not been visually inspected in this
  connector session. Atlas crops, frame counts, alpha quality and GLB presence
  remain unconfirmed.
- Asset redistribution licences are not established. Do not bundle assets
  until permissions are confirmed.
- No VST3 build, pluginval run or FL Studio host test is claimed by this change.
