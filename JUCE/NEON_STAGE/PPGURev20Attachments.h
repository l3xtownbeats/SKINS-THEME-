#pragma once
#include <juce_audio_processors/juce_audio_processors.h>
#include <array>
#include <memory>

/**
  Binds existing controls to the established REV.20 APVTS IDs.
  This class does not create, rename, or modify parameters. The referenced
  sliders/buttons must already be owned by the editor and outlive this object.
*/
class PPGURev20Attachments final
{
public:
    using APVTS = juce::AudioProcessorValueTreeState;
    using SliderAttachment = APVTS::SliderAttachment;
    using ButtonAttachment = APVTS::ButtonAttachment;

    PPGURev20Attachments(APVTS& state,
        const std::array<juce::Slider*, 9>& controls,
        const std::array<juce::Button*, 7>& fxButtons);

private:
    std::array<std::unique_ptr<SliderAttachment>, 9> sliderAttachments;
    std::array<std::unique_ptr<ButtonAttachment>, 7> buttonAttachments;
    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR(PPGURev20Attachments)
};
