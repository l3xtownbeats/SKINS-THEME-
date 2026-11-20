#pragma once
#include <juce_gui_basics/juce_gui_basics.h>

/** Layout adapter for the approved NEON STAGE console.
    Pass the existing components; this class neither creates replacements nor
    changes their internal behaviour or audio/parameter contracts. */
class PPGUStageLayout final
{
public:
    struct Parts
    {
        juce::Component* header = nullptr;
        juce::Component* autoChords = nullptr;
        juce::Component* fxEdit = nullptr;
        juce::Component* ampTone = nullptr;
        juce::Component* fxChain = nullptr;
        juce::Component* piano = nullptr;
    };

    explicit PPGUStageLayout(Parts components) : parts(components) {}
    void resized(juce::Rectangle<int> area) const;

private:
    Parts parts;
};
