# Title:   JPT.ConvertValueToDocUnit()
# Desc:    Convert the inputted value from SI\[m\] units (Jupiter macro units) to the current Jupiter unit system
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_ConvertValueToDocUnit
# ---
# Convert 1m in Jupiter macro unit system to the current unit system of Jupiter
convertToDoc = JPT.ConvertValueToDocUnit(1, JPT.UnitType.Unit_Length)  # [hl]
JPT.Debugger(convertToDoc)
