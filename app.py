#! /bin/python3.9
# app.py
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


from flask import Flask, request
from src.apiadvisor.climatempo import ClimaTempo


app = Flask(__name__)

@app.route('/')
def home():
    return "olá mundo!"

@app.route('/country/<country>', methods=['GET'])
def pais(country):
    api = ClimaTempo()
    try:
        dados = api.get_pais()
        if not dados:
            raise
        return dados
    except Exception:
        return "Por favor, tente mais tarde!"


@app.route('/cidade', methods=['GET'])
def cidade():
    api = ClimaTempo()
    try:
        post_id = int(request.args.get("id"))
        dados = api.get_cidade(id_cidade=post_id)
        if not dados:
            raise
        return dados
    except Exception:
        return "Por favor, informe um id valido!"
