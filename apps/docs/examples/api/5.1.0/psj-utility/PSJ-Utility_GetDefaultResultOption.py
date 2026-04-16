# Title:   JPT.GetDefaultResultOption()
# Desc:    Get default result option setting of the inputted result type
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetDefaultResultOption
# ---
# Prepare model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
JPT.Exec('CmdImportTSVOp2Post({}, 1, 1.0472, 1.0472, 0, 0, 0)'.format(samplePath))

default_result_option = \  # [hl:start]
    JPT.GetDefaultResultOption(JPT.PostAnalysisType.POST_ANALYSIS_LINEAR_STATIC,
                               1,
                               1,
                               "Displacement",
                               "X",
                               1)
  # [hl:end]
JPT.Debugger(default_result_option)

# Component of PostDataOp
print("Location: " + str(default_result_option.loc))
print("Conversion: " + str(default_result_option.cnv))
print("Continuously: " + str(default_result_option.cont))
print("Coordinate: " + str(default_result_option.coord))
print("Load 1D: " + str(default_result_option.load1d))
print("Load 2D: " + str(default_result_option.load2d))
print("Complex: " + str(default_result_option.complex))
print("Phase Angle: " + str(default_result_option.phaseAngle))
print("User Coordinate ID: " + str(default_result_option.userCoordSysId))
