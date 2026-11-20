#include "PPGUSpriteRenderer.h"

bool PPGUSpriteRenderer::isValidAtlas(const juce::Image& image,
                                      int columns, int rows) noexcept
{
    return image.isValid() && columns > 0 && rows > 0
        && image.getWidth() >= columns && image.getHeight() >= rows
        && image.getWidth() % columns == 0 && image.getHeight() % rows == 0;
}

void PPGUSpriteRenderer::drawFrame(juce::Graphics& g, const juce::Image& image,
                                   int columns, int rows, int frameIndex,
                                   juce::Rectangle<float> destination, float opacity)
{
    if (! isValidAtlas(image, columns, rows) || destination.isEmpty())
        return;
    const int count = columns * rows;
    const int index = juce::jlimit(0, count - 1, frameIndex);
    const int fw = image.getWidth() / columns;
    const int fh = image.getHeight() / rows;
    const juce::Rectangle<int> source((index % columns) * fw, (index / columns) * fh, fw, fh);
    g.saveState();
    g.setOpacity(juce::jlimit(0.0f, 1.0f, opacity));
    g.drawImage(image, destination, juce::RectanglePlacement::stretchToFit, false, source);
    g.restoreState();
}
