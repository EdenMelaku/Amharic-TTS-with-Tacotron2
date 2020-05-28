from .amharicSymbols import symbols

dictt = {'ሀ': 'HA', 'ሁ': 'HU', 'ሂ': 'HI', 'ሃ': 'HA', 'ሄ': 'HAE', 'ህ': 'H', 'ሆ': 'HO',
         'ለ': 'LA', 'ሉ': 'LU', 'ሊ': 'LI', 'ላ': 'LA', 'ሌ': 'LAE', 'ል': 'L', 'ሎ': 'LO', 'ሏ': 'LUA',
         'ሐ': 'HA', 'ሑ': 'HU', 'ሒ': 'HI', 'ሓ': 'HA', 'ሔ': 'HAE', 'ሕ': 'H', 'ሖ': 'HO', 'ሗ': 'HUA',
         'መ': 'ME', 'ሙ': 'MU', 'ሚ': 'MI', 'ማ': 'MA', 'ሜ': 'MAE', 'ም': 'M', 'ሞ': 'MO', 'ሟ': 'MUA',
         'ሠ': 'SE', 'ሡ': 'SU', 'ሢ': 'SI', 'ሣ': 'SA', 'ሤ': 'SAE', 'ሥ': 'S', 'ሦ': 'SO', 'ሧ': 'SUA',
         'ረ': 'RE', 'ሩ': 'RU', 'ሪ': 'RI', 'ራ': 'RA', 'ሬ': 'RAE', 'ር': 'R', 'ሮ': 'RO', 'ሯ': 'RUA',
         'ሰ': 'SE', 'ሱ': 'SU', 'ሲ': 'SI', 'ሳ': 'SA', 'ሴ': 'SAE', 'ስ': 'S', 'ሶ': 'SO', 'ሷ': 'SUA',
         'ሸ': 'SHE', 'ሹ': 'SHU', 'ሺ': 'SHI', 'ሻ': 'SHA', 'ሼ': 'SHAE', 'ሽ': 'SH', 'ሾ': 'SHO', 'ሿ': 'SHUA',
         'ቀ': 'QE', 'ቁ': 'QU', 'ቂ': 'QI', 'ቃ': 'QA', 'ቄ': 'QAE', 'ቅ': 'Q', 'ቆ': 'QO', 'ቈ': 'QUAA', 'ቊ': 'QUI',
         'ቋ': 'QUA', 'ቌ': 'QUE', 'ቍ': 'QWAE',
         'በ': 'BE', 'ቡ': 'BU', 'ቢ': 'BI', 'ባ': 'BA', 'ቤ': 'BAE', 'ብ': 'B', 'ቦ': 'BO', 'ቧ': 'BUA',
         'ቨ': 'VE', 'ቩ': 'VU', 'ቪ': 'VI', 'ቫ': 'VA', 'ቬ': 'VAE', 'ቭ': 'V', 'ቮ': 'VO', 'ቯ': 'VUA',
         'ተ': 'TE', 'ቱ': 'TU', 'ቲ': 'TI', 'ታ': 'TA', 'ቴ': 'TAE', 'ት': 'T', 'ቶ': 'TO', 'ቷ': 'TUA',
         'ቸ': 'CHE', 'ቹ': 'CHU', 'ቺ': 'CHI', 'ቻ': 'CHA', 'ቼ': 'CHAE', 'ች': 'CH', 'ቾ': 'CHO', 'ቿ': 'CHUA',
         'ኀ': 'HA', 'ኁ': 'HU', 'ኂ': 'HI', 'ኃ': 'HA', 'ኄ': 'HAE', 'ኅ': 'HI', 'ኆ': 'HO', 'ኈ': 'HUAA', 'ኊ': 'HUI',
         'ኋ': 'HUA', 'ኌ': 'HUE', 'ኍ': 'HWAE',
         'ነ': 'NE', 'ኑ': 'NU', 'ኒ': 'NI', 'ና': 'NA', 'ኔ': 'NAE', 'ን': 'N', 'ኖ': 'NO', 'ኗ': 'NUA',
         'ኘ': 'GNE', 'ኙ': 'GNU', 'ኚ': 'GNI', 'ኛ': 'GNA', 'ኜ': 'GNAE', 'ኝ': 'GN', 'ኞ': 'GNO', 'ኟ': 'GNUA',
         'አ': 'A', 'ኡ': 'U', 'ኢ': 'I', 'ኣ': 'A', 'ኤ': 'E', 'እ': 'AE', 'ኦ': 'O', 'ኧ': 'AA',
         'ከ': 'KE', 'ኩ': 'KU', 'ኪ': 'KI', 'ካ': 'KA', 'ኬ': 'KAE', 'ክ': 'K', 'ኮ': 'KO', 'ኰ': 'KUAA', 'ኲ': 'KUI',
         'ኳ': 'KUA', 'ኴ': 'KUE', 'ኵ': 'KWAE',
         'ኸ': 'HHE', 'ኹ': 'HHU', 'ኺ': 'HHI', 'ኻ': 'HHA', 'ኼ': 'HHAE', 'ኽ': 'HH', 'ኾ': 'HHO',
         'ወ': 'WE', 'ዉ': 'WU', 'ዊ': 'WI', 'ዋ': 'WA', 'ዌ': 'WAE', 'ው': 'W', 'ዎ': 'WO',
         'ዐ': 'A', 'ዑ': 'U', 'ዒ': 'I', 'ዓ': 'A', 'ዔ': 'E', 'ዕ': 'AE', 'ዖ': 'O',
         'ዘ': 'ZE', 'ዙ': 'ZU', 'ዚ': 'ZI', 'ዛ': 'ZA', 'ዜ': 'ZAE', 'ዝ': 'Z', 'ዞ': 'ZO', 'ዟ': 'ZUA',
         'ዠ': 'ZHE', 'ዡ': 'ZHU', 'ዢ': 'ZHI', 'ዣ': 'ZHA', 'ዤ': 'ZHAE', 'ዥ': 'ZH', 'ዦ': 'ZHO', 'ዧ': 'ZHUA',
         'የ': 'YE', 'ዩ': 'YU', 'ዪ': 'YI', 'ያ': 'YA', 'ዬ': 'ZAE', 'ይ': 'Y', 'ዮ': 'YO',
         'ደ': 'DE', 'ዱ': 'DU', 'ዲ': 'DI', 'ዳ': 'DA', 'ዴ': 'DAE', 'ድ': 'D', 'ዶ': 'DO', 'ዷ': 'DUA',
         'ጀ': 'JE', 'ጁ': 'JU', 'ጂ': 'JI', 'ጃ': 'JA', 'ጄ': 'JAE', 'ጅ': 'J', 'ጆ': 'JO', 'ጇ': 'JUA',
         'ገ': 'GE', 'ጉ': 'GU', 'ጊ': 'GI', 'ጋ': 'GA', 'ጌ': 'GAE', 'ግ': 'G', 'ጎ': 'GO', 'ጐ': 'GO', 'ጒ': 'GUAA',
         'ጕ': 'GUI', 'ጓ': 'GUA', 'ጔ': 'GUE', 'ጕ': 'GWAE',
         'ጠ': 'TTE', 'ጡ': 'TTU', 'ጢ': 'TTI', 'ጣ': 'TTA', 'ጤ': 'TTAE', 'ጥ': 'TT', 'ጦ': 'TTO', 'ጧ': 'TTUA',
         'ጨ': 'CCHE', 'ጩ': 'CCHU', 'ጪ': 'CCHI', 'ጫ': 'CCHA', 'ጬ': 'CCHAE', 'ጭ': 'CCH', 'ጮ': 'CCHO', 'ጯ': 'CCHUA',
         'ጰ': 'PPE', 'ጱ': 'PPU', 'ጲ': 'PPI', 'ጳ': 'PPA', 'ጴ': 'PPAE', 'ጵ': 'PPI', 'ጶ': 'PPO', 'ጷ': 'PPUA',
         'ጸ': 'TSE', 'ጹ': 'TSU', 'ጺ': 'TSI', 'ጻ': 'TSA', 'ጼ': 'TSAE', 'ጽ': 'TS', 'ጾ': 'TSO', 'ጿ': 'TSUA',
         'ፀ': 'TSE', 'ፁ': 'TSU', 'ፂ': 'TSI', 'ፃ': 'TSA', 'ፄ': 'TSAE', 'ፅ': 'TS', 'ፆ': 'TSO',
         'ፈ': 'FE', 'ፉ': 'FU', 'ፊ': 'FI', 'ፋ': 'FA', 'ፌ': 'FAE', 'ፍ': 'F', 'ፎ': 'FO', 'ፏ': 'FUA',
         'ፐ': 'PE', 'ፑ': 'PU', 'ፒ': 'PI', 'ፓ': 'PA', 'ፔ': 'PAE', 'ፕ': 'P', 'ፖ': 'PO', 'ፗ': 'PUA',
         '።': '።', '!': '!', '፣': '፣ ', '?': '?', '፤': '፤'}


def convert_to_dict_sentence(sentence):
    out = ''
    sentence = sentence.split(" ")
    while sentence:
        word = sentence.pop(0)
        for character in word:
            if (dictt.get(character) is not None):
                out = out + dictt.get(character) + " "

        out = out + ". "
    out = out.strip()
    return out


def convert_to_numbers(text):
    dict_text = convert_to_dict_sentence(text)
    finalinput = []
    current = []
    values = dict_text.split('.')
    while values:
        ch = values.pop(0)
        for i in ch.split(' '):
            if len(i) != 0:
                current.append(symbols.index(i))
        finalinput.extend(current)
        # To avoid adding a space in the last
        # TODO this doesn't seem to work.
        if values:
            finalinput.append(symbols.index(' '))
        current = []

    return finalinput
