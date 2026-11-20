#pragma once
#include "PPGUSpriteRenderer.h"

class PPGUKnobAtlas final
{
public:
    PPGUKnobAtlas(juce::Image image, int columns, int rows);
    bool isValid() const noexcept;
    int frameForNormalisedValue(float value) const noexcept;
    void draw(juce::Graphics&, juce::Rectangle<float>, float value,
              float opacity = 1.0f) const;
private:
    juce::Image atlas;
    int columns = 0, rows = 0;
};
