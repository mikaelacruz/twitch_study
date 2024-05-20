import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# List of names to replace in the URL
names = ['KaiCenat', 'xQc', 'tarik', 'HasanAbi', 'summit1g', 'ESLCS', 'zackrawrr', 'Fextralife', 'Jynxzi', 'shroud',
         'k3soju', 'LIRIK', 'BLASTPremier', 'Quin69', 'Riot Games (riotgames)', 'ohnePixel', 'LEC', 'Gorgc', 'scump',
         'LVNDMARK', 'sodapoppin', 'loltyler1', 'MOONMOON', 'CohhCarnage', 'Clix', 'Caedrel', 'Mizkif',
         'TSM_ImperialHal', 'ESL_DOTA2', 'forsen', 'GamesDoneQuick', 'VALORANT', 'LCK', 'Elajjaz', 'NICKMERCS',
         'Thebausffs', 'ironmouse', 'Call of Duty (callofduty)', 'Maximilian_DOOD', 'Rainbow6', 'RocketLeague',
         'Jinnytty', 'LCS', 'Pestily', 'Foolish', 'Maximum', 'Agent00', 'QuickyBaby', 'Distortion2', 'PGL_Dota2',
         'caseoh_', 'Nmplol', 'PENTA', 'EsfandTV', 'Symfuhny', 'Lord_Kebun', 'Dantes', 'dota2ti', 'Kyedae',
         'AdmiralBahroo', 'Echo_Esports', 'boxbox', 'iiTzTimmy', 'JokerdTV', 'BarbarousKing', 'Nikolarn', 'Mande',
         'yourragegaming', 'moistcr1tikal', 'SmiteGame', 'EpulzeGaming', 'qojqva', 'Fanum', 'hJune', 'CDawgVA',
         'singsing', 'Chess', 'Tubbo', 'mrbluwu', 'pokelawls', 'Xaryu', 'Emiru', 'Drututt', 'supertf', 'skill4ltu',
         'NiceWigg', 'LPL', 'hitsquadgodfather', 'Zoomaa', 'Sequisha', 's0mcs', '39daph', 'EWC_a', 'Kyle', 'DatModz',
         'Otzdarva', 'wudijo', 'Glorious_E', 'mira', 'runthefutmarket', 'Ninja', 'Emongg', 'RduLIVE', 'DansGaming',
         'Faide', 'mL7support', 'nl_Kripp', 'HisWattson', 'robcdee', 'fl0m', 'TeePee', 'ChilledChaos', 'Stewie2K',
         'AussieAntics', 'erobb221', 'Towelliee', 'buddha', 'Dakillzor', 'CasinoDaddy', 'Grubby', 'RealzBlueWater',
         'setsuko', 'ESLCSb', 'w0n23', 'Gladd', 'Philza', 'agurin', 'aceu', 'Jay3', 'DisguisedToast', 'PaymoneyWubby',
         'Aydan', 'plaqueboymax', 'OverwatchContenders', 'NickEh30', 'ExtraEmily', 'AdmiralBulldog', 'TenZ', 'B0aty',
         'Northernlion', 'MissMikkaa', 'HutchMF', 'JenFoxxx', 'Jerma985', 'angryginge13', 'playapex', 'fifakillvizualz',
         'GernaderJake', 'Payo', 'Flats', 'Saintone', 'Zizaran', 'Tectone', 'TFBlade', 'ZealsAmbitions', 'IWDominate',
         'GMHikaru', 'henyathegenius', 'Zentreya', 'CCT_CS', 'HusKerrs', 'Jankos', 'sneakylol', 'BadBoyHalo',
         'easportsfc', 'Subroza', 'Mongraal', 'Insym', 'GingiTV', 'CoconutB', 'dogdog', 'lol_nemesis', 'Broxah',
         'dasMEHDI', 'SypherPK', 'AuzioMF', 'Skermz', 'Mathil1', 'Castro_1021', 'WorldofTanks', 'Enviosity', 'Shylily',
         'MrSavage', 'willneff', 'VALORANT_EMEA', 'Beast1k', 'Guzu', 'Steelmage', 'SlotsMarko', 'btssmash', 'CYR',
         'PrimeVideo', 'dafran', 'The_Happy_Hob', 'Giantwaffle', 'midbeast', 'CriticalRole', 'Trey24k', 'vedal987',
         'Wirtual', 'Smoke', 'TheRunningManZ', 'Aztecross', 'sinatraa', 'Thijs', 'Grimmmz', 'TeamLiquid', 'anny',
         'VALORANT_Americas', 'Vinesauce', 'Brawlhalla', 'Bawkbasoup', 'Ben_', 'AlveusSanctuary', 'superjj102',
         'imaqtpie', 'QTCinderella', 'Strippin', 'Deadlyslob', 'WillerZ', 'Raxxanterax', 'Psychoghost', 'VeliaInn',
         'emilyywang', 'AvoidingThePuddle', 'Sommerset', 'Shotzzy', 'MST3K', 'zwebackhd', 'AnnieFuchsia', 'BurkeBlack',
         'UtopiaGaming', 'StaysafeTV', 'BobRoss', 'BobbyPoffGaming', 'imls', 'robinsongz', 'Fakturka', 'OTKnetwork',
         'Oatley', 'DiazBiffle', 'AdinRoss', 'ShahZaM', 'Replays', 'BLAST', 'Ray__C', 'Pobelter', 'ESL_SC2', 'Xop0',
         'Silent', 'Stoopzz', 'SmallAnt', 'StreamerHouse', 'BotezLive', 'jasontheween', 'CapcomFighters', 'Zemie',
         'masondota2', 'DougDoug', 'RATIRL', 'Surefour', 'bebe872', 'Aurateur', 'MitchJones', 'Warcraft', 'Pikabooirl',
         'Loeya', 'Warframe', 'AnthonyZ', 'buckefps', 'FoxenKin', 'daltoosh', 'KingGothalion', 'Ziqoftw', 'shanks_ttv',
         'Posty', 'Kxpture', 'shxtou', 'Tomato', 'TrU3Ta1ent', 'QuarterJade', 'roflgator', 'RDCgaming', 'Nadeshot',
         'Sacriel', 'vei', 'A_Seagull', 'Faux', 'Doublelift', 's1mple', 'KungenTV', '4HEAD', 'BruceDropEmOff', 'Klean',
         'filian', 'Thiefs', 'Knut', 'chocoTaco', 'Pieface23', 'Kitboga', 'RiffTrax', 'AsianJeff', 'Tfue',
         'olofmeister', 'Nadia', 'Fairlight_Excalibur', 'Rob2628', 'PGL_DOTA2EN2', 'ESAMarathon', 'TwitchRivals',
         'TheJRM_', 'dorki', 'crokeyz', 'JeffHoogland', 'SharonQueen', 'Taylor_Jevaux', 'Alkaizerx', 'AmazonMusic',
         'Calebhart42', 'Timmac', 'Halo', 'JOEYKAOTYK', 'fobm4ster', 'nyanners', 'Naowh', 'lilsimsie', 'MembTV',
         'dakotaz', 'KYR_SP33DY', 'Joe_Bartolozzi', 'LoLWorldChampionship', 'BoxyFresh', 'Quantum', 'kkatamina', 'NymN',
         'Method', 'dannyaarons', 'Scarra', 'Preachlfw', 'Spear_Shot', 'TinaKitten', 'MuTeX', 'Shotz', 'sweetdreams',
         'tarzaned', 'NBA2KLeague', 'DooleyNotedGaming', 'Gingy', 'lydiaviolet', 'iateyourpie', 'kyootbot', 'cloakzy',
         'Scrapie', 'Yogscast', 'AriaSaki', 'Lacari', 'KatEvolved', 'TeeGrizzley', 'KingGeorge', 'coopertv', 'Sliggytv',
         'taxi2g', 'asianbunnyx', 'Graycen', 'Alinity', 'Ray', 'Nick28T', 'LilAggy', 'Aspen', 'VGBootCamp',
         'PUBG_BATTLEGROUNDS', 'cdewx', 'Insym_', 'Rusty', 'FlixGames', 'TheRealKnossi', 'Grimmmz1', 'zizaran1', 'Nich',
         'Neace', 'Five0AnthO', 'ClintStevens', 'Karazh', 'shiey', 'Fandy', 'Awkward_Travels', 'Susu_jpg',
         'tacticalgramma', 'Phixate', 'Swagg', 'AndyMilonakis', 'Kananda', 'Sodapoppin', 'Trick2g', 'HasanAbi',
         's1mple', 'shroud', 'ESL_CSGO', 'ESL_SC2', 'pokimane', 'Trainwreckstv', 'itsHafu', 'Nightblue3', 'Limmy',
         'Wolfabelle', 'Katrine', 'joshseki', 'DeraJN', 'stableronaldo', 'DashDucks', 'bbreadman', 'Central_Committee',
         'OkCode', 'sips_', 'SheefGG', 'bananabrea', 'itmeJP', 'Louuis', 'Zoil', 'Anthony_Kongphan', 'LordAethelstan',
         'Sanchovies', 'Simurgh', 'Mr_Mammal', 'Lacy', 'RTGame', 'RachtaZ', 'Jabroni_Mike', 'Rogue', 'Auslots',
         'Mortdog', 'Silvervale', 'RanbooLive', 'XenosysVex', 'Sweatcicle', 'PsheroTV', 'ibabyrainbow', 'Vader',
         'Mmorpg', 'PROD', 'Trick2g', 'Arteezy', 'Albralelie', 'DolphinChemist', 'Bugs', 'PlayOverwatch', 'Quackity',
         'MurderCrumpet', 'Lobanjicaa', 'uhSnow', 'stankRat', 'Rengawr', 'MacieJay', 'xChocoBars', 'JASONR',
         'OLESYALIBERMAN', 'Tigz', 'Odablock', 'CRREAM', 'GrandPooBear', 'Dashy', 'Lysium', 'EvaLangwin', 'Datto',
         'Whippy', 'jingggxd', 'Ssaab', 'Atrioc', 'UFDTech', 'Kaysan', 'SheriffEli', 'Tyrone', 'KarasMai', 'KarQ',
         'Warn', 'Bajheera', 'dishsoaptft', 'Liam', 'Grimm', 'DezGamez', 'JohnPanio', 'WagamamaTV', 'Hiko', 'CuteDog_',
         'PirateSoftware', 'Savix', 'JayGriffyuh', 'AnnaCramling', 'Hungrybox', 'OniGiri', 'starsmitten', 'Harry',
         'keanelol', 'FitMC', 'itsRyanHiga', 'KeshaEuw', 'VALORANT_Pacific', 'Robbaz', 'chessbrah', 'blau', 'VERHULST',
         'AsmodaiTV', 'Criken', 'Arex', '윤개굴이 (yoon_froggy)', 'LuluLuvely', 'Back2Warcraft', 'hpduketv', 'TheChief1114',
         'Pokemon', 'Kiaraakitty', 'PewDiePie', 'DanucD', 'AutoSpeed', 'wadu', 'Dino_xx', 'ATK', 'Dekkster', 'Nagzz21',
         'Aa9skillz']

