# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    auth.settings.remember_me_form = False
    user = auth.login_bare(request.post_vars.email,request.post_vars.password)
    if request.post_vars and not user:
        response.flash = "Login inválido"
    return dict(form=auth())

def signup():
    # def onvalidation():
        # print "entrou aqui"
    # auth.settings.register_onvalidation.append(onvalidation)
    db.auth_user.last_name.requires = None
    form = auth.register()
    if form.process().accepted:
        session.flash = 'cadastro realizado'
        redirect(URL('default', 'user'))
    elif form.errors:
        response.flash = 'erro ao cadastrar'
    else:
        response.flash = 'por favor, preencha o formulário'
    return locals()


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def conference_form():
    form = SQLFORM(db.conferencia, submit_button=T('Submeter'))
    if form.process().accepted:
        session.flash = 'enviado com sucesso'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'dados com erro'
    else:
        response.flash = 'por favor, preencha o formulário'

    return dict(form=form)

def article():
    form = SQLFORM(db.article, submit_button=T('Submeter'))
    if form.process().accepted:
        session.flash = 'enviado com sucesso'
        redirect(URL('index'))
    elif form.errors:
        response.flash = 'dados com erro'
    else:
        response.flash = 'por favor, preencha o formulário'

    return dict(form=form)
