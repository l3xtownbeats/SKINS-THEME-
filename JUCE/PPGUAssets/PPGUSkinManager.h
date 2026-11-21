#pragma once
#include <juce_graphics/juce_graphics.h>

/** Single approved NEON STAGE palette: graphite, machined silver,
    purple/magenta and crimson. Green/yellow are reserved for functional
    status and level metering; no blue/cyan/turquoise accents are used. */
struct PPGUSkinManager final
{
    static constexpr const char* skinId = "skin-053";
    static constexpr const char* skinName = "NEON_STAGE_DEFAULT_SKIN_1";
    static constexpr const char* layoutFamily = "STUDIO_CONSOLE";

    static juce::Colour windowBg()      { return juce::Colour(0xff09090d); }
    static juce::Colour panel()         { return juce::Colour(0xff15151b); }
    static juce::Colour panelElevated() { return juce::Colour(0xff202027); }
    static juce::Colour controlBg()     { return juce::Colour(0xff101015); }
    static juce::Colour controlFace()   { return juce::Colour(0xff292932); }
    static juce::Colour controlBorder() { return juce::Colour(0xff77717f); }

    static juce::Colour textPrimary()   { return juce::Colour(0xfff4f1f5); }
    static juce::Colour textSecondary() { return juce::Colour(0xffbeb8c3); }
    static juce::Colour textDisabled()  { return juce::Colour(0xff716b76); }

    static juce::Colour accent()        { return juce::Colour(0xffd12b8a); }
    static juce::Colour accentGlow()    { return juce::Colour(0xff9146d8); }
    static juce::Colour purple()        { return juce::Colour(0xff8a4de8); }
    static juce::Colour crimson()       { return juce::Colour(0xffe43d58); }

    static juce::Colour danger()        { return crimson(); }
    static juce::Colour warning()       { return juce::Colour(0xfff2b544); }
    static juce::Colour success()       { return juce::Colour(0xff55c78a); }

    static juce::Colour lcdBg()         { return juce::Colour(0xff09070d); }
    static juce::Colour lcdText()       { return juce::Colour(0xfff3d6ea); }
    static juce::Colour ledOn()         { return accent(); }
    static juce::Colour ledOff()        { return juce::Colour(0xff39313c); }

    static juce::Colour shadow()        { return juce::Colour(0xff030305); }
    static juce::Colour highlight()     { return juce::Colour(0xffd6d0d8); }
    static juce::Colour lowlight()      { return juce::Colour(0xff111116); }
};
