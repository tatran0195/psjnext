# Title:   JPT.GetAvailableResultOption()
# Desc:    Get available result option of the inputted result type
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_GetAvailableResultOption
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

available_result_option = \  # [hl:start]
    JPT.GetAvailableResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                 1,
                                 1,
                                 "Displacement",
                                 "X",
                                 JPT.PostResultDataLoc.POST_LOC_ON_NODE,
                                 JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                                                            1,
                                                            1,
                                                            "Displacement",
                                                            "X",
                                                            JPT.PostResultDataLoc.POST_LOC_ON_NODE)
                                )  # [hl:end]

JPT.Debugger(available_result_option)

#Component of PostDataOp
print("Location: " + str(available_result_option.loc))
print("Conversion: " + str(available_result_option.cnv))
print("Continuously: " + str(available_result_option.cont))
print("Coordinate: " + str(available_result_option.coord))
print("Load 1D: " + str(available_result_option.load1d))
print("Load 2D: " + str(available_result_option.load2d))
print("Complex: " + str(available_result_option.complex))
print("Phase Angle: " + str(available_result_option.phaseAngle))
print("User Coordinate ID: " + str(available_result_option.userCoordSysId))
