FROM nginx:latest

HEALTHCHECK --interval=30s \
	--timeout=60s \
	--start-period=5s \
	--retries=3 \
	CMD curl --fail http://localhost || exit 1
