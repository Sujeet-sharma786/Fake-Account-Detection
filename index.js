const express = require("express");
const bodyParser = require("body-parser");
const {spawn} = require("child_process");
const path = require("path")

const app = express();

app.set('view engine', 'ejs');
app.set("views", path.join(__dirname, "views"))//configuring templates files to ejs extension
app.use(express.static(path.join(__dirname, "public")));//location of static file

app.get("/",async(req,res)=>{
    let username = req.query.username;
    if(username){
        const pyProg =  await spawn('python',['Checker.py',username]);
        pyProg.stdout.on('data',(data)=>{
            res.render("index.ejs",{data:data.toString().trim(),status:200,result:"show"});
        });
        pyProg.stderr.on('data',(data)=>{
            res.render("index.ejs",{data:data.toString(),status:404,result:"show"});
        });
    }else{
        res.render("index.ejs",{result:"hide"});
    }
});


app.listen(process.env.PORT || 3000,()=>{
    console.log("listining at port 3000");
})