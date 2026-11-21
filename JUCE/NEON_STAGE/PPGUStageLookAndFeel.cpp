#include "PPGUStageLookAndFeel.h"

PPGUStageLookAndFeel::PPGUStageLookAndFeel()
{
    setColour(juce::Slider::textBoxTextColourId, PPGUSkinManager::textPrimary());
    setColour(juce::Slider::textBoxBackgroundColourId, PPGUSkinManager::lcdBg());
    setColour(juce::Slider::textBoxOutlineColourId, PPGUSkinManager::controlBorder());
    setColour(juce::TextButton::textColourOffId, PPGUSkinManager::textSecondary());
    setColour(juce::TextButton::textColourOnId, PPGUSkinManager::lcdText());
}

void PPGUStageLookAndFeel::drawRotarySlider(juce::Graphics& g, int x, int y, int w, int h,
                                            float position, float startAngle, float endAngle,
                                            juce::Slider& slider)
{
    auto bounds = juce::Rectangle<float>((float)x, (float)y, (float)w, (float)h)
                      .reduced(5.0f);
    const auto diameter = juce::jmin(bounds.getWidth(), bounds.getHeight());
    auto knob = bounds.withSizeKeepingCentre(diameter, diameter);
    const auto centre = knob.getCentre();
    const auto radius = diameter * 0.5f;
    const auto angle = startAngle + position * (endAngle - startAngle);

    // Outer shadow, machined silver rim and approved magenta halo.
    g.setColour(PPGUSkinManager::shadow());
    g.fillEllipse(knob.translated(0.0f, 2.5f));
    g.setColour(PPGUSkinManager::accent().withAlpha(0.13f));
    g.drawEllipse(knob.expanded(2.0f), 3.0f);
    g.setGradientFill(juce::ColourGradient(PPGUSkinManager::controlBorder(),
                                           knob.getX(), knob.getY(),
                                           PPGUSkinManager::lowlight(),
                                           knob.getRight(), knob.getBottom(), false));
    g.fillEllipse(knob);
    g.setColour(PPGUSkinManager::highlight().withAlpha(0.8f));
    g.drawEllipse(knob.reduced(1.0f), 1.2f);

    auto face = knob.reduced(radius * 0.13f);
    g.setGradientFill(juce::ColourGradient(PPGUSkinManager::panelElevated(),
                                           face.getX(), face.getY(),
                                           PPGUSkinManager::controlBg(),
                                           face.getRight(), face.getBottom(), false));
    g.fillEllipse(face);
    g.setColour(PPGUSkinManager::controlBorder());
    g.drawEllipse(face, 1.0f);

    // Track and value arc.
    const auto arcRadius = radius * 0.88f;
    juce::Path track;
    track.addCentredArc(centre.x, centre.y, arcRadius, arcRadius, 0.0f,
                        startAngle, endAngle, true);
    g.setColour(PPGUSkinManager::ledOff());
    g.strokePath(track, juce::PathStrokeType(3.5f, juce::PathStrokeType::curved,
                                             juce::PathStrokeType::rounded));
    juce::Path valueArc;
    valueArc.addCentredArc(centre.x, centre.y, arcRadius, arcRadius, 0.0f,
                           startAngle, angle, true);
    g.setColour(PPGUSkinManager::accent().withAlpha(0.22f));
    g.strokePath(valueArc, juce::PathStrokeType(7.0f, juce::PathStrokeType::curved,
                                                juce::PathStrokeType::rounded));
    g.setColour(PPGUSkinManager::accent());
    g.strokePath(valueArc, juce::PathStrokeType(3.0f, juce::PathStrokeType::curved,
                                                juce::PathStrokeType::rounded));

    // Pointer: a slim machined-silver indicator.
    juce::Path pointer;
    pointer.addRoundedRectangle(-1.7f, -radius * 0.70f, 3.4f, radius * 0.34f, 1.4f);
    g.setColour(PPGUSkinManager::textPrimary());
    g.fillPath(pointer, juce::AffineTransform::rotation(angle).translated(centre.x, centre.y));

    if (slider.isEnabled())
    {
        g.setColour(PPGUSkinManager::accent().withAlpha(0.18f));
        g.fillEllipse(face.reduced(face.getWidth() * 0.34f));
    }
}

void PPGUStageLookAndFeel::drawButtonBackground(juce::Graphics& g, juce::Button& button,
                                                 const juce::Colour&, bool hovered, bool pressed)
{
    auto r = button.getLocalBounds().toFloat().reduced(1.5f);
    if (r.isEmpty()) return;

    // Explicit state priority: Disabled > Pressed > Active > Hover > Normal.
    const bool disabled = !button.isEnabled();
    const bool active = button.getToggleState();
    const auto bg = disabled ? PPGUSkinManager::lowlight()
                  : pressed ? PPGUSkinManager::controlBg()
                  : active ? PPGUSkinManager::panel()
                  : hovered ? PPGUSkinManager::panelElevated()
                            : PPGUSkinManager::controlFace();
    const auto edge = disabled ? PPGUSkinManager::ledOff()
                    : (pressed || active) ? PPGUSkinManager::accent()
                    : hovered ? PPGUSkinManager::accentGlow()
                              : PPGUSkinManager::controlBorder();

    if (!disabled && (pressed || active))
    {
        g.setColour(PPGUSkinManager::accent().withAlpha(0.16f));
        g.drawRoundedRectangle(r.expanded(2.0f), 5.0f, 4.0f);
    }
    g.setGradientFill(juce::ColourGradient(bg.brighter(0.12f), r.getX(), r.getY(),
                                           bg.darker(0.25f), r.getRight(), r.getBottom(), false));
    g.fillRoundedRectangle(r, 5.0f);
    g.setColour(edge);
    g.drawRoundedRectangle(r, 5.0f, 1.2f);
    g.setColour(PPGUSkinManager::highlight().withAlpha(disabled ? 0.08f : 0.25f));
    g.drawLine(r.getX() + 5.0f, r.getY() + 1.5f, r.getRight() - 5.0f, r.getY() + 1.5f, 1.0f);
}

void PPGUStageLookAndFeel::drawButtonText(juce::Graphics& g, juce::TextButton& button,
                                          bool hovered, bool pressed)
{
    auto colour = !button.isEnabled() ? PPGUSkinManager::textDisabled()
                 : (button.getToggleState() || pressed) ? PPGUSkinManager::lcdText()
                 : hovered ? PPGUSkinManager::textPrimary()
                           : PPGUSkinManager::textSecondary();
    g.setColour(colour);
    g.setFont(juce::Font(11.0f, juce::Font::bold));
    g.drawFittedText(button.getButtonText(), button.getLocalBounds().reduced(4),
                     juce::Justification::centred, 2);
}
