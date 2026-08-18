import asyncio
import edge_tts
import os

BASE = os.path.join(os.path.dirname(__file__), 'audio')
OUTPUT_RATE = '+0%'

SENTENCES = {
    'marathi': [
        "आज शाळेत जायचं आहे.",
        "तुझं नाव काय आहे?",
        "आईने आज खीर केली.",
        "पाऊस खूप जोरात पडतोय.",
        "आपण उद्या गावाला जाऊया.",
        "माझं घर झाडाच्या जवळ आहे.",
        "शेतात धान्य चांगलं झालंय.",
        "आज संध्याकाळी भेटूया.",
        "तो खूप चांगला मुलगा आहे.",
        "आपल्या भाषेची काळजी घेतली पाहिजे.",
    ],
    'warli': [
        "आज शाळेला जायचं आहे.",
        "तुजं नाव काय आहे?",
        "आयी आज खीर केली.",
        "पावस खूप जोरानं वरतोय.",
        "आपण उद्या गावला जावूया.",
        "माजं घर झाडाच्या लागून आहे.",
        "शेतात धान्य बरं झालंय.",
        "आज सांजवेळी भेटूया.",
        "तो खूप चांगलो मुलगा आहे.",
        "आपल्या भाषेची काळजी घेवूया.",
    ],
    'ahirani': [
        "आज शाळेला जायचं आहे.",
        "तुझं नाव काय आहे?",
        "आईने आज खीर करली.",
        "पावस खूप जोरात पडतोय.",
        "आपण उद्या गावात जाऊ.",
        "माझं घर झाडाच्या जवळ आहे.",
        "शेतात धान्य चांगलं झालंय.",
        "आज संध्याकाळी भेटूया.",
        "तो बरंच चांगला मुलगा आहे.",
        "आपल्या भाषेची काळजी घेतली पाहिजे.",
    ],
    'vaidarbhi': [
        "आज शाळेत जायचं आहे.",
        "तुझं नाव काय आहे?",
        "आईनं आज खीर केली.",
        "पाऊस खूप जोरात पडतोय.",
        "आपण उद्या गावात जावंय.",
        "माझं घर झाडाच्या जवळ आहे.",
        "शेतात धान्य चांगलं झालंय.",
        "आज संध्याकाळी भेटूया.",
        "तो खूप चांगला मुलगा आहे.",
        "आपल्या भाषेची काळजी घ्यायला हवी.",
    ],
    'konkani': [
        "आज शाळेक जायचं आसा.",
        "तुजें नाव कितें आसा?",
        "आवयेन आज खीर केली.",
        "पावस खूप जोरान पडता.",
        "आमी उद्या गांवाक वचूया.",
        "मजें घर झाडाक लागून आसा.",
        "शेतात धान्य चांगलें जालें.",
        "आज सांजेर भेटूया.",
        "तो खूप चांगलो चेडो आसा.",
        "आमच्या भाशेची जतन करून घेवची.",
    ],
}

VOICES = {
    'marathi': 'mr-IN-AarohiNeural',
    'warli': 'mr-IN-ManoharNeural',
    'ahirani': 'mr-IN-ManoharNeural',
    'vaidarbhi': 'mr-IN-ManoharNeural',
    'konkani': 'mr-IN-ManoharNeural',
}


async def gen():
    for dialect, sentences in SENTENCES.items():
        out_dir = os.path.join(BASE, dialect)
        os.makedirs(out_dir, exist_ok=True)
        voice = VOICES[dialect]
        for i, text in enumerate(sentences, start=1):
            fname = os.path.join(out_dir, f's{i:02d}.mp3')
            communicate = edge_tts.Communicate(text, voice=voice, rate=OUTPUT_RATE)
            await communicate.save(fname)
            print(f'{dialect} s{i:02d}: {text}')
    print('DONE')


if __name__ == '__main__':
    asyncio.run(gen())
