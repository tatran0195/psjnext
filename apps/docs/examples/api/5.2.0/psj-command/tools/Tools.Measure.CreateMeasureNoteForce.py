# Title:   Tools.Measure.CreateMeasureNoteForce()
# Desc:    Create a Measure Note for Measure > Force function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.CreateMeasureNoteForce
# ---
#Please load result contains force result here.
#Input IDs of nodes to measure.
n1=1
n2=2  # [hl:start]
n3=3
  # [hl:end]
Tools.Measure.CreateMeasureNoteForce(
        strNoteName="Force1", 
        crlTargets=[Node(n1, n2, n3)])
