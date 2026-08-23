# PixelVault AI Customer Support Lab — Technical Decisions

## Status

These decisions define the v1 reference build.

Exact software versions will only be pinned after we have installed and tested them together.

## Project goal

Build a complete AI customer-support system that support professionals can install, inspect, test, break, and understand.

The project uses the fictional PixelVault Retro business and synthetic customer data.

## Reference-build principle

The main tutorial must be possible to complete without buying an API subscription or entering a credit card.

We will provide one fully tested reference stack.

Other tools may be supported through adapters, but they are optional.

## Reference stack

- Ubuntu Linux — reference host
- Docker Engine — containers
- Docker Compose — run multiple services together
- Python — application language
- FastAPI — application/API framework
- PostgreSQL — business database
- pgvector — vector search inside PostgreSQL
- Ollama — local language-model runner
- Chatwoot — human support inbox
- pytest — automated testing

## Development tools

- Git — version control
- GitHub — public repository
- GitHub CLI — GitHub authentication and repository commands
- Visual Studio Code — reference editor

## Architecture rules

- Use synthetic PixelVault data only.
- Never commit real customer data.
- Never commit passwords, API keys, or other secrets.
- Keep configuration separate from application code.
- Do not make the business logic depend directly on one AI provider.
- Allow LLM providers to be replaced through adapters.
- Allow embedding providers to be replaced through adapters.
- Allow vector storage to be replaced.
- Allow the helpdesk integration to be replaced.
- Enforce authority and permission rules outside the language model.
- Test every instruction before publishing it as working.
- Keep failures and troubleshooting discoveries in the tutorial.

## Build process

1. Build the feature.
2. Test it.
3. Break it deliberately.
4. Diagnose the failure.
5. Fix it.
6. Test again.
7. Rebuild from a clean environment.
8. Capture screenshots.
9. Write the tutorial.
10. Create a Git checkpoint.

## Guiding principle

Popular where practical.

Free for the reference build.

Open interfaces everywhere.

Paid services are optional.

No vendor is required to complete the course.