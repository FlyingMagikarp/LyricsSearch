import pandas as pd
import os


def convert_row_to_csv(row):
    if row.Language == 'en':
        return """
        <doc>
            <field name="artist">%s</field>
            <field name="song">%s</field>
            <field name="genre">%s</field>
            <field name="language">%s</field>
            <field name="lyrics_en">%s</field>
            <field name="lyrics_es">%s</field>
        </doc>
        """ % (row.Artist, row.Song, row.Genre, row.Language, row.Lyrics, '')

    return """
        <doc>
            <field name="artist">%s</field>
            <field name="song">%s</field>
            <field name="genre">%s</field>
            <field name="language">%s</field>
            <field name="lyrics_en">%s</field>
            <field name="lyrics_es">%s</field>
        </doc>
        """ % (row.Artist, row.Song, row.Genre, row.Language, '', row.Lyrics)



OUTPUT_PATH = '/data/out.xml'
if os.path.exists(OUTPUT_PATH):
    os.remove(OUTPUT_PATH)


df = pd.read_csv('data/archive/train.csv', sep=',')
# length
print("Row Count: "+str(len(df.index)))

# list of entries in col Language
language_list = df['Language'].unique()
print("LANGUAGE: ")
print(language_list)
print("LANGUAGE COUNT: "+str(language_list.size))

# list of entries in col genre
genre_list = df['Genre'].unique()
print("GENRE: "+genre_list)
print("GENRE COUNT: "+str(genre_list.size))

## clean dataset
# remove lyrics with guitar tabs
df_notabs = df.drop(df[df["Lyrics"].str.contains(r"\|-", na=False)].index)

# remove spanish translations
df_no_es_transl = df_notabs.drop(df[df["Song"].str.contains("raducc", na=False)].index)
df_no_es_transl = df_no_es_transl.drop(df[df["Song"].str.contains("español", na=False)].index)

# get only spanish entries
df_only_spanish = df_no_es_transl.loc[df_no_es_transl['Language'] == 'es']

# get only english entries
df_only_english = df_no_es_transl.loc[df_no_es_transl['Language'] == 'en']

# sample 2000 entries
df_en_sample = df_only_english.sample(n=1400)

# merge spanish df end english sample
final_df = pd.concat([df_only_spanish, df_en_sample])

# write csv rows
tmp = ('\n'.join(final_df.apply(convert_row_to_csv, axis=1)))

# write to file with <add> tag
with open('data/out.xml', 'w') as f:
    f.write("<add>"+tmp+"</add>")

print('Exported to data/out.xml')
