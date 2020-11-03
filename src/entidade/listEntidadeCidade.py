# listCidade.py
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


from src.entidade.entidadeCidade import EntidadeCidade


class ListEntidadeCidade:
    def __init__(self, _json):
        self._list = []
        if not _json:
            return None
        elif not _json['data']:
            return None
        for item in _json['data']:
            cid = EntidadeCidade()
            cid.idApi = _json['id']
            cid.pais = _json['country']
            cid.estado = _json['state']
            cid.nome = _json['name']
            cid.data = item['date']
            cid.probabilidade = item['rain']['probability']
            cid.precipitacao = item['rain']['precipitation']
            cid.temperatura_max = item['temperature']['max']
            cid.temperatura_min = item['temperature']['min']
            self._list.append(cid)
