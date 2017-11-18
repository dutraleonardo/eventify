from applications.eventify.modules.countries import *
import datetime

db.define_table(
    'conferencia',
    Field('nome','string',label=T('Nome da Conferência'), notnull=True),
    Field('sigla','string', label=T('Sigla da Conferência'),notnull=True),
    Field('pais', requires=IS_IN_SET(COUNTRIES)),
    Field('data_inicio', 'date',label=T('Data de Início'), requires=IS_DATE(format='%d-%m-%Y')),
    Field('data_fim', 'date',label=T('Data de Término'), requires=IS_DATE(format='%d-%m-%Y')))

db.define_table(
	'artigo',
	Field('titulo', 'string', label=T('Título do Artigo'), notnull=True),
	Field('autor', 'string', label=T('Autor'), notnull=True),
	Field('email', 'string', label=T('E-mail'), notnull=True),
	Field('keywords', 'string', label=T('Palavras-chave (separar por vírgula)')),
	Field('resumo', 'text', label=T('Resumo do Artigo')),
	Field('arquivo', 'upload', label=T('Upload'), notnull=True))