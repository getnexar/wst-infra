# Code assignment: document search

This assignment walks through a process of turning a simple Python application into a more production-ready app.

The task list may be long, so if there's anything you're struggling with, you're welcome to skip ahead. We don't need you to check items on a shopping list of tech skills, rather we want to focus on _how_ you work on the things you're already familiar with.

## Getting started

This assignment makes use of VS Code's remote development features, so that your development environment requires no toil to set up, and is consistent regardless of operating system or other dependencies.

### System Requirements

You need only two components:
1. A container runtime like Docker Desktop
2. Visual Studio Code

### Starting the development environment

1. Using Nexar's repository as a template, [create a new repository under your own Github account](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template#creating-a-repository-from-a-template), then clone that repo into a local directory, e.g. `$HOME/nexar-assignment`.
    Using the [GitHub CLI](https://cli.github.com/manual/gh_repo_create) you can do this with a single command:
    ```bash
    cd $HOME
    gh repo create \
       nexar-assignment \
       --template https://github.com/getnexar/infra-eng-assignment.git \
       --private # optional \
       --confirm # optional
    ```

2. Open your working copy in VS Code (e.g. `code $HOME/nexar-assignment` in macOS). A prompt should pop up asking you to open the directory in a container. Click 'Yes', let it build the dev container (takes 1-3 minutes), and once it's done, you're good to go.

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

### Part 3: Observability

1. In the app's Python code, instrument latency of the `search/` endpoint, and expose a metrics HTTP endpoint on port `8000`. You may use any open-source library for this purpose.
2. Add code and/or configuration that installs Prometheus onto the k8s cluster and configures it to scrape metrics from the app.
3. Using a load generator like [`hey`](https://github.com/rakyll/hey), generate some load on the app.
4. Using the built-in web UI for Prometheus, chart the p50, p90, p99 latencies of `search/` requests over the load you generated before.
5. (Bonus) which other key metrics are important/useful to instrument in a web service like this? Add them as you see fit and show how you can query them in Prometheus.
---

Good luck!
