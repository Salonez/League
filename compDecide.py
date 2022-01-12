
# This is the user data
userComp = {}
userComp['Akali'] =
userComp['Blitzcrank'] =
userComp['Braum'] =
userComp['Caitlyn'] =
userComp['Camille'] =
userComp['Chogath'] =
userComp['Darius'] =
userComp['DrMundo'] =
userComp['Ekko'] =
userComp['Ezreal'] =
userComp['Fiora'] =
userComp['Galio'] =
userComp['Gangplank'] =
userComp['Garen'] =
userComp['Graves'] =
userComp['Heimerdinger'] =
userComp['Illaoi'] =
userComp['Janna'] =
userComp['Jayce'] =
userComp['Jhin'] =
userComp['Jinx'] =
userComp['Kaisa'] =
userComp['Kassadin'] =
userComp['Katarina'] =
userComp['Kogmaw'] =
userComp['Leona'] =
userComp['Lissandra'] =
userComp['Lulu'] =
userComp['Lux'] =
userComp['Malzahar'] =
userComp['MissFortune'] =
userComp['Orianna'] =
userComp['Poppy'] =
userComp['Quinn'] =
userComp['Samira'] =
userComp['Seraphine'] =
userComp['Shaco'] =
userComp['Singed'] =
userComp['Sion'] =
userComp['Swain'] =
userComp['TahmKench'] =
userComp['Talon'] =
userComp['Taric'] =
userComp['Tristana'] =
userComp['Trundle'] =
userComp['TwistedFate'] =
userComp['Twitch'] =
userComp['Urgot'] =
userComp['Veigar'] =
userComp['Vex'] =
userComp['Vi'] =
userComp['Viktor'] =
userComp['Warwick'] =
userComp['Yone'] =
userComp['Yuumi'] =
userComp['Zac'] =
userComp['Ziggs'] =
userComp['Zilean'] =
userComp['Zyra'] =

# Comps in our database
allComps = {}

yordle = {}
yordle['Blitzcrank'] = 9
yordle['Heimerdinger'] = 9
yordle['Janna'] = 9
yordle['Lulu'] = 9
yordle['Poppy'] = 9
yordle['Tristana'] = 9
yordle['Vex'] = 9
yordle['Ziggs'] = 9
allComps[0] = yordle

innovatorEnchanterSocialite = {}
innovatorEnchanterSocialite['Ezreal'] = 9
innovatorEnchanterSocialite['Heimerdinger'] = 9
innovatorEnchanterSocialite['Janna'] = 9
innovatorEnchanterSocialite['Jayce'] = 9
innovatorEnchanterSocialite['Orianna'] = 9
innovatorEnchanterSocialite['Seraphine'] = 9
innovatorEnchanterSocialite['Taric'] = 9
innovatorEnchanterSocialite['Zilean'] = 9
allComps[1] = innovatorEnchanterSocialite

syndicateAssassin = {}
syndicateAssassin['Akali'] = 9
syndicateAssassin['Braum'] = 9
syndicateAssassin['Darius'] = 9
syndicateAssassin['Ekko'] = 9
syndicateAssassin['Janna'] = 9
syndicateAssassin['Shaco'] = 9
syndicateAssassin['Talon'] = 9
syndicateAssassin['Zyra'] = 9
allComps[2] = syndicateAssassin

arcanist = {}
arcanist['Janna'] = 9
arcanist['Lux'] = 9
arcanist['Malzahar'] = 9
arcanist['Swain'] = 9
arcanist['TwistedFate'] = 9
arcanist['Vex'] = 9
arcanist['Yuumi'] = 9
arcanist['Ziggs'] = 9
allComps[3] = arcanist

chemtech = {}
chemtech['DrMundo'] = 9
chemtech['Kaisa'] = 9
chemtech['Lissandra'] = 9
chemtech['Singed'] = 9
chemtech['Twitch'] = 9
chemtech['Urgot'] = 9
chemtech['Warwick'] = 9
chemtech['Zac'] = 9
allComps[4] = chemtech

protector = {}
protector['Blitzcrank'] = 9
protector['Caitlyn'] = 9
protector['Garen'] = 9
protector['Graves'] = 9
protector['Jayce'] = 9
protector['Kassadin'] = 9
protector['Kogmaw'] = 9
protector['Malzahar'] = 9
allComps[5] = protector

challenger = {}
challenger['Braum'] = 9
challenger['Camille'] = 9
challenger['Fiora'] = 9
challenger['Kaisa'] = 9
challenger['Leona'] = 9
challenger['Quinn'] = 9
challenger['Samira'] = 9
challenger['Yone'] = 9
allComps[6] = challenger

mutantColossus = {}
mutantColossus['Chogath'] = 9
mutantColossus['DrMundo'] = 9
mutantColossus['Kassadin'] = 9
mutantColossus['Kogmaw'] = 9
mutantColossus['Malzahar'] = 9
mutantColossus['Sion'] = 9
allComps[7] = mutantColossus

imperial = {}
imperial['Camille'] = 9
imperial['Ekko'] = 9
imperial['Janna'] = 9
imperial['Orianna'] = 9
imperial['Samira'] = 9
imperial['Swain'] = 9
imperial['Talon'] = 9
imperial['Yuumi'] = 9
allComps[8] = imperial

scrapSister = {}
scrapSister['Blitzcrank'] = 9
scrapSister['Ekko'] = 9
scrapSister['Ezreal'] = 9
scrapSister['Janna'] = 9
scrapSister['Jinx'] = 9
scrapSister['Leona'] = 9
scrapSister['Trundle'] = 9
scrapSister['Vi'] = 9
allComps[9] = scrapSister


# Deciding comp
decidedComp = ''
decidedCompPoints = 0
currPoints = 0

for comp in allComps:
    currPoints = 0
    for champ in comp:
        if champ in userComp:
            currPoints += userComp[champ]
    if currPoints > decidedCompPoints:
        decidedComp = comp
        decidedCompPoints = currPoints
