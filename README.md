# rye-init

Demo repository to use [`rye`](https://rye.astral.sh/).

## pre-requisites

- rust ([ref](https://www.rust-lang.org/tools/install))
- rye ([ref](https://rye.astral.sh/guide/installation/))

**Note**: Select [`uv`](https://github.com/astral-sh/uv) as the package
installer. For more customisations, refer to
[docs](https://rye.astral.sh/guide/installation/#customized-installation).

## setup

1. initialise project:

   ```shell
   rye init && rye pin 3.12
   ```

1. add, lock and install dependencies:

   ```shell
   rye add fastapi pillow pydantic && rye sync
   ```

1. code check (optional):

   ```shell
   rye fmt && rye lint --fix
   ```

## usage

1. run development server:

   ```shell
   rye run dev
   ```

1. run app with docker:

   ```shell
   # start app
   rye run docker-up -d --build

   # stop app
   rye run docker-down
   ```

## notes

- `uv` is an incredible package resolver 🤯! below is a terminal screenshot of
  how fast it resolves and locks dependencies for the above `rye add` command:

  ```
  Initializing new virtualenv in /home/ajinkya/repos/rye-init/.venv
  Python version: cpython@3.12.4
  Added fastapi>=0.111.1 as regular dependency
  Added pillow>=10.4.0 as regular dependency
  Added pydantic>=2.8.2 as regular dependency
  Reusing already existing virtualenv
  Generating production lockfile: /home/ajinkya/repos/rye-init/requirements.lock
  Generating dev lockfile: /home/ajinkya/repos/rye-init/requirements-dev.lock
  Installing dependencies
  Resolved 35 packages in 24ms
  Built rye-init @ file:///home/ajinkya/repos/rye-init
  Prepared 1 package in 524ms
  Installed 35 packages in 53ms
  + annotated-types==0.7.0
  + anyio==4.4.0
  + certifi==2024.7.4
  + click==8.1.7
  + dnspython==2.6.1
  + email-validator==2.2.0
  + fastapi==0.111.1
  + fastapi-cli==0.0.4
  + h11==0.14.0
  + httpcore==1.0.5
  + httptools==0.6.1
  + httpx==0.27.0
  + idna==3.7
  + jinja2==3.1.4
  + markdown-it-py==3.0.0
  + markupsafe==2.1.5
  + mdurl==0.1.2
  + pillow==10.4.0
  + pydantic==2.8.2
  + pydantic-core==2.20.1
  + pygments==2.18.0
  + python-dotenv==1.0.1
  + python-multipart==0.0.9
  + pyyaml==6.0.1
  + rich==13.7.1
  + rye-init==0.1.0 (from file:///home/ajinkya/repos/rye-init)
  + shellingham==1.5.4
  + sniffio==1.3.1
  + starlette==0.37.2
  + typer==0.12.3
  + typing-extensions==4.12.2
  + uvicorn==0.30.3
  + uvloop==0.19.0
  + watchfiles==0.22.0
  + websockets==12.0
  Done!
  Reusing already existing virtualenv
  Generating production lockfile: /home/ajinkya/repos/rye-init/requirements.lock
  Generating dev lockfile: /home/ajinkya/repos/rye-init/requirements-dev.lock
  Installing dependencies
  Resolved 35 packages in 24ms
  Audited 35 packages in 0.14ms
  Done!
  ```

- `rye scripts` are similar to npm scripts and can used to setup automation or
  simplify development processes.

- setting up local dependencies is still a work in progress
  ([ref](https://github.com/astral-sh/rye/issues/1179)). `rye` supports local
  dependencies but the lock files use the absolute paths instead of relative.
  This can be a nuisance when working on a complex project with multiple
  developers.

- compared to poetry, rye provided a simpler experience to setup this demo
  project. Although both are very similar in terms of features, rye also offers
  python version management. read this amazing blog for more in-depth comparison
  of the other python tooling ecosystem:
  [An unbiased evaluation of environment management and packaging tools](https://alpopkes.com/posts/python/packaging_tools/)

<p align="center">
   <img src="https://alpopkes.com/posts/python/figures/venn_diagram.png" width="500"/>
</p>
