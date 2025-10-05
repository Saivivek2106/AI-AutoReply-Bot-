import pyautogui
import time
import pyperclip
import google.generativeai as genai

# Configure your Gemini API key here
GEMINI_API_KEY = "<Enter you api key>"
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

def is_last_message_from_sender(chat_log, sender_name="Tanish"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2025] ")[-1]
    if sender_name in messages:
        return True 
    return False
    # 1349 1065 --> chrome icon
    # from 733 222 to 1425 ,1045-->text sel
    # 1436 958 -->deselect
    # 1215 1059 -->click vs code
# Step 1: Click on the chrome icon at coordinates (1284, 1057)
pyautogui.click(1349, 1065)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (877,248)  to(905, 901) to select the text
    pyautogui.moveTo(736 ,202)
    pyautogui.dragTo(728 ,972, duration=2.0, button='left')  # Drag for 2 seconds

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 2 seconds to ensure the copy command is completed
    pyautogui.click(1440 , 945)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    
    if is_last_message_from_sender(chat_history):
        # Create a single, detailed prompt for the Gemini model
        prompt = f"""
        You are a person named Medipally Saivivek who speaks both Telugu and English. You are a student of electrical department in NIT Rourkela , India.
        Your task is to analyze the following chat history and provide a funny roast as the next response.
        IMPORTANT: Do not start your response with a timestamp and name like '[21:02, 12/6/2025] Tanish: '. Just give the text message content.

        Chat History:
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

        """
        
        # Generate content using the Gemini model
        completion = model.generate_content(prompt)
        response = completion.text
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(776 , 987)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('enter')


