# NEON STAGE source-art inventory and deduplication audit

Date: 2026-11-21
Repository: l3xtownbeats/SKINS-THEME-
Reference: main tree snapshot inspected during REV.20 NEON STAGE work.

## Scope and safety

This is an inventory-only audit. No original artwork is deleted, renamed, recompressed,
or overwritten. Duplicate paths are retained in the repository as source history;
the eventual Runtime Asset Package should reference one canonical file per unique
content hash. Redistribution rights are not established by file presence or by a
GitHub repository being public.

## Exact duplicate-content groups

The following paths share the exact Git blob SHA and therefore contain identical
repository content:

| Blob SHA | Canonical source path | Duplicate paths |
|---|---|---|
| 424541c754ae0d8d89f45521465b989c30569ddb | IMG_20261120_221242_190.jpg | IMG_20261120_221255_496.jpg |
| 6c83e04470010cb2b406faf8b4ee376372ba2f54 | IMG_20261120_221243_837.jpg | IMG_20261120_221257_600.jpg |
| 42e2e4c0d9a7503949bee70e8705ccea58293562 | IMG_20261120_221306_448.dds | IMG_20261120_221306_448 (1).dds |
| 087dfb49eba0a037e07585a6bfa6c5022e5662d0 | Meshy_AI_NeonStage_AmpTone_Module.png | Meshy_AI_NeonStage_AmpTone_Module(1).png; image_c6ddf042-6841-4651-8041-8e58195d600c_0.png |
| 90bb4d9d2aece2b583a24a57962ada66130221b0 | Meshy_AI_NeonStage_Console_Panel_Background.png | Meshy_AI_NeonStage_Console_Panel_Background(1).png; Meshy_AI_NeonStage_Console_Panel_Background(2).png; image_36efa747-b377-4eca-97f6-eef727b278d9_0.png |
| 3c8baab15145e938770268383200c9323f0f0886 | Meshy_AI_NeonStage_FX_Switch_OFF.png | Meshy_AI_NeonStage_FX_Switch_OFF(1).png; image_390b19ba-9272-4881-8944-077602691118_0.png |
| b3048a05031618f739fbadf80a7c6fee3dd69efd | Meshy_AI_NeonStage_AutoChords_Fretboard.png | image_9e7cb67c-d752-44fd-9bfb-0f9fe80ac5ee_0.png |
| 26bc1d80d94316cb21996411cacb85ec41d3fe16 | Meshy_AI_NeonStage_Full_FX_Chain_Bar.png | image_73987b36-aa61-4c8a-8b10-a53ce08bceda_0.png |
| c6f2e1c666e6cabf3d9f3590c5f47f928e81f7e6 | Meshy_AI_NeonStage_Master_Rotary_Knob.png | image_6b411c05-51c2-48db-8e2c-cc4d9496da51_0.png |
| f2cd738f3ca9fd90622a968a369b6591c62d8fed | Meshy_AI_NeonStage_Piano_Keyboard_Module.png | image_83cf0db9-acd2-4bfb-9eac-c63d0489bd34_0.png |
| 4b7c6b2611aedb7e00f3a7d746805be0af3a3be5 | Meshy_AI_neon_stage_buttons_and_switches.png | image_0e082f89-7397-48d0-ab9a-7bf1e29d04b3_0.png |
| 290be8b28cd40026720b1f5e988549cc0c65b86c | Meshy_AI_knob_gain_reference.png | image_19ce2fd8-296b-4efe-88fd-2e44b269dd79_0.png; image_19ce2fd8-296b-4efe-88fd-2e44b269dd79_0 (1).png |
| fd639e613f23d96ede299fbe02011e95b54f00c7 | Meshy_AI_neon_stage_knobs_and_meters.png | Meshy_AI_neon_stage_knobs_and_meters (1).png; image_2db2539a-1ec4-4dc9-a950-2391773c8623_0.png |
| 73d75392dd48dc1cc8db3f7096e43140143fc296 | Meshy_AI_neon_stage_buttons_sheet.png | image_792d352b-7c68-472f-906e-d3e574750d0f_0.png |
| d7499e74cab2cefa68e6e52fbb7007e0f8230b62 | Meshy_AI_neon_stage_frames_and_panels.png | Meshy_AI_image_b8bd8bfa-30ec-48dd-8ef5-a623b3524137_0.png |
| ba9aafa398a2d65bcb8ee6ad2a223309e11bd138 | Meshy_AI_image_40495746-4235-4c4f-a4ee-67082ab6a06d_0.png | image_4a27a43e-6e65-4565-9048-6b6ea574d283_0.png |
| 4363e8e2fb901db0a882cf8c7e9beb2e78600e82 | Meshy_AI_neon_stage_meters_sheet.png | image_48d8b443-ef2b-449a-b0c6-7398b89da7e4_0.png |
| 3494a4f2c7be8b5225175d726e933e0f86dde334 | Meshy_AI_neon_stage_ui_icons_set.png | Meshy_AI_image_992fba18-4054-48d1-99ee-1af715b9b701_0.png |

Canonical names are recommendations for manifest/runtime references only. Do not
delete the duplicate paths as part of this integration.

## Visual review completed so far

- `Meshy_AI_NeonStage_Master_Rotary_Knob.png`: metallic knob is clearly blue-tinted
  with bright cyan/blue ring and pointer. Not compliant with the locked palette.
- `Meshy_AI_NeonStage_FX_Switch_OFF.png`: switch plate and metal frame are blue-tinted.
  Not compliant with the locked palette.
- `preview.webp`: shows a separate dark textured object with cyan illumination; it
  is not a preview of the complete NEON STAGE control-deck layout.
- Binary source sheets for all remaining modules have not yet been visually reviewed
  at full resolution. Their filenames and roles do not prove their actual contents.

## Runtime packaging decision

Do not mark any source image as runtime-ready solely because it exists. For each
candidate atlas/sprite:
1. Inspect the full-resolution image and identify cell boundaries and frame count.
2. Confirm alpha/transparency, dimensions, colour profile and pixel format.
3. Record exact SHA-256, source path and license/provenance evidence.
4. Remove blue/cyan accents through a controlled image-editing pass; preserve metallic
   material detail and transparent edges.
5. Reinspect edited output and compare dimensions/alpha against the source.
6. Add only approved derivatives to `Assets/NEON_STAGE_DEFAULT_SKIN_1/`.
7. Change manifest status from `not_imported` only after files exist and validator
   checks pass.

## Integration risks recorded

- `PPGUAssetManager` is editor/UI-only and must never be called from
  `processBlock()` or any real-time audio callback.
- Its current path resolver blocks absolute paths and lexical traversal outside the
  root, but does not establish symlink containment. Runtime packaging must use a
  trusted fixed asset root and avoid user-controlled symlink trees.
- No image decoding, filesystem access, or asset scanning may be added to the audio
  thread.
- The nine APVTS IDs and seven primary FX IDs in the manifest remain unchanged.
- No redistribution license has been verified; source art remains excluded from
  distributable plugin packages.

## Current conclusion

Exact duplicate groups are mapped without deleting originals. The two directly
inspected control assets fail the approved colour requirement and must be remastered
before runtime use. The asset package remains a scaffold; no Runtime Asset is
claimed complete by this audit.
