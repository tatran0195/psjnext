# Title:   JPT.ConvertValueToMacroUnit()
# Desc:    Convert the inputted value from the SI\[m\] unit (Jupiter macro unit) to the specified unit
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_ConvertValueToMacroUnit
# ---
# Convert 1m from Jupiter macro unit system to mm
convertToMacro = JPT.ConvertValueToMacroUnit(1, JPT.UnitType.Unit_Length, 'mm') # 1m -> mm  # [hl]
JPT.Debugger(convertToMacro) # 1000
