
DEFAULT_STGS = {"commas":"false"}
SETTINGS_PATH = "fibonacci.cfg"
TYPE_STR = type("")
TYPE_LIST = type([])

def validateString( s ):
    # returns True if OK, False if invalid
    assert(type(s)==TYPE_STR)
    return not( True in [ (c in ['=','\n']) for c in s ] )

def writeSettings( settings_list ):
    assert(type(settings_list)==TYPE_LIST)
    try:
        f = open(SETTINGS_PATH,"w")
        f.write( "\n".join([ "=".join(s) for s in settings_list ]) )
        f.close()
    except IOError:
        print("Could not write cfg file.")
        return False
    return True

def getSettingsList():
    # returns settings as
    # <dict> "ok":boolean
    # if ok == True , TYPE_LIST:list
    try:
        f = open(SETTINGS_PATH,"r")
        l = [ p.strip().split('=') for p in f ]
        f.close()
    except FileNotFoundError:
        print("Could not find cfg file. Creating default cfg file...")
        if generateSettingsFile():
            print("The default cfg file was created successfully.")
        return None
    except IOError:
        print("Could not read cfg file.")
        return None
    return l

def generateSettingsFile():
    # generates cfg file according to default settings
    # returns True if successful and False if error occurred on I/O
    return writeSettings([ [k,v] for k,v in DEFAULT_STGS.items() ])

def validateSettingFormat( s ):
    if type(s) != TYPE_LIST:
        print("Setting isn't table.")
        return False
    if len(s) != 2:
        print("Setting table size is wrong.")
        return False
    if True in [ type(x) != TYPE_STR for x in s]:
        print("Settings variables aren't string.")
        return False
    if False in [ validateString(x) for x in s]:
        print("Settings variables are invalid.")
        return False
    return True

def getSettingLabel( s ):
    assert(validateSettingFormat(s))
    return s[0]

def getSettingValue( s ):
    assert(validateSettingFormat(s))
    return s[1]

def formatSetting( label, new_value ):
    return [label,new_value]

def getSettingValueFromLabel( settings_list , label ):
    assert(type(settings_list)==TYPE_LIST)
    assert(type(label)==TYPE_STR)
    for s in settings_list:
        if getSettingLabel(s) == label:
            return getSettingValue(s)
    return None

def printSettings( settings_list ):
    assert(type(settings_list)==TYPE_LIST)
    print("Label\tValue")
    print("---------------")
    for s in settings_list:
        if not validateSettingFormat(s):
            return
        print(getSettingLabel(s)+'\t'+getSettingValue(s))
    if len(settings_list) == 0:
        print("No settings found.")

def EditSetting( settings_list , label , new_value ):
    # saves the new value in the cfg file
    assert(type(settings_list)==TYPE_LIST)
    assert(type(label)==TYPE_STR)
    assert(type(new_value)==TYPE_STR)
    if len(new_value) == 0 or not validateString(new_value):
        print("\nInvalid string for new value.")
        return False
    lbl_list = [ getSettingLabel(s) for s in settings_list ]
    if not label in lbl_list:
        print("\nUnexpected error occurred. Label not in list.")
        return False
    idx = lbl_list.index(label)
    settings_list[idx] = formatSetting(label,new_value)
    return writeSettings(settings_list) 

def launch( cmd ):
    assert(type(cmd)==TYPE_STR)
    if cmd == 'sd':
        #resets settings to default
        if generateSettingsFile():
            print("Settings were set to default.")
    elif cmd in ['se','sv']:
        #print settings list
        slist = getSettingsList()
        if slist == None:
            print("Could not print settings list.\n")
            return
        printSettings(slist)
        if cmd == 'se':
            print()
            lbl = input("Label: ")
            curr_value = getSettingValueFromLabel(slist,lbl)
            if curr_value == None:
                print("Label not recognized.\n")
                return
            print("Current value for '"+lbl+"': "+curr_value)
            new_value = input("Setting new value: ")
            if EditSetting(slist,lbl,new_value):
                print("New value set successfully.")
    else:
        print("Command '"+cmd+"' not recognized.")
    print()

