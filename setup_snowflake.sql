-- Run with a role authorized to create integrations; adjust grants for your organization.
CREATE DATABASE IF NOT EXISTS DDL_AGENT_POC;
CREATE SCHEMA IF NOT EXISTS DDL_AGENT_POC.DEVOPS;
-- This example configures the Snowflake GitHub App; authenticate interactively in Workspaces.
CREATE OR REPLACE API INTEGRATION DDL_GITHUB_INTEGRATION
  API_PROVIDER = git_https_api
  API_ALLOWED_PREFIXES = ('https://github.com')
  API_USER_AUTHENTICATION = (TYPE = SNOWFLAKE_GITHUB_APP)
  ENABLED = TRUE;
-- For a separate SQL-readable repo clone (optional), use CREATE GIT REPOSITORY
-- with your verified remote URL, API integration and appropriate credentials.
