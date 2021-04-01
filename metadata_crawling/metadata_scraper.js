'uses strict';


fs = require('fs')
var gplay = require('google-play-scraper');

var filename = process.argv[2];
console.log(filename)
var path = '/home/budi/adblocker_project/metadata_crawling/res_by_keyword/'+filename
gplay.search({
    term: filename,
    num: 249
    }) .then(function(result){
            // console.log(result);
            fs.writeFile(path+'.txt', JSON.stringify(result) , 'utf-8', err => {
                if (err) throw err;
                console.log('File successfully written to disk');
        })  
});
