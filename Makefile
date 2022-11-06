install brain-games:
	poetry install
	poetry build
	python3 -m pip install --force-reinstall --user dist/*.whl

install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

force-reinstall:
	python3 -m pip install --force-reinstall --user dist/*.whl

make lint:
	poetry run flake8 brain_games
