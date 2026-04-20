# Title:   BoundaryConditions.Force.General()
# Desc:    Create a general force applied to the selected Face, Edge or Node. User inputs the force values and it will apply the force to the selected items
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/boundary-conditions/BoundaryConditions.Force.General
# ---
Geometry.Part.Cube()

created_bcs = BoundaryConditions.Force.General(strName="Force1",  # [hl]
                                               forceLBC=FORCE_LBC(vecForce=[1.0,  # [hl]
                                                                            DFLT_DBL,   # [hl]
                                                                            DFLT_DBL]),  # [hl]
                                               crlTargets=[Face(23)])  # [hl]

JPT.Debugger(created_bcs)
