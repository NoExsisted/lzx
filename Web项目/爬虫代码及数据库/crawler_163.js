var source_name = "网易";
var myEncoding = "utf-8";
var seedURL = 'https://www.163.com/';

var seedURL_format = "$('a')";
var keywords_format = "$('meta[name=\"keywords\"]').eq(0).attr(\"content\")";
var title_format = "$('title').text()";
var date_format = "$('meta[property=\"article:published_time\"]').eq(0).attr(\"content\")";
var author_format = "$('.post_author').text()";
var content_format = "$('.post_body').text()";
var desc_format = "$('meta[name=\"description\"]').eq(0).attr(\"content\")";
var source_format = "$('.post_author').text()"; // 这里和责编同一个
var url_reg = /\/news\/article\/(\w{16}).html/;

var fs = require('fs');
var myRequest = require('request');
var myCheerio = require('cheerio');
var myIconv = require('iconv-lite');
var schedule = require('node-schedule');
var mysql = require('./mysql.js');
require('date-utils');

//防止网站屏蔽我们的爬虫
var headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'
}

//request模块异步fetch url
function request(url, callback) {
    var options = {
        url: url,
        encoding: null,
        headers: headers,
        timeout: 10000 //
    };
    myRequest(options, callback);
}

var rule = new schedule.RecurrenceRule();
var times = [10, 12, 14, 16, 18, 20, 22]; //每天7次自动执行
var times2 = 1; // 定义在第几分钟执行
rule.hour = times;
rule.minute = times2;

//定时执行seedget()函数
schedule.scheduleJob(rule, function() {
    seedget();
});

seedget();

function seedget() {
    request(seedURL, function(err, res, body) { //读取种子页面
        //用iconv转换编码
        var html = myIconv.decode(body, myEncoding);
        //准备用cheerio解析html
        var $ = myCheerio.load(html, { decodeEntities: true });
        var seedurl_news;

        try {
            seedurl_news = eval(seedURL_format);
        } catch (e) { console.log('url列表所处的html块识别出错：' + e) };

        seedurl_news.each(function(i, e) { //遍历种子页面里所有的a链接
            var myURL = "";
            try {
                var href = ""; //得到具体新闻url
                href = $(e).attr("href");
                if (typeof href == "undefined") {
                    return;
                }
                myURL = href; //https://开头的

                if (myURL == "https://jubao.163.com/") return;
                if (href.toLowerCase().indexOf('https://') >= 0) myURL = href;
                else if (href.startsWith('//')) myURL = 'http:' + href; ////开头的
                else myURL = seedURL.substr(0, seedURL.lastIndexOf('/') + 1) + href; //其他
            } catch (e) { console.log('识别种子页面中的新闻链接出错：' + e); };

            if (!url_reg.test(myURL)) return;
            //console.log(myURL);

            var fetch_url_Sql = 'select url from fetches where url=?';
            var fetch_url_Sql_Params = [myURL];
            mysql.query(fetch_url_Sql, fetch_url_Sql_Params, function(qerr, vals, fields) {
                if (vals.length > 0) {
                    console.log('URL duplicate!')
                } else newsGet(myURL); //读取新闻页面
            });
        });
    });
};

function newsGet(myURL) { //读取新闻页面
    request(myURL, function(err, res, body) {
        var html_news = myIconv.decode(body, myEncoding); //用iconv转换编码
        var $ = myCheerio.load(html_news, { decodeEntities: true });
        myhtml = html_news;

        console.log("转码读取成功:" + myURL);

        //动态执行format字符串，构建json对象准备写入文件或数据库
        var fetch = {};
        fetch.title = "";
        fetch.content = "";
        fetch.publish_date = "";
        fetch.url = myURL;
        fetch.source_name = source_name;
        fetch.source_encoding = myEncoding; //编码
        fetch.crawltime = new Date();

        if (keywords_format == "") fetch.keywords = source_name; //没有关键词就用sourcename
        else fetch.keywords = eval(keywords_format);

        if (title_format == "") fetch.title = "";
        else fetch.title = eval(title_format); //标题

        //console.log(fetch.title);
        console.log(fetch.crawltime);

        if (date_format != "") fetch.publish_date = eval(date_format); //刊登日期
        console.log('date: ' + fetch.publish_date);
        
        try{
            temp = fetch.publish_date;
            t1 = temp.split("T")[0];
            t2 = temp.split("T")[1].split("+")[0];
            fetch.publish_date = t1 + " " + t2;
            fetch.publish_date = new Date(fetch.publish_date).toFormat("YYYY-MM-DD");
        }   
        catch (e)
        {
            var pubtime_format = "$('.pub_time').text()";
            fetch.publish_date = eval(pubtime_format);
            fetch.publish_date = new Date(fetch.publish_date).toFormat("YYYY-MM-DD");
        }
        console.log('date: ' + fetch.publish_date);

        fetch.author = eval(author_format);
        if (fetch.author == "") fetch.author = source_name; //eval(author_format);  //作者
        else
        {
            //console.log(fetch.author);
            //fetch.author = eval(author_format);
            t = fetch.author.split("责任编辑")[1].split("\n")[1];
            author = t.split(/[\t\r\f\n\s]*/g).join(''); // 去除全部空格
            fetch.author = author;
            //console.log(fetch.author);
        }

        //console.log(fetch.author);

        fetch.content = eval(content_format);
        if (fetch.content == "") fetch.content = "";
        else
        {
            fetch.content = eval(content_format).replace("\r\n" + fetch.author, ""); //内容,是否要去掉作者信息自行决定
        }
        if(fetch.content == "")
        {
            var endText_format = "$('.endText').text()";
            fetch.content = eval(endText_format);
            //console.log("here");
        }
        //console.log(fetch.content);


        fetch.source = eval(source_format);
        if (fetch.source == "") fetch.source = fetch.source_name;
        else
        {
            fetch.source = eval(source_format);
            t = fetch.source.split("本文来源：")[1].split("\n")[0];
            fetch.source = t + " " + fetch.author;
            //console.log(fetch.source);
        }
        console.log(fetch.source);

        if (desc_format == "") fetch.desc = fetch.title;
        else fetch.desc = eval(desc_format).replace("\r\n", ""); //摘要    

        //let filename = source_name + "_" + (new Date()).toFormat("YYYY-MM-DD") +
        //    "_" + myURL.slice(myURL.lastIndexOf('/') + 1, myURL.lastIndexOf('.')) + ".json";
        ////存储json
        //fs.writeFileSync(filename, JSON.stringify(fetch));
        var fetchAddSql = 'INSERT INTO fetches(url,source_name,source_encoding,title,' +
            'keywords,author,publish_date,crawltime,content) VALUES(?,?,?,?,?,?,?,?,?)';
        var fetchAddSql_Params = [fetch.url, fetch.source_name, fetch.source_encoding,
            fetch.title, fetch.keywords, fetch.source, fetch.publish_date,
            fetch.crawltime.toFormat("YYYY-MM-DD HH24:MI:SS"), fetch.content
        ];
        //执行sql，数据库中fetch表里的url属性是unique的，不会把重复的url内容写入数据库
        mysql.query(fetchAddSql, fetchAddSql_Params, function(qerr, vals, fields) {
            if (qerr) {
                //console.log(qerr);
            }
        }); //mysql写入
    });
}