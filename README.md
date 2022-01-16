# Code assignment: document search

This assignment aims to explore multiple aspects of taking a simple Python web application and making it production-grade.

## Background

The `doc-search` application implements a simple search endpoint over a set of documents. More specifically, given a dataset of documents, where each document has a numeric identifier, the endpoint returns a list of all of the document IDs containing ALL words in the `q` query parameter.

For example, if the web server is serving at http://localhost:8080, and the words `hello` and `world` both exist only in document 1, then the command `curl http://localhost:8080/?q=hello+world` should return:

```json
{
    "results": ["1"]
}
```

### Sanity checks

1. Run unit tests `cd doc-search/src/ && python -m unittest -b test_index`
2. Build the container image: `docker build . -t doc-search`
3. Run the app: `docker run -p 8080:8080 doc-search`. 
4. Test the app: you can use `curl` to query it, for example: `curl http://localhost:8080/?q=hello+world` will return a JSON document with all of the documents containing both `hello` and `world`

## Tasks

### Part 1: Improving the build

The app currently has a `Dockerfile` included under `doc-search/`.

1. Every commit to application code (`.py` files) results in a slow build of the container image. Modify the `Dockerfile` to make the build faster.
2. How can you minimize the size of the resulting container image? Modify the `Dockerfile` or describe your solution.

### Part 2: Deploying to Kubernetes

Here you will deploy the application to a local Minikube.

1. Implement a minimal Helm chart for this application.
2. Deploy the chart to Minikube, under the `default` namespace.
3. Verify that you can call the service from outside the cluster.
4. We want Kubernetes to tolerate a slow start for our app. Implement this behavior in your chart. Bonus points if you can simulate a slow start and test your solution.

---

Good luck!