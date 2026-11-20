# PPGU asset runtime

Editor-side image loading and atlas drawing. Add the three .cpp files to the
existing JUCE target. Do not call the loader from processBlock or any realtime
audio thread. Inspect atlas dimensions before choosing columns/rows. Keep
source alpha intact. No source images are considered redistribution-cleared.
