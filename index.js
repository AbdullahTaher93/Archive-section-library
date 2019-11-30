
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
    console.log('all is good')
    //...	
  })
