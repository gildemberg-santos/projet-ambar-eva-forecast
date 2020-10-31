# climatempo.py
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


from src.json.json import Json


class ClimaTempo:
    def __init__(self):
        self.token = "b22460a8b91ac5f1d48f5b7029891b53" # token da api
        self.urlbase = "http://apiadvisor.climatempo.com.br/api/v1/"

    def get_pais(self):
        json = Json()
        url="{0}locale/city?country=BR&token={1}".format(self.urlbase, self.token)
        dados = json.get_json(url=url)
        return str(dados)

    def get_cidade(self, id_cidade : int):
        json = Json()
        url="{0}forecast/locale/{1}/days/15?token={2}".format(self.urlbase, id_cidade, self.token)
        dados = json.get_json(url=url)
        return dados

