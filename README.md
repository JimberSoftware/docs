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
6. Builds a container and deploys changed documentation to testing.

## Deployment

The multilingual documentation is served independently from the existing
Signalserver documentation service. It uses a dedicated Compose project and a
Traefik route at `/documentation`:

- Testing: `https://sase.testing.jimber.io/documentation/`
- Staging: `https://sase.staging.jimber.io/documentation/`
- Production: `https://sase.jimber.io/documentation/`

The existing `/docs` route is not modified. Synchronization deploys to testing
automatically. Staging and production deployments are started manually from the
`Deploy multilingual documentation` workflow after testing the generated site.
Testing and staging attach to `traefik-proxy`; production attaches to the
existing external `proxy` network used by the production edge router.

`docs.jimber.io` remains a GitHub Pages redirect to
`https://sase.jimber.io/docs/` from the legacy `release_1.15` branch.

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
