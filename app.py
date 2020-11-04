#! /bin/python3.9
# -*- coding: utf-8 -*-
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


from flask import Flask, request, make_response, render_template
from src.negocio.negocioCidade import NegocioCidade


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', title="Ambar EVA", titleapp="Avaliação técnica Backend Python")

@app.route('/cidade', methods=['GET'])
def cidade():
    try:
        negCid = NegocioCidade()
        post_id = int(request.args.get("id"))
        negCid.addCidade(_id=post_id)
        return ("Cadastrado com sucesso!", 200)
    except Exception as e:
        print(e)
        return ("Por favor, informe um id valido!", 404)

@app.route('/analise', methods=['GET'])
def analise():
    try:
        negCid = NegocioCidade()
        data_inicial = str(request.args.get("data_inicial"))
        data_final = str(request.args.get("data_final"))
        _json = negCid.getAnalise(data_inicial=data_inicial, data_final=data_final)
        if not _json:
            raise
        response = make_response(_json)
        response.content_type = "application/json"
        return (response, 200)

    except Exception as e:
        print(e)
        return ("Por favor, informe um periodo valido!", 404)
        
