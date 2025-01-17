import insightconnect_plugin_runtime
from .schema import SearchDocumentsInput, SearchDocumentsOutput, Input, Output, Component

# Custom imports below


class SearchDocuments(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="search_documents",
            description=Component.DESCRIPTION,
            input=SearchDocumentsInput(),
            output=SearchDocumentsOutput(),
        )

    def run(self, params={}):
        index = params.get(Input.INDEX)
        query = params.get(Input.QUERY)

        results = self.connection.client.search_documents(index, query, params.get(Input.ROUTING))

        hits = results.get("hits", {})
        hhits = hits.get("hits")

        for hit in hhits:
            if "_score" not in hit or hit["_score"] is None:
                hit["_score"] = 0
                self.logger.info("One or most results lack a relevance score, assuming 0")

        return insightconnect_plugin_runtime.helper.clean(
            {
                Output.SHARDS: results.get("_shards"),
                Output.HITS: {"total": hits.get("total"), "max_score": hits.get("max_score", 0), "hits": hhits},
                Output.TOOK: results.get("took"),
                Output.TIMED_OUT: results.get("timed_out"),
            }
        )
