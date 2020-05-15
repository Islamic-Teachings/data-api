import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import (
    QuranModel,
    SurahModel,
    AyahModel,
    AyahRecitation,
    TafseerModel
)

class QuranNode(DjangoObjectType):
    class Meta:
        model = QuranModel
        interfaces = (relay.Node,)

class SurahNode(DjangoObjectType):
    class Meta:
        model = SurahModel
        filter_fields = {
            'juza': ['exact'],
            'arabic_name': ['exact'],
            'english_name': ['exact']
        }
        interfaces = (relay.Node,)

class AyahNode(DjangoObjectType):
    class Meta:
        model = AyahModel
        interfaces = (relay.Node,)

class Query(object):
    quran = relay.Node.Field(QuranNode)
    surah = relay.Node.Field(SurahNode)
    ayat = relay.Node.Field(AyahNode)
    allSurahs = DjangoFilterConnectionField(SurahNode)
