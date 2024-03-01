render:
	find -name "*.plantuml" | xargs -I{} curl localhost:8080/png --data-binary @{} --output {}-rendered.png
clean:
	find -name "*-rendered.png" -print -delete

server-up:
	docker run --rm -d -p 8080:8080 plantuml/plantuml-server:jetty
	sleep 2
server-down:
	docker stop $$(docker ps | grep plantuml/plantuml-server:jetty | cut -d' ' -f1)
