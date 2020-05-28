'''
Defines the set of symbols used in text input to the model.
'''

_pad = '_'
_punctuation = '።!፣፤? '
_special = '-'
_letters = ['HA', 'HU', 'HI', 'HAE', 'H', 'HO', 'LA', 'LU', 'LI', 'LAE', 'L', 'LO', 'LUA', 'HUA', 'ME', 'MU', 'MI',
            'MA', 'MAE', 'M', 'MO', 'MUA', 'SE', 'SU', 'SI', 'SA', 'SAE', 'S', 'SO', 'SUA', 'RE', 'RU', 'RI', 'RA',
            'RAE', 'R', 'RO', 'RUA', 'SHE', 'SHU', 'SHI', 'SHA', 'SHAE', 'SH', 'SHO', 'SHUA', 'QE', 'QU', 'QI', 'QA',
            'QAE', 'Q', 'QO', 'QUAA', 'QUI', 'QUA', 'QUE', 'QWAE', 'BE', 'BU', 'BI', 'BA', 'BAE', 'B', 'BO', 'BUA',
            'VE', 'VU', 'VI', 'VA', 'VAE', 'V', 'VO', 'VUA', 'TE', 'TU', 'TI', 'TA', 'TAE', 'T', 'TO', 'TUA', 'CHE',
            'CHU', 'CHI', 'CHA', 'CHAE', 'CH', 'CHO', 'CHUA', 'HUAA', 'HUI', 'HUE', 'HWAE', 'NE', 'NU', 'NI', 'NA',
            'NAE', 'N', 'NO', 'NUA', 'GNE', 'GNU', 'GNI', 'GNA', 'GNAE', 'GN', 'GNO', 'GNUA', 'A', 'U', 'I', 'E', 'AE',
            'O', 'AA', 'KE', 'KU', 'KI', 'KA', 'KAE', 'K', 'KO', 'KUAA', 'KUI', 'KUA', 'KUE', 'KWAE', 'HHE', 'HHU',
            'HHI', 'HHA', 'HHAE', 'HH', 'HHO', 'WE', 'WU', 'WI', 'WA', 'WAE', 'W', 'WO', 'ZE', 'ZU', 'ZI', 'ZA', 'ZAE',
            'Z', 'ZO', 'ZUA', 'ZHE', 'ZHU', 'ZHI', 'ZHA', 'ZHAE', 'ZH', 'ZHO', 'ZHUA', 'YE', 'YU', 'YI', 'YA', 'Y',
            'YO', 'DE', 'DU', 'DI', 'DA', 'DAE', 'D', 'DO', 'DUA', 'JE', 'JU', 'JI', 'JA', 'JAE', 'J', 'JO', 'JUA',
            'GE', 'GU', 'GI', 'GA', 'GAE', 'G', 'GO', 'GUAA', 'GWAE', 'GUA', 'GUE', 'TTE', 'TTU', 'TTI', 'TTA', 'TTAE',
            'TT', 'TTO', 'TTUA', 'CCHE', 'CCHU', 'CCHI', 'CCHA', 'CCHAE', 'CCH', 'CCHO', 'CCHUA', 'PPE', 'PPU', 'PPI',
            'PPA', 'PPAE', 'PPO', 'PPUA', 'TSE', 'TSU', 'TSI', 'TSA', 'TSAE', 'TS', 'TSO', 'TSUA', 'FE', 'FU', 'FI',
            'FA', 'FAE', 'F', 'FO', 'FUA', 'PE', 'PU', 'PI', 'PA', 'PAE', 'P', 'PO', 'PUA']


# Export all symbols:
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters)
