from .quote_mappings import quote_mappings, quote_settings


class Index:
    def __init__(self, name, mappings={}, settings={}, docs=[]) -> None:
        self.name = name
        self.mappings = mappings
        self.settings = settings
        self.docs = docs


class IndexQuote(Index):
    def __init__(self, name, docs=[]) -> None:
        super().__init__(name, quote_mappings, quote_settings, docs)