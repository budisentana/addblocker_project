'uses strict';


fs = require('fs')
var gplay = require('google-play-scraper');

var app_id = process.argv[2];
console.log(app_id);
var res_path = process.argv[3];
var write_path = res_path+app_id;
gplay.similar({
    appId: app_id
    }) .then(function(result){
            // console.log(result);
            fs.writeFile(write_path+'.txt', JSON.stringify(result) , 'utf-8', err => {
                if (err) throw err;
                console.log('File successfully written to disk');
        })  
});
