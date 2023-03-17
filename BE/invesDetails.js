const mongoose = require("mongoose");

const InvesDetailsScehma = new mongoose.Schema(
  {
    fname: String,
    lname: String,
    uname: String,
    email:  {type:String,unique:true},
    password: String,
  },
  {
    collection: "InvesInfo",
  }
);

mongoose.model("InvesInfo", InvesDetailsScehma);