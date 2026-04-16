# Title:   BoundaryConditions.BodyLoads.Gravity()
# Desc:    Define the acceleration load of gravity to the selected part. User inputs the value of the acceleration load of gravity and it will return the acceleration load of gravity to the selected parts
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.BodyLoads.Gravity
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.BodyLoads.Gravity(strName="Gravity1",   # [hl]
                                                   dlGravity=[0.0, 0.0, -9810.0],  # [hl]
                                                   crlTargets=[Part(1)])  # [hl]

JPT.Debugger(created_bcs)
