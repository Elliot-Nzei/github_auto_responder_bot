# Makefile for FastAPI GitHub Auto Responder

run:
	@echo "Running server with uvicorn..."
	@mkdir -p logs
	@touch logs/output.log
	@uvicorn app.main:app --reload

lint:
	ruff check app

typecheck:
	mypy app

test:
	pytest tests

clean:
	rm -rf logs/*.log _pycache_ .mypy_cache .ruff_cache

env:
	@echo "Setting environment variables..."
	@export $(cat .env | xargs)