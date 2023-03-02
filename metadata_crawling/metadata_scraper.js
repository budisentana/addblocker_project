'uses strict';


fs = require('fs')
var gplay = require('google-play-scraper');

var filename = process.argv[2];
console.log(filename);
var res_path = process.argv[3];
console.log(res_path);
var write_path = res_path+filename;
console.log(write_path);
gplay.search({
    term: filename,
    num: 249
    }) .then(function(result){
        //     console.log(result);
            fs.writeFile(write_path+'.txt', JSON.stringify(result) , 'utf-8', err => {
                if (err) throw err;
                console.log('File successfully written to disk');
        })  
});
