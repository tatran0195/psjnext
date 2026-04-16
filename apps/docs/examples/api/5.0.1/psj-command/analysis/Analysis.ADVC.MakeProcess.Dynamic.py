# Title:   Analysis.ADVC.MakeProcess.Dynamic()
# Desc:    Create an ADVC Dynamic process. This process could be created in one time or multiple times
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/analysis/Analysis.ADVC.MakeProcess.Dynamic
# ---
step = Analysis.ADVC.MakeProcess.Dynamic(strName="Process_0",   # [hl]
                                         iGeomNonlinear=0,  # [hl]
                                         advcStructTimeStep=ADVC_STRUCT_TIME_STEP(),   # [hl]
                                         bConvergence=False,  # [hl]
                                         advcConvergence=ADVC_CONVERGENCE(),   # [hl]
                                         bContact=False,  # [hl]
                                         advcContactIter=ADVC_CONTACT_ITER(),  # [hl]
                                         bAutoIncrement=False,   # [hl]
                                         advcAutoIncrement=ADVC_AUTO_INCREMENT(),   # [hl]
                                         bDynamic=False,  # [hl]
                                         advcDynamic=ADVC_DYNAMIC(),   # [hl]
                                         crEdit=None,   # [hl]
                                         listLoadNode=[],   # [hl]
                                         listLoadCaseNode=[],  # [hl]
                                         listLoadNodeContact=[],   # [hl]
                                         ilOutputParamList=[],   # [hl]
                                         iRefType=-1,   # [hl]
                                         strRefPath="",  # [hl]
                                         listAdvcRefStressResult=[])  # [hl]

JPT.Debugger(step)
