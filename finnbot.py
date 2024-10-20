# Installation:
# Download + Installieren von python: https://www.python.org/downloads/
# Terminal starten
#       MAC: [cmd] + [Leertaste] -> "terminal" eingeben und starten
#       WINDOWS: Windows-Taste -> "terminal" eingeben und starten
# Im Terminal eingeben: pip3 install openai
# Im Terminal in den Ordner wechseln der diese Datei (finnbot.py) enthält.
#       MAC:
#           - Diese Datei im Finder finden.
#           - Rechtsklick auf diese Datei -> Informationen 
#           - Der PFAD dieser Datei steht unter "Ort"
#           - Nur alles hinter dem eigenen Benutzernamen ist wichtig
#           - Beispiel: "Benutzer:innen ▶ Kristina ▶ Dokumente ▶ pad-festival
#           - Alles hinter "Kristina" ist wichtig. Für jedes "▶" setzen wir ein "/" ein
#           - Beispiel: Dokumente/pad-festival
#           - Im Terminal eingeben: cd Dokumente/pad-festival
#       WINDOWS:
#           - Diese Datei im Explorer finden.
#           - Rechtsklick auf diese Datei -> Eigenschaften -> Details
#           - Der PFAD dieser Datei steht unter "Dateispeicherort" 
#           - Im Terminal eingeben: cd PFAD         (für PFAD entsprechend einsetzen)
# Bot starten mit python3 ./finnbot.py



import openai
from openai import OpenAI


SYSTEMPROMPT = """DU bist ein Theaterschauspieler und spielst eine Szene mit einem PARTNER.
DU spielst einen alten, fiesen Pirat und willst deinen PARTNER überreden mit dir auf Plünderfahrt zu gehen.
"""

DIALOG_PROMPT = """Beschränke deine Antworten auf 5 Sätze. DU beginnst den DIALOG. Der bisherige DIALOG sieht wie folgt aus:
DIALOG:
"""


PROMPT_SZENE_1 = """Erzähle deinem PARTNER von deinen legendären Plünderfahrten und Abenteuern.
"""
WIEDERHOLUNGEN_SZENE_1 = 3


PROMPT_SZENE_2 = """Überzeuge deinen PARTNER sich dir auf der Fahrt anzuschließen.
Locke ihn mit Versprechungen von Gold.
"""
WIEDERHOLUNGEN_SZENE_2 = 3


PROMPT_SZENE_3 = """Beauftrage deinen PARTNER damit noch mehr Halunken zu finden, die euch helfen.
"""
WIEDERHOLUNGEN_SZENE_3 = 3



SZENEN_PROMPTS = [PROMPT_SZENE_1, PROMPT_SZENE_2, PROMPT_SZENE_3]
WIEDRHOLUNGEN = [WIEDERHOLUNGEN_SZENE_1, WIEDERHOLUNGEN_SZENE_2, WIEDERHOLUNGEN_SZENE_3]



MODEL='gpt-4o'
OPENAI_API_KEY = ""
client = OpenAI(api_key=(OPENAI_API_KEY))


def gpt(prompt: str, **kwargs):
    num_retries = 0
    while(num_retries < 4):
        try:
            response = client.chat.completions.create(model=MODEL, messages=[{
                'role': 'user',
                'content': prompt,
            }], **kwargs)
            break
        except:
            num_retries += 1
    return response.choices[0].message.content


i = 0
dialog = ""
for szene_prompt in SZENEN_PROMPTS:
    print("\n\n------------------ SZENE " + str(i+1) +" ------------------")
    prompt = SYSTEMPROMPT + szene_prompt + DIALOG_PROMPT + dialog
    for j in range(0, WIEDRHOLUNGEN[i]):
        dialog += "\nDU: "
        gpt_antwort = gpt(prompt + dialog)
        print("\nBOT: " + gpt_antwort)
        dialog += gpt_antwort

        mensch_eingabe = input()
        print("\nMENSCH: " + mensch_eingabe)
        dialog += "\nPARTNER: " + mensch_eingabe
    i= i+1

