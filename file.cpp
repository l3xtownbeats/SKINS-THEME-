// Пример использования готового ассета в JUCE LookAndFeel:
class PPGUKnobLookAndFeel : public juce::LookAndFeel_V4
{
public:
    void drawRotarySlider (juce::Graphics& g, int x, int y, int width, int height,
                           float sliderPosProportional, float rotaryStartAngle,
                           float rotaryEndAngle, juce::Slider& slider) override
    {
        // Отрисовка кадров поворотного спрайта или векторного/3D ассета
        auto radius = (float) juce::jmin (width / 2, height / 2) - 4.0f;
        auto centreX = (float) x + (float) width  * 0.5f;
        auto centreY = (float) y + (float) height * 0.5f;
        auto angle = rotaryStartAngle + sliderPosProportional * (rotaryEndAngle - rotaryStartAngle);
        
        // Базовый цвет и подсветка
        g.setColour (juce::Colour::fromString ("FF00D9FF")); // accent token
        // ... трансформация и вывод кадра регулятора ...
    }
};
