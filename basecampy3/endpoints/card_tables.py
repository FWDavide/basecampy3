"""
Card tables
A card table is made of multiple columns which contain cards.

https://github.com/basecamp/bc3-api/blob/master/sections/card_tables.md

You cannot create a card table directly. Instead, you create a project and then add a card table to it. Using the web interface.

"""

from . import _base, projects, util
from .. import constants

class CardTable(_base.BasecampObject):

    def list(self):
        """
        :return: a list of the CardTable objects in this Project
        :rtype: collections.Iterable[basecampy3.endpoints.card_tables.CardTable]
        """
        return self._endpoint._api.card_tables.list(cardtable=self)
    

class CardTables(_base.BasecampEndpoint):
    OBJECT_CLASS = CardTable
    
    GET_URL = "{base_url}/buckets/{project_id}/card_tables/{cardtable_id}.json"

    def get(self, project, cardtable):
        """
        Get a CardTable object either from a project ID and a cardtable ID or just a Project object.

        :param project: a Project object or ID
        :type project: projects.Project|int
        :param cardtable: a CardTable object or ID
        :type cardtable: CardTable|int
        :return: a CardTable object
        :rtype: CardTable
        """
        project_id, cardtable_id = project, cardtable
        url = self.GET_URL.format(base_url=self.url, project_id=project_id, cardtable_id=cardtable_id)
        return self._get(url)