all: check html

clean:
	make -C docs $@
	hg st -in | xargs rm
	rm -rf build dist lupyne.egg-info

html:
	make -C docs $@ SPHINXOPTS=-W

dist: html
	python3 setup.py sdist bdist_wheel

check:
	python3 setup.py $@ -ms
	flake8
	python3 -m examples
	pytest-2.7 tests/test_engine.py --cov=lupyne.engine --cov-fail-under=100
	pytest --cov --cov-fail-under=100
	pytest -vk example
