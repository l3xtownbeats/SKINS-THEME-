#include "PPGUKnobAtlas.h"
PPGUKnobAtlas::PPGUKnobAtlas(juce::Image image, int c, int r)
    : atlas(std::move(image)), columns(c), rows(r) {}
bool PPGUKnobAtlas::isValid() const noexcept
{
    return PPGUSpriteRenderer::isValidAtlas(atlas, columns, rows);
}
int PPGUKnobAtlas::frameForNormalisedValue(float value) const noexcept
{
    if (!isValid()) return 0;
    const int total = columns * rows;
    return juce::jlimit(0, total - 1,
        juce::roundToInt(juce::jlimit(0.0f, 1.0f, value) * (total - 1)));
}
void PPGUKnobAtlas::draw(juce::Graphics& g, juce::Rectangle<float> bounds,
                         float value, float opacity) const
{
    if (isValid())
        PPGUSpriteRenderer::drawFrame(g, atlas, columns, rows,
                                      frameForNormalisedValue(value), bounds, opacity);
}
