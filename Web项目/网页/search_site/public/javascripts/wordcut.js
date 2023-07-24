let titles = require('C:/Users/lianxiang/Downloads/results1.json');
let fs = require('fs');
//console.log(data)

const cncut = require("cncut")
const cn = cncut()
//let titles = ["你是不”是“傻啊！你|", "昨天下楼倒垃圾——的时——候就对你一见钟情了"]
let t = []
for (let i in titles) {
    titles[i] = titles[i].replace(/[&\|\”“："":.……m²/≠‘’《》→∣@①②⑤\[\]「」⑥⑦⑧⑨℃︱~()·＋\\*^%$+（）丨｜？【】，、——#！@\-_]/g, "");
    titles[i] = titles[i].split(/[\t\r\f\n\s]*/g).join('');
    titles[i] = titles[i].replace(/[0-9]/g, '');
    titles[i] = titles[i].replace(/[a-z]/ig, '');
    //console.log(titles[i]);
    //console.log(cn.cut(titles[i]));
    t.push(titles[i])
}
let filename2 = 'f6.json';
        //存储json
fs.writeFileSync(filename2, JSON.stringify(t));
//console.log(t)
let dic = new Array();
for (let k in t) {
    let j = cn.cut(t[k]);
    for (let i in j) {
        if (j[i] in dic) {
            dic[j[i]] += 1;
        }
        else {
            dic[j[i]] = 10
        }
    }
}
delete(dic['网易']);
delete(dic['新闻']);
delete(dic['有']);
delete(dic['对']);
delete(dic['不']);
delete(dic['与']);
delete(dic['的']);
delete(dic['在']);
delete(dic['向']);
delete(dic['热']);
delete(dic['点']);
delete(dic['媒']);
delete(dic['做']);
delete(dic['人']);
delete(dic['大']);
delete(dic['何']);
delete(dic['了']);
delete(dic['是']);
delete(dic['中']);
delete(dic['国']);
delete(dic['易']);
delete(dic['新']);
delete(dic['被']);
delete(dic['网']);
delete(dic['世']);
delete(dic['将']);
delete(dic['政务']);
delete(dic['何以']);

let l = [];
//var word = [];
//var freq = [];
for (let i in dic) {
    //var w = i;
    //var f = dic[i];
    //word.push(w);
    //freq.push(f);
    if(dic[i] > 20) {
        let d = [i, dic[i]];
        l.push(d);
    }
}
//l.push(word);
//l.push(freq);
function descend(x,y){
    return y[1] - x[1];  //按照数组的第2个值升序排列
}
l = l.sort(descend);
console.log(l);
let filename = 'f2.json';
        //存储json
fs.writeFileSync(filename, JSON.stringify(l));
//console.log(l);