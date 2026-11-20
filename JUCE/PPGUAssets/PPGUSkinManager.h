#pragma once
#include <juce_graphics/juce_graphics.h>

struct PPGUSkinManager final
{
    static constexpr const char* skinId = "skin-053";
    static constexpr const char* skinName = "NEON_STAGE_DEFAULT_SKIN_1";
    static constexpr const char* layoutFamily = "STUDIO_CONSOLE";
    static juce::Colour windowBg()      { return juce::Colour(0xff080b14); }
    static juce::Colour panel()         { return juce::Colour(0xff101827); }
    static juce::Colour panelElevated() { return juce::Colour(0xff17243a); }
    static juce::Colour controlBg()     { return juce::Colour(0xff0c1422); }
    static juce::Colour controlFace()   { return juce::Colour(0xff1a2940); }
    static juce::Colour controlBorder() { return juce::Colour(0xff31506f); }
    static juce::Colour textPrimary()   { return juce::Colour(0xfff4f7ff); }
    static juce::Colour textSecondary() { return juce::Colour(0xffb5c4dc); }
    static juce::Colour textDisabled()  { return juce::Colour(0xff71829d); }
    static juce::Colour accent()        { return juce::Colour(0xff00d9ff); }
    static juce::Colour accentGlow()    { return juce::Colour(0xff6b8cff); }
    static juce::Colour danger()        { return juce::Colour(0xffff557a); }
    static juce::Colour warning()       { return juce::Colour(0xffffbe55); }
    static juce::Colour success()       { return juce::Colour(0xff42e6b0); }
    static juce::Colour lcdBg()         { return juce::Colour(0xff050d1b); }
    static juce::Colour lcdText()       { return juce::Colour(0xff8deBff); }
    static juce::Colour ledOn()         { return juce::Colour(0xff00e5ff); }
    static juce::Colour ledOff()        { return juce::Colour(0xff263b55); }
    static juce::Colour shadow()        { return juce::Colour(0xff03060b); }
    static juce::Colour highlight()     { return juce::Colour(0xff8dcbff); }
    static juce::Colour lowlight()      { return juce::Colour(0xff080f1b); }
};
