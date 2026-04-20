# Title:   JPT.EnableScreenAnimation()
# Desc:    Enable screen animation effect
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_EnableScreenAnimation
# ---
# Disable the screen animation
JPT.DisableScreenAnimation()

# Create a cube and check the screen animation
# The animation effect is disabled
Geometry.Part.Cube(iPartColor=7011837)

# Enable the screen animation effect after using JPT.DisableScreenAnimation()
JPT.EnableScreenAnimation()  # [hl]

# Create a cube and check the screen animation
# The animation effect will be enabled
Geometry.Part.Cube(iPartColor=7011837)
