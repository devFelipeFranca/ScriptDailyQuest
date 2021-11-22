Foresdracke = 0
Crysmantis = 0
Ifrit = 0
Bloodbeak = 0
Horrornet = 0
Bastinx = 0
Redeath = 0
Gigantula = 0
Crustea = 0
questMod = False


def updateKillsAmount(name):
    if(name == 'Foresdrake'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 48):
            script.StatusMessage(
                "Foresdrake Done! I'm back in 50 minutes")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
            script.LogoutFor(3000)
    if(name == 'Crysmantis'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 48):
            script.StatusMessage(
                "Crysmantis Done! I'm back in 50 minutes")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
            script.LogoutFor(3000)
    if(name == 'Ifrit'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 48):
            script.StatusMessage(
                "Ifrit Done! I'm back in 50 minutes")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
            script.LogoutFor(3000)
    if(name == 'Bloodbeak'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 60):
            script.StatusMessage(
                "Bloodbeak Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Horrornet'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 60):
            script.StatusMessage(
                "Horrornet Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Bastinx'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 60):
            script.StatusMessage(
                "Bastinx Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Redeath'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 50):
            script.StatusMessage(
                "Redeath Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Gigantula '):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 50):
            script.StatusMessage(
                "Gigantula Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Crustea'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 50):
            script.StatusMessage(
                "Crustea Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Observer'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 50):
            script.StatusMessage(
                "Observer Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Zealot'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 50):
            script.StatusMessage(
                "Zealot Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Forgotten'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 50):
            script.StatusMessage(
                "Forgotten Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Ninjana'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 100):
            script.StatusMessage(
                "Ninjana Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Krakomin'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 50):
            script.StatusMessage(
                "Krakomin Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Gorgon'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 100):
            script.StatusMessage(
                "Gorgon Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Petraclops'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 10):
            script.StatusMessage(
                "Petraclops Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)
    if(name == 'Darktaur'):
        beforeKillsAmount = script.GetVar(name)
        script.SetVar(name, beforeKillsAmount + 1)
        currentKillsAmount = script.GetVar(name)
        script.StatusMessage(str(name) + " " + str(currentKillsAmount))
        if(currentKillsAmount > 100):
            script.StatusMessage(
                "Darktaur Done!")
            script.SetVar('questMod', False)
            script.SetVar(name, 0)


def changeWayPoint():
    currentWayPoint = script.GetWay()
    inQuest = script.GetVar('questMod')
    if(currentWayPoint != 89 & inQuest == False):
        nextWayPoint = currentWayPoint + 1
        script.SetWay(nextWayPoint, 0)
        if(currentWayPoint == 8):
            script.SetVar('questMod', True)
        if(currentWayPoint == 11):
            script.SetVar('questMod', True)
        if(currentWayPoint == 14):
            script.SetVar('questMod', True)
        if(currentWayPoint == 17):
            script.SetVar('questMod', True)
        if(currentWayPoint == 20):
            script.SetVar('questMod', True)
        if(currentWayPoint == 23):
            script.SetVar('questMod', True)
        if(currentWayPoint == 26):
            script.SetVar('questMod', True)
        if(currentWayPoint == 29):
            script.SetVar('questMod', True)
        if(currentWayPoint == 32):
            script.SetVar('questMod', True)
        if(currentWayPoint == 45):
            script.SetVar('questMod', True)
        if(currentWayPoint == 49):
            script.SetVar('questMod', True)
        if(currentWayPoint == 53):
            script.SetVar('questMod', True)
        if(currentWayPoint == 62):
            script.SetVar('questMod', True)
        if(currentWayPoint == 66):
            script.SetVar('questMod', True)
        if(currentWayPoint == 76):
            script.SetVar('questMod', True)
        if(currentWayPoint == 80):
            script.SetVar('questMod', True)
        if(currentWayPoint == 84):
            script.SetVar('questMod', True)
    if(currentWayPoint == 89):
        currentKillsAmount = script.GetVar('Darktaur')
        script.StatusMessage(str(currentKillsAmount))
        script.StatusMessage("The end...")
        script.Logout()


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
