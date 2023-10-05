<h1>Tarefas:</h1>

<ul>
    <li>Add fresh and refresh token to be requested on methods</li>
</ul>

<h3>Testar:</h3>
<ul>
</ul>

<h3>Testado:</h3>
<ul>
</ul>

<h3>Comandos docker local:</h3>
<ul>
    <li>docker build -t nome_da_imagem .</li>
    <li>docker run -ip 5000:5000 -w /app -v "$(pwd):/app" nome_da_imagem sh -c "flask run --host 0.0.0.0"</li>
</ul>
<h3>Comandos docker queue:</h3>
<ul>
    <li>docker build -t flask_api .</li>
    <li>docker run -w /app flask_api sh -c "rq worker -u rediss://red-ckev9amnpffc73e2hf7g:37iQ930xK46vEnNMWevWBqyL6YOHBvtm@oregon-redis.render.com:6379 emails"</li>
    <li>docker run -p 5000:80 flask_api</li>
</ul>

<h3>Comando gunicorn localmente:</h3>
<ul>
    <li>gunicorn -w 4 'app:create_app()'</li>
</ul>

<h3>Materiais:</h3>
<ul>
    <li>Documentação blueprint: https://flask.palletsprojects.com/en/2.3.x/blueprints/</li>
    <li>Apoio com flask api: https://medium.com/@hedgarbezerra35/api-rest-com-flask-autenticacao-25d99b8679b6</li>
    <li>Vídeo de apoio: https://www.youtube.com/watch?v=LP8besicfH4&t=2s&ab_channel=PycodeBR</li>
    <li>Documentação Twitter: https://developer.twitter.com/en/docs/twitter-api/migrate/twitter-api-endpoint-map</li>
</ul>
<h3>Observações:</h3>
<ul>
    <li>Adicionar jwt claims se quiser funções de admin</li>
</ul>