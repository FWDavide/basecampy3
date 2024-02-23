"""
Card table columns

https://github.com/basecamp/bc3-api/blob/master/sections/card_table_columns.md

Project -> CardTable -> CardTableColumns -> Cards
                                ^
                        You are here.
"""

from . import _base, projects, util
from .. import constants

class CardTableColumn(_base.BasecampObject):
    def list(self):
        """
        :return: a list of the CardTableColumn objects in this CardTable
        :rtype: collections.Iterable[basecampy3.endpoints.card_table_columns.CardTableColumn]
        """
        return self._endpoint._api.card_table_columns.list(cardtablecolumn=self)
    
class CardTableColumns(_base.BasecampEndpoint):
    OBJECT_CLASS = CardTableColumn
    
    GET_URL = "{base_url}/buckets/{project_id}/card_tables/columns/{cardtablecolumn_id}.json"

    def get(self, project, cardtablecolumn):
        """
        Get a CardTableColumn object from a project ID, and a cardtablecolumn ID.
        :param project: a Project object or ID
        :type project: projects.Project|int
        :param cardtablecolumn: a CardTableColumn object or ID
        :type cardtablecolumn: CardTableColumn|int
        :return: a CardTableColumn object
        :rtype: CardTableColumn
        """
        project_id, cardtablecolumn_id = project, cardtablecolumn
        url = self.GET_URL.format(base_url=self.url, project_id=project_id, cardtablecolumn_id=cardtablecolumn_id)
        return self._get(url)