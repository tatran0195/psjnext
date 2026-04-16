# Title:   Analysis.ADVC.MakeProcess.DynamicExplicit()
# Desc:    Create an ADVC Dynamic Explicit process. This process could be created in one time or multiple times
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.ADVC.MakeProcess.DynamicExplicit
# ---
step = Analysis.ADVC.MakeProcess.DynamicExplicit(strName="Process_0",   # [hl]
                                                 iGeomNonlinear=3,  # [hl]
                                                 advcStructTimeStep=ADVC_STRUCT_TIME_STEP(iNumOfInc=10),   # [hl]
                                                 listLoadNode=[],   # [hl]
                                                 listLoadCaseNode=[],  # [hl]
                                                 listLoadNodeContact=[],   # [hl]
                                                 listAdvcRefStressResult=[])  # [hl]

JPT.Debugger(step)
