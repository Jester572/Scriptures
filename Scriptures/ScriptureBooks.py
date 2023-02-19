
import sqlite3
    
def create_table (table, columns):
    c.execute(f'CREATE TABLE IF NOT EXISTS {table}({table}_id INTEGER PRIMARY KEY,{columns})')
    conn.commit()
    
def add_data (table,values):
    c.execute(f"INSERT INTO {table} VALUES(null,{values})")
    conn.commit()
    
    
scriptures = [["Old Testament", "New Testament","Book of Mormon", "Doctrine & Covenants","Pearl of Great Price"]
,["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi"]
,["Mathew","Mark","Luke","John","Acts","Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians","1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon","Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"]
,["1 Nephi","2 Nephi","Jacob","Enos","Jarom","Omni","Words of Mormon","Mosiah","Alma","Helaman","3 Nephi","4 Nephi","Mormon","Ether","Moroni"]
,["Sections","Official Declarations"]
,["Moses","Abraham","Joseph Smith-Mathew","Joseph Smith-History","Articles of Faith"]]

sections = scriptures[0]
oldTestamentBooks = scriptures[1]
newTestamentBooks = scriptures[2]
bookOfMormonBooks = scriptures[3]
doctrineCovenantBooks = scriptures[4]
pearlOfGreatPriceBooks = scriptures[5]

oldTestamentChapters = [50,40,27,36,34,24,21,4,31,24,22,25,29,36,10,13,10,42,150,31,12,8,66,52,5,48,12,14,3,9,1,4,7,3,3,3,2,14,4]
newTestamentChapters = [28,16,24,21,28,16,16,13,6,6,4,4,5,3,6,4,3,1,13,5,5,3,5,1,1,1,22]
bookOfMormonChapters = [22,33,7,1,1,1,1,29,63,16,30,1,9,15,10]
doctrineCovenantChapters = [138,2]
pearlOfGreatPriceChapters = [8,5,1,1,1]


#Creates a database
conn = sqlite3.connect('scriptures.db')
#creates a cursor
c = conn.cursor()


#Creates sections table
create_table("sections","section_name TEXT, num_books INT")
#Populates sections table
i = 0
for name in sections:
    length = len(scriptures[i])
    text = '"{}", {}'.format(name, length)
    add_data("sections",text)
    i+= 1
    
#Creates oldTestament table
create_table("books","booksSections INT, book_name TEXT, num_chapters INT,FOREIGN KEY(booksSections) REFERENCES sections(sections_id)")
i = 0
for name in oldTestamentBooks:
    chapters = oldTestamentChapters[i]
    text = '1,"{}", {}'.format(name, chapters)
    add_data("books",text)
    i+= 1
    

i = 0
#Populates newTestament table
for name in newTestamentBooks:
    chapters = newTestamentChapters[i]
    text = '2,"{}", {}'.format(name, chapters)
    add_data("books",text)
    i+= 1
    

i = 0
#Populates bookofMormon table
for name in bookOfMormonBooks:
    chapters = bookOfMormonChapters[i]
    text = '3,"{}", {}'.format(name, chapters)
    add_data("books",text)
    i+= 1

i = 0
#Populates doctrineCovenant table
for name in doctrineCovenantBooks:
    chapters = doctrineCovenantChapters[i]
    text = '4,"{}", {}'.format(name, chapters)
    add_data("books",text)
    i+= 1
 
i = 0
#PopulpearlOfGreatPrice table
for name in pearlOfGreatPriceBooks:
    chapters = pearlOfGreatPriceChapters[i]
    text = '5,"{}", {}'.format(name, chapters)
    add_data("books",text)
    i+= 1    
    
conn.commit()
c.close()
conn.close()



# c.execute("SELECT * FROM sections WHERE section_id < 20")
# print(c.fetchall())
# print()
# c.execute("SELECT * FROM oldTestament")
# print(c.fetchall())
# print()
# c.execute("SELECT * FROM newTestament")
# print(c.fetchall())
# print()
# c.execute("SELECT * FROM bookOfMormon")
# print(c.fetchall())
# print()
# c.execute("SELECT * FROM doctrineCovenants")
# print(c.fetchall())
# print()
# c.execute("SELECT * FROM pearlOfGreatPrice")
# print(c.fetchall())