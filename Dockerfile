# The repository declares Python 3 but does not pin a narrower version.
FROM python:3 AS build

WORKDIR /workspace
COPY . .

# This repository has no compilation or packaging step.  The build stage keeps
# the documented Python 3 toolchain separate from the small runtime image.

FROM python:3-slim AS runtime

RUN addgroup --system app && adduser --system --ingroup app --home /workspace app

WORKDIR /workspace
COPY --from=build --chown=app:app /workspace /workspace

USER app

# There is no application entry point.  This is the repository's documented
# executable command, supplied by the referee test itself.
CMD ["python3", "-m", "unittest", "discover", "-s", ".referee/002-test-evidence-definition", "-v"]
