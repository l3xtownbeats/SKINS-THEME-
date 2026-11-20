#pragma once
#include <juce_gui_basics/juce_gui_basics.h>
#include "../PPGUAssets/PPGUSkinManager.h"

/** NEON STAGE metallic/neon LookAndFeel. No processor or parameter ownership. */
class PPGUStageLookAndFeel final : public juce::LookAndFeel_V4
{
public:
    PPGUStageLookAndFeel();
    void drawRotarySlider(juce::Graphics&, int, int, int, int, float,
                          float, float, juce::Slider&) override;
    void drawButtonBackground(juce::Graphics&, juce::Button&, const juce::Colour&,
                              bool, bool) override;
    void drawButtonText(juce::Graphics&, juce::TextButton&,
                        bool, bool) override;
private:
    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR(PPGUStageLookAndFeel)
};
