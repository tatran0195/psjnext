# Title:   JPT.ConvertFromMacroUnit()
# Desc:    Convert the inputted value with the specified unit to the SI\[m\] unit (Jupiter macro unit)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ConvertFromMacroUnit
# ---
# Convert 1mm to the Jupiter macro unit system
convertFromMacro = JPT.ConvertFromMacroUnit(1, JPT.UnitType.Unit_Length, 'mm') # mm -> m  # [hl]
JPT.Debugger(convertFromMacro) # 0.001 m
