run: ## Roda aplicação
	python src/main.py

run-deps: ## Sobe compose das dependências (MySQL)
	cd docker && docker-compose -f docker-compose-dependencies.yml up