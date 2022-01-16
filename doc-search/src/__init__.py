import sys
from index import Index
from bottle import route, run, template, request


if __name__ == '__main__':
    index = Index.new(sys.argv[1])

    @route('/')
    def search():
        q = request.query.q
        print(q, type(q))
        return dict(results=list(index.search(str(q))))

    run()
