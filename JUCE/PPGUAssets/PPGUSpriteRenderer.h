#pragma once
#include <juce_graphics/juce_graphics.h>

class PPGUSpriteRenderer final
{
public:
    static bool isValidAtlas(const juce::Image&, int columns, int rows) noexcept;
    static void drawFrame(juce::Graphics&, const juce::Image&, int columns, int rows,
                          int frameIndex, juce::Rectangle<float> destination,
                          float opacity = 1.0f);
};
