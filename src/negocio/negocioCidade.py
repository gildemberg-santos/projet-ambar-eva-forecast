# cidade.py
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


from src.apiadvisor.climatempo import ClimaTempo
from src.database.dao import Dao
from src.entidade.listEntidadeCidade import ListEntidadeCidade


class NegocioCidade:
    def __init__(self):
        pass

    def getCidadeData(self, data_inicial: str, data_final: str):
        pass

    def addCidade(self, _id : int):
        try:
            api = ClimaTempo()
            dao = Dao()
            dados = api.get_cidade(id_cidade=_id)
            if not dados:
                raise
            lentcid = ListEntidadeCidade(_json=dados)
            for item in lentcid._list:
                entdao = dao.getCidadeIdApiDate(_id=item.idApi, data=item.data)
                if len(entdao) == 0:
                    dao.addCidade(values=item)
                else:
                    if ((item.probabilidade != entdao[0].probabilidade) or \
                        (item.precipitacao != entdao[0].precipitacao) or \
                        (item.temperatura_max != entdao[0].temperatura_max) or \
                        (item.temperatura_min != entdao[0].temperatura_min)):
                        print("DAO, Atualizar")
                        # implementar
        except Exception as e:
            print(e)
