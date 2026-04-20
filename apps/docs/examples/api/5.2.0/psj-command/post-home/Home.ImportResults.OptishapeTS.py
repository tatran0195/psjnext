# Title:   Home.ImportResults.OptishapeTS()
# Desc:    Import Optishape-TS result file.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ImportResults.OptishapeTS
# ---
import os
#Put your result
result_data='C:/Temp/OptiShapeResult'

Home.ImportResults.OptishapeTS(  # [hl:start]
    strlPaths=[os.path.join(result_data,"sample.op2")])  # [hl:end]
