from unittest import TestCase

from film.models import Actor,Movie
from film.serializers import ActorSerializer,MovieSerializer

# class ActorTestSer(TestCase):
#     def setUp(self) -> None:
#         pass
#     def test_actor(self):
#         a=Actor.objects.all()
#         bb=ActorSerializer(a,many=True)
#         assert bb.data[0]["name"] == "Oyatillo"
#         assert bb.data[0]["birth_date"] == "2006-10-12"
#         assert bb.data[0]["gender"] == "erkak"

#
# class MovieTestSer(TestCase):
#     def test_movie(self):
#         a=Movie.objects.all()
#         bb=MovieSerializer(a,many=True)
#         assert bb.data[0]["title"] == "Tom Krus"
#         assert bb.data[0]["janr"] == "action"
#         assert bb.data[0]["date"] == "2007-10-12"
#         assert bb.data[0]["actor"] == [1]
class ActorModelsTest(TestCase):
    def setUp(self):
        pass
    def test_actor(self):
        b=Actor.objects.all()
        assert b is not None
        assert b[0].name=="Oyatillo"

        print(b[0])
        assert b[0].gender == "erkak"







