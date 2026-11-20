#include "PPGURev20Attachments.h"

PPGURev20Attachments::PPGURev20Attachments(APVTS& state,
    const std::array<juce::Slider*, 9>& controls,
    const std::array<juce::Button*, 7>& fxButtons)
{
    static constexpr std::array<const char*, 9> controlIds {{
        "ampGain", "eqHigh", "eqMid", "eqLow", "velocity",
        "dynamics", "swing", "humanize", "accent"
    }};
    static constexpr std::array<const char*, 7> fxIds {{
        "compressorOn", "eqOn", "distortionOn", "chorusOn",
        "delayOn", "reverbOn", "cabinetOn"
    }};

    for (size_t i = 0; i < controls.size(); ++i)
        if (controls[i] != nullptr && state.getParameter(controlIds[i]) != nullptr)
            sliderAttachments[i] = std::make_unique<SliderAttachment>(state, controlIds[i], *controls[i]);

    for (size_t i = 0; i < fxButtons.size(); ++i)
        if (fxButtons[i] != nullptr && state.getParameter(fxIds[i]) != nullptr)
            buttonAttachments[i] = std::make_unique<ButtonAttachment>(state, fxIds[i], *fxButtons[i]);
}
