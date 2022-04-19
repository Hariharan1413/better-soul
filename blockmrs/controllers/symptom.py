"""Symptom controller module"""

from tg import expose, request, abort, redirect, predicates
from xml.etree import ElementTree as ET
import uuid

from bettersoul.lib.base import BaseController
from bettersoul.model import DBSession, User, PrivateKey
from bettersoul.lib.renderpr import match_field
from bettersoul.lib.records import retrieve_record, store_record


__all__ = ['SymptomController']


class SymptomController(BaseController):
    allow_only = predicates.not_anonymous()

    @expose('bettersoul.templates.symptoms')
    def index(self):
        return dict()

    @expose('bettersoul.templates.diagnosis')
    def diagnosis(self):
        print('ohea')
        return dict()
