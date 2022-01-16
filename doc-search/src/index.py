import os
import codecs

class Index:
    # builds a naive, in efficient index
    
    def __init__(self, docs):
        self.docs = docs

    @staticmethod
    def new(data_path):
        
        docs = {}
        for path in os.listdir(data_path):
            if path.endswith('.xml'):
                doc_id = path.split(".")[0]

                with codecs.open(data_path + '/' + path, "r", encoding='utf-8', errors='ignore') as f:
                    data = f.read()
                    docs[doc_id] = data

        return Index(docs=docs)
    
    def search(self, phrase):
        words = phrase.split()
        results = set()
        for doc, text in self.docs.items():
            found_all = True
            for word in words:
                if word not in text:
                    found_all = False
                    break
            if found_all:
                results.add(doc)
        return results

