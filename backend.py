
# Function which decides the best comp(s) the user should go for.
def compDecide(userComp):
    # Convert strings to integers and empty strings to 0 in userComp dictionary
    for champion in userComp:
        if userComp[champion] == "":
            userComp[champion] = "0"
        userComp[champion] = int(userComp[champion])
    
    # Comps in our database
    allComps = {}

    yordles = {}
    yordles['Blitzcrank'] = 9
    yordles['Heimerdinger'] = 9
    yordles['Janna'] = 9
    yordles['Lulu'] = 9
    yordles['Poppy'] = 9
    yordles['Tristana'] = 9
    yordles['Vex'] = 9
    yordles['Ziggs'] = 9
    allComps['Yordles'] = yordles

    innovatorEnchanterSocialites = {}
    innovatorEnchanterSocialites['Ezreal'] = 9
    innovatorEnchanterSocialites['Heimerdinger'] = 9
    innovatorEnchanterSocialites['Janna'] = 9
    innovatorEnchanterSocialites['Jayce'] = 9
    innovatorEnchanterSocialites['Orianna'] = 9
    innovatorEnchanterSocialites['Seraphine'] = 9
    innovatorEnchanterSocialites['Taric'] = 9
    innovatorEnchanterSocialites['Zilean'] = 9
    allComps['Innovator Enchanter Socialites'] = innovatorEnchanterSocialites

    syndicateAssassins = {}
    syndicateAssassins['Akali'] = 9
    syndicateAssassins['Braum'] = 9
    syndicateAssassins['Darius'] = 9
    syndicateAssassins['Ekko'] = 9
    syndicateAssassins['Janna'] = 9
    syndicateAssassins['Shaco'] = 9
    syndicateAssassins['Talon'] = 9
    syndicateAssassins['Zyra'] = 9
    allComps['Syndicate Assassins'] = syndicateAssassins

    arcanists = {}
    arcanists['Janna'] = 9
    arcanists['Lux'] = 9
    arcanists['Malzahar'] = 9
    arcanists['Swain'] = 9
    arcanists['TwistedFate'] = 9
    arcanists['Vex'] = 9
    arcanists['Yuumi'] = 9
    arcanists['Ziggs'] = 9
    allComps['Arcanists'] = arcanists

    chemtechs = {}
    chemtechs['DrMundo'] = 9
    chemtechs['Kaisa'] = 9
    chemtechs['Lissandra'] = 9
    chemtechs['Singed'] = 9
    chemtechs['Twitch'] = 9
    chemtechs['Urgot'] = 9
    chemtechs['Warwick'] = 9
    chemtechs['Zac'] = 9
    allComps['Chemtechs'] = chemtechs

    protectors = {}
    protectors['Blitzcrank'] = 9
    protectors['Caitlyn'] = 9
    protectors['Garen'] = 9
    protectors['Graves'] = 9
    protectors['Jayce'] = 9
    protectors['Kassadin'] = 9
    protectors['Kogmaw'] = 9
    protectors['Malzahar'] = 9
    allComps['Protectors'] = protectors

    challengers = {}
    challengers['Braum'] = 9
    challengers['Camille'] = 9
    challengers['Fiora'] = 9
    challengers['Kaisa'] = 9
    challengers['Leona'] = 9
    challengers['Quinn'] = 9
    challengers['Samira'] = 9
    challengers['Yone'] = 9
    allComps['Challengers'] = challengers

    mutantColossus = {}
    mutantColossus['Chogath'] = 9
    mutantColossus['DrMundo'] = 9
    mutantColossus['Kassadin'] = 9
    mutantColossus['Kogmaw'] = 9
    mutantColossus['Malzahar'] = 9
    mutantColossus['Sion'] = 9
    allComps['Mutant Colossus'] = mutantColossus

    imperials = {}
    imperials['Camille'] = 9
    imperials['Ekko'] = 9
    imperials['Janna'] = 9
    imperials['Orianna'] = 9
    imperials['Samira'] = 9
    imperials['Swain'] = 9
    imperials['Talon'] = 9
    imperials['Yuumi'] = 9
    allComps['Imperials'] = imperials

    scrapSisters = {}
    scrapSisters['Blitzcrank'] = 9
    scrapSisters['Ekko'] = 9
    scrapSisters['Ezreal'] = 9
    scrapSisters['Janna'] = 9
    scrapSisters['Jinx'] = 9
    scrapSisters['Leona'] = 9
    scrapSisters['Trundle'] = 9
    scrapSisters['Vi'] = 9
    allComps['Scrap Sisters'] = scrapSisters

    # Deciding comp
    comp_list = []
    decidedComp = 'none'
    decidedCompPoints = 0
    currPoints = 0

    for comp in allComps:
        currPoints = 0
        for champ in allComps[comp]:
            if champ in userComp:
                currPoints += userComp[champ]
        if currPoints > decidedCompPoints:
            decidedComp = comp
            decidedCompPoints = currPoints
    comp_list.append(decidedComp)
    for comp in allComps:
        currPoints = 0
        for champ in allComps[comp]:
            if champ in userComp:
                currPoints += userComp[champ]
        if currPoints == decidedCompPoints and comp != decidedComp:
            comp_list.append(comp)

    for comp in comp_list:
        print(comp)
    

#the bot determines highest power spike with the comp : rolling or levelling 
def power_spike_decide(compChosen, userLevel):
    if userLevel == 9:
        print("Roll Down")
    else:
        if compChosen == 'Yordles':
            print("Slow Roll")

        if compChosen == 'Innovator Enchanter Socialites':
            print("Level up to 9")

        if compChosen == 'Syndicate Assassins':
            print("Standard")

        if compChosen == 'Arcanists':
            print("Standard")

        if compChosen == 'Chemtechs':
            print("Level up to 9")

        if compChosen == 'Protectors':
            print("Level up to 9")

        if compChosen == 'Challengers':
            print("Standard")

        if compChosen == 'Mutant Colossus':
            print("Slow Roll")

        if compChosen == 'Imperials':
            print("Slow Roll")  
        
        if compChosen == 'Scrap Sisters':
            print("Level up to 9")