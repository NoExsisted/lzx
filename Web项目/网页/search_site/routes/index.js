var express = require('express');
var router = express.Router();
var mysql = require('../mysql.js');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/process_get', function(request, response) {
    //sql字符串和参数
    var fetchSql = "select url,source_name,title,author,publish_date from fetches where title like '%" +
        request.query.title + "%'" + "and keywords like '%" + request.query.keywords + "%'" + 
        "and author like '%" + request.query.author + "%'";
    mysql.query(fetchSql, function(err, result, fields) {
        response.writeHead(200, {
            "Content-Type": "application/json"
        });
        response.write(JSON.stringify(result));
        response.end();
    });
    /*mysql.query(fetchSql, function(err, result, fields) {
      console.log(result);
      response.end(JSON.stringify(result));
    });*/
});
module.exports = router;
