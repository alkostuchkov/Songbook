# -*- coding: utf-8 -*-
# ====== Songs for my own using ======
# = Example how my Songs looks like. =
# songs = {
#     "Song 1": {
#         genre: "genre 1",
#         categories: ["category 1", "category 2"],
#         song_image: "path to Song 1 image",
#         song_text: "path to Song 1 text",
#         last_performed: "01.01.2024",
#         is_recently: 0,
#         comment: "Comment for Song 1"
#     },
#     "Song 2": {
#         genre: "genre 2",
#         categories: ["category 1", "category 2"],
#         song_image: "path to Song 2 image",
#         song_text: "path to Song 2 text",
#         last_performed: "01.02.2024",
#         is_recently: 0,
#         comment: "Comment for Song 2"
#     },
# }

from pprint import pprint
import os
from sqlite3 import (
    DatabaseError,
    connect,
)


class Songs:
    """
    Class Songs.
    """

    def __init__(self):
        # TODO: delete after tests
        print("Songs' __init__")

        self.songs = {}
        # self.__path_to_db = os.path.abspath(".") + os.path.sep + "Database" + os.path.sep
        self.__path_to_db = f"{os.path.abspath(".")}{os.path.sep}database{os.path.sep}"
        print("__path_to_db", self.__path_to_db)

    # TODO: delete after ALL corrections.
    def __del__(self):
        print("Songs Class's destructor  called...")

    def open_db_and_get_dict(self):
        """
        Create database and tables if they not exist.
        Get data from sqlite3 db and transform it into dict self.songs.
        """
        # if dir 'database' not exists or not a dir, create this.
        if not os.path.exists(self.__path_to_db) or not os.path.isdir(self.__path_to_db):
            os.makedirs(self.__path_to_db)

        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        sql = """\
        CREATE TABLE IF NOT EXISTS genres(
           id INTEGER PRIMARY KEY NOT NULL,
           genre TEXT UNIQUE NOT NULL COLLATE NOCASE
        );
        CREATE TABLE IF NOT EXISTS categories(
           id INTEGER PRIMARY KEY NOT NULL,
           category TEXT UNIQUE NOT NULL COLLATE NOCASE
        );
        CREATE TABLE IF NOT EXISTS songs(
           id INTEGER PRIMARY KEY NOT NULL,
           title TEXT UNIQUE NOT NULL COLLATE NOCASE,
           id_category INTEGER NOT NULL,
           song_image TEXT DEFAULT "" COLLATE NOCASE,
           song_text TEXT DEFAULT "" COLLATE NOCASE,
           last_performed TEXT NOT NULL COLLATE NOCASE,
           is_recently INTEGER DEFAULT 0,
           comment TEXT DEFAULT "" COLLATE NOCASE,
           FOREIGN KEY(id_category) REFERENCES categories(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        CREATE TABLE IF NOT EXISTS songs_genres(
           id_song INTEGER NOT NULL,
           id_genre INTEGER NOT NULL,
           PRIMARY KEY (id_song, id_genre),
           FOREIGN KEY(id_song) REFERENCES songs(id) ON DELETE CASCADE ON UPDATE CASCADE,
           FOREIGN KEY(id_genre) REFERENCES genres(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """
        try:
            cur.executescript(sql)
        # except DatabaseError:
        #     raise DatabaseError  # ("Не удалось создать DB.")
        except DatabaseError as exc:
            raise exc  # ("Не удалось создать DB.")
        else:  # transform data to dict.
            sql = """\
            SELECT
              songs.title, genres.genre, categories.category, songs.song_image,
              songs.song_text, songs.last_performed, songs.is_recently, songs.comment
            FROM songs, genres, categories, songs_genres
            WHERE songs.id_category=categories.id 
              AND songs.id_category=categories.id
              AND songs_genres.id_song=songs.id
              AND songs_genres.id_genre=genres.id
            """
            try:
                cur.execute(sql)
            except DatabaseError as exc:
                raise exc  # ("Не удалось выполнить запрос.")
            for (
                title, genre, category, song_image, song_text,
                last_performed, is_recently, comment
            ) in cur:
                self.songs.setdefault(title, {"genres": []})

                self.songs[title]["genres"].append(genre)
                self.songs[title]["category"] = category
                self.songs[title]["song_image"] = song_image
                self.songs[title]["song_text"] = song_text
                self.songs[title]["last_performed"] = last_performed
                self.songs[title]["is_recently"] = is_recently
                self.songs[title]["comment"] = comment

            pprint(self.songs)
        finally:
            cur.close()
            conn.close()

