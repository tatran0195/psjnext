# Title:   JPT.ConvertFromDocUnit()
# Desc:    Convert the inputted value from the current using Jupiter unit system to SI\[m\] units (Jupiter macro units)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ConvertFromDocUnit
# ---
# Convert the value = 1 from the current Jupiter Unit system to Jupiter macro unit system
convertFromDoc = JPT.ConvertFromDocUnit(1, JPT.UnitType.Unit_Length)  # [hl]
JPT.Debugger(convertFromDoc)
