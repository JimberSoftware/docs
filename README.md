# Jimber SASE documentation

This repository publishes the multilingual Jimber SASE documentation.

English content is mirrored automatically from
[`JimberSoftware/jimberfw_signalserver/apps/docs`](https://github.com/JimberSoftware/jimberfw_signalserver/tree/development/apps/docs).
Do not edit `content/en` directly. Translations are generated from that English
source using the language configuration and terminology in `translation/`.

## Synchronization

The `Synchronize translations` workflow runs hourly, on manual request, or after
a `signalserver-docs-changed` repository dispatch. It performs these operations
atomically:

1. Sparse-checks out `apps/docs` from Signalserver.
2. Mirrors English Markdown into `content/en` and shared assets into `shared`.
3. Translates files whose source, prompt, or glossary hash changed.
4. Validates protected Markdown, translation state, and the rendered site.
5. Commits directly to `main` only when every step succeeds.
6. Deploys the resulting multilingual site to GitHub Pages.

Required Actions secrets:

- `SIGNALSERVER_DEPLOY_KEY`: read-only deploy key for the private source repository.
- `OPENAI_API_KEY`: project-scoped OpenAI API key used for translation.

Optional Actions variables:

- `SIGNALSERVER_DOCS_REF`: source branch or tag, defaults to `development`.
- `OPENAI_TRANSLATION_MODEL`: model override, defaults to `gpt-6-luna`.

Run checks locally with:

```sh
python -m unittest discover
python -m scripts.validate_docs
python -m scripts.build_site
```
