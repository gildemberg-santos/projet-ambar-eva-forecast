# conectionSQLite.py
#
# Copyright 2020 Gildemberg Santos <gildemberg.santos@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later


import sqlite3


class ConectionSQLite(object):
    def __init__(self):
        self.connection = None
        self.c = None

    def createTable(self):
        try:
            sql = """
            CREATE TABLE IF NOT EXISTS tbCidade (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                idApi INTEGER NOT NULL,
                nome VARCHAR(255) NOT NULL,
                estado VARCHAR(255) NOT NULL,
                pais VARCHAR(255) NOT NULL,
                data DATETIME NOT NULL,
                probabilidade INTEGER NOT NULL,
                precipitacao INTEGER NOT NULL,
                temperatura_min INTEGER NOT NULL,
                temperatura_max INTEGER NOT NULL
            );
            """
            self.c.execute(sql)
        except Exception as e:
            print(e)

    def openConnection(self):
        try:
            database_sqlite_path = 'db_cidades.sqlite3'
            self.connection = sqlite3.connect(database_sqlite_path)
            self.c = self.connection.cursor()
        except Exception as e:
            print(e)

    def closeConnection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)

    def setInformation(self, sql=str(), val=()):
        try:
            self.c.execute(sql, val)
            self.connection.commit()
        except Exception as e:
            print(e)

    def getInformation(self, sql=str()):
        _list = []
        try:
            for row in self.c.execute(sql):
                _list.append(row)
        except Exception as e:
            print(e)
        return _list

