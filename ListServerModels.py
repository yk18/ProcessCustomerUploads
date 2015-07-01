__author__ = 'ykogan'


known_series = ["PROLIANT", "UCS", "UCSB", "UCSC", "FLEX", "POWEREDGE", "THINKSERVER", "THINKSTATION", "BLADE CENTER", "BLADECENTER",
                 "OPTIPLEX", "OMNICUBE", "SUPERSERVER", "GEMINI", "INTEGRITY"]

known_models = [# HP ProLiant Models
                "DL580", "BL460c", "MICROSERVER", "DL120", "BL280C", "DL180",
                "DL320E", "DL360", "DL360P","DL360E","DL380", "DL380P","DL380E", "DL560", "DL585", "DL385P",
                "DL980", "ML310E", "SL390S", "BL685C", "ML370", "BL420C", "BL460C", "BL620C", "BL660C", "DL160",
                "BL465C", "DL165", "ML350", "ML350P", "ML330", "BL260C", "DL385", "BL490C", "SL270S", "DL185",
                "DL320", "ML350E", "SL230S", "SL170S", "BL680C", "DL785", "ML150", "DL365", "DL370", "DL388P",
                # IBM xSeries Models
                "X3100", "X3200", "X3250", "X3350", "X3400", "X3630", "X3650", "X3655", "X3550", "X3500", "X3690", "X3740",
                "X3750", "X3755", "X3850", "X3950", "X3530", "X3300", "X3620",
                # IBM Flex Models
                "X240", "X440", "X220", "X480", "X280", "X222", "X880",
                # Cisco UCS Models
                "C220", "B200", "C210", "C240", "C22", "C24", "B22", "C200", "B230", "C260",
                # Dell PowerEdge Models
                "R620", "R420", "R620", "T110", "R720", "T620", "T420", "T320", "M620", "M520", "R610",
                "R710", "2950", "R520", "M605", "2900", "M600", "R320", "R510", "1950", "R910", "R210",
                # ThinkServer Models
                "RD230", "RD330", "RD340", "RD430", "RD440", "RD540", "RD630", "RD640", "TS130", "TS140", "TD340",
                "RD530", "TS430", "RD220", "TS440", "TD230", "RD240", "RD650", "RS140", "TS200", "TD350", "TD100",
                # BladeCenter Models
                "HS23E", "HX5", "HS23", "HS21", "HS12", "HS22", "HS22V",
                # OptiFlex
                "790", "7010",
                # Acer Models
                "AB460", "AR180", "AT350", "AR180", "AT115", "AC100", "AB2X280", "AT110", "AN1600", "AR380", "AR160",
                "AR320", "AR360", "AT310", "AP130", "AR585"]

known_generations = ["GEN9", "GEN8", "G9", "G8", "G7", "G6", "G5", "M1", "M2", "M3", "M4", "M5", "F1", "F2"]

words_to_skip = ["SERVER", "PLATFORM"]

def getKnownModels():
    return known_models

def getKnownSeries():
    return known_series

def getKnownGenerations():
    return known_generations

def getWordsToSkip():
    return words_to_skip