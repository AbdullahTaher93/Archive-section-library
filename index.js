
var express=require("express");
var MongoClient=require("mongodb").MongoClient;
var url = "mongodb://localhost:27017/";

//connect mongodb with nodejs
MongoClient.connect(url, (err, client) => {	
    if (err) {	
      console.error(err)	
  
       return	
    }	
    var dbase = client.db("lib");	
    const col1 = dbase.createCollection('accounts')
    const col2 = dbase.createCollection('books')	
    console.log('lib database is created,accounts and books are created.')
    //...	
  })

  var app = express();
  var bodyParser=require('body-parser');  
  var port = process.env.PORT || 5000;
  //set the port to the porject
  app.set('port', port);
  app.use(express.static(__dirname + '/public'));
  app.use(bodyParser.json())
  app.use(bodyParser.urlencoded({ extended: false }))

  app.get('/', function (req, res) {

    var msg = {
           "checking server status": "OK"
         }
          res.status(200);
          res.send(msg);
          console.log('done server')
        });
  
app.listen(port, function () {

          console.log('Example app listening on port 127.0.0.1:5000');
      
        });
//export the project
module.exports=app;


