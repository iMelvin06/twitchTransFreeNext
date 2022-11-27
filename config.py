######################################################
# PLEASE CHANGE FOLLOWING CONFIGS ####################
Twitch_Channel          = 'target_channel_name'

Trans_Username          = 'trans_user_name'
Trans_OAUTH             = 'oauth_for_trans_user'
SeventvUserID           = '7Tv_User_ID'

#######################################################
# OPTIONAL CONFIGS ####################################
Trans_TextColor         = 'GoldenRod'
# Blue, Coral, DodgerBlue, SpringGreen, YellowGreen, Green, OrangeRed, Red, GoldenRod, HotPink, CadetBlue, SeaGreen, Chocolate, BlueViolet, and Firebrick

Main_Language           = 'en'
Translate_Me            = True
lang_TransToHome        = 'en'
lang_HomeToOther        = 'es'

FeatureAddBackEmotes    = True

Show_ByName             = True
Show_ByLang             = True

Ignore_Lang             = ['jp','af','sq','am','ar','hy','as','ay','az','bm','eu','be','bn','bho','bs','bg','ca','ceb','zh-CN','zh','zh-TW','co','hr','cs','da','dv','doi','nl','eo','et','ee','fil','fi','fr','fy','gl','ka','de','el','gn','gu','ht','ha','haw','he','iw','hi','hmn','hu','is','ig','ilo','id','ga','it','ja','jv','jw','kn','kk','km','rw','gom','ko','kri','ku','ckb','ky','lo','la','lv','ln','lt','lg','lb','mk','mai','mg','ms','ml','mt','mi','mr','mni-Mtei','lus','mn','my','ne','no','ny','or','om','ps','fa','pl','pt','pa','qu','ro','ru','sm','sa','gd','nso','sr','st','sn','sd','si','sk','sl','so','su','sw','sv','tl','tg','ta','tt','te','th','ti','ts','tr','tk','ak','uk','ur','ug','uz','vi','cy','xh','yi','yo','zu']
#Ignore_Lang             = ['']
Ignore_Users            = ['Nightbot', 'BikuBikuTest', 'StreamElements','ai_yui_translator']
Ignore_Line             = ['http', 'BikuBikuTest', '888', '８８８', 'https']
Delete_Words            = ['saatanNooBow', 'BikuBikuTest']

# Any emvironment, set it to `True`, then text will be read by TTS voice!
# TTS_In:User Input Text, TTS_Out:Bot Output Text
TTS_In                  = False
TTS_Out                 = False
TTS_Kind                = "gTTS" # You can choice "CeVIO" if you want to use CeVIO as TTS.
# CeVIO_Cast            = "さとうささら" # When you are using CeVIO, you must set voice cast name.

# if you make TTS for only few lang, please add langID in the list
# for example, ['ja'] means Japanese only, ['ko','en'] means Korean and English are TTS!
ReadOnlyTheseLang       = []

# Select the translate engine ('deepl' or 'google')
Translator              = 'google'

# Use Google Apps Script for tlanslating
# e.g.) GAS_URL         = 'https://script.google.com/macros/s/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/exec'
GAS_URL                 = ''

# Enter the suffix of the Google Translate URL you normally use.
# Example: translate.google.co.jp -> 'co.jp'
#          translate.google.com   -> 'com'
GoogleTranslate_suffix  = 'co.jp'

# If you meet any bugs, You can check some error message using Debug mode (Debug = True)
Debug                   = False
