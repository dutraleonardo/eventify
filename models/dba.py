from applications.eventify.modules.countries import *
import datetime

db.define_table(
    'conferencia',
    Field('nome','string',label=T('Nome da Conferência'), notnull=True),
    Field('sigla','string', label=T('Sigla da Conferência'),notnull=True),
    Field('pais', 'string', label=T('País'), requires=IS_IN_SET(COUNTRIES)),
    Field('data_inicio', 'date',label=T('Data de Início'), requires=IS_DATE(format='%d-%m-%Y')),
    Field('data_fim', 'date',label=T('Data de Término'), requires=IS_DATE(format='%d-%m-%Y')))

db.define_table(
	'article',
	Field('titulo', 'string', label=T('Título do Artigo'), notnull=True),
	Field('autor', 'string', label=T('Autor'), notnull=True),
	Field('email', 'string', label=T('E-mail'), notnull=True),
	Field('autor2', 'string', label=T('Autor')),
	Field('email2', 'string', label=T('E-mail')),
	Field('autor3', 'string', label=T('Autor')),
	Field('email3', 'string', label=T('E-mail')),
	Field('keywords', 'string', label=T('Palavras-chave (separar por vírgula)')),
	Field('status_id', requires=IS_IN_DB(db,'status.status'), default='aguardando revisão'),
	Field('resumo', 'text', label=T('Resumo do Artigo')),
	Field('arquivo', 'upload', label=T('Upload')))

db.define_table(
	'status',
	Field('status', 'string', label=T('Status do Artigo'), requires=IS_IN_SET(('aguardando revisão', 'em revisão', 'aprovado', 'rejeitado')))
	)

db.define_table(
	'revisor',
	Field('nome_revisor', label=T('Nome do Revisor'), requires=IS_IN_DB(db, 'auth_user.tipo')),
	Field('artigo_revisao', label=T('Artigo'), requires=IS_IN_DB(db, 'article.titulo')),
	)
