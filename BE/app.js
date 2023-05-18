const { request } = require("express");
const express= require("express");
const app = express();
const mongoose=require("mongoose");
app.use(express.json());
const cors=require("cors");
app.use(cors());
const bcrypt=require("bcryptjs");
app.set("view engine", "ejs")
app.use(express.urlencoded({extended:false}));
const jwt=require("jsonwebtoken");

var nodemailer=require('nodemailer');
const JWT_SECRET= "fbvjdfbvksfbsk1213#$@flvfjdngf13565!";

const mongoUrl= "mongodb+srv://anatshulman:2HBYgG53On6MzWu4@cluster0.i84nq3q.mongodb.net/?retryWrites=true&w=majority";


mongoose.connect(mongoUrl,{
    useNewUrlParser:true,
}).then(()=>{console.log("connect to db");}).catch(e=>console.log(e));


require("./userDetails");
const User=mongoose.model("UserInfo");
const Inves=mongoose.model("InvesInfo");
const Machin=mongoose.model("CSV");

const checkUrls = require('./urlscan_list.js');
const getUrls = require('./get_urls.js');
const checkHashes = require("./virustotal_list.js");
const getHashes = require("./get_hashes.js");
const { all } = require("axios");

app.post("/network-connections", (req, res) => {
    const { email, date } = req.body;
    console.log('Credentials: +++++++++++++++++++');
    console.log(email, date);
 
    getUrls(email, date)
      .then(async (concatenatedList) => {
        console.log(concatenatedList.slice(0, 50));
        // sending only first 50 elements unlisted (due to Urlscan API's limitation)
        const results = await checkUrls(concatenatedList.slice(0, 50));
        res.send({status:"ok",data:results});
  
        // TODO: send the 'concatenatedList' to Machine-learning algorithm in additionally to Urlscan
  
        console.log(results);
      })
      .catch((error) => {
        console.error(error);
      });
  });
  
  app.post("/hashes", (req, res) => {
    const { email, date } = req.body;
    console.log('Credentials: +++++++++++++++++++');
    console.log(email, date);

    getHashes(email, date)
      .then(async (sha256List) => {
        console.log(sha256List);
        // sending only first 4 elements (due to VirusTotal API's limitation)
        const results = await checkHashes(sha256List.slice(0, 4));
        res.send({status:"ok",data:results});
  
        // TODO: send the 'sha256List' to Machine-learning algorithm in additionally to Virustotal
  
        console.log(results);
      })
      .catch((error) => {
        console.error(error);
      });
  });


app.post("/register",async(req,res)=>{
    const {fname,lname,email,password, userType}=req.body;

    const encryptedPassword=await bcrypt.hash(password,10);
    try{

        const oldUser= await User.findOne({email});

        if (oldUser){
         return res.send({error:"User Exists"});
        }
        await User.create({
            fname,
            lname,
            email,
            password :encryptedPassword,
            userType,
        });
        res.send({status:"OK"});
    } catch (error){
        res.send({status:"problem"});
        
    }
});

app.post("/login-user", async(req,res)=>{
    const {email,password}=req.body;
    const user=await User.findOne({email});
    if (!user){
        return res.json({error: "User Not Found"});
    }
    if (await bcrypt.compare(password,user.password)){
        const token=jwt.sign({email:user.email}, JWT_SECRET,{
            expiresIn:"15m",
        });
        if (res.status(201)){
            return res.json({status: "ok", data:token});
        } else{
            return res.json({error:"error"});
        }
    }
    res.json({status:"error",error:"Invalid Password"});

});

app.post("/userData",async(req,res)=>{
    const {token}=req.body;
    try{
        const user=jwt.verify(token,JWT_SECRET,(err,res)=>{
            if (err){
                return "token expired";
            }
            return res;
           
        });
        console.log(user);
        if (user == "token expired") {
            return res.send({ status: "error", data: "token expired" });
          }
        const useremail=user.email;
        User.findOne({email:useremail})
        .then((data)=>{
            res.send({status:"ok", data:data});
        }).catch((error)=>{
            res.send({status:"error", data:error});
        });

    }catch(error){

    }
});

app.listen(5000,()=>{
    console.log("server started");
});

app.post("/forgot-password",async(req,res)=>{
    const {email}=req.body;
    try {
        const oldUser=await User.findOne({email});
        if(!oldUser){
            return res.json({status :"User Not Exists!"});
        }
        const secret=JWT_SECRET+oldUser.password;
        const token=jwt.sign({email:oldUser.email, id:oldUser._id},secret);
        const link=`http://localhost:5000/reset-password/${oldUser._id}/${token}`;
       

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'moaosint@gmail.com',
    pass: 'qlnvnewmxuijadcb'
  }
});

var mailOptions = {
  from: 'moaosint@gmail.com',
  to: 'moaosint@gmail.com',
  subject: 'password reset',
  text: link
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});
        console.log(link);
    } catch (error) {
        
    }
});

app.get("/reset-password/:id/:token",async(req,res)=>{
    const{id,token}=req.params;
    console.log(req.params);
    const oldUser= await User.findOne({_id:id});
    if (!oldUser){
        return res.json({status :"User Not Exists!"});
    }
    const secret=JWT_SECRET+oldUser.password;
    try {
        const verify= jwt.verify(token,secret);
        res.render("index",{email:verify.email,status:"not verified"})
    } catch (eroor) {
        res.send("Not verified")
        
    }

});

app.post("/reset-password/:id/:token",async(req,res)=>{
    const{id,token}=req.params;
    const {password}=req.body;
    const oldUser= await User.findOne({_id:id});
    if (!oldUser){
        return res.json({status :"User Not Exists!"});
    }
    const secret=JWT_SECRET+oldUser.password;
    try {
        const verify= jwt.verify(token,secret);
        const encryptedPassword= await bcrypt.hash(password,10);
        await User.updateOne({
            _id:id,
        },
        {
            $set:{
                password:encryptedPassword,
            }

        });
        res.json("password updated");
        res.render("index",{email:verify.email})
    } catch (eroor) {
        res.send("somthing went wrong")
        
    }

});

app.get("/getAllUser",async(req,res)=>{
    try{
        const allUser=await User.find({});
        res.send({status:"ok",data: allUser});
        console.log(allUser);
    }catch(error){
        console.log(error);
    }
});

app.get("/getMachines",async(req,res)=>{
    try{
        const allMachine=await Machin.find({});
        res.send({status:"ok",data: allMachine});
        console.log(allMachine);
    }catch(error){
        console.log(error);
    }
});
