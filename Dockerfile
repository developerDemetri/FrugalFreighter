FROM python:3.9.2-slim

RUN useradd -m freighter
WORKDIR /home/freighter

RUN pip install -U pip "poetry>=1.1.5,<1.2.0"

COPY frugal_freighter ./frugal_freighter
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry build -f wheel
RUN cd dist && ls | grep .whl | xargs pip install && cd ..
RUN ls | xargs rm -rf

USER freighter
ENTRYPOINT ["python", "-m", "awslambdaric"]
CMD ["frugal_freighter.app.lambda_handler"]
