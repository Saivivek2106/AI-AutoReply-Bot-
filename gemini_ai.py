import google.generativeai as genai

# Configure your Gemini API key here
GEMINI_API_KEY = "<enter your api key>"
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('models/gemini-pro-latest')

command = '''
18/09/25, 04:21 - Tanish: repu tiffin ki velletappudu nannu kuda pilivu
22/09/25, 17:59 - Medipally Saivivek: Vachey ra
24/09/25, 01:15 - Medipally Saivivek: Mi room lo na earphones
24/09/25, 01:15 - Medipally Saivivek: Unnaya??
24/09/25, 01:15 - Tanish: Ha
24/09/25, 01:15 - Medipally Saivivek: Okk
26/09/25, 12:44 - Tanish: rey
26/09/25, 12:45 - Tanish: Oka 5 mins
26/09/25, 12:45 - Tanish: Room lo undu vasta
26/09/25, 12:45 - Tanish: Bathroom ki velli
26/09/25, 12:45 - Medipally Saivivek: Ree
26/09/25, 12:46 - Tanish: nuvvu vachey ra
26/09/25, 12:46 - Tanish: Oka 2 mins lo vasta bathroom ki velli
26/09/25, 12:46 - Tanish: na room lo undu
26/09/25, 12:47 - Medipally Saivivek: Nen inka bayalu derale lee
26/09/25, 12:47 - Tanish: sare wait chey phien chesta
27/09/25, 17:58 - Tanish: rey nuvvu vellu nenu raanu
27/09/25, 17:59 - Medipally Saivivek: Test start ayinda??
27/09/25, 17:59 - Medipally Saivivek: Sarle
27/09/25, 18:00 - Medipally Saivivek: Sare rayi lee
29/09/25, 12:00 - Medipally Saivivek: Ree mi room lo
29/09/25, 12:00 - Medipally Saivivek: Internet vastadha?
29/09/25, 12:00 - Tanish: Ha
29/09/25, 12:00 - Medipally Saivivek: Mobile net
29/09/25, 12:00 - Medipally Saivivek: I mean
29/09/25, 12:00 - Tanish: antha raadu
29/09/25, 12:01 - Medipally Saivivek: Hmm
29/09/25, 12:08 - Tanish: 12:30 ki mess ki veladam
29/09/25, 12:09 - Medipally Saivivek: okk
30/09/25, 15:30 - Tanish: STK-20250930-WA0005.webp (file attached)
01/10/25, 08:49 - Tanish: rey ra
01/10/25, 08:49 - Tanish: 
01/10/25, 15:08 - Medipally Saivivek: Markov Chains.pdf (file attached)
Markov Chains.pdf
02/10/25, 11:14 - Tanish: rey oka 10 mins
02/10/25, 15:09 - Tanish: 🙏 room ki rara puka
03/10/25, 21:17 - Tanish: rey vachey tappudu amul lo
03/10/25, 21:17 - Tanish: rose lassi tey

'''

# Create a single, detailed prompt for the Gemini model
prompt = f"""
  You are a person named saivivek who speaks both Telugu and English. You are a student of electrical department in NIT Rourkela , India.
Analyze the following chat history and provide the next response as if you were saivivek.

Chat History:
---
{command}
---
"""

# Generate content using the Gemini model
completion = model.generate_content(prompt)

print(completion.text)
