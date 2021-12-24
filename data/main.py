import pandas as pd
import numpy as np
import os


def convert_row_to_xml(row):
    return """
        <doc>
            <field name="artist">%s</field>
            <field name="song">%s</field>
            <field name="genre">%s</field>
            <field name="language">%s</field>
            <field name="lyrics">%s</field>
        </doc>
        """ % (row.Artist, row.Song, row.Genre, row.Language, row.Lyrics)


OUTPUT_PATH = 'data/out.xml'
if os.path.exists(OUTPUT_PATH):
    os.remove(OUTPUT_PATH)

df = pd.read_csv('data/archive/train.csv', sep=',')
# length
print("Row Count: " + str(len(df.index)))

# list of entries in col Language
language_list = df['Language'].unique()
print("LANGUAGE: ")
print(language_list)
print("LANGUAGE COUNT: " + str(language_list.size))

# list of entries in col genre
genre_list = df['Genre'].unique()
print("GENRE: " + genre_list)
print("GENRE COUNT: " + str(genre_list.size))

## clean dataset
# remove lyrics with guitar tabs
df_notabs = df.drop(df[df["Lyrics"].str.contains(r"\|-", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<-", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<1", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<2", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<3", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<4", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<5", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<6", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<7", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<8", na=False)].index)
df_notabs = df_notabs.drop(df_notabs[df_notabs["Lyrics"].str.contains(r"<9", na=False)].index)

# remove spanish translations
df_no_es_transl = df_notabs.drop(df[df["Song"].str.contains("raducc", na=False)].index)
df_no_es_transl = df_no_es_transl.drop(df[df["Song"].str.contains("español", na=False)].index)

# get only spanish entries
df_only_spanish = df_no_es_transl.loc[df_no_es_transl['Language'] == 'es']
spanish_artists = df_only_spanish['Artist'].unique()

# get only english entries
df_only_english = df_no_es_transl.loc[df_no_es_transl['Language'] == 'en']
english_artists = df_only_english['Artist'].unique()

spanish_artist = [
    'matanza',
    'os mutantes',
    'oficina g3',
    'paralamas do sucesso',
    'pato fu',
    'rosa de saron',
    'tihuana',
    'ultraje a rigor',
    'vivendo do ocio',
    'velhaas virgens',
    'calle 13',
    'becky g',
    'camila',
    'camila cabello',
    'enrique iglesias',
    'julieta venegas',
    'laura pausini',
    'luan santana',
    'paulina rubio',
    'ricky martin',
    'shakira',
    'la factoria',
    'la gusana ciega',
    'la ley',
    'la lupita',
    'angeles del infierno',
    'menudo',
    'mercedes sosa',
    'don tetto',
    'roque valero',
    'todos tus muertos',
    'tolidos',
    'juan fernnado velasco',
    'juan gabriel',
    'juan luis guerra',
    'juana molina',
    'juanes',
    'el canto del loco',
    'el gran silencio',
    'elefante',
    'miguel mateos',
    'mijares',
    'alex ubago',
    'carlos santana',
    'antonio orozco',
    'antonio vega',
    'maldita vecindad',
    'bajofondo',
    'ana gabriel',
    'ana isabelle',
    'ana torroja',
    'mecano',
    'ely guerra',
    'aterciopelados',
    'attaque 77',
    'vicentico',
    'pastora soler',
    'omara portuondo',
    'armando manzanero',
    'noelia',
    'ismael miranda',
    'ismael rivera',
    'supersubmarina',
    'saantos inocentes',
    'soraya',
    'helado negro',
    'divididos',
    'aventura',
    'andy & lucas',
    'india',
    'presuntos implicados',
    'jovenes pordioseros',
    'joan manuel serrat',
    'mano negra',
    'manolo escobar',
    'los amigos invisibles',
    'los lobos',
    'los pericos',
    'los piojos',
    'los terricolas',
    'jaguares',
    'luis miguel',
    'soler, alvaro',
    'adrian celentano',
    'ana mena',
    'alexis y fido',
    'conjunto atardecer',
    'amistades peligrosas'
]


english_artist = [
    '3 doors down',
    'a day to remember',
    'ac dc',
    'aerosmith',
    'afi',
    'alice cooper'
    'alice in chains',
    'avenged sevenfold',
    'beastie boys'
    'black sabbath',
    'blink 182',
    'breaking benjamin',
    'bring me the horizon',
    'bullet for my valentine',
    'coldplay',
    'disturbed',
    'evanescence',
    'fall out boy',
    'flyleaf',
    'foo fighters',
    'freddie mercury',
    'george michael',
    'guns n roses',
    'hollywood undead',
    'jimi hendrix',
    'john lennon',
    'korn',
    'led zeppelin',
    'lenny kravitz',
    'limp bizkit',
    'linkin park',
    'marilyn manson',
    'metallica',
    'my chemical romance',
    'nickelback',
    'nirvana',
    'ozzy osbourne',
    'papa roach',
    'pink floyd',
    'queen',
    'rage against the machine',
    'red hot chili peppers',
    'the killers',
    'three days grace',
    'the white stripes',
    'black eyes peas',
    'chance the rapper',
    'cher lloyd',
    'fergie',
    'frank ocean',
    'g unit',
    'gucci mane',
    'iggy azalea',
    'jason derulo',
    'justin timberlake',
    'kevin gates',
    'kid cudi',
    'meek mill',
    'nate dogg',
    'nelly',
    'nelly furtado',
    'sean kingston',
    'sean paul',
    'snoop dog',
    'the game',
    'timbaland',
    'nsync',
    'abba',
    'adele',
    'backstreet boys',
    'benny benassi',
    'britney spears',
    'bruno mars',
    'calvin harris',
    'cascada',
    'celine dion',
    'cher',
    'christina aguilera',
    'ed sheeran',
    'ellie goulding',
    'gwen stefani',
    'michael buble',
    'rick astley',
    'robbie williams',
    'shawn mendes',
    'sia',
    'spice girls',
    'whitney houston',
    'ray charles',
    'five finger death punch',
    'vengaboys',
    'joyner lucas',
    'aqua',
    'architects',
    'seven nations',
    'judas priest',
    'earth, wind & fire',
    'as i lay dying',
    'salt-n-pepa',
    'gigi d\'agostino',
    'bone thugs-n-harmony',
    'ramones',
    'scatman john',
    'schoolboy q'
]

df_es = df_only_spanish.loc[df_only_spanish['Artist'] == 'alvaro soler']
for t in spanish_artist:
    df_tmp = df_only_spanish.loc[df_only_spanish['Artist'] == t]
    df_es = df_es.append(df_tmp)

df_en = df_only_english.loc[df_only_english['Artist'] == 'juicy j']
for t in english_artist:
    df_tmp = df_only_english.loc[df_only_english['Artist'] == t]
    df_en = df_en.append(df_tmp)

# merge spanish df end english sample
final_df = pd.concat([df_es, df_en])

split_final_df = np.array_split(final_df, 10)

# write xml rows
for i, d in enumerate(split_final_df):
    tmp = ('\n'.join(d.apply(convert_row_to_xml, axis=1)))
    # fix some janky symbols
    tmp = tmp.replace('\n', ' \n')
    tmp = tmp.replace('&', 'and')
    tmp = tmp.replace(' < ', ' ')
    tmp = tmp.replace('<br />', '&lt;br /&gt;')
    tmp = tmp.replace('\n', '&lt;br /&gt;')
    # write to file with <add> tag
    with open(OUTPUT_PATH+'_'+str(i), 'w') as f:
        f.write("<add>" + tmp + "</add>")

    print('Exported to ', OUTPUT_PATH+'_'+str(i))
