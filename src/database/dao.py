# dao.py
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


from src.database.conectionSQLite import ConectionSQLite
from src.entidade.entidadeCidade import EntidadeCidade


class Dao(object):
    def __init__(self):
        try:
            conn = ConectionSQLite()
            conn.openConnection()
            conn.createTable()
            conn.closeConnection()
        except Exception as e:
            print(e)

    def getCidadeMediaPrec(self, data_inicial: str, data_final: str):
        try:
            conn = ConectionSQLite()
            conn.openConnection()
            sql = "SELECT AVG(precipitacao) FROM tbCidade WHERE data BETWEEN '{0}' and '{1}'".format(data_inicial, data_final)
            _listTemp = conn.getInformation(sql=sql)
            conn.closeConnection()
            if len(_listTemp) == 0:
                raise
            return float(_listTemp[0][0])
        except Exception as e:
            print(e)
            return None

    def getCidadeTempMax(self, data_inicial: str, data_final: str):
        try:
            conn = ConectionSQLite()
            conn.openConnection()
            sql = "SELECT MAX(temperatura_max) FROM tbCidade WHERE data BETWEEN '{0}' and '{1}'".format(data_inicial, data_final)
            _listTemp = conn.getInformation(sql=sql)
            conn.closeConnection()
            if len(_listTemp) == 0:
                raise
            return int(_listTemp[0][0])
        except Exception as e:
            print(e)
            return None

    def getCidadeIdApiDate(self, _id : int, data: str):
        try:
            _list = []
            conn = ConectionSQLite()
            conn.openConnection()
            sql = "SELECT * FROM tbCidade WHERE idApi=={0} AND data=='{1}'".format(_id, data)
            _listTemp = conn.getInformation(sql=sql)
            conn.closeConnection()
            cid = EntidadeCidade()
            for item in _listTemp:
                cid.id = item[0]
                cid.idApi = item[1]
                cid.nome = item[2]
                cid.estado = item[3]
                cid.pais = item[4]
                cid.data = item[5]
                cid.probabilidade = item[6]
                cid.precipitacao = item[7]
                cid.temperatura_min = item[8]
                cid.temperatura_max = item[9]
                _list.append(cid)
            return _list
        except Exception as e:
            print(e)
            return None

    def addCidade(self, values: EntidadeCidade):
        try:
            conn = ConectionSQLite()
            conn.openConnection()
            sql = "INSERT INTO tbCidade (idApi, nome, estado, pais, data, probabilidade, precipitacao, temperatura_min, temperatura_max) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (values.idApi, values.nome, values.estado, values.pais, values.data, values.probabilidade, values.precipitacao, values.temperatura_min, values.temperatura_max)
            conn.setInformation(sql=sql, val=val)
            conn.closeConnection()
        except Exception as e:
            print(e)

    def toEditCidade(self, values: EntidadeCidade):
        try:
            conn = ConectionSQLite()
            conn.openConnection()
            sql = "UPDATE tbCidade SET probabilidade=?, precipitacao=?, temperatura_min=?, temperatura_max=? WHERE idApi=={0} AND data=='{1}'".format(values.idApi, values.data)
            val = (values.probabilidade, values.precipitacao, values.temperatura_min, values.temperatura_max)
            conn.setInformation(sql=sql, val=val)
            conn.closeConnection()
        except Exception as e:
            print(e) 
