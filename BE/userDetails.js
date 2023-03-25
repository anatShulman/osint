const mongoose = require("mongoose");

const UserDetailsScehma = new mongoose.Schema(
  {
    fname: String,
    lname: String,
    uname: String,
    email:  {type:String,unique:true},
    password: String,
   // userType: String,
  },
  {
    collection: "UserInfo",
  }
);
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

mongoose.model("UserInfo", UserDetailsScehma);

mongoose.model("InvesInfo", InvesDetailsScehma);
