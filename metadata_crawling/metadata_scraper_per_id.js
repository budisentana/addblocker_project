'uses strict';


fs = require('fs')
var gplay = require('google-play-scraper');

var filename = process.argv[2];
console.log(filename)
// var path = '/home/budi/adblocker_project/metadata_crawling/selected_metadata/'+filename
var path = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/metadata_2022_based_on_2021/'+filename
gplay.app({appId: filename,country:'au'}) 
    .then(function(result){
            // console.log(result);
            fs.writeFile(path+'.txt', JSON.stringify(result) , 'utf-8', err => {
                if (err) throw err;
                console.log('File successfully written to disk');
            })  
    });
