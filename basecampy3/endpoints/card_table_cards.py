"""
Card table cards

https://github.com/basecamp/bc3-api/blob/master/sections/card_table_cards.md

Project -> CardTable -> CardTableColumns -> Cards
                                              ^
                                            You are here.

"""

from . import _base, projects, util
from .. import constants

class CardTableCard(_base.BasecampObject):
    def list(self):
        """
        :return: a list of the CardTableCard objects in this CardTableColumn
        :rtype: collections.Iterable[basecampy3.endpoints.card_table_cards.CardTableCard]
        """
        return self._endpoint._api.card_table_cards.list(cardtablecard=self)
    
class CardTableCards(_base.BasecampEndpoint):
    OBJECT_CLASS = CardTableCard

    GET_URL = "{base_url}/buckets/{project_id}/card_tables/cards/{cardtablecard_id}.json"
    LIST_URL = "{base_url}/buckets/{project_id}/card_tables/lists/{cardtablecolumn_id}/cards.json"
    UPDATE_URL = "{base_url}/buckets/{project_id}/card_tables/cards/{cardtablecard_id}.json"
    MOVES_URL = "{base_url}/buckets/{project_id}/card_tables/cards/{cardtablecard_id}/moves.json"


    def get(self, project, cardtablecard):
        """
        Get a CardTableCard object from a project ID, and a cardtablecard ID.
        :param project: a Project object or ID
        :type project: projects.Project|int
        :param cardtablecard: a CardTableCard object or ID
        :type cardtablecard: CardTableCard|int
        :return: a CardTableCard object
        :rtype: CardTableCard
        """
        project_id, cardtablecard_id = project, cardtablecard
        url = self.GET_URL.format(base_url=self.url, project_id=project_id, cardtablecard_id=cardtablecard_id)
        return self._get(url)

    def list(self, project, cardtablecolumn):
        """
        Get a list of CardTableCard objects from a project ID and a cardtablecolumn ID.

        :param project: a Project object or ID
        :type project: projects.Project|int
        :param cardtablecolumn: a CardTableColumn object or ID
        :type cardtablecolumn: CardTableColumn|int
        :return: a list of CardTableCard objects
        :rtype: collections.Iterable[CardTableCard]
        """
        project_id, cardtablecolumn_id = project, cardtablecolumn
        url = self.LIST_URL.format(base_url=self.url, project_id=project_id, cardtablecolumn_id=cardtablecolumn_id)
        return self._get_list(url)
    
    def create(self, project, card_list_id, title, content="", due_date=None):
        """
        Create a new CardTableCard in a CardTableColumn.

        :param project: a Project object or ID
        :type project: projects.Project|int
        :param card_list_id: a CardTableColumn object or ID
        :type card_list_id: CardTableColumn|int
        :param title: the title of the new card
        :type title: str
        :param content: the content of the new card
        :type content: str
        :return: a CardTableCard object
        :rtype: CardTableCard
        """
        project_id, card_list_id = util.project_or_object(project, card_list_id)
        url = self.LIST_URL.format(base_url=self.url, project_id=project_id, cardtablecolumn_id=card_list_id)
        data = {
            "title": title,
            "content": content,
            "due_on": due_date
        }
        return self._create(url, data)
    
    def update(self, project, cardtablecard, title=False, content=False, assignee_ids=False, due_on=False):
        """
        Update a CardTableCard.

        :param project: a Project object or ID
        :type project: projects.Project|int
        :param card_id: a CardTableCard object or ID
        :type card_id: CardTableCard|int
        :param title: the title of the new card
        :type title: str
        :param content: the content of the new card
        :type content: str
        :param assignee_id: the assignee of the new card
        :type assignee_id: int
        :param due_date: the due date of the new card
        :type due_date: str
        :return: a CardTableCard object
        :rtype: CardTableCard
        """
        project_id, card_id = project, cardtablecard
        url = self.UPDATE_URL.format(base_url=self.url, project_id=project_id, cardtablecard_id=card_id)
        if title is False and content is False and assignee_ids is False and due_on is False:
            raise ValueError("Nothing about this TodoItem would be modified.")
        
        data = {}
        if title is not False:
            data['title'] = title
        if content is not False:
            data['content'] = content
        if assignee_ids is not False:
            data['assignee_ids'] = assignee_ids
        if due_on is not False:
            data['due_on'] = self._normalize_date(due_on)

        return self._update(url, data)
    
    def moves(self, project, card_id, destination_list_id):
        """
        Move a CardTableCard to a different CardTableColumn.

        :param project: a Project object or ID
        :type project: projects.Project|int
        :param card_id: a CardTableCard object or ID
        :type card_id: CardTableCard|int
        :param destination_list_id: a CardTableColumn object or ID
        :type destination_list_id: CardTableColumn|int
        :return: the CardTableCard object
        :rtype: CardTableCard
        """
        project_id, card_id, destination_list_id = project, card_id, destination_list_id
        url = self.MOVES_URL.format(base_url=self.url, project_id=project_id, cardtablecard_id=card_id)
        data = {
            "column_id": destination_list_id
        }
        return self._moves(url, data)
