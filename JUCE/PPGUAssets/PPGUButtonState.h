#pragma once
enum class PPGUButtonState { Normal, Hover, Pressed, Active, Disabled };
inline const char* ppguButtonStateName(PPGUButtonState state) noexcept
{
    switch (state) {
        case PPGUButtonState::Normal: return "normal";
        case PPGUButtonState::Hover: return "hover";
        case PPGUButtonState::Pressed: return "pressed";
        case PPGUButtonState::Active: return "active";
        case PPGUButtonState::Disabled: return "disabled";
    }
    return "normal";
}
