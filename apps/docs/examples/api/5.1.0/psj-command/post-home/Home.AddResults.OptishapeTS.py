# Title:   Home.AddResults.OptishapeTS()
# Desc:    Add Optishape-TS results to the current Jupiter Database.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.AddResults.OptishapeTS
# ---
# Put your sample files
Result1 = "C:/Temp/topo.op2"
Result2 = "C:/Temp/topo_result.op2"

Home.ImportResults.OptishapeTS(strlPaths=[Result1])
Home.AddResults.OptishapeTS(strlPaths=[Result2])
