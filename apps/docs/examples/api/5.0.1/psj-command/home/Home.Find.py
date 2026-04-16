# Title:   Home.Find()
# Desc:    Search entities in Jupiter by using their IDs or names
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/home/Home.Find
# ---
Geometry.Part.Cube()
Geometry.Part.Cube(dlOrigin=[0.01,
                             0.0,
                             0.0],
                   strName="Cube_2",
                   iPartColor=6409934)

find_name = Home.Find(strSearch="cube")  # [hl:start]
find_name_match = Home.Find(strSearch="cube_2",
                            bFindMatch=True)
find_id = Home.Find(strSearch="1")  # [hl:end]

JPT.Debugger(find_name)

JPT.Debugger(find_name_match)

JPT.Debugger(find_id)
