FROM python:3.7

WORKDIR /code

# Get the preview version of poetry
RUN pip install -U pip && \
    pip install poetry

COPY poetry.lock pyproject.toml ./
COPY server.py  ./

# Install poetry globally - with the current version of
# poetry, there is a known issue where poetry config will
# not create config.toml: https://github.com/sdispater/poetry/issues/1179
# As such, we create it ourselves.
RUN mkdir -p ${HOME}/.config/pypoetry/ && \
    touch ${HOME}/.config/pypoetry/config.toml && \
    poetry config settings.virtualenvs.create false && \
    poetry config --list

# Set PRODUCTION to anything to invoke installation with --no-dev
ARG PRODUCTION
RUN poetry install ${PRODUCTION:+--no-dev}
RUN curl https://gist.githubusercontent.com/vzvenyach/b9d4cf6d57d34889469368cf9b53f3f9/raw/b0183a1b3df6e2dae13a9bc1ba8bdeaea90195ec/fapiis-demo.json --output /code/fapiis.json
CMD waitress-serve --listen=*:5000 server:application
