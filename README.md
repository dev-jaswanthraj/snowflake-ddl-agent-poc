# Snowflake DDL Agent — Git & Quality POC

Demonstrates Python DDL generation, code quality and Git synchronization. This is a **scaffold**, not a deployed integration or production agent.

## Local

```bash
python -m venv .venv
# activate your venv
pip install -e . pytest pytest-cov ruff bandit sqlfluff
ruff check src tests
bandit -r src -ll
pytest
sqlfluff parse sql --dialect snowflake
```

## GitHub setup

1. Create a **private** GitHub repo and push these files to `main`; ensure it has at least one commit.
2. In Snowflake use an admin role, create DB/schema, and add a Git API integration (see `setup_snowflake.sql`).
3. Go to Snowsight > Projects > Workspaces > From Git repository, paste HTTPS URL, choose API integration, and authenticate via the Snowflake GitHub app or a scoped PAT.
4. Create a feature branch, edit a file, push from Workspace and open a GitHub pull request.
5. Under GitHub settings, require the `quality` check and reviewer approval before merging to `main`.
6. Optional: Connect SonarQube Cloud and make its quality gate a required PR check.
7. For deployments, configure Snowflake CLI with workload identity/OIDC (preferred) or another supported non-interactive authentication, then create a separate restricted CD workflow. Do **not** paste credentials into Git.

## Safety/limits

- Generator only **returns** SQL; it never runs SQL. Don't execute LLM-generated DDL without schema/type allowlisting and approval.
- The illustrative Snowflake SQL scripts are manually applied to a disposable POC database; no automatic production deployment is configured.
- SQL files are for demonstration and are *not* an extraction of your existing Snowflake agent.
- Snowflake Git repository objects are generally read-only; Workspaces/Notebooks/Streamlit can push changes.
- Do not commit data, tokens, connection strings, proprietary prompts or PII.
