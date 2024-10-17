# -*- coding: utf-8 -*-
""" Module contains class Songbook. """
# ====== Songbook for my own using ======
# = Example how my Songbook looks like. =
# songbook = {
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

import os
from sqlite3 import (
    connect,
    DatabaseError,
)


class Songbook:
    """ Class Songbook to manipulate DB data. """
    def __init__(self):
        self._songbook: dict = {}
        self._path_to_db: str = f"{os.path.abspath(".")}{os.path.sep}database{os.path.sep}"
        self._create_db()

    # def __del__(self):

    def _create_db(self) -> None:
        """
        Create database and tables if they not exist.
        """
        # if dir 'database' not exists or not a dir, create this.
        if not os.path.exists(self._path_to_db) or not os.path.isdir(self._path_to_db):
            os.makedirs(self._path_to_db)

        conn = connect(self._path_to_db + "songbook.db")
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
        except DatabaseError as err:
            raise DatabaseError("_create_db", err)
        finally:
            cur.close()
            conn.close()

    def get_data_as_dict(self) -> dict:
        """
        Get data from sqlite3 db and transform them into dict self.songbook.
        """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        sql = """\
        SELECT
          songs.title, genres.genre, categories.category, songs.song_image,
          songs.song_text, songs.last_performed, songs.is_recently, songs.comment
        FROM songs, genres, categories, songs_genres
        WHERE songs.id_category=categories.id 
          AND songs_genres.id_song=songs.id
          AND songs_genres.id_genre=genres.id
        """
        try:
            cur.execute(sql)
        except DatabaseError as err:
            raise DatabaseError("get_data_as_dict", err)
        else:
            self._songbook.clear()
            for (
                title, genre, category, song_image, song_text,
                last_performed, is_recently, comment
            ) in cur:
                self._songbook.setdefault(title, {"genres": []})

                self._songbook[title]["genres"].append(genre)
                self._songbook[title]["category"] = category
                self._songbook[title]["song_image"] = song_image
                self._songbook[title]["song_text"] = song_text
                self._songbook[title]["last_performed"] = last_performed
                self._songbook[title]["is_recently"] = is_recently
                self._songbook[title]["comment"] = comment
        finally:
            cur.close()
            conn.close()
        return self._songbook

    def get_the_song_as_dict(self, the_title: str) -> dict:
        """
        Get the song from DB and transform it into dict.
        """
        the_song: dict = {}
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        sql = """\
        SELECT
          songs.title, genres.genre, categories.category, songs.song_image,
          songs.song_text, songs.last_performed, songs.is_recently, songs.comment
        FROM songs, genres, categories, songs_genres
        WHERE songs.id_category=categories.id 
          AND songs_genres.id_song=songs.id
          AND songs_genres.id_genre=genres.id
          AND songs.title=:title
        """
        try:
            cur.execute(sql, {"title": the_title})
        except DatabaseError as err:
            raise DatabaseError("get_the_song_as_dict", err)
        else:
            for (
                title, genre, category, song_image, song_text,
                last_performed, is_recently, comment
            ) in cur:
                the_song.setdefault(title, {"genres": []})

                the_song[title]["genres"].append(genre)
                the_song[title]["category"] = category
                the_song[title]["song_image"] = song_image
                the_song[title]["song_text"] = song_text
                the_song[title]["last_performed"] = last_performed
                the_song[title]["is_recently"] = is_recently
                the_song[title]["comment"] = comment
        finally:
            cur.close()
            conn.close()
        return the_song

    def get_titles_from_db(self) -> list[str]:
        """ Get songs titles from DB. """
        titles: list = []
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("SELECT title FROM songs")
        except DatabaseError as err:
            raise DatabaseError("get_titles_from_db", err)
        else:
            for title in cur:
                titles.append(title[0])
        finally:
            cur.close()
            conn.close()

        return titles

    def get_categories_from_db(self) -> list[str]:
        """ Get categories from DB. """
        categories: list = []
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("SELECT category FROM categories")
        except DatabaseError as err:
            raise DatabaseError("get_categories_from_db", err)
        else:
            for category in cur:
                categories.append(category[0])
        finally:
            cur.close()
            conn.close()

        return categories

    def get_genres_from_db(self) -> list[str]:
        """ Get genres from DB. """
        genres: list = []
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("SELECT genre FROM genres")
        except DatabaseError as err:
            raise DatabaseError("get_genres_from_db", err)
        else:
            for genre in cur:
                genres.append(genre[0])
        finally:
            cur.close()
            conn.close()

        return genres

    def insert_genres_into_db(self, genres: list[str]) -> None:
        """ Insert genres into the table genres of DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for genre in genres:
                cur.execute("INSERT INTO genres(genre) VALUES(:genre)",
                        {"genre": genre})
        except DatabaseError as err:
            raise DatabaseError("insert_genres_into_db", err)
        else:
            conn.commit()  # complete transaction
        finally:
            cur.close()
            conn.close()

    def insert_categories_into_db(self, categories: list[str]) -> None:
        """ Insert categories into the table categories of DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for category in categories:
                cur.execute("INSERT INTO categories(category) VALUES(:category)",
                        {"category": category})
        except DatabaseError as err:
            raise DatabaseError("insert_categories_into_db", err)
        else:
            conn.commit()  # complete transaction
        finally:
            cur.close()
            conn.close()

    def insert_song_into_db(self, song: dict) -> None:
        """ Insert a song into the songs table of DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()

        id_category: int = self._get_id_category(song["category"])
        try:
            cur.execute(
                "INSERT INTO songs(title, id_category, song_image, song_text, "
                                   "last_performed, is_recently, comment) "
                "VALUES(:title, :id_category, :song_image, :song_text, "
                       ":last_performed, :is_recently, :comment) ",
                {
                    "title": song["title"],
                    "id_category": id_category,
                    "song_image": song["song_image"],
                    "song_text": song["song_text"],
                    "last_performed": song["last_performed"],
                    "is_recently": song["is_recently"],
                    "comment": song["comment"],
                }
            )
            # I need the NEW song_id for the just inserted song (and genres_ids)!
            cur.execute(
                "SELECT id FROM songs WHERE title=:title",
                {"title": song["title"]}
            )
            id_song: int = cur.fetchone()[0]
            # id_song: int = self._get_id_song(title)  # Doesn't work in this
            # case because the conn.commit() will be executed after ALL
            # transactions and a NEW CURSOR in a NEW CONNECT in the _get_id_song
            # doesn't see id and title of the new inserting song because of
            # incompletted transaction above.
            # I need ALL inserts to be completted for ALL tables!!!
            # And then I do conn.commit().
            ids_genres: list = self._get_ids_genres(song["genres"])

            for id_genre in ids_genres:
                cur.execute(
                    "INSERT INTO songs_genres(id_song, id_genre) "
                    "VALUES(:id_song, :id_genre)",
                    {"id_song": id_song, "id_genre": id_genre}
                )
        except DatabaseError as err:
            raise DatabaseError("insert_song_into_db", err)
        else:
            conn.commit()  # complete ALL transactions!
        finally:
            cur.close()
            conn.close()

    def delete_categories_from_db(self, categories: list[str]) -> None:
        """ Delete categories from the DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for category in categories:
                cur.execute("DELETE FROM categories WHERE category=:category",
                            {"category": category})
        except DatabaseError as err:
            raise DatabaseError("delete_categories_from_db", err)
        else:
            conn.commit()  # complete transaction.
        finally:
            cur.close()
            conn.close()

    def delete_genres_from_db(self, genres: list[str]) -> None:
        """ Delete genres from the DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for genre in genres:
                cur.execute("DELETE FROM genres WHERE genre=:genre",
                            {"genre": genre})
        except DatabaseError as err:
            raise DatabaseError("delete_genres_from_db", err)
        else:
            conn.commit()  # complete transaction.
        finally:
            cur.close()
            conn.close()

    def delete_songs_from_db(self, titles: list[str]) -> None:
        """ Delete songs from the DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for title in titles:
                cur.execute("DELETE FROM songs WHERE title=:title",
                            {"title": title})
        except DatabaseError as err:
            raise DatabaseError("delete_songs_from_db", err)
        else:
            conn.commit()  # complete transaction.
        finally:
            cur.close()
            conn.close()

    def update_genres(self, current_genre: str, new_genre: str) -> None:
        """ Update genres in DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute(
                "UPDATE genres "
                "SET genre=:new_genre "
                "WHERE genre=:current_genre",
                {
                    "new_genre": new_genre,
                    "current_genre": current_genre,
                }
            )
        except DatabaseError as err:
            raise DatabaseError("update_genres", err)
        else:
            conn.commit()  # complete transaction
        finally:
            cur.close()
            conn.close()

    def update_categories(self, current_category: str, new_category: str) -> None:
        """ Update categories in DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute(
                "UPDATE categories "
                "SET category=:new_category "
                "WHERE category=:current_category",
                {
                    "new_category": new_category,
                    "current_category": current_category,
                }
            )
        except DatabaseError as err:
            raise DatabaseError("update_categories", err)
        else:
            conn.commit()  # complete transaction
        finally:
            cur.close()
            conn.close()

    def update_song(self, current_title: str, new_song: dict) -> None:
        """ Update song in DB. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()

        id_category: int = self._get_id_category(new_song["category"])
        id_song: int = self._get_id_song(current_title)
        try:
            # Update songs
            cur.execute(
                "UPDATE songs "
                "SET "
                  "title=:new_title, "
                  "id_category=:id_category, "
                  "song_image=:song_image, "
                  "song_text=:song_text, "
                  "last_performed=:last_performed, "
                  "is_recently=:is_recently, "
                  "comment=:comment "
                "WHERE title=:current_title",
                {
                    "new_title": new_song["title"],
                    "current_title": current_title,
                    "id_category": id_category,
                    "song_image": new_song["song_image"],
                    "song_text": new_song["song_text"],
                    "last_performed": new_song["last_performed"],
                    "is_recently": new_song["is_recently"],
                    "comment": new_song["comment"],
                }
            )
            # Delete from songs_genres the current song with old genres.
            cur.execute("DELETE FROM songs_genres WHERE id_song=:id_song",
                        {"id_song": id_song})

            # Update songs_genres
            ids_genres: list = self._get_ids_genres(new_song["genres"])
            # insert the current song with updated genres. 
            for id_genre in ids_genres:
                cur.execute(
                    "INSERT INTO songs_genres(id_song, id_genre) "
                    "VALUES(:id_song, :id_genre)",
                    {"id_song": id_song, "id_genre": id_genre}
                )
        except DatabaseError as err:
            raise DatabaseError("update_song", err)
        else:
            conn.commit()  # complete ALL transactions!
        finally:
            cur.close()
            conn.close()

    def delete_multi_records(self, titles_list: list[str]) -> None:
        """
        Delete songs with all dependences in songs_genres from the database.
        """
        # Get ids all deleting songs by their titles.
        ids_songs: list = self._get_ids_songs(titles_list)
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for id_song in ids_songs:  # Deleting from songs_genres table.
                cur.execute("DELETE FROM songs_genres WHERE id_song=:id_song",
                            {"id_song": id_song})
            for id in ids_songs:  # Deleting from songs table.
                cur.execute("DELETE FROM songs WHERE id=:id", {"id": id})
        except DatabaseError as err:
            raise DatabaseError("delete_multi_records:", err)
        else:
            conn.commit()  # commit transactions after completion all deletings.
        finally:
            cur.close()
            conn.close()

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

    def clear_db(self):
        """ Delete all data from the database. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        sql = """\
        DELETE FROM categories;
        DELETE FROM genres;
        """
        try:
            cur.executescript(sql)
        except DatabaseError as err:
            raise DatabaseError("clear_db", err)
        else:
            conn.commit()  # complete transaction.
        finally:
            cur.close()
            conn.close()

    def _get_id_category(self, category: str) -> int:
        """ Get id_category by its UNIQUE category. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("SELECT id FROM categories WHERE category=:category",
                        {"category": category})
        except DatabaseError as err:
            raise DatabaseError("_get_id_category:", err)
        else:
            # get id_category from the list[0]
            id_category: int = cur.fetchone()[0]
        finally:
            cur.close()
            conn.close()

        return id_category

    def _get_ids_genres(self, genres: list[str]) -> list[int]:
        """ Get genres ids by their UNIQUE genre. """
        ids_genres: list = []
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for genre in genres:
                cur.execute("SELECT id FROM genres WHERE genre=:genre", {"genre": genre})
                ids_genres.append(cur.fetchone()[0])
        except DatabaseError as err:
            raise DatabaseError("_get_ids_genres", err)
        finally:
            cur.close()
            conn.close()

        return ids_genres

    def _get_id_song(self, title: str) -> int:
        """ Get id_song by its UNIQUE title. """
        conn = connect(self._path_to_db + "songbook.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("SELECT id FROM songs WHERE title=:title", {"title": title})
        except DatabaseError as err:
            raise DatabaseError("_get_id_song:", err)
        else:
            # get id_song from the list[0]
            id_song: int = cur.fetchone()[0]
        finally:
            cur.close()
            conn.close()

        return id_song

    def _get_ids_songs(self, titles_list: list[str]) -> list[int]:
        """ Get ids_songs by its UNIQUE title. """
        ids_songs: list = []
        for title in titles_list:
            ids_songs.append(self._get_id_song(title))

        return ids_songs