#     def funInsertIntoDb(self, name, phonesList):
#         """ Insert data to the database. """
#         conn = sqlite3.connect(self.__path_to_db + "PhoneBook.sqlite3")
#         conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
#         cur = conn.cursor()
#         try:  # insert a new name into names.
#             cur.execute("INSERT INTO names(name) VALUES(:name)", {"name": name})
#         except sqlite3.DatabaseError as err:
#             raise sqlite3.DatabaseError("funInsertIntoDb: INSERT INTO names(name) VALUES(:name)", err)
#         else:
#             # don't do conn.commit() because
#             # if error will occur in the next inserting (for phoneNumbers)
#             # name will be without any phoneNumber!!!
#             try:  # get names_id by the name.
#                 cur.execute("SELECT id FROM names WHERE name=:name", {"name": name})
#             except sqlite3.DatabaseError as err:
#                 raise sqlite3.DatabaseError("funInsertIntoDb: SELECT id FROM names WHERE name=:name", err)
#             else:  # insert phoneNumbers into the PhoneBook's database.
#                 # get names_id from the list[0]
#                 names_id = cur.fetchone()[0]
#                 for phoneNumber in phonesList:
#                     try:
#                         cur.execute("INSERT INTO phoneNumbers(phoneNumber, names_id) VALUES(:phoneNumber, :names_id)",
#                                     {"phoneNumber": phoneNumber, "names_id": names_id})
#                     except sqlite3.DatabaseError as err:
#                         raise sqlite3.DatabaseError("funInsertIntoDb: INSERT INTO phoneNumbers(phoneNumber, names_id)", err)
#                     else:
#                         conn.commit()  # complete transactions for BOTH inserting: names and phoneNumbers.
#         finally:
#             cur.close()
#             conn.close()
#
#     def funMultiRecordDeleting(self, namesList):
#         """
#         Delete records with all phone numbers from the database.
#         :param namesList:
#         """
#         conn = sqlite3.connect(self.__path_to_db + "PhoneBook.sqlite3")
#         conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
#         cur = conn.cursor()
#         try:
#             for name in namesList:
#                 try:  # cascade deleting all records from names and phoneNumbers for THIS name.
#                     cur.execute("DELETE FROM names WHERE name=:name", {"name": name})
#                 except sqlite3.DatabaseError as err:
#                     raise sqlite3.DatabaseError("funDeleteOneRecord: DELETE FROM names WHERE name=:name", err)
#             conn.commit()  # commit transactions after completion all deleting.
#         finally:
#             cur.close()
#             conn.close()
#
#     def funDeleteOldThenInsertNewRecord(self, oldName, newName, phonesList):
#         """
#         Delete and then insert data.
#         Using ONE TRANSACTION for both: deleting and inserting.
#         :param oldName:
#         :param newName:
#         :param phonesList:
#         """
#         conn = sqlite3.connect(self.__path_to_db + "PhoneBook.sqlite3")
#         conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
#         cur = conn.cursor()
#         try:
#             # cascade deleting all records from names and phoneNumbers for the oldName
#             cur.execute("DELETE FROM names WHERE name=:oldName", {"oldName": oldName})
#             # inserting newName into the names
#             cur.execute("INSERT INTO names(name) VALUES(:newName)", {"newName": newName})
#             # get id by the newName.
#             cur.execute("SELECT id FROM names WHERE name=:newName", {"newName": newName})
#         except sqlite3.DatabaseError as err:
#             raise sqlite3.DatabaseError("funDeleteOldThenInsertNewRecord: DELETE FROM names WHERE name=:name", err)
#         else:
#             # get id from the list[0]
#             id = cur.fetchone()[0]
#             # and then cascade inserting new phones for the newName.
#             for phoneNumber in phonesList:
#                 try:
#                     cur.execute("INSERT INTO phoneNumbers(phoneNumber, names_id) VALUES(:phoneNumber, :names_id)",
#                                 {"phoneNumber": phoneNumber, "names_id": id})
#                 except sqlite3.DatabaseError as err:
#                     raise sqlite3.DatabaseError("funInsertIntoDb: INSERT INTO phoneNumbers(phoneNumber, names_id)", err)
#             # only if all inserting completed successfully, commit!!!
#             conn.commit()  # complete transactions for BOTH inserting: names and phoneNumbers.
#         finally:
#             cur.close()
#             conn.close()
#
#     def funClearDb(self):
#         """ Delete all data from the database. """
#         conn = sqlite3.connect(self.__path_to_db + "PhoneBook.sqlite3")
#         conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
#         cur = conn.cursor()
#         sql = """\
#         DELETE FROM names;
#         """
#         try:
#             cur.executescript(sql)
#         except sqlite3.DatabaseError:
#             raise sqlite3.DatabaseError  # ("Не удалось выполнить запрос.")
#         else:
#             conn.commit()  # complete transaction.
#         finally:
#             cur.close()
#             conn.close()
#
#     # def funDeleteSeveralPhonesFromRecord(self, name, phonesList):
#     #     """ Delete several phones from the record. """
#     #     conn = sqlite3.connect(self.__path_to_db + "PhoneBook.sqlite3")
#     #     conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
#     #     cur = conn.cursor()
#     #     try:  # get names_id by the name.
#     #         cur.execute("SELECT id FROM names WHERE name=:name", {"name": name})
#     #     except sqlite3.DatabaseError as err:
#     #         raise sqlite3.DatabaseError("funDeleteSeveralPhonesFromRecord: SELECT id FROM names...", err)
#     #     else:  # deleting phoneNumbers from the PhoneBook's database.
#     #         # get id from the list[0]
#     #         id = cur.fetchone()[0]
#     #         for phoneNumber in phonesList:
#     #             try:
#     #                 cur.execute("DELETE FROM phoneNumbers WHERE names_id=:id AND phoneNumber=:phoneNumber",
#     #                             {"id": id, "phoneNumber": phoneNumber})
#     #             except sqlite3.DatabaseError as err:
#     #                 raise sqlite3.DatabaseError("funDeleteSeveralPhonesFromRecord: DELETE FROM phoneNumbers...", err)
#     #             else:
#     #                 conn.commit()  # commit transactions.
#     #     finally:
#     #         cur.close()
#     #         conn.close()
