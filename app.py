from flask import Flask, request, jsonify, render_template
import utils



# app izeneko aldagai batean Flask objetu bat sortzen dugu. 
# Objetu honek metodo asko ditu, eta horietaz aprobetxatuko gara behar ditugun deiak egiteko
app = Flask(__name__)





# ========================= #
#        TEMPLATES          #
# ========================= #
'''
Ruta hutsean index.html plantilla kargatuko du
render_template metodoak "templates" izeneko karpeta baten barruan HTML formatuko dokumentuak bilatuko ditu.
Metodo hau erabili ahal izateko inportatu egin behar dugu. Hau lehen lerroan egin dugu. 
'''
@app.route("/")
def home():
    return render_template("index.html")






# ========================= #
#        ITZULPENA          #
# ========================= #
'''
Funtzio honek "/translate" URL-an gertatzen dena definituko du.

main.js dokumentuan deitu diogu URL honi.
const response = await fetch("/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ phrase })
    });

JS-rekin JSON bat bidaliko dugu URL horretara piglatinera itzuli nahi dugun esaldia duena "phrase" izeneko elementuan gordeta
'''
@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json() # request.get_jason() metodoak JS-ak bidali duena jasoko du
    phrase = data.get("phrase", "") # Ondoren .get metodoarekin "phrase" izeneko atributu
    translated = utils.translate_to_piglatin(phrase) # utils.py dokumentuan gordeta dugun "transalte_to_piglatin" funtzioari deituko diogu
    return jsonify({"translation": translated}) # Itzulpena JSON batean bidaliko dugu "translation" izeneko elementuan


