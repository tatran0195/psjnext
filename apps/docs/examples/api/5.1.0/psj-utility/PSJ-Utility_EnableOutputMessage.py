# Title:   JPT.EnableOutputMessage()
# Desc:    Enable the output message which will be written to the Python API window
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_EnableOutputMessage
# ---
# Disable the screen animation
JPT.DisableOutputMessage()

# Print a string to test the output message
# on the Python API window
# The string will not be printed on the Python API window
print("Test")

# Enable the output message on the Python API window
# after using JPT.DisableOutputMessage()
JPT.EnableOutputMessage()  # [hl]

# Print a string to test the output message
# on the Python API window
# The string will be printed on the Python API window
print("Test")
