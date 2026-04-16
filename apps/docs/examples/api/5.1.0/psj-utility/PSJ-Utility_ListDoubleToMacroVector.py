# Title:   JPT.ListDoubleToMacroVector()
# Desc:    Convert a list of 3 double values to a vector3d (Macro string type)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ListDoubleToMacroVector
# ---
# Convert a list of 3 double values to a vector3d (Macro string type)
inputValue1 = 0.001
inputValue2 = 2.1
inputValue3 = 5.5
# Return a string object with value = [0.001,2.1,5.5]
JPT.Debugger(JPT.ListDoubleToMacroVector(inputValue1, inputValue2, inputValue3))  # [hl]
