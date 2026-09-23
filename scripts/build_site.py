#!/usr/bin/env python3
"""Build a static multilingual Docsify site."""

from __future__ import annotations

import json
import posixpath
import shutil
from argparse import ArgumentParser
from pathlib import Path


LANGUAGE_INDEX = r"""<!doctype html>
<html lang="{code}">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify@4/themes/vue.css" />
        <link rel="stylesheet" href="style.css" />
        <title>Jimber SASE Platform - Documentation</title>
        <style>
            .sidebar-header {{
                background: #fff;
                border-bottom: 1px solid #e8e8ee;
                padding: 20px 22px 16px;
                position: sticky;
                top: 0;
                z-index: 2;
            }}

            .sidebar-header img {{
                display: block;
                height: auto;
                margin: 0 auto 16px;
                max-width: 170px;
                width: 75%;
            }}

            .language-picker label {{
                color: #555;
                display: block;
                font-size: 12px;
                font-weight: 600;
                letter-spacing: 0.04em;
                margin-bottom: 6px;
                text-transform: uppercase;
            }}

            .language-picker select {{
                appearance: auto;
                background: #fff;
                border: 1px solid #c9c9d4;
                border-radius: 6px;
                color: #111279;
                cursor: pointer;
                font: inherit;
                padding: 8px 10px;
                width: 100%;
            }}
        </style>
    </head>
    <body>
        <div class="sidebar-header">
            <img src="logo.png" alt="Jimber" />
            <div class="language-picker">
                <label for="language">Language</label>
                <select id="language" onchange="switchLanguage(this.value)">
{options}
                </select>
            </div>
        </div>
        <div id="app"></div>
        <script>
            const supportedLanguages = {supported};
            const documentationBasePath = '{base_path}';

            function switchLanguage(language) {{
                window.location.href = documentationBasePath + '/' + language + '/' + window.location.hash;
            }}

            function localizeInternalUrl(url) {{
                const documentationOrigin = 'https://docs.jimber.io/';
                if (url.startsWith(documentationOrigin)) {{
                    url = '/' + url.slice(documentationOrigin.length);
                }}
                if (!url.startsWith('/') || url.startsWith('//')) {{
                    return url;
                }}

                url = url.replace(/^\/\.\//, '/');
                if (url === documentationBasePath || url.startsWith(documentationBasePath + '/')) {{
                    return url;
                }}
                const firstSegment = url.slice(1).split('/')[0];
                if (supportedLanguages.includes(firstSegment)) {{
                    return documentationBasePath + url;
                }}
                return documentationBasePath + '/{code}' + url;
            }}

            function localizeRenderedUrls(html) {{
                return html.replace(/\b(href|src)="([^"]+)"/g, function (_, attribute, url) {{
                    return attribute + '="' + localizeInternalUrl(url) + '"';
                }});
            }}

            function cleanSearchResultTitles() {{
                document.querySelectorAll('.matching-post h2').forEach(function (title) {{
                    title.textContent = title.textContent
                        .replace(/!\[[^\]]*\]\([^)]*\)\s*/g, '')
                        .trim();
                }});
            }}

            window.$docsify = {{
                alias: {{ '/.*/_sidebar.md': documentationBasePath + '/{code}/_sidebar.md' }},
                basePath: documentationBasePath + '/{code}/',
                loadSidebar: true,
                search: {{
                    paths: 'auto',
                    namespace: 'jimber-sase-documentation-{code}',
                    placeholder: '{search_placeholder}',
                    noData: '{search_no_data}',
                }},
                subMaxLevel: 1,
                'flexible-alerts': {{ style: 'flat' }},
                plugins: [
                    function (hook) {{
                        hook.ready(function () {{
                            const header = document.querySelector('.sidebar-header');
                            const sidebar = document.querySelector('.sidebar');
                            if (header && sidebar) {{
                                sidebar.insertBefore(header, sidebar.firstChild);
                            }}

                            const results = document.querySelector('.results-panel');
                            if (results) {{
                                new MutationObserver(cleanSearchResultTitles).observe(results, {{
                                    childList: true,
                                    subtree: true,
                                }});
                            }}
                        }});
                        hook.afterEach(function (html, next) {{
                            document.documentElement.scrollTop = 0;
                            document.body.scrollTop = 0;
                            next(localizeRenderedUrls(html));
                        }});
                    }},
                ],
            }};
        </script>
        <script src="https://cdn.jsdelivr.net/npm/docsify@4"></script>
        <script src="https://unpkg.com/docsify-copy-code"></script>
        <script src="https://unpkg.com/docsify-plugin-flexible-alerts"></script>
        <script src="https://cdn.jsdelivr.net/npm/docsify/lib/plugins/search.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/docsify-tabs@1"></script>
    </body>
</html>
"""


ROOT_INDEX = """<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width,initial-scale=1" />
        <title>Jimber SASE Platform - Documentation</title>
        <script>
            const supported = {supported};
            const preferred = (navigator.language || 'en').split('-')[0];
            const language = supported.includes(preferred) ? preferred : 'en';
            window.location.replace('{base_path}/' + language + '/' + window.location.hash);
        </script>
    </head>
    <body>
        <p><a href="{base_path}/en/">Open the Jimber SASE documentation</a></p>
    </body>
</html>
"""


def overlay(source: Path, destination: Path) -> None:
    if source.exists():
        shutil.copytree(source, destination, dirs_exist_ok=True)


def normalize_base_path(base_path: str) -> str:
    normalized = "/" + base_path.strip("/")
    if normalized == "/":
        return ""
    return posixpath.normpath(normalized)


def build(repository: Path, base_path: str = "/documentation") -> Path:
    config = json.loads(
        (repository / "translation/config.json").read_text(encoding="utf-8")
    )
    output = repository / "public"
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)

    languages = {"en": {"name": "English"}, **config["languages"]}
    supported = list(languages)
    base_path = normalize_base_path(base_path)
    (output / "index.html").write_text(
        ROOT_INDEX.format(
            supported=json.dumps(supported),
            base_path=base_path,
        ),
        encoding="utf-8",
    )
    (output / ".nojekyll").touch()

    cname = repository / "CNAME"
    if cname.exists():
        shutil.copy2(cname, output / "CNAME")

    for code, language in languages.items():
        destination = output / code
        overlay(repository / "shared", destination)
        overlay(repository / "content" / code, destination)
        options = "\n".join(
            f'                <option value="{option_code}"'
            f'{" selected" if option_code == code else ""}>{option["name"]}</option>'
            for option_code, option in languages.items()
        )
        (destination / "index.html").write_text(
            LANGUAGE_INDEX.format(
                code=code,
                options=options,
                supported=json.dumps(supported),
                base_path=base_path,
                search_placeholder=(
                    "Rechercher dans la documentation" if code == "fr" else "Search the documentation"
                ),
                search_no_data=(
                    "Aucun résultat" if code == "fr" else "No results"
                ),
            ),
            encoding="utf-8",
        )

    return output


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--base-path",
        default="/documentation",
        help="Public URL prefix used by the deployed site.",
    )
    arguments = parser.parse_args()
    repository = Path(__file__).resolve().parents[1]
    output = build(repository, arguments.base_path)
    print(f"Built documentation site in {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
