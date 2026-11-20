#include "PPGUAssetManager.h"

PPGUAssetManager::PPGUAssetManager(juce::File assetRoot)
{
    if (assetRoot != juce::File{})
        setAssetRoot(assetRoot);
}

void PPGUAssetManager::setAssetRoot(const juce::File& newRoot)
{
    const juce::ScopedLock guard(lock);
    rootDirectory = newRoot.getFullPathName();
    imageCache.clear();
}

juce::File PPGUAssetManager::getAssetRoot() const
{
    const juce::ScopedLock guard(lock);
    return rootDirectory;
}

juce::File PPGUAssetManager::resolvePath(const juce::String& relativePath) const
{
    const juce::ScopedLock guard(lock);
    if (rootDirectory == juce::File{} || relativePath.isEmpty()
        || juce::File::isAbsolutePath(relativePath))
        return {};

    const auto root = rootDirectory.getFullPathName().trimCharactersAtEnd("/\\");
    const auto candidate = rootDirectory.getChildFile(relativePath).getFullPathName();
    const auto prefix = root + juce::File::getSeparatorString();
    if (! candidate.startsWithIgnoreCase(prefix))
        return {};
    return juce::File(candidate);
}

juce::Image PPGUAssetManager::loadImage(const juce::String& relativePath)
{
    const auto key = relativePath.replaceCharacter('\\', '/');
    {
        const juce::ScopedLock guard(lock);
        if (imageCache.contains(key))
            return imageCache[key];
    }

    const auto file = resolvePath(key);
    if (! file.existsAsFile())
        return {};
    auto loaded = juce::ImageFileFormat::loadFrom(file);
    if (! loaded.isValid())
        return {};

    const juce::ScopedLock guard(lock);
    if (! imageCache.contains(key))
        imageCache.set(key, loaded);
    return imageCache[key];
}

void PPGUAssetManager::clearCache()
{
    const juce::ScopedLock guard(lock);
    imageCache.clear();
}

int PPGUAssetManager::getCachedImageCount() const
{
    const juce::ScopedLock guard(lock);
    return imageCache.size();
}
