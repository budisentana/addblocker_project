fs = require('fs')

var gplay = require('google-play-scraper');
var app_id = 'cz.mobilesoft.appblock';
path = '/home/budi/adblocker_project/adblocker_code/metadata_crawling/test_write_to_json';

let x = gplay.app({appId: app_id})
// let x = gplay.app({appId: "com.mobisoft.webguard"})
x.then(function(result){
    try{    
        const json_data = JSON.stringify(result)
        console.log(json_data)
        fs.writeFileSync(path+'.txt', json_data );
        console.log(result);
    }catch(err){
        console.log(err);
    }
})