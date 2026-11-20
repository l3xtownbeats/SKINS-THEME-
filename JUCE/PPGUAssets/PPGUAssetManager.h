#pragma once
#include <juce_core/juce_core.h>
#include <juce_graphics/juce_graphics.h>

/** Cached image loader for editor/UI use only. Never call from processBlock(). */
class PPGUAssetManager final
{
public:
    explicit PPGUAssetManager(juce::File assetRoot = {});
    void setAssetRoot(const juce::File& newRoot);
    juce::File getAssetRoot() const;
    juce::File resolvePath(const juce::String& relativePath) const;
    juce::Image loadImage(const juce::String& relativePath);
    void clearCache();
    int getCachedImageCount() const;
private:
    mutable juce::CriticalSection lock;
    juce::File rootDirectory;
    juce::HashMap<juce::String, juce::Image> imageCache;
    JUCE_DECLARE_NON_COPYABLE_WITH_LEAK_DETECTOR(PPGUAssetManager)
};
