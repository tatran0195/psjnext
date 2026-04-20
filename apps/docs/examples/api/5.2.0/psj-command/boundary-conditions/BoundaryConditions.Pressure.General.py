# Title:   BoundaryConditions.Pressure.General()
# Desc:    Create a general pressure applied to the selected Face, Element or Group. User inputs the pressure value and it will apply the pressure to the selected items
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.Pressure.General
# ---
Geometry.Part.Cube()

created_lbc = BoundaryConditions.Pressure.General(dPressure=10000000.0,   # [hl]
                                                  crlTargets=[Face(26)])  # [hl]

JPT.Debugger(created_lbc)
