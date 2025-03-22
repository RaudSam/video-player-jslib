from livereload import Server, shell

server = Server()
server.watch("*.html", shell("make html", cwd=""))
server.watch("*.js")
server.serve(
    root=".",
    port=5500,
    default_filename="index.html")
