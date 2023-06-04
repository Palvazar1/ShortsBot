from hugchat import hugchat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import re
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
from cleantext import clean


def splitTextToTriplet(string):
  words = string.split()
  grouped_words = [' '.join(words[i:i + 3]) for i in range(0, len(words), 3)]
  return grouped_words


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("window-size=1400,600")
driver = webdriver.Chrome(chrome_options=chrome_options)

#driver.maximize_window()

file = 'cookies.json'

chatbot = hugchat.ChatBot(cookie_path=file)

voices = [
  "Donald Trump", "joe biden", "barack obama", "bart simpson", "elon musk",
  "morgan freeman", "watchMojo", "Yoda", "MrBeast", "spongebob",
  "patrick star", "Squidward", "quandale dingle"
]
pres = ["Donald Trump", 'joe biden', "barack obama"]

voice = random.choice(voices)

vids = ['Minecraft1.mp4', 'M1.mp4', 'M3.mp4', 'M4.mp4', 'F1.mp4']

start = random.randrange(0, 200)

print(voice)

audExp = []

subs = []

from selenium.common.exceptions import NoSuchElementException


def check_exists_by_xpath(xpath):
  try:
    driver.find_element(By.XPATH, xpath)
  except NoSuchElementException:
    return False
  return True


def uploading(title):
  driver = webdriver.Chrome(chrome_options=chrome_options)
  driver.get(
    'https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F&ec=65620&hl=en&passive=true&service=youtube&uilel=3&ifkv=Af_xneFobKCyy5N9vyD1ikh80ny1X-wQGnR6da5y5ML5InrZuL3CNMACRS2Y6ABbcwgUQFL3Y8TV1A&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
  )
  WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierId"]')))
  driver.find_element(
    By.XPATH,
    '//*[@id="identifierId"]').send_keys("celebritysnippets@gmail.com" +
                                         Keys.ENTER)
  ##
  ##
  time.sleep(15)
  print(
    driver.find_element(By.XPATH,
                        '//*[@id="captchaimg"]').get_attribute("src"))
  ##
  ##
  capans = input("Waiting for human Captcha answer: ")
  driver.find_element(By.XPATH, '//*[@id="ca"]').send_keys(capans + Keys.ENTER)
  time.sleep(20)
  driver.find_element(By.XPATH,
                      '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(
                        'k^sR!9m*7@j$2#5q' + Keys.ENTER)
  time.sleep(10)
  if check_exists_by_xpath(
      '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/span/figure'
  ):
    print("Code is: " + driver.find_element(
      By.XPATH,
      '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/section/div/div/span/figure/samp'
    ).text)

  time.sleep(15)
  driver.get(
    'https://studio.youtube.com/channel/UCXjCgWcn8LXeAR85xryZBJA/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D'
  )
  time.sleep(15)
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input"
  ).send_keys("/home/runner/Shorts-Bot-With-New-Voice-FORKED/finalTest.mp4")
  #driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input").submit()
  time.sleep(15)
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"
  ).send_keys(Keys.CONTROL + "a")
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"
  ).send_keys(Keys.BACKSPACE)
  time.sleep(5)
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div"
  ).send_keys(title)
  time.sleep(5)
  driver.execute_script(
    "return arguments[0].scrollIntoView();",
    driver.find_element(
      By.XPATH,
      '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/div/ytcp-button/div'
    ))
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/div/ytcp-button/div").click()
  time.sleep(5)
  driver.execute_script(
    "return arguments[0].scrollIntoView();",
    driver.find_element(
      By.XPATH,
      '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input'
    ))
  time.sleep(15)
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input"
  ).send_keys("Fun Facts, ai, shorts")
  time.sleep(7)
  driver.execute_script(
    "return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]"))
  time.sleep(5)
  driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]").click()
  time.sleep(5)
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]"
  ).click()
  time.sleep(10)
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]"
  ).click()
  
  time.sleep(5)

  #PRIVATE
  #driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[1]").click()

  #PUBLIC
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]"
  ).click()

  time.sleep(5)
  driver.find_element(
    By.XPATH,
    "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[3]"
  ).click()


