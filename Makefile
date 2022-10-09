# run homework
.PHONY: homework-i-run
homework-i-run:
	@python generate_users.py

# install requirements
.PHONY: init-dev
init-dev:
	@python -m pip install --upgrade pip
	pip -requirement requirements.txt

# Run tools for files from commit.
.PHONY: pre-commit-run
pre-commit-run:
	@pre-commit run

# Run tools for all files.
.PHONY: pre-commit-run-all
pre-commit-run-all:
	@pre-commit run --all-files

.PHONY: d-homework-i-run
# Make all actions needed for run project.
d-homework-i-run:
	@make doc-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge project and related data.
d-homework-i-purge:
	@make doc-purge


.PHONY: doc-run
# Run docker
doc-run:
		@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose \
			up --build

.PHONY: doc-purge
# Stop docker
doc-purge:
		@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose \
			down --remove-orphans --rmi local --timeout 0