FROM python:3.7

WORKDIR /code

# Get the preview version of poetry
RUN pip install -U pip && \
    pip install poetry

COPY poetry.lock pyproject.toml ./
COPY server.py fapiis.json ./

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

CMD waitress-serve --listen=*:5000 server:application
