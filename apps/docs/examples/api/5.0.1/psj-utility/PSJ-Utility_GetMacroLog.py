# Title:   JPT.GetMacroLog()
# Desc:    Get the current text existing on the Macro window
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetMacroLog
# ---
# Do some operations, such as open a dialog of a function or
# creating something to store its macro to the Macro window
# In case the Macro dialog is blanked, its returning value is ""
# Get the stored macro on the Macro window
storedMacro = JPT.GetMacroLog()  # [hl]
JPT.Debugger(storedMacro)
