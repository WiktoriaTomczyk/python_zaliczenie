import arcpy
from os import path

OSRODKI_PATH = path.abspath("C://Users//Wika//PycharmProjects//zaliczenie//osrodki.txt")
SHP_NAME = "dziwny.shp"
SHP_PATH = path.abspath("C://Users//Wika//PycharmProjects//zaliczenie")
PATH = path.join(SHP_PATH, SHP_NAME)



def osrodki:
    arcpy.CreateFeatureclass_management(SHP_PATH, SHP_NAME, "POINT")
    arcpy.AddField_management(PATH, "NAZWA", "TEXT")
    arcpy.AddField_management(PATH, "WMO", "TEXT")
    arcpy.AddField_management(PATH, "H", "SHORT")
    
    cur = arcpy.InsertCursor(PATH)
    with open(OSRODKI_PATH) as file:
        lines = file.readlines()[1:]
        for line in lines:
            l = line.split("\t")
            wmo = l[0]
            name = l[1]
            h = l[3]
            xst = float(l[4].split("\xb0")[0])
            xm = float(l[4].split("\xb0")[1].split("'")[0])
            xs = float(l[4].split("\xb0")[1].split("'")[1].split("''")[0])
            x = xst + (xm/60) + (xs/3600)
            yst = float(l[5].split("\xb0")[0])
            ym = float(l[5].split("\xb0")[1].split("'")[0])
            ys = float(l[5].split("\xb0")[1].split("'")[1].split("''")[0])
            y = yst + (ym/60) + (ys/3600)
            
            try:
                row = cur.newRow()
                point = arcpy.Point(x, y)
                row.Shape = point
                row.setValue("NAZWA", name)
                row.setValue("WMO", wmo)
                row.setValue("H", h)
                cur.insertRow(row)
            except Exception as e:
                print str(e)
    
    del cur
    del row


