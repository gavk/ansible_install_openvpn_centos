lint: yamllint ansible-lint flake8

yamllint:
	yamllint -c .yamllint .

ansible-lint:
	ansible-lint

flake8:
	flake8 .