def GoBotGo():
  #ChatGPT Script
  id = chatbot.new_conversation()
  chatbot.change_conversation(id)

  msg = "Write a short piece of text with less than 150 letters total and less than 220 characters about random interesting facts using simple and short words, making sure it is NOT political. Make sure that it is only the words of the script and that you DO NOT ADD ANY stage cues such as [scene opens], speaking cues such as 'Nararator:' at the beginning, make sure there is NO title or scene descriptions, or sentences of you saying that you are attempting to write a script such as 'Here is your script:' are added. Also, spell any usage of the word 'don't' as 'do not'. Do not use emojis and do NOT put hashtags at the end."

  msgFunny = "Write a short piece of text with less than 150 letters and less than 220 characters total about comically incorrect facts that you make seem legitamate using simple and short words, making sure it is NOT political. Make sure that it is only the words of the script and that you DO NOT ADD ANY stage cues such as [scene opens], speaking cues such as 'Nararator:' at the beginning, make sure there is NO title or scene descriptions, or sentences of you saying that you are attempting to write a script such as 'Here is your script:' are added. Also, spell any usage of the word 'don't' as 'do not'. Do not use emojis and do NOT put hashtags at the end."

  msgchoice = random.choice([msg, msg, msg, msg, msgFunny])

  if msgchoice == msgFunny:
    print("this ones a laugher")

  Speech = chatbot.chat(msgchoice)
  Speech = Speech.replace('*', "")
  Speech = Speech.replace('"', "")
  Speech = Speech.replace("#", "")
  Speech = clean(Speech, no_emoji=True)
  Speech = Speech.upper()
  print(Speech)
  #Speech = "This is just a temporary test cause i dont think the vid is working and now im making it longer to not get errors"

  clip = VideoFileClip(random.choice(vids))
  clip = clip.without_audio()

  strt = 0
  sn = 1
  durCalc = 0

  #Audio
  email = "fjskl@fsjkl.com"
  passwrd = "asdf1234"

  #driver.get("https://account.topmediai.com/login")
  #driver.find_element(By.XPATH, '//*[@id="app"]/section/div[1]/div[2]/div/div/form/div[1]/div/div/input').send_keys(email)
  #time.sleep(5)
  #driver.find_element(By.XPATH, '//*[@id="app"]/section/div[1]/div[2]/div/div/form/div[2]/div/div/input').send_keys(passwrd)
  #time.sleep(10)
  #driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="app"]/section/div[1]/div[2]/div/div/button'))
  #time.sleep(10)
  #n = 125
  miniScripts = re.findall(r'\W*(?:\w+\W+){1,15}', Speech)
  #mst = []
  #for i in miniScripts:
    #i = i.rstrip("\n")
    #mst.append(i.rstrip("\ "))
  #miniScripts = mst
  print(miniScripts)

  for i in miniScripts:
    driver.minimize_window()
    driver.get("https://www.topmediai.com/text-to-speech/")
    time.sleep(20)
    driver.execute_script(
    "return arguments[0].scrollIntoView();",
    driver.find_element(
      By.XPATH, '/html/body/main/section[8]/div[2]/div[2]/div/button[1]'))
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '/html/body/main/section[8]/div[2]/div[2]/div/button[1]'))
    time.sleep(10)
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '/html/body/main/section[2]/div[1]/div[1]/div[2]/input'))
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/div[1]/div[2]/input").send_keys(voice)
    time.sleep(5)
    
    #if driver.find_element(By.XPATH, '//*[@id="Login"]').is_displayed():
    if i == miniScripts[0]:
      driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '//*[@id="Login"]'))
      time.sleep(5)
      driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/input').send_keys(email)
      time.sleep(3)
      driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[2]/div[1]/input').send_keys(passwrd)
      time.sleep(3)
      driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/form/div[2]/button'))
      
    else:
      pass
      
    driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/div[3]/div[2]/ul/li[1]"))
    charact = WebDriverWait(driver, 30).until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/div[3]/div[2]/ul/li[1]")))
    driver.execute_script("arguments[0].click();", charact)
    #driver.find_element(By.XPATH, "/html/body/main/section[2]/div[1]/div[3]/div[2]/ul/li[1]").click()
    time.sleep(5)
    driver.execute_script(
    "return arguments[0].scrollIntoView();",
    driver.find_element(By.XPATH, '/html/body/main/section[2]/div[2]/div[3]/div[1]/div[2]/div'))
    driver.execute_script("arguments[0].click();", driver.find_element(
    By.XPATH, "/html/body/main/section[2]/div[2]/div[3]/div[1]/div[2]/div"))
    time.sleep(5)
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "/html/body/main/section[4]/div/p"))
    time.sleep(5)
    driver.find_element(
    By.XPATH, "/html/body/main/section[2]/div[2]/div[3]/div[1]/div[2]/div").send_keys(i)
    driver.maximize_window()
    time.sleep(20)
    if driver.find_element(By.XPATH, "/html/body/main/section[4]/div/p").is_displayed() == True:
      print("click")
      driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '/html/body/main/section[4]/div/p'))
      driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "/html/body/main/section[4]/div/p"))
    time.sleep(5)
    driver.execute_script("return arguments[0].scrollIntoView();",
    driver.find_element(By.XPATH, '/html/body/main/section[2]/div[2]/div[3]/div[2]/button'))
    time.sleep(5)
    driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "/html/body/main/section[2]/div[2]/div[3]/div[2]/button"))
    time.sleep(5)
      #WebDriverWait(driver, 30).until(driver.find_element(
      #By.XPATH, "/html/body/main/section[5]/div/div").is_displayed())
    while driver.find_element(By.XPATH, "/html/body/main/section[5]/div/div").is_displayed():
      time.sleep(10)
      print("generating")
    time.sleep(5)
    if driver.find_element(By.XPATH, "/html/body/main/section[4]/div/p").is_displayed() == True:
      print("click")
      driver.execute_script("return arguments[0].scrollIntoView();", driver.find_element(By.XPATH, '/html/body/main/section[4]/div/p'))
      driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "/html/body/main/section[4]/div/p"))
    time.sleep(10)
    audioFile = driver.find_element(
    By.XPATH, "/html/body/main/section[3]/ul/li[1]/audio").get_attribute("src")
    audExp.append(AudioFileClip(audioFile).set_start(durCalc))
    print(audioFile)

    durCalc = durCalc + AudioFileClip(audioFile).duration
  
  strt = 0

  for i in splitTextToTriplet(Speech):
    end = strt + (durCalc * (len(i) / len(Speech)) * .95)
    print((durCalc * (len(i) / len(Speech)) * .98))
    subs.append(((strt, end), i))
    strt = end
    sn += 1

  nmbr = 0
  for i in range(len(subs)):
      i = list(subs[i])
      print(i)
      if i[1] == '':
        print(i[1])
        i[1] = " "
        i = tuple(i)
        print(i)
        subs[nmbr] = i
        nmbr += 1
      else:
        i = tuple(i)
        subs[nmbr] = i
        nmbr += 1
  print(subs)

  #name = re.sub("\(.*?\)","()", voice)
  #name = name.replace("(","").replace(")","")

  generator = lambda txt: TextClip(
    txt, font='Futura Bold.otf', fontsize=50, color='white', size=clip.size)

  name = voice

  if name in pres:
    name = "THE PRESIDENTS"
  else:
    pass

  title = "FUN FACTS W/ " + name.upper()

  driver.close()

  clip = clip.subclip(start, start + durCalc + .5)
  print(clip.duration)
  subtitles = SubtitlesClip(subs, generator)

  ps = random.randrange(10, int(3540 - CompositeAudioClip(audExp).duration))

  phonk = AudioFileClip("phonk.mp3").subclip(
    ps, ps + CompositeAudioClip(audExp).duration + .5)

  phnkQ = phonk.volumex(0.1)

  finalVidSO = CompositeAudioClip(audExp).volumex(2.5)
  miniclips = [
    'https://us-tuna-sounds-files.voicemod.net/b102e197-ad50-4dae-8c76-c37b4ac495b7-1644403871266.mp3',
    'https://us-tuna-sounds-files.voicemod.net/ad617e2a-e2e6-4495-91ad-f586b9d3d1fe.mp3',
    'https://us-tuna-sounds-files.voicemod.net/d44b327c-fae1-4908-a0cd-3d6aeef9dbfe-1646727004917.mp3',
    'https://us-tuna-sounds-files.voicemod.net/ade71f0d-a41b-4e3a-8097-9f1cc585745c-1646035604239.mp3',
    'https://us-tuna-sounds-files.voicemod.net/794c04b5-a20a-4b2e-bf1f-a5a9dec17c79-1648531449530.mp3',
    'https://us-tuna-sounds-files.voicemod.net/5f0dc8f4-6f19-41c8-b81b-94ff6f28c315-1654031850107.mp3',
    'https://us-tuna-sounds-files.voicemod.net/13ea69f4-17da-4a45-b22a-78a9f46dd101-1648192838035.mp3',
    'https://us-tuna-sounds-files.voicemod.net/bfd07a08-90ca-478e-b1ea-f4bbe03bf4b9-1648744376186.mp3',
    'https://us-tuna-sounds-files.voicemod.net/c0cc75b6-82a8-454e-b599-0fa330c9c5d7-1645675251182.mp3',
    'https://us-tuna-sounds-files.voicemod.net/becad187-dd1a-490e-8f26-4d4ccfebd661-1648110260760.mp3',
    'https://us-tuna-sounds-files.voicemod.net/1086e37b-e0d8-4d3d-9bbd-267a2d48eda6-1640189422789.mp3',
    'https://us-tuna-sounds-files.voicemod.net/3e9d7e5c-5d4e-4c06-a954-80b5c3e75307.mp3',
    'https://us-tuna-sounds-files.voicemod.net/2146f784-2b85-4cbe-ab0d-fad01ca35656-1643678952525.mp3',
    'https://us-tuna-sounds-files.voicemod.net/0f7a844f-9e39-4705-8fa0-70671d8bcd20-1643206976731.mp3'
  ]
  minichosen = random.choice(miniclips)

  minichosen = AudioFileClip(minichosen)

  ministrt = random.randrange(0, int(CompositeAudioClip(audExp).duration - minichosen.duration))

  AfinalVid = clip.set_audio(CompositeAudioClip([finalVidSO, phnkQ]))

  print("Doing first half of video...")
  AfinalVid.write_videofile("finalAlmost.mp4", codec='libx264', audio_codec='aac')

  clip.close()
  AfinalVid.close()

  nclp = VideoFileClip("finalAlmost.mp4")

  finalVid = nclp.set_audio(CompositeAudioClip([nclp.audio, CompositeAudioClip([minichosen]).set_start(ministrt)]))

  finalVid = CompositeVideoClip([finalVid, subtitles.set_position('center', 'middle')])
  print("Wrapping up the video...")
  finalVid.write_videofile("finalTest.mp4", codec='libx264', audio_codec='aac', threads=5)

  finalVid.close()
  nclp.close()

  uploading(title=title)
  print("Posted!")

  while True:
    pass


GoBotGo()

#uploading(title="FUN FACTS W/ THE PRESIDENTS!")
