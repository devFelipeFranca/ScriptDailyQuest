Foresdracke = 0
Crysmantis = 0
Ifrit = 0
Bloodbeak = 0
Horrornet = 0
Bastinx = 0
Redeath = 0
Gigantula = 0
Crustea = 0

Forgotten = 0
Zealot = 0
Observer = 0

Darktaur = 0
Petraclops = 0
Gorgon = 0

Krakomin = 0
Ninjana = 0

kill49 = False
kill50 = False
kill100 = False

questMode = False


def updateQuestCount(name, questMode):
    script.SetVar('questMode', False)
    script.SetVar(questMode, False)
    script.SetVar(name, 0)
    if(questMode == 'kill49'):
        script.StatusMessage(
        str(name) + " Done! I'm back in 50 minutes")
        script.LogoutFor(3000) # 50 min
    else:
         script.StatusMessage(str(name) + "done!")

def killStatusQuest(name):
    prevValue = script.GetVar(name)
    script.SetVar(name, prevValue + 1)
    currentValue = script.GetVar(name)
    script.StatusMessage(str(name) + " " + str(currentValue))

    return currentValue


def updateKillsAmount(name):

    if(questMode):
        if(kill49):
            currentValue = killStatusQuest(name)

            if(currentValue > 48):
                updateQuestCount(name, 'kill49')

        if(kill50):
            currentValue = killStatusQuest(name)
            
            if(currentValue > 50):
                updateQuestCount(name, 'kill50')

        if(kill100):
            currentValue = killStatusQuest(name)
            
            if(currentValue > 100):
                updateQuestCount(name, 'kill100')



def changeWayPoint():
    currentWayPoint = script.GetWay()
    inQuest = script.GetVar('questMode')
    if(currentWayPoint != 89 & inQuest == False):
        nextWayPoint = currentWayPoint + 1
        script.SetWay(nextWayPoint, 0)
        if(currentWayPoint == 8):
            script.SetVar('kill49', True)
            script.SetVar('questMode', True)
        if(currentWayPoint == 11):
            script.SetVar('questMode', True)
            script.SetVar('kill49', True)
        if(currentWayPoint == 14):
            script.SetVar('questMode', True)
            script.SetVar('kill49', True)
        if(currentWayPoint == 17):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
        if(currentWayPoint == 20):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
        if(currentWayPoint == 23):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
        if(currentWayPoint == 26):
            script.SetVar('questMode', True)
            script.SetVar('kill50', True)
        if(currentWayPoint == 29):
            script.SetVar('questMode', True)
            script.SetVar('kill50', True)
        if(currentWayPoint == 32):
            script.SetVar('questMode', True)
            script.SetVar('kill50', True)
        if(currentWayPoint == 45):
            script.SetVar('questMode', True)
            script.SetVar('kill50', True)
        if(currentWayPoint == 49):
            script.SetVar('questMode', True)
            script.SetVar('kill50', True)
        if(currentWayPoint == 53):
            script.SetVar('questMode', True)
            script.SetVar('kill50', True)
        if(currentWayPoint == 62):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
        if(currentWayPoint == 66):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
        if(currentWayPoint == 76):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
        if(currentWayPoint == 80):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
        if(currentWayPoint == 84):
            script.SetVar('questMode', True)
            script.SetVar('kill100', True)
    if(currentWayPoint == 89):
        script.StatusMessage("The end...")
        script.LogoutFor(86400) # 24hrs


def onWaypointsEnded():
    changeWayPoint()


def onKilledEnemy(name, templateId):
    updateKillsAmount(name)


def onReceiveEnemyHp(uid, hp_percent, name):
    if(name == 'Ninjana'):
        script.UseItemIdEx(2603, 5)


def onConnect():
    currentWayPoint = script.GetWay()
    if(currentWayPoint == 90):
        nextWayPoint = 1
        script.SetWay(nextWayPoint, 0)
