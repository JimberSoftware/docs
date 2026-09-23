FROM python:3.13-alpine AS builder

WORKDIR /src

COPY content content
COPY scripts scripts
COPY shared shared
COPY translation translation

RUN python -m scripts.validate_docs \
    && python -m scripts.build_site --base-path /documentation

FROM nginx:stable-alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /src/public /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]
