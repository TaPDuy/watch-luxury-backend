from rest_framework.filters import SearchFilter as RestSearchFilter


class SearchFilter(RestSearchFilter):

    def get_search_terms(self, request):
        keyword = request.query_params.get(self.search_param, '')
        keyword = keyword.replace('\x00', '')
        return (keyword, )
