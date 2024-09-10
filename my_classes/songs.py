# -*- coding: utf-8 -*-
""" Module contains class Songs. """
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
        self.songs: dict = {}
        self.__path_to_db: str = f"{os.path.abspath(".")}{os.path.sep}database{os.path.sep}"

        # TODO: delete after ALL tests.
        print("Constructor called...")
        print("__path_to_db", self.__path_to_db)

    # TODO: delete after ALL corrections.
    def __del__(self):
        print("Destructor called...")

    def open_db_and_get_dict(self) -> None:
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
        finally:
            cur.close()
            conn.close()

    def get_categories_from_db(self) -> list:
        """ Get categories from DB. """

        categories: list = []
        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("SELECT category FROM categories")
        except DatabaseError as err:
            raise DatabaseError("get_categories_from_db", err)
        else:
            for category in cur:
                categories.append(category)
        finally:
            cur.close()
            conn.close()

        return categories

    def get_genres_from_db(self) -> list:
        """ Get genres from DB. """

        genres: list = []
        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("SELECT genre FROM genres")
        except DatabaseError as err:
            raise DatabaseError("get_genres_from_db", err)
        else:
            for genre in cur:
                genres.append(genre)
        finally:
            cur.close()
            conn.close()

        return genres

    def insert_genre_into_db(self, genre: str) -> None:
        """ Insert a genre into the table genres of DB. """

        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO genres(genre) VALUES(:genre)",
                        {"genre": genre})
        except DatabaseError as err:
            raise DatabaseError("insert_genre_into_db", err)
        else:
            conn.commit()  # complete transaction
        finally:
            cur.close()
            conn.close()

    def insert_category_into_db(self, category: str) -> None:
        """ Insert a category into the table categories of DB. """

        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO categories(category) VALUES(:category)",
                        {"category": category})
        except DatabaseError as err:
            raise DatabaseError("insert_category_into_db", err)
        else:
            conn.commit()  # complete transaction
        finally:
            cur.close()
            conn.close()

    # TODO: change args for this method to dict!
    def insert_song_into_db(
        self, title: str, genres: list, category: str, song_image: str,
        song_text: str, last_performed: str, is_recently: int, comment: str
    ) -> None:
        """ Insert a song into the songs table of DB. """

        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()

        id_category: int = self._get_id_category(category)
        try:
            cur.execute(
                "INSERT INTO songs(title, id_category, song_image, song_text, "
                                   "last_performed, is_recently, comment) "
                "VALUES(:title, :id_category, :song_image, :song_text, "
                       ":last_performed, :is_recently, :comment) ",
                {
                    "title": title,
                    "id_category": id_category,
                    "song_image": song_image,
                    "song_text": song_text,
                    "last_performed": last_performed,
                    "is_recently": is_recently,
                    "comment": comment,
                }
            )
            # I need the NEW song_id for the just inserted song (and genres_ids)!
            cur.execute("SELECT id FROM songs WHERE title=:title", {"title": title})
            id_song: int = cur.fetchone()[0]
            # id_song: int = self._get_id_song(title)  # Doesn't work in this
            # case because the conn.commit() will be executed after ALL
            # transactions and a NEW CURSOR in a NEW CONNECT in the _get_id_song
            # doesn't see id and title of the new inserting song because of
            # incompletted transaction above.
            # I need ALL inserts to be completted for ALL tables!!!
            # And then I do conn.commit().
            ids_genres: list = self._get_ids_genres(genres)

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
#
    # TODO: change args for this method to dict!
    # def update_record(self, old_song: dict, new_song: dict) -> None:
    def update_record(
        self, old_title: str, new_title: str, old_genres: list, new_genres: list,
        old_category: str, new_category: str, song_image: str, song_text: str,
        last_performed: str, is_recently: int, comment: str
    ) -> None:
        """ Update record in DB. """

        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            # Update songs
            cur.execute(
                "UPDATE songs "
                "SET "
                  "title=:title, "
                  "song_image=:song_image, "
                  "song_text=:song_text, "
                  "last_performed=:last_performed, "
                  "is_recently=:is_recently, "
                  "comment=:comment "
                "WHERE title=:old_title",
                {
                    "title": new_title,
                    "old_title": old_title,
                    "song_image": song_image,
                    "song_text": song_text,
                    "last_performed": last_performed,
                    "is_recently": is_recently,
                    "comment": comment,
                }
            )
            # Update genres
            for old_genre, new_genre in zip(old_genres, new_genres):
                cur.execute(
                    "UPDATE genres "
                    "SET genre=:genre "
                    "WHERE genre=:old_genre",
                    {
                        "genre": new_genre,
                        "old_genre": old_genre,
                    }
                )
            # Update categories
            cur.execute(
                "UPDATE categories "
                "SET category=:category "
                "WHERE category=:old_category",
                {
                    "category": new_category,
                    "old_category": old_category,
                }
            )
        except DatabaseError as err:
            raise DatabaseError("update_record:", err)
        else:
            conn.commit()  # complete ALL transactions!
        finally:
            cur.close()
            conn.close()

    def delete_multi_records(self, titles_list: list) -> None:
        """
        Delete songs with all dependences in songs_genres from the database.
        """

        # Get ids all deleting songs by their titles.
        ids_songs: list = self._get_ids_songs(titles_list)
        conn = connect(self.__path_to_db + "songs.db")
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
        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        sql = """\
        DELETE FROM categories;
        DELETE FROM genres;
        """
        try:
            cur.executescript(sql)
        except DatabaseError as exc:
            raise exc  # ("Не удалось выполнить запрос.")
        else:
            conn.commit()  # complete transaction.
        finally:
            cur.close()
            conn.close()

    def _get_id_category(self, category: str) -> int:
        """ Get id_category by its UNIQUE category. """

        conn = connect(self.__path_to_db + "songs.db")
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

    def _get_ids_genres(self, genres: list) -> list:
        """ Get genres ids by their UNIQUE genre. """

        ids_genres: list = []
        conn = connect(self.__path_to_db + "songs.db")
        conn.execute("PRAGMA foreign_keys=1")  # enable cascade deleting and updating.
        cur = conn.cursor()
        try:
            for genre in genres:
                cur.execute("SELECT id FROM genres WHERE genre=:genre", {"genre": genre})
                ids_genres.append(cur.fetchone()[0])
        except DatabaseError as err:
            raise DatabaseError("_get_genres_ids:", err)
        finally:
            cur.close()
            conn.close()
        return ids_genres

    def _get_id_song(self, title: str) -> int:
        """ Get id_song by its UNIQUE title. """

        conn = connect(self.__path_to_db + "songs.db")
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

    def _get_ids_songs(self, titles_list: list) -> list:
        """ Get ids_songs by its UNIQUE title. """

        ids_songs: list = []
        for title in titles_list:
            ids_songs.append(self._get_id_song(title))

        return ids_songs
