
const scrape = require('website-scraper');

//house: http://www.house.leg.state.mn.us/members/hmem.asp
//senate: http://www.senate.mn/members/index.php

let options = {
    urls: ['http://www.senate.mn/members/index.php'],
    directory: '/web/gis/imageScraper/senate',
    sources: [
    {selector: 'img', attr: 'src'}
  ]
};

scrape(options).then((result) => {
    console.log("Website succesfully downloaded");
}).catch((err) => {
    console.log("An error ocurred", err);
});