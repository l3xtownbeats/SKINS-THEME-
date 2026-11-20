#include "PPGUStageLayout.h"

void PPGUStageLayout::resized(juce::Rectangle<int> area) const
{
    auto bounds = area.reduced(10);
    constexpr int gap = 8;
    constexpr int headerH = 52;
    constexpr int fxH = 66;
    constexpr int pianoH = 112;

    if (parts.header) parts.header->setBounds(bounds.removeFromTop(headerH));
    bounds.removeFromTop(gap);

    auto pianoArea = bounds.removeFromBottom(pianoH);
    bounds.removeFromBottom(gap);
    if (parts.piano) parts.piano->setBounds(pianoArea);

    auto fxArea = bounds.removeFromBottom(fxH);
    bounds.removeFromBottom(gap);
    if (parts.fxChain) parts.fxChain->setBounds(fxArea);

    auto workspace = bounds;
    const int leftW = juce::jlimit(190, 260, workspace.getWidth() / 4);
    const int rightW = juce::jlimit(210, 290, workspace.getWidth() / 4);
    if (parts.autoChords) parts.autoChords->setBounds(workspace.removeFromLeft(leftW));
    workspace.removeFromLeft(gap);
    if (parts.ampTone) parts.ampTone->setBounds(workspace.removeFromRight(rightW));
    workspace.removeFromRight(gap);
    if (parts.fxEdit) parts.fxEdit->setBounds(workspace);
}