# URL pattern
base_url = "https://streamscharts.com/channels/{}"

# Path to GeckoDriver (ensure it's in your PATH or provide the full path)
driver_path = "/Users/miki/Documents/geckodriver"

# Initialize the WebDriver for Firefox
driver = webdriver.Firefox(executable_path=driver_path)

# Prepare a list to store the data
data_list = []

for name in names:
    try:
        # Construct the URL
        url = base_url.format(name)

        # Open the URL
        driver.get(url)

        # Give some time for the page to load (adjust the sleep time as needed)
        time.sleep(3)

        # Extract the desired data
        # Modify the following line to select the correct element containing the data
        # Example: data = driver.find_element(By.ID, "data-element-id").text
        data = driver.find_element(By.CSS_SELECTOR, "div.about-block__item:nth-child(5) > span:nth-child(2)").text

        # Append the name and data to the list
        data_list.append([name, data])
    except NoSuchElementException:
        # If the element is not found, skip this name and continue with the next one
        print(f"Data not found for {name}. Skipping...")
        continue

# Close the WebDriver
driver.quit()

# Write the data to a CSV file
output_path = '/Users/miki/Downloads/create_list_of_birthdays.csv'
with open(output_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write the header
    writer.writerow(['Name', 'Data'])
    # Write the data rows
    writer.writerows(data_list)

print(f"Data collection complete. Check the {output_path} file.")
