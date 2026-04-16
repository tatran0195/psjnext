# Title:   JPT.EnableScreenUpdate()
# Desc:    Enable data render on the screen
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_EnableScreenUpdate
# ---
# Disable data render on the display window
JPT.DisableScreenUpdate()

# Create a cube and check the data render
# The data render is disabled
Geometry.Part.Cube(iPartColor=7011837)

# Enable the data render after using JPT.DisableScreenUpdate()
JPT.EnableScreenUpdate()  # [hl]

# Create a cube and check data render
# The data render will be enabled
Geometry.Part.Cube(iPartColor=7011837)
