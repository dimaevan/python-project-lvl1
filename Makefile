install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python -m pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8 brain_games
calc:
	poetry run brain-calc
gcd:
	poetry run brain-gcd
progression:
	poetry run brain-progression
brain-prime:
	poetry run brain-prime
