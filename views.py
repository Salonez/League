from flask import Blueprint, render_template, request, url_for, redirect
import backend

views = Blueprint(__name__, "views")

@views.route("/", methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        # print(request.form["0"])
        # Make dictionary for number of each champion the user has
        userComp = {}
        userComp['Akali'] = request.form["0"]
        userComp['Blitzcrank'] = request.form["1"]
        userComp['Braum'] = request.form["2"]
        userComp['Caitlyn'] = request.form["3"]
        userComp['Camille'] = request.form["4"]
        userComp['Chogath'] = request.form["5"]
        userComp['Darius'] = request.form["6"]
        userComp['DrMundo'] = request.form["7"]
        userComp['Ekko'] = request.form["8"]
        userComp['Ezreal'] = request.form["9"]
        userComp['Fiora'] = request.form["10"]
        userComp['Galio'] = request.form["11"]
        userComp['Gangplank'] = request.form["12"]
        userComp['Garen'] = request.form["13"]
        userComp['Graves'] = request.form["14"]
        userComp['Heimerdinger'] = request.form["15"]
        userComp['Illaoi'] = request.form["16"]
        userComp['Janna'] = request.form["17"]
        userComp['Jayce'] = request.form["18"]
        userComp['Jhin'] = request.form["19"]
        userComp['Jinx'] = request.form["20"]
        userComp['Kaisa'] = request.form["21"]
        userComp['Kassadin'] = request.form["22"]
        userComp['Katarina'] = request.form["23"]
        userComp['Kogmaw'] = request.form["24"]
        userComp['Leona'] = request.form["25"]
        userComp['Lissandra'] = request.form["26"]
        userComp['Lulu'] = request.form["27"]
        userComp['Lux'] = request.form["28"]
        userComp['Malzahar'] = request.form["29"]
        userComp['MissFortune'] = request.form["30"]
        userComp['Orianna'] = request.form["31"]
        userComp['Poppy'] = request.form["32"]
        userComp['Quinn'] = request.form["33"]
        userComp['Samira'] = request.form["34"]
        userComp['Seraphine'] = request.form["35"]
        userComp['Shaco'] = request.form["36"]
        userComp['Singed'] = request.form["37"]
        userComp['Sion'] = request.form["38"]
        userComp['Swain'] = request.form["39"]
        userComp['TahmKench'] = request.form["40"]
        userComp['Talon'] = request.form["41"]
        userComp['Taric'] = request.form["42"]
        userComp['Tristana'] = request.form["43"]
        userComp['Trundle'] = request.form["44"]
        userComp['TwistedFate'] = request.form["45"]
        userComp['Twitch'] = request.form["46"]
        userComp['Urgot'] = request.form["47"]
        userComp['Veigar'] = request.form["48"]
        userComp['Vex'] = request.form["49"]
        userComp['Vi'] = request.form["50"]
        userComp['Viktor'] = request.form["51"]
        userComp['Warwick'] = request.form["52"]
        userComp['Yone'] = request.form["53"]
        userComp['Yuumi'] = request.form["54"]
        userComp['Zac'] = request.form["55"]
        userComp['Ziggs'] = request.form["56"]
        userComp['Zilean'] = request.form["57"]
        userComp['Zyra'] = request.form["58"]
        backend.compDecide(userComp)
        return render_template("index.html")
    else:
        return render_template("index.html")

@views.route("/metacomps")
def metacomps():
    return render_template("metacomps.html")