var fs = require ('fs');
var path = require('path');

var sass_middleware = require('node-sass-middleware')
var mustache_middleware = require('mustache-express')

var express = require('express');
var app = express();

// Express Middleware
app.use(sass_middleware({
	src:__dirname+'/public',
	dest:__dirname+'/public',
	debug:true
}));

app.engine('html', mustache_middleware());
app.set('view engine', 'html');
app.set('views', __dirname + '/public/html');

// Public Folder
app.use(express.static(__dirname + '/public'));

// Routing
app.get('/', function(req, res) {
	res.render('index', {})
});

// Program Start
var http_server = app.listen(3000, function () {
	console.log('Listening...');
});

// Program Exit
process.on('exit', function () {
	console.log('close from exit')

}).on('SIGINT', function () {
	console.log('SIGINT')
	process.exit()
});
