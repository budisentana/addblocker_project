// This script is used to scrap apps metadata per id
// update made to the result write path wchich is made dynamically and sent from python through a parameter
// required 2 parameter which is app id and a path to write the result in txt json format
'uses strict';


fs = require('fs')
var gplay = require('google-play-scraper');

// var app_id = 'cz.mobilesoft.appblock';
// path = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/test_write_to_json';

var app_id = process.argv[2];
var path = process.argv[3];


let x = gplay.app({appId: app_id})
// let x = gplay.app({appId: "com.mobisoft.webguard"})
x.then(function(result){
    try{    
        const json_data = JSON.stringify(result)
        fs.writeFileSync(path+'.txt', json_data );
        // console.log(json_data)
    }catch(err){
        console.log('Throw Error');
        // console.log(err);
    }
})

