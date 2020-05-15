import graphene
from graphene import Schema, relay, resolve_only_args
from graphene_django import DjangoConnectionField, DjangoObjectType

from .models import (
    QuranModel
)

class Quran(DjangoObjectType):
    class Meta:
        model = QuranModel
        interfaces = (relay.Node,)

    @classmethod
    def get_node(cls, info):
        node = QuranModel.objects.all()[0]
        return node

class Query(graphene.ObjectType):
    quran = graphene.List(Quran)

schema = graphene.Schema(query=Query)
